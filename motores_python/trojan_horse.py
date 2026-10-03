import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# ==============================================================================
# MOTOR 1: EL CABALLO DE TROYA (Auditoría de Conversión)
# ==============================================================================

def analyze_website(url):
    print(f"[+] Escaneando la web: {url}...")
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Análisis Básico (Emulación del Agente Analista)
        has_whatsapp = 'wa.me' in response.text or 'whatsapp' in response.text.lower()
        has_forms = len(soup.find_all('form')) > 0
        speed_proxy = len(response.text) # Proxy de peso
        
        flaws = []
        if not has_whatsapp:
            flaws.append("FALTA GRAVE: No tienen botón de WhatsApp directo. Pierden ventas impulsivas.")
        if speed_proxy > 2000000:
            flaws.append("FALTA MEDIA: La web es demasiado pesada (más de 2MB de HTML bruto). Carga lenta en móviles.")
        if not has_forms:
            flaws.append("FALTA GRAVE: No tienen sistema de captura de leads (Formularios).")
            
        if not flaws:
            flaws.append("OPORTUNIDAD: Tienen lo básico, pero falta un Agente de IA para responder 24/7.")

        return flaws
    except Exception as e:
        return [f"Error al escanear: {e}"]

def generate_report(url, flaws):
    print(f"[+] Generando reporte corporativo premium para enviar al dueño...")
    domain = url.split("//")[-1].split("/")[0]
    
    # Generando las listas de fallas con íconos de Tailwind/FontAwesome
    flaws_html = "".join([f'<li class="flex items-start"><span class="text-red-500 mr-3">⚠️</span><span class="text-gray-300">{f}</span></li>' for f in flaws])
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Auditoría Técnica - {domain}</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-[#0b1325] text-gray-200 font-sans antialiased p-4 md:p-10">
        <div class="max-w-4xl mx-auto bg-gray-900 border border-gray-800 rounded-2xl shadow-2xl overflow-hidden">
            <!-- Cabecera Corporativa -->
            <div class="bg-gray-950 border-b border-gray-800 p-6 flex justify-between items-center">
                <div class="flex items-center space-x-3">
                    <div class="w-3 h-3 bg-red-500 rounded-full animate-pulse"></div>
                    <h1 class="text-xl font-bold tracking-widest text-white uppercase">AURA INTELLIGENCE LAB</h1>
                </div>
                <span class="text-xs font-mono text-gray-500">ID DE REPORTE: {int(datetime.now().timestamp())}</span>
            </div>
            
            <!-- Cuerpo del Reporte -->
            <div class="p-8 md:p-12">
                <h2 class="text-3xl font-bold text-white mb-2">Auditoría Técnica de Conversión</h2>
                <p class="text-gray-400 mb-8 font-mono">Objetivo Escaneado: <span class="text-[#00f3ff]">{domain}</span> | Fecha: {datetime.now().strftime('%d/%m/%Y')}</p>
                
                <div class="bg-red-900/20 border border-red-500/30 rounded-xl p-6 mb-8">
                    <h3 class="text-red-400 font-bold mb-4 uppercase tracking-wide">Fugas de Capital Detectadas</h3>
                    <ul class="space-y-4">
                        {flaws_html}
                    </ul>
                </div>

                <div class="bg-gray-800/50 border border-gray-700 rounded-xl p-6 mb-8">
                    <h3 class="text-gray-300 font-bold mb-2">Análisis de Impacto Financiero</h3>
                    <p class="text-gray-400 text-sm leading-relaxed">El tráfico actual que llega a su sitio web está abandonando la página debido a fricción en los canales de contacto. Las inmobiliarias líderes en 2026 utilizan <strong>Ecosistemas Digitales Inteligentes</strong> para calificar al 100% de los visitantes en tiempo real, perfilando presupuestos y agendando visitas automáticamente 24/7 sin intervención humana.</p>
                </div>

                <!-- Call to Action -->
                <div class="bg-gradient-to-r from-gray-900 to-[#0b1325] border border-[#00f3ff]/30 p-8 rounded-xl text-center">
                    <h3 class="text-xl font-bold text-white mb-4">Detenga la pérdida de clientes hoy.</h3>
                    <p class="text-gray-400 text-sm mb-6">Agende una llamada técnica de 15 minutos con nuestro Arquitecto de Software para ver una demostración en vivo del sistema instalado en su sitio.</p>
                    <a href="#" class="inline-block bg-[#00f3ff] text-black font-bold py-3 px-8 rounded hover:bg-cyan-400 transition shadow-[0_0_15px_rgba(0,243,255,0.4)]">
                        Agendar Demostración (Google Meet)
                    </a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    report_path = f"reporte_{domain}.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"[!] REPORTE PREMIUM CREADO: {report_path}")
    print(f"[!] MENSAJE LISTO PARA ENVIAR EN LINKEDIN: 'Hola, armé un reporte técnico sobre las fallas de tu web. Te lo dejo acá: [Link al reporte]'")

if __name__ == "__main__":
    # Test real de Inmobiliaria
    target_url = "https://www.remax.com.ar" 
    flaws_found = analyze_website(target_url)
    generate_report(target_url, flaws_found)

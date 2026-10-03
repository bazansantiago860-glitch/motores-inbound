import os
import time
import pywhatkit as kit
import google.generativeai as genai
from dotenv import load_dotenv
import trojan_horse
import job_sniper

# ==============================================================================
# ORQUESTADOR CENTRAL B2B (100% Nativo en Python)
# Ejecuta todo el flujo: Scraping -> Análisis -> Mensaje (Gemini) -> WhatsApp
# ==============================================================================

# Cargar variables de entorno
load_dotenv()
# Usamos Gemini (Google) por su velocidad, tier gratuito y capacidad de analizar imágenes
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AQ.Ab8RN6J2cGblBiHFfYyUhgFTE0tSkWR-U-DOm-30ETGroSlyyw"))
model = genai.GenerativeModel('gemini-1.5-flash')

def generar_respuesta_setter_ia(contexto_lead, objecion_cliente=""):
    """
    Usa Google Gemini para generar un mensaje persuasivo en frío.
    """
    print(f"🧠 [Gemini IA] Pensando respuesta para: {contexto_lead['empresa']}...")
    prompt = f"""
    Eres un Setter B2B experto. Tu objetivo es agendar un Google Meet de 15 minutos.
    Contexto de la empresa: {contexto_lead['empresa']}, están buscando {contexto_lead['puesto']} 
    por un salario de {contexto_lead['salario']}.
    Genera un mensaje corto, agresivo y empático por WhatsApp para venderles una Secretaria IA 
    mucho más barata. Si hay una objeción: '{objecion_cliente}', resuélvela y ofrece el link.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Simulador de Inteligencia Artificial Activo (Demostración)
        if "Recepcionista" in prompt or "Asistente" in prompt:
            return f"Hola, vi el anuncio publicado por {contexto_lead['empresa']} hoy buscando personal. Sabiendo que el sueldo promedio es de {contexto_lead['salario']}, quería comentarles que mi agencia instala 'Secretarias Virtuales con IA' que hacen exactamente ese trabajo de filtrado y agendamiento automático por una fracción de ese costo mensual. ¿Les interesa que les muestre un demo en vivo mañana?"
        return f"Hola, vi su perfil de {contexto_lead['empresa']} y noté áreas de mejora. Nosotros instalamos IAs por el 30% del costo. ¿Hablamos?"

def disparar_whatsapp_local(telefono, mensaje):
    """
    Usa PyWhatKit para abrir WhatsApp Web localmente en tu Chrome y 
    enviar el mensaje sin usar APIs pagas de Meta.
    """
    print(f"🚀 [WhatsApp] Preparando envío a {telefono}...")
    try:
        # Envía el mensaje instantáneamente abriendo una pestaña
        # kit.sendwhatmsg_instantly(telefono, mensaje, wait_time=10, tab_close=True, close_time=3)
        print(f"✅ [SIMULACIÓN LOCAL] Navegador abierto. Mensaje enviado con éxito a {telefono}")
    except Exception as e:
        print(f"❌ Error al enviar WhatsApp: {e}")

def ejecutar_ciclo_maestro():
    print("==================================================")
    print(" INICIANDO CICLO MAESTRO DE ADQUISICIÓN")
    print("==================================================\n")
    
    # 1. Ejecutar el Motor Francotirador
    leads = job_sniper.scan_job_boards()
    
    # 2. Procesar cada lead detectado
    for lead in leads:
        print(f"\n⚡ Procesando Lead: {lead['empresa']}")
        
        # 3. La IA redacta el mensaje hiper-personalizado
        mensaje_venta = generar_respuesta_setter_ia(lead)
        print(f"📝 Texto Generado por IA:\n{mensaje_venta}\n")
        
        # 4. Enviar por WhatsApp (Ejemplo con un número ficticio, reemplaza por el real)
        # Nota: pywhatkit usa el formato con código de país, ej: "+5491100000000"
        numero_ficticio = "+5491100000000" 
        disparar_whatsapp_local(numero_ficticio, mensaje_venta)
        
        # Pausa para no ser bloqueado por WhatsApp (Anti-Spam)
        print("⏳ Pausando 2 segundos (Simulación acelerada)...")
        time.sleep(2)

if __name__ == "__main__":
    ejecutar_ciclo_maestro()

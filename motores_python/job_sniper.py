import json
from datetime import datetime

# ==============================================================================
# MOTOR 2: EL FRANCOTIRADOR DE EMPLEOS (Lógica Base)
# ==============================================================================

def scan_job_boards(keyword="Recepcionista"):
    print(f"[+] Iniciando rastreo de empleos buscando: '{keyword}'...")
    
    # Simulación del Scraper (Acá se conecta la API de LinkedIn Jobs o Computrabajo)
    # Para la prueba, simulamos 3 avisos encontrados hoy.
    jobs_found = [
        {"empresa": "Inmobiliaria Palermo Group", "puesto": "Asistente Virtual / Recepcionista", "salario": "$500 USD"},
        {"empresa": "Desarrollos Norte", "puesto": "Secretaria Administrativa", "salario": "$400 USD"},
        {"empresa": "TechCorp SA", "puesto": "Atención al Cliente B2B", "salario": "$600 USD"}
    ]
    
    print(f"[!] Se detectaron {len(jobs_found)} empresas quemando presupuesto en contratación humana.")
    return jobs_found

def generate_outreach_sequence(jobs):
    print("\n[+] Generando Mensajes de Intercepción Directa para los Dueños/CEOs:\n")
    
    for job in jobs:
        empresa = job["empresa"]
        sueldo = job["salario"]
        
        mensaje_frio = (
            f"🎯 OBJETIVO: CEO de {empresa}\n"
            f"💬 MENSAJE DE ATAQUE:\n"
            f"'Hola, vi que publicaron hoy buscando contratar personal de {job['puesto']}. "
            f"Asumo que el presupuesto mensual ronda los {sueldo}. Por una fracción de ese costo, "
            f"les instalo una Secretaria de IA que trabaja 24/7, agenda clientes directo a su calendario "
            f"y atiende a 100 personas en simultáneo. ¿Tienen 10 minutos mañana para mostrarles un demo?'\n"
            f"-----------------------------------------------------------------"
        )
        print(mensaje_frio)

if __name__ == "__main__":
    leads_urgentes = scan_job_boards()
    generate_outreach_sequence(leads_urgentes)

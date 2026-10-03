import streamlit as st
import pandas as pd
from datetime import datetime

# ==============================================================================
# CENTRO DE COMANDO B2B (REEMPLAZO DE MAKE.COM)
# Ejecutar con: streamlit run dashboard_comando.py
# ==============================================================================

st.set_page_config(page_title="NovaTech Command Center", layout="wide")

st.title("🛰️ NovaTech - Centro de Comando Autónomo")
st.markdown("Monitor de Agentes IA operando en tiempo real. Cero dependencias externas.")

# Métricas rápidas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Leads Extraídos Hoy", "42")
col2.metric("Mensajes Enviados", "38")
col3.metric("Respuestas Recibidas", "5")
col4.metric("Zooms Agendados", "2", "+2")

st.divider()

# Monitor de Leads
st.subheader("📡 Radar de Prospectos (Motor Francotirador & Troya)")
datos_mock = {
    "Empresa": ["Inmobiliaria Palermo", "Desarrollos Norte", "Consultora B2B"],
    "Teléfono": ["+54 9 11 1234-5678", "+54 9 11 8765-4321", "+54 9 11 5555-5555"],
    "Falla Detectada": ["No tiene WhatsApp", "Busca Secretaria", "Web Lenta"],
    "Estado del Agente": ["Mensaje Enviado", "En Conversación", "Zoom Agendado"]
}
df = pd.DataFrame(datos_mock)
st.dataframe(df, use_container_width=True)

st.divider()

# Monitor de Chats en Vivo
st.subheader("💬 Consola de Setter IA (Intercepción de WhatsApp en vivo)")
chat_log = st.container(height=300)
with chat_log:
    st.markdown("**[10:15 AM] Inmobiliaria Palermo:** Hola, vi tu reporte. ¿Cómo es eso de la secretaria virtual?")
    st.markdown("🤖 **[10:15 AM] Agente Setter IA:** ¡Hola! Es un sistema que pre-califica a tus compradores por WhatsApp antes de pasártelos, así no perdés tiempo respondiendo precios. ¿Tenés 5 min mañana a la mañana para mostrarte cómo funciona en pantalla?")
    st.markdown("**[10:22 AM] Inmobiliaria Palermo:** Dale, a las 11 am me viene bien.")
    st.markdown("🤖 **[10:22 AM] Agente Setter IA:** ¡Perfecto! Te acabo de agendar. Te llega el link de Google Meet por acá. ¡Nos vemos mañana!")

st.success("Operación 100% local. Sin Make.com. Sin cuotas mensuales.")

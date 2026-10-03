from flask import Flask, request, render_template_string
import trojan_horse

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditoría IA para Inmobiliarias</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #0b1325; color: #ffffff; }
        .neon-border { border: 1px solid #00f3ff; box-shadow: 0 0 10px #00f3ff; }
    </style>
</head>
<body class="flex items-center justify-center min-h-screen p-4">
    <div class="max-w-2xl w-full bg-gray-900 p-8 rounded-xl neon-border">
        <div class="text-center mb-8">
            <h1 class="text-3xl md:text-4xl font-bold text-white mb-4">¿Estás perdiendo ventas en WhatsApp?</h1>
        </div>
        <div class="bg-gray-800 p-6 rounded-lg mb-8 border border-gray-700">
            <form action="/auditar" method="POST" class="space-y-4">
                <div>
                    <label class="block text-sm text-gray-400 mb-1">Sitio Web (Para escanear fallas)</label>
                    <input type="url" name="sitio_web" required class="w-full bg-gray-900 border border-gray-600 rounded p-3 text-white" placeholder="https://www.remax.com.ar">
                </div>
                <div>
                    <label class="block text-sm text-gray-400 mb-1">WhatsApp</label>
                    <input type="text" name="telefono" required class="w-full bg-gray-900 border border-gray-600 rounded p-3 text-white" placeholder="+54 9 11...">
                </div>
                <button type="submit" class="w-full bg-[#00f3ff] text-black font-bold py-3 rounded">
                    ESCANEAR MI NEGOCIO AHORA
                </button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/auditar', methods=['POST'])
def auditar():
    sitio_web = request.form.get('sitio_web')
    telefono = request.form.get('telefono')
    
    print(f"\n[+] NUEVO LEAD INBOUND]")
    print(f"Teléfono: {telefono}")
    print(f"Web a auditar: {sitio_web}")
    
    # Llamamos al script trojan_horse que creamos antes
    fallas = trojan_horse.analyze_website(sitio_web)
    trojan_horse.generate_report(sitio_web, fallas)
    
    # Respuesta para el usuario en la web
    return f"""
    <body style="background-color: #0b1325; color: #00f3ff; text-align: center; padding-top: 20%; font-family: sans-serif;">
        <h1>¡Auditoría Completada!</h1>
        <p>El escaneo de {sitio_web} finalizó.</p>
        <p>Revisa la terminal de tu computadora para ver cómo el sistema interceptó tu número: {telefono}</p>
        <p>(Recuerda: El envío real de WhatsApp está bloqueado por el Seguro de Simulación en el código)</p>
        <a href="/" style="color: white; text-decoration: underline;">Volver</a>
    </body>
    """

if __name__ == '__main__':
    print("\n===========================================")
    print("SERVIDOR INBOUND ACTIVADO EN EL PUERTO 5000")
    print("Entra a: http://127.0.0.1:5000")
    print("===========================================\n")
    app.run(debug=True, port=5000)

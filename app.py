import os
from flask import Flask, request, jsonify
from flask_cors import CORS
# Asegúrate de que este módulo existe en tu estructura de carpetas
from src.business_logic import process_data

app = Flask(__name__)

# 1. CONFIGURACIÓN DE CORS COMPLETA
# Se define a nivel de aplicación para capturar todas las rutas /api/
CORS(
    app,
    resources={
        r"/api/*": {
            "origins": [
                "*"
            ],
            "methods": ["POST", "OPTIONS"],
            "allow_headers": ["Authorization", "Content-Type", "X-Client-Identifier"],
            "max_age": 3600 # Cachear la respuesta de OPTIONS por 1 hora
        }
    }
)

# 2. RUTA CON MÉTODOS EXPLÍCITOS
# Es VITAL incluir 'OPTIONS' aquí para que flask-cors intercepte el preflight
@app.route('/api/v1/special/task', methods=['POST', 'OPTIONS'])
def handle_request():
    # Si la petición es OPTIONS, flask-cors ya respondió automáticamente antes de entrar aquí.
    # No obstante, si entrara, devolvemos una respuesta vacía exitosa.
    if request.method == 'OPTIONS':
        return '', 204

    # --- LÓGICA PARA EL MÉTODO POST ---

    # Extraer identificador (enviado por el cliente o inyectado por el Gateway)
    client_id = request.headers.get('X-Client-Identifier', 'CLIENTE_DESCONOCIDO')
    
    # Intentar obtener el cuerpo JSON
    try:
        input_data = request.get_json()
        if input_data is None:
            input_data = {}
    except Exception:
        return jsonify({"error": "Invalid JSON body"}), 400

    # Invocación de la lógica de negocio modularizada
    try:
        result = process_data(client_id, input_data)
        return jsonify({
            "status": "Servicio-B Ejecutado", 
            "result": result
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Cloud Run usa la variable de entorno PORT
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
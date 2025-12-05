# servicio-a/app.py

import os
from flask import Flask, request, jsonify
from src.business_logic import process_data

# Flask se inicializa y Gunicorn lo utilizará
app = Flask(__name__)

# Definición de la ruta
@app.route('/api/v1/process/data', methods=['POST'])
def handle_request():
    
    # 🚨 Pauta de Seguridad y Contexto (Importante) 🚨
    # El API Gateway adjuntará la identidad autenticada 
    # en un header especial. Usaremos un header de prueba por ahora.
    # En producción, se usaría 'X-Apigw-Api-Key' o similares.
    
    # Simulación de extracción de un identificador del cliente (AuthN/AuthZ)
    client_id = request.headers.get('X-Client-Identifier', 'CLIENTE_DESCONOCIDO')
    
    try:
        input_data = request.get_json()
    except Exception:
        # Manejo de error si el cuerpo no es JSON válido
        input_data = {'message': 'No JSON body provided'}

    # Invocación de la lógica de negocio modularizada
    result = process_data(client_id, input_data)
    
    return jsonify({"status": "Servicio-A Ejecutado", "result": result}), 200

if __name__ == '__main__':
    # Cloud Run usa la variable de entorno PORT para la escucha
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
# servicio-b/src/business_logic.py

def process_data(client_identifier: str, input_data: dict) -> str:
    """
    Simula la lógica de negocio del Servicio B.
    
    Esta función solo será invocada si el API Gateway ha autenticado
    y autorizado previamente al cliente.
    """
    # En el entorno real, 'client_identifier' provendría del JWT validado 
    # y se usaría para auditoría o lógica específica del cliente.
    
    input_str = str(input_data.get('message', 'datos_de_prueba_default'))
    
    response = (f"✅ OK: Recibido por SERVICIO-B. "
                f"Identificador Cliente: {client_identifier}. "
                f"Mensaje: '{input_str}'")
    
    return response

# Si se requiere alguna clase o inicialización compleja, iría aquí
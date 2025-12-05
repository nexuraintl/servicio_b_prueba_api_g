# servicio-a/Dockerfile

# Usamos una imagen base ligera de Python
FROM python:3.11-slim

# Establecer la carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas (optimización de capas de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Comando para iniciar el servidor usando Gunicorn (Mejor Práctica para Cloud Run)
# Gunicorn utiliza el archivo 'app.py' y la variable 'app' (Flask app)
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
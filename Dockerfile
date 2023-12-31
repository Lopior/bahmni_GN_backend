# Usa la imagen oficial de Python como base
FROM python:3.12

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor en /app
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido actual al contenedor en /app
COPY backend/ /app/

# Expone el puerto 5000 (el mismo que está configurado en tu aplicación Flask)
EXPOSE 8093

# Ejecuta los scripts cuando el contenedor se inicia
CMD ["python", "app.py"] 

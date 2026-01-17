# Usamos una imagen base oficial de Python
FROM python:3.12-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Evitamos que Python genere archivos .pyc y activamos logs inmediatos
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copiamos las dependencias del proyecto
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código fuente
COPY . .

# Documentamos que el contenedor escuchará en el puerto 8080
EXPOSE 8080

# Comando para ejecutar la aplicación
# Dejamos el host en 0.0.0.0 ya que es necesario para que Docker escuche desde fuera
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
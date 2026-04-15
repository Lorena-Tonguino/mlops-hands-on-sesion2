# Imagen base: Python 3.11 en versión 'slim' (ligera). 
# Nota: 'slim' reduce el tamaño pero no trae librerías de C++ (como libgomp1), hay que instalarlas aparte.
FROM python:3.11-slim

# 1. Instalamos las dependencias del sistema
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# 2. Establecemos el directorio de trabajo
WORKDIR /app

# 3. Copiamos los archivos y los requerimientos
COPY requirements.txt .

# 4. Instalamos las librerías de Python
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el resto de la aplicación
COPY . .

# 6. Comando para iniciar la app
CMD ["python", "app.py"]

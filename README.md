# Laboratorio MLOps: Predicción de Seguros Médicos

Este proyecto consiste en el despliegue de un modelo de regresión entrenado para predecir los costos anuales de seguros médicos basado en características del paciente.

## Tecnologías Utilizadas
* **Python 3.11-slim**: Base del sistema.
* **Flask**: Framework para la interfaz web y API.
* **PyCaret**: Librería para la inferencia del modelo de Machine Learning.
* **Docker**: Containerización del entorno para asegurar la portabilidad.

## Configuración de Infraestructura
Para solucionar problemas de dependencias en arquitecturas ligeras (Linux Slim), se incluyó en el `Dockerfile` la instalación manual de:
* `libgomp1`: Necesaria para el funcionamiento de LightGBM.

## Ejecución del Proyecto
Para construir y correr esta aplicación en cualquier entorno con Docker, use los siguientes comandos:

1. **Construir la imagen:**
   ```bash
   docker build -t mi-app-medica:v1 .

2. **Ejecutar el contenedor:**

   ```bash    
   docker run -p 5000:5000 mi-app-medica:v1

3. **Acceso local:**

   Abrir en el navegador: http://localhost:5000


## Solución de Problemas (Lecciones Aprendidas)

Durante el desarrollo se identificaron y resolvieron los siguientes puntos críticos:

1. **Error de Librerías en Imágenes Slim (`OSError: libgomp.so.1`):**
   * *Problema:* Las imágenes de Docker tipo "slim" son muy ligeras y no incluyen librerías de procesamiento paralelo.
   * *Solución:* Se debe añadir `apt-get install -y libgomp1` en el Dockerfile y reconstruir la imagen.

2. **Conexión con el Daemon de Docker:**
   * *Problema:* Error al conectar con la API de Docker (Engine no disponible).
   * *Solución:* Asegurarse de que **Docker Desktop** esté abierto y en estado "Running" (verde) antes de ejecutar comandos en la terminal.

3. **Acceso desde el Host al Contenedor:**
   * *Problema:* La aplicación no cargaba en el navegador de Windows.
   * *Solución:* Configurar Flask para escuchar en `host='0.0.0.0'` y realizar el mapeo de puertos `-p 5000:5000` al ejecutar el contenedor.

4. **Persistencia de Cambios:**
   * *Recomendación:* Siempre que se modifique el `Dockerfile` o el código `app.py`, es necesario realizar un nuevo `docker build` para que los cambios se apliquen a la imagen.
   

   
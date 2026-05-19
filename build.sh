#!/bin/bash

# 1. Limpiar contenedores anteriores para evitar choques de nombres
echo "Limpiando contenedores antiguos..."
docker rm -f indicator-running 2>/dev/null || true

# 2. Construir la imagen de la aplicación de Digimon
echo "Construyendo la imagen digimon-app..."
docker build -t digimon-app .

# 3. Ejecutar el contenedor pasando la variable de entorno obligatoria
echo "Iniciando el contenedor..."
docker run --name indicator-running -e API_URL_PROYECTO="https://digimon-api.vercel.app/api/digimon/name/" digimon-app

# 4. Documentar la salida para las evidencias (output.txt)
echo "Generando registro de salida..."
docker ps -a --filter "name=indicator-running" > output.txt
docker logs indicator-running >> output.txt

echo "Proceso de automatización finalizado con éxito."

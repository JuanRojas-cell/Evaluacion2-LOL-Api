#!/bin/bash

# 1. Definir la variable de entorno localmente
export API_URL_PROYECTO="https://ddragon.leagueoflegends.com/cdn/13.18.1/data/es_ES/champion/Aatrox.json"

echo "=== 1. Construyendo la imagen Docker ==="
docker build -t lol-app .

echo "=== 2. Borrando contenedor antiguo si existe ==="
docker rm -f indicator-running 2>/dev/null

echo "=== 3. Corriendo el nuevo contenedor ==="
# Ejecutamos el contenedor pasándole la variable de entorno
docker run --name indicator-running -e API_URL_PROYECTO=$API_URL_PROYECTO lol-app
# Analizador de Campeones - League of Legends (LoL-Stats)

## 1. Definición del Contexto y Narrativa
* **Stakeholder:** Un Analista de Esports y Entrenador de League of Legends. Necesita revisar las estadísticas base de los campeones antes de una partida para planificar estrategias.
* **Propuesta de Valor:** Este usuario pierde tiempo buscando en páginas web llenas de publicidad. Mi aplicación soluciona esto consultando la API de Riot de forma automática, procesando los datos y mostrando la Vida y el Maná del campeón directamente en la consola de forma rápida.

---

## 2. Guía de Configuración
Para que la aplicación funcione de forma segura y sin dejar rutas fijas en el código, se usa la siguiente variable de entorno:

* **Variable:** `API_URL_PROYECTO`
* **Valor:** `https://ddragon.leagueoflegends.com/cdn/13.18.1/data/es_ES/champion/Aatrox.json`

### Comandos para activar la variable:
* **En Linux:** `export API_URL_PROYECTO="https://ddragon.leagueoflegends.com/cdn/13.18.1/data/es_ES/champion/Aatrox.json"`
* **En Windows:** `$env:API_URL_PROYECTO = "https://ddragon.leagueoflegends.com/cdn/13.18.1/data/es_ES/champion/Aatrox.json"`

---

## 3. Instrucciones de Ejecución (Docker)
Comandos obligatorios para crear la imagen y correr el contenedor:

```bash
# 1. Construir la imagen Docker
docker build -t lol-app .

# 2. Correr el contenedor pasándole la variable
docker run --name indicator-running -e API_URL_PROYECTO=$API_URL_PROYECTO lol-app
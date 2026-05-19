# Analizador de Digimon - Sistema de Consultas (Digimon-Stats)

## 1. Definición del Contexto y Narrativa

* **Stakeholder:** Un Investigador Digital y Coleccionista del Mundo Digimon. Necesita revisar las estadísticas y niveles de evolución de los Digimon de forma rápida para planificar estrategias de combate y entrenamiento.
* **Propuesta de Valor:** Este usuario pierde demasiado tiempo buscando datos en wikis desactualizadas o páginas web llenas de publicidad invasiva. Nuestra aplicación soluciona este problema consultando la API pública de Digimon de forma automatizada, procesando los datos de forma nativa en un contenedor y mostrando el Nombre, Nivel y URL de la imagen del Digimon directamente en la consola de manera limpia, rápida y segura.

---

## 2. Guía de Configuración

Para que la aplicación funcione de forma segura, dinámica y sin dejar rutas fijas (*hardcodeadas*) en el código fuente, se utiliza una variable de entorno para parametrizar el punto de enlace de la API:

* **Variable:** `API_URL_PROYECTO`
* **Valor por defecto (Ejemplo Agumon):** `https://digimon-api.vercel.app/api/digimon/name/`

### Comandos para activar la variable de entorno:

* **En Linux / Bash:**
  ```bash
  export API_URL_PROYECTO="[https://digimon-api.vercel.app/api/digimon/name/](https://digimon-api.vercel.app/api/digimon/name/)"

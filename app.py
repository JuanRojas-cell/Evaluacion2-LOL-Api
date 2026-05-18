import os
import requests

def consultar_lol():
    # Lee la URL desde las variables de entorno para cumplir seguridad
    url_api = os.getenv('API_URL_PROYECTO')
    
    if not url_api:
        print("ERROR CRÍTICO: Falta configurar la variable 'API_URL_PROYECTO'.")
        return

    try:
        # Hacemos la consulta a la base de datos de Riot
        respuesta = requests.get(url_api, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        # Entramos al diccionario para sacar los datos de Aatrox
        info_campeon = datos['data']['Aatrox']
        
        # Mostramos los 3 datos que pide la guía (Nombre, Vida y Maná)
        print("\n=== ANALIZADOR DE CAMPEONES: LEAGUE OF LEGENDS ===")
        print(f"Campeón: {info_campeon['name']} ({info_campeon['title']})")
        print(f"Vida Base: {info_campeon['stats']['hp']} HP")
        print(f"Maná Base: {info_campeon['stats']['mp']} MP")
        print("==================================================\n")

    # Los 4 manejos de errores obligatorios
    except requests.exceptions.ConnectionError:
        print("Error 1: No hay conexión a internet.")
    except requests.exceptions.Timeout:
        print("Error 2: El servidor de Riot tardó demasiado.")
    except requests.exceptions.HTTPError:
        print("Error 3: No se encontró el campeón (404 Error).")
    except Exception as e:
        print(f"Error 4: Error inesperado al procesar: {e}")

if __name__ == "__main__":
    consultar_lol()
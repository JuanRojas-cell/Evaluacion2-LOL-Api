import os
import sys
import requests


def buscar_digimon_automatico():
    # 1. Variable de entorno obligatoria de la pauta. Por defecto busca a Agumon.
    api_url_base = os.getenv(
        "API_URL_PROYECTO", "https://digimon-api.vercel.app/api/digimon/name/"
    )
    digimon_por_defecto = "agumon"

    url_final = f"{api_url_base}{digimon_por_defecto}"

    print("\n--- INICIANDO CONTENEDOR DIGIMON API ---")
    print(f"Conectando a: {url_final}")

    try:
        # 2. Petición con tiempo límite de 10 segundos
        response = requests.get(url_final, timeout=10)
        response.raise_for_status()
        data = response.json()

        # La API devuelve una lista, extraemos el primer elemento [0]
        nombre = data[0]["name"]
        nivel = data[0]["level"]
        imagen = data[0]["img"]

        # 3. Impresión limpia para los Logs de Jenkins y Docker
        print("\n========================================")
        print("DATOS DEL DIGIMON OBTENIDOS CON ÉXITO:")
        print(f"Nombre: {nombre}")
        print(f"Nivel: {nivel}")
        print(f"URL Imagen: {imagen}")
        print("========================================")
        print("Contenedor ejecutado correctamente.")

    except requests.exceptions.HTTPError:
        print(f"Error 1: No se encontró al Digimon '{digimon_por_defecto}'.")
    except requests.exceptions.ConnectionError:
        print("Error 2: Problema de red o internet dentro del contenedor.")
    except requests.exceptions.Timeout:
        print("Error 3: Tiempo de espera agotado al conectar con la API.")
    except (ValueError, KeyError, IndexError):
        print("Error 4: Los datos recibidos no tienen el formato JSON correcto.")


if __name__ == "__main__":
    # Ejecuta una vez y cierra limpio (Exited 0) para que Jenkins no se quede pegado
    buscar_digimon_automatico()
    sys.exit(0)

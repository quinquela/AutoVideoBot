import json
import random

def Eleccion(ruta_json):

    try:
        with open(ruta_json, "r", encoding="utf-8") as file:
            data = json.load(file)

        return random.choice(list(data.keys()))
    except Exception as e:
        print(f"Error al procesar el archivo JSON: {e}")
        return None



    
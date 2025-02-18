from elegirVideo import Eleccion
import meme
from meme import generar_meme
import videoPeleaTipo1
from videoPeleaTipo1 import editarVideo
import json
import os 

def juntarTodo(rutaJson):
    cantidad = input("Enter the number of videos:")
    idioma = input("Language")
    cantidad2 = int(cantidad)

    base_dir = os.path.dirname(os.path.abspath(rutaJson))
    for i in range(cantidad2):
        
        #ABRIR EL JSON
        videoElegido = Eleccion(rutaJson)
        with open(f'{rutaJson}', 'r') as archivo:
           datos = json.load(archivo)
        ruta_relativa = datos[videoElegido]['file_path']
        #EXTRAER DATOS DEL JSON
        ruta_del_video = os.path.join(base_dir, ruta_relativa)
        descripcion = datos[f'{videoElegido}']['description']
        recomendacion = datos[f'{videoElegido}']['recommendation']
        ejemplo = datos[f'{videoElegido}']['example']
        #CHISTE
        chiste1 = generar_meme(descripcion, recomendacion, ejemplo, idioma)
        chiste2 = str(chiste1)
        chiste3 = chiste2.strip().replace("\n", " ")
        #VIDEO
        print(ruta_del_video)
        editarVideo(texto=chiste3, path=ruta_del_video)
    

    
    

juntarTodo("ejemplosVideos.json")

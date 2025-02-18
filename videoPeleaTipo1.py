import ffmpeg
import re
import random
import subprocess
import json
import os
final_width = 1080
final_height = 1920

base_dir = os.path.dirname(os.path.abspath(__file__))






def get_video_duration(video_path):
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", video_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    
    info = json.loads(result.stdout)
    return float(info["format"]["duration"])

def editarVideo(texto, path):
    numero = random.randint(0, 9999)
    nombre = str(numero)

    canciones = [
    r"audios\disturbing_the_peaceeeee (mp3cut.net).mp3",
    r"audios\a.mp3",
    r"audios\b.mp3",
    r"audios\c.mp3",
    r"audios\d.mp3",
    r"audios\f.mp3",]
    cancion = random.choice(canciones)
    cancion_absoluta = os.path.join(base_dir, cancion)
    output_path = os.path.join(base_dir, f"outputVideos/{nombre}.mp4")




    #EXTRAER DATOS DEL VIDEO
    input_file = f"{path}" # Tu video original
    duracion = get_video_duration(path)
    audio = ffmpeg.input(cancion) 
    audio_trimmed = ffmpeg.filter_(audio, 'atrim', duration = duracion)
    output_file = output_path
    info = ffmpeg.probe(input_file)
    video_streams = [stream for stream in info['streams'] if stream['codec_type'] == 'video']
    ancho = video_streams[0]["width"]
    alto = video_streams[0]["height"]
    anchoTexto = len(texto)

    
    if anchoTexto < 43:
        fontsize = 45
    elif anchoTexto > 43 and anchoTexto < 50:
        fontsize = 36
    elif anchoTexto >= 50:
        fontsize = 28
    else:
        fontsize = 33
    #ajustar resolucion
    if ancho / alto > 1080 / 1080:
        new_ancho = 1080
        new_alto = int((1080 / ancho) * alto)
    else:
        new_alto = 1080
        new_ancho = int((1080 / alto) * ancho)



    



    video = (
        ffmpeg.input(input_file)
        .filter("scale", new_ancho, new_alto)
        .filter("pad", 1080, 1920, "(ow-iw)/2", "1450-ih")
        .filter("drawtext",
                text=texto,
                x="w/2-text_w/2",
                y = 500,
                fontfile = r"C:\Users\manda\OneDrive\Escritorio\programacion\proyectos\VideosAutomatizados\fuente\Open_Sans\OpenSans-Italic-VariableFont_wdth,wght.ttf",
                fontsize = fontsize,
                fontcolor = "white",
                shadowcolor="black",
                shadowx=2,          
                shadowy=2,
                  )
        
    )
    out = ffmpeg.output(audio_trimmed, video, output_file, shortest=None)
    out.run(overwrite_output=True)

    
    

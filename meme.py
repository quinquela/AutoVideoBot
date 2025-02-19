import os
from google import genai
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'variables.env')
load_dotenv(dotenv_path)
apikey = os.getenv("API_KEY")
client = genai.Client(api_key=apikey)
def generar_meme(descripcion, recomendacion, ejemplo, idioma):
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=(f"Respond in {idioma} and Respond only with the text that goes over the video . Create a meme with a video and a caption on top. I'll give you the video's description, a joke suggestion, and an example. Description: {descripcion}. Suggestion: {recomendacion}. Example: {ejemplo}. Respond only with the text that goes over the video, no more than 50 characters including spaces. Avoid special characters except asterisks, and don't use line breaks. Respond only with the text that goes over the video"))
    
    return response.text


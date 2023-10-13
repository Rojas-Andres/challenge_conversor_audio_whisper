import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
import whisper

def convert_audio_to_mp3(input_path, output_dir="media"):
    """
    Convierte un archivo de audio a MP3 usando pydub. Si el archivo ya es MP3, simplemente devuelve la ruta original.
    
    Parámetros:
    - input_path (str): Ruta del archivo de audio de entrada.
    - output_dir (str): Directorio donde se guardará el archivo MP3 convertido si es necesario.
    
    Retorna:
    - str: Ruta del archivo MP3, ya sea convertido o el original si ya era MP3.
    """
    # Verificar que el archivo de entrada existe
    if not os.path.exists(input_path):
        print(f"Error: El archivo {input_path} no existe.")
        return None

    # Comprobar si el archivo ya es MP3
    if input_path.lower().endswith('.mp3'):
        print("El archivo ya es MP3. No se requiere conversión.")
        return input_path

    # Extraer el nombre del archivo sin extensión y formatear la ruta de salida
    filename_without_ext = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_dir, f"{filename_without_ext}.mp3")

    # Crear el directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Convertir el archivo a MP3
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="mp3")
        print("Conversión completada exitosamente.")
        return output_path
    except CouldntDecodeError:
        print(f"Error: No se pudo decodificar el archivo {input_path}.")
        return None
    except Exception as e:
        print(f"Error inesperado durante la conversión: {e}")
        return None

def convert_audio_to_text(input_audio):
    """
    Convierte un archivo de audio en texto usando el modelo Whisper.
    
    Parámetros:
    - input_audio (str): Ruta del archivo de audio a transcribir.
    
    Retorna:
    - str: Texto transcribido del audio si la transcripción es exitosa, None en caso contrario.
    """
    # Verificar que el archivo de entrada existe
    if not os.path.exists(input_audio):
        print(f"Error: El archivo {input_audio} no existe.")
        return None
    try:
        # Cargar el modelo Whisper
        model = whisper.load_model("base")
    except Exception as e:
        print(f"Error al cargar el modelo Whisper: {e}")
        return None
    try:
        # Transcribir el audio
        result = model.transcribe(input_audio)
        return result["text"]
    except KeyError:
        print("Error: El resultado de la transcripción no contiene la clave 'text'.")
        return None
    except Exception as e:
        print(f"Error inesperado durante la transcripción: {e}")
        return None
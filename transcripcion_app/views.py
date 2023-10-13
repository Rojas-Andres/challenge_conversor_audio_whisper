from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .utils import convert_audio_to_mp3, convert_audio_to_text


class TranscripcionView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request):
        file = request.data['file']
        
        # Guardar el archivo temporalmente
        with open("temp_audio", "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Convertir a MP3 y transcribir
        output_audio = convert_audio_to_mp3("temp_audio")
        output_text = convert_audio_to_text(output_audio)

        # Limpiar el archivo temporal
        os.remove("temp_audio")
        if output_audio != "temp_audio":
            os.remove(output_audio)

        if output_text:
            return Response({"transcription": output_text}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Transcripción fallida"}, status=status.HTTP_400_BAD_REQUEST)

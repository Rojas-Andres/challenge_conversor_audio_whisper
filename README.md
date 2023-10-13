# Transcripción de Audio con Django y AWS Lambda

Este proyecto proporciona un microservicio construido con Django que acepta archivos multimedia, los convierte a formato MP3 y luego transcribe el contenido de audio a texto utilizando el modelo Whisper.

## Características
* Conversión a MP3: Convierte cualquier archivo  multimedia aceptado a formato MP3.
* Transcripción Automática: Usa el modelo Whisper para convertir el contenido de audio a texto.
* Despliegue Serverless: Desplegado como función AWS Lambda para escalabilidad y eficiencia.
## Requisitos previos
* Python 3.x
* Entorno virtual (virtualenv o venv)
* Cuenta de AWS y AWS CLI configurado
* ffmpeg (si se requiere para pydub) https://ffmpeg.org/

## Configuración
Clonar el Repositorio:
```
git clone https://direccion_de_tu_repositorio.git
cd nombre_del_proyecto
```
### Crear y activar un entorno virtual:

```
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
```
### Instalar Dependencias:

```
pip install -r requirements.txt
Configurar Variables de Entorno:
```

### Asegúrate de tener configuradas las siguientes variables:

* AWS_ACCESS_KEY_ID: Tu clave de acceso AWS.
* AWS_SECRET_ACCESS_KEY: Tu clave secreta de acceso AWS.

### Desplegar con Zappa:

Si es tu primera vez desplegando:
```
zappa deploy
```
Para actualizaciones posteriores:
```
zappa update
```
## Uso
#### Enviar Archivo Multimedia para Transcripción:

Haz una solicitud POST a la URL proporcionada por Zappa (después del despliegue) con el archivo multimedia que deseas transcribir.

La respuesta incluirá la transcripción del audio.

#### Ejemplo con curl:

```
curl -X POST -F "file=@ruta_del_archivo" https://url_proveída_por_zappa/transcribe/
```

Contribución
Para contribuir al proyecto, crea un fork, realiza tus cambios y envía una solicitud de Pull Request.

Licencia
MIT

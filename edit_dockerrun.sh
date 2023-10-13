#!/bin/bash

# Lee el contenido actual del archivo Dockerrun.aws.json
content=$(cat Dockerrun.aws.json)

# Reemplaza el primer parámetro por el segundo parámetro
new_content=${content//\"$1\"/\"$2\"}

# Sobrescribe el archivo con el nuevo contenido
echo "$new_content" > Dockerrun.aws.json
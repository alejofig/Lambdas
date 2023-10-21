Pasos para probar una función en local con sam:
1. Tener docker
2. Tener python
3. instalar el sdk de aws
4. Crear unas credenciales de aws (secret_key y access_key)
5. aws configure con las credenciales para poder utilizar el sdk en local.
6. Crear un entorno virtual
7. Instalar sam
    - pip install aws-sam-cli
8. Crear un bucket y un archivo en s3
9. Modificar event.json con los datos del bucket y el archivo
8. ejecutar
    - sam local invoke HelloWorldFunction --event event.json
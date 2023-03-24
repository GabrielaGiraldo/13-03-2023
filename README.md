# FAST API
## Creación del entorno virtual
---
1. Instalar la libreria del entorno virtual ````pip install virtualenv````
2. Creación de entorno virtual ````python -m virtualenv [NOMBRE]````
3. Verificamos el python general ````pip freeze```` deben salir varias librerias.
4. Entro a mi entorno virtual (EN WINDOWS DESDE GIT BASH) ````source venc/Script/activate```` y sale el nombre de mi entorno virtual en mi linea de comandos.
5. cd sirve para acceder a una carpetap
 
 ## Instalar FastAPI
 1. Instalación de FastAPI ````pip install fastapi uvicorn````
 2. Ejecuta  FastAPI ```uvicorn entrypoint:app```
 ## (pip install python-dotenv)
 
 ## Creacion de primera ruta
 
 @app.get("/")

    def hello_world_check():

     return {
         "titulo":"Biblioteca STEAM",
         "versión":"v0.0.1"
     }
 
## Metodos HTTP
|metodo|acción DB|uso|
|--|--|--|
|POST|Create|Crear un registro en nuestro Backend para agregar o guardar recursos|
|GET|Read|acceder, recuperar o leer información|
|PUT|Modify|Lo usamos para las partes del programa que se dedican  a actualizar o modificar recursos|
|DELETE|Delete|Se usa para eliminar la información almacenada|

 ## Creacion de schemas
 ```Python
 from pydantic import Basemodel 
 class personas(Basemodel):
    iden:str
    nombre:str
    edad:str
    ocupación:str
def personas_add(request:person):
    personas[request.id]= {
        "nombre":request.nombre,
        "edad":request.edad,
        "ocupación":request.ocupación
    }
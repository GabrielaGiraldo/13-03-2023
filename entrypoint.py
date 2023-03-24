from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
import os

#Cargamos el entorno virtual
load_dotenv()
NAME = os.getenv("NAME")
VERSION = os.getenv("VERSION")
print(NAME,VERSION)
server = FastAPI(
    title = NAME,
    version = VERSION
)

biblioteca = {}

@server.get("/",tags=["Lectura de datos"])
def hello_world_check():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {
        "titulo":"Biblioteca STEAM",
        "versión":"v0.0.1"
    }

@server.get("/personas",tags=["Lectura de datos"])
def personas_all():
    """_summary_

    Returns:
        _type_: _description_
    """
    return biblioteca

@server.get("/personas/{id}",tags=["Lectura de datos"])
def personas_one(id:str):
    """_summary_

    Args:
        id (str): _description_

    Returns:
        _type_: _description_
    """
    return biblioteca[id]

class PersonaBiblioteca(BaseModel):
    id:str
    nombre:str
    edad:int
    libros:str
    fecha:str
    clave:int   
@server.post("/personas",tags=["Añadir usuarios"])
def personas_add(request:PersonaBiblioteca):
    """Función de añadir usuarios

    Args:
        request (PersonaBiblioteca): _description_

    Returns:
        _type_: _description_
    """
    j = {
        "nombre":request.nombre,
        "edad":request.edad,
        "libros": {
            request.clave:{
                "libro":request.libros,
                "fecha":request.fecha,
                "estado":"prestadito"
            }            
        }
    }
    biblioteca[request.id] = j
    return "Listico"

class Modificar(BaseModel):
    id:str
    nombre:str
    edad:int
@server.put("/persona",tags=["Modificar usuario"])
def persona_modify(request:Modificar):
    """_Función de modificar:

    Args:
        request (Modificar): La función se encarga de modificar la información del usuario (en este caso solo el nombre y la edad)
    """
    if biblioteca[request.id]["nombre"] != request.nombre:
        biblioteca[request.id]["nombre"] = request.nombre
    elif biblioteca[request.id]["edad"] != request.edad:
        biblioteca[request.id]["edad"] = request.edad

class Eliminar(BaseModel):
    id:str           
@server.delete("/personas",tags=["Eliminar usuario"])
def personas_delete(request:Eliminar):
    """Función de eliminar:

    Args:
        request (eliminar): En esta función se da la opción de eliminar los usuarios, dependediendo de la id que coloquen se eliminara el usuario
    """
    del biblioteca[request.id]
    
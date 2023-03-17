from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

biblioteca = {}

@app.get("/")
def hello_world_check():
    return {
        "titulo":"Biblioteca STEAM",
        "versión":"v0.0.1"
    }

@app.get("/personas")
def personas_all():
    return biblioteca

@app.get("/personas/{id}")
def personas_one(id:str):
    return biblioteca[id]

class PersonaBiblioteca(BaseModel):
    id:str
    nombre:str
    edad:int
    libros:str
    fecha:str
    clave:int
    
@app.post("/personas")
def personas_add(request:PersonaBiblioteca):
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
@app.put("/persona")
def persona_modify(request:Modificar):
    if biblioteca[request.id]["nombre"] != request.nombre:
        biblioteca[request.id]["nombre"] = request.nombre
    elif biblioteca[request.id]["edad"] != request.edad:
        biblioteca[request.id]["edad"] = request.edad

class eliminar(BaseModel):
    id:str
            
@app.delete("/personas")
def personas_delete(request:eliminar):
    del biblioteca[request.id]
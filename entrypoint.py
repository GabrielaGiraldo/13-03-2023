from fastapi import FastAPI

app = FastAPI()

biblioteca = {
    "1":{
        "nombre":"Gabriela",
        "edad":"17",
        "libros":{
            "1":{
                "libro":"El retrato de Dorian grey",
                "fecha":"13/03/2023",
                "estado":"prestado"
                },
            "2":{
                "libro":"La divina comedia",
                "fecha":"16/12/2023",
                "estado":"prestado"
                }
        }
    },
    "2":{
        "nombre":"Sammy",
        "edad":"16",
        "libros":{
            "1":{
                "libro":"Como no tirarme fisica",
                "fecha":"13/03/2023",
                "estado":"prestado"
                },
            "2":{
                "libro":"Michis.com",
                "fecha":"04/01/2023",
                "estado":"prestado"
                }
        }
    }       
}

@app.get("/{id}")
def usuario(id:str):
    if id == "1":
        return biblioteca["1"]
    elif id == "2":
        return biblioteca["2"]

@app.get("/{id}/{idlib}")
def usuario(id:str,idlib:str):
    return biblioteca[id]["libros"][idlib]
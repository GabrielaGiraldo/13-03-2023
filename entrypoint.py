from fastapi import FastAPI

app = FastAPI()

# @app.get("/hola/{persona}")
# def buenas(persona):
#     return f"Buenas {persona}"

# @app.get("/mellamo/{nombre}")
# def mellamo(nombre):
#     return f"me llamo {nombre}"

# @app.get("/apellido/{apellido}")
# def apellido(apellido):
#     return f"Y mi apellido es {apellido}"

# @app.get("/tengo/{edad}")
# def tengo(edad):
#     return f"{edad} años"

# @app.get("/momia/{ser}")
# def momia(ser):
#     return f"Y honestamente soy, una {ser}"

@app.get("/saludo/{nombre}")
def saludo(nombre:str):
    return f"Hola {nombre}, buenas tardes"

@app.get("/cuadrado/{l1}/{l2}")
def saludo(l1:float,l2:float):
    resultado = (l1*l2)
    return f"El area del cuadro tiene como resultado {resultado}"

@app.get("/edad/{nombre}/{edad}")
def saludo(nombre:str,edad:int):
    if edad>=18:
        return f"{nombre} tienes {edad}, por ende eres mayor de edad"
    return f"{nombre} tienes {edad}, por ende eres menor de edad"

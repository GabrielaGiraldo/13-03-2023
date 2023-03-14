from fastapi import FastAPI

app = FastAPI()

@app.get("/hola/{persona}")
def buenas(persona):
    return f"Buenas {persona}"

@app.get("/mellamo/{nombre}")
def mellamo(nombre):
    return f"me llamo {nombre}"

@app.get("/apellido/{apellido}")
def apellido(apellido):
    return f"Y mi apellido es {apellido}"

@app.get("/tengo/{edad}")
def tengo(edad):
    return f"{edad} años"

@app.get("/momia/{ser}")
def momia(ser):
    return f"Y honestamente soy, una {ser}"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def buenas():
    return "Buenas people"

@app.get("/mellamo/{nombre}")
def mellamo(nombre):
    return f"me llamo {nombre}"

@app.get("/apellido")
def apellido():
    return "Y mi apellido es Socrátes"

@app.get("/tengo")
def tengo():
    return "800 años"

@app.get("/momia")
def momia():
    return "Y honestamente soy, una momia"
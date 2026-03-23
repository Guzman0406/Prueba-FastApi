from fastapi import FastAPI

# Crear una instancia de FastAPI
app = FastAPI()

app.title = "Mi primer Api con FastApi"
app.version = "1.0.0"
app.description = "Primera vez creando una Api con FastApi"

# Crear una ruta basica
@app.get("/", tags=["Home"])
def home():
    return "FastApi funcionando ahuevo" 




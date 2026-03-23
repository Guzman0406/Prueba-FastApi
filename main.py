from fastapi import FastAPI
from fastapi.responses import HTMLResponse #Nos permite retornar HTML

# Crear una instancia de FastAPI
app = FastAPI()

app.title = "Mi primer Api con FastApi"
app.version = "1.0.0"
app.description = "Primera vez creando una Api con FastApi"

# Crear una lista de peliculas
movie_list = [
    {
        "id": 1,
        "title": "The Matrix",
        "year": 1999,
        "rating": 8.7,
        "category": "Action"
    },
    {
        "id": 2,
        "title": "The Godfather",
        "year": 1972,
        "rating": 9.2,
        "category": "Crime"
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "category": "Action"
    }
]

# Crear una ruta basica
@app.get("/", tags=["Home"])
def home():
    return "FastApi funcionando ahuevo" 

# Ruta para devolver un HTML
@app.get("/movies", tags=["Movies"])
def getMovies():
    return HTMLResponse("<h1>Hello World</h1>")
    return movie_list

# Ruta para devolver una lista de peliculas en formato JSON
@app.get("/movies_list", tags=["Movies_list"])
def getMovies_list():
    return movie_list


 

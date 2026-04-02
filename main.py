from fastapi import FastAPI
from fastapi.responses import HTMLResponse #Nos permite retornar HTML
from fastapi import Body #Permite recibir datos en formato JSON
from pydantic import BaseModel # permitir crear una clase 
from typing import Optional, List # permitir que un atributo sea opcional y que un atributo sea una lista
from fastapi import Field # Permite definir los datos en el body

# Crear una instancia de FastAPI
app = FastAPI()

# Clase para una instancia de pelicula
class Movie (BaseModel):
    id: Optional[int] = None
    title: str
    year: int
    rating: float
    category: str

class MovieUpdate(BaseModel):
    title: str
    year: int
    rating: float
    category: str

class MovieCreate(BaseModel):
    title: str
    year: int = Field(ge=1900, le=2025)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=1, max_length=15)


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


# Ruta para devolver una lista de peliculas en formato JSON
@app.get("/movies", tags=["Movies"])
def getMovies_list():
    return movie_list


# Ruta para devolver una pelicula por id 
@app.get("/movies/{id}", tags=["Movies"])
def getMovie(id:int)-> Movie:
    try:
        for movie in movie_list: # Recorrer un arreglo por cada pelicula en la lista
            if movie["id"] == id:
                return movie
    except Exception as e:
        return {"message": str(e)}


# Ruta para devolver una lista de peliculas por categoria 
@app.get("/movies/category/{category}", tags=["Movies"])
def get_movie_by_category(category: str):
    try:
        movie_category = [movie for movie in movie_list if movie["category"] == category]
        return movie_category
    except Exception as e:
        return {"Mesagge": str(e)}  



## POST mediante clase
@app.post("/movies", tags=["Post_Movies"])
def create_movie(movie: MovieCreate):
    movie_list.append(movie.model_dump()) # Diccionario para que pueda ser insertado 
    return movie_list 


## PUT ##
# Ruta para actualizar una pelicula (id lo toma de la ruta)
@app.put("/movies/{id}", tags=["Put_Movies"])
def update_movie(
    id: int,
    movie: MovieUpdate
) -> List[Movie]:
    try:
        for item in movie_list: # Por cada pelicula en la lista
            if item["id"] == id: # Si el id de la pelicula es igual al id de la ruta
                item["title"] = movie.title
                item["year"] = movie.year
                item["rating"] = movie.rating
                item["category"] = movie.category
        return movie 
    except Exception as e:
        return {"message": str(e)}


## DELETE ##
@app.delete("/movies/{id}", tags=["Delete_Movies"])
def delete_movie(id :int,
):

    try:
        for movie in movie_list:
            if movie["id"] == id:
                movie_list.remove(movie) #Eliminar la pelicula
        return movie_list   
    except Exception as e: 
        return {"mesagge": str(e)}


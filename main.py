from typing import Union
from routers import tasks
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
origins = [
    "http://127.0.0.1:5500",  # tu frontend
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # permite las solicitudes de estos orígenes
    #allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # especifica los métodos permitidos
    allow_headers=["*"],  # permite todos los encabezados
)

# Rutas
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the To-Do API"}

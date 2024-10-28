# models/task_model.py
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class TaskModel(BaseModel):
    id: Optional[ObjectId]  # ID autogenerado en MongoDB
    title: str  # Título de la tarea
    description: Optional[str] = None  # Descripción opcional
    completed: bool = False  # Estado de la tarea

    class Config:
        arbitrary_types_allowed = True

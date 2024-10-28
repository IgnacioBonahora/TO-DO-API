# schemas/task_schema.py
from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

class TaskResponseSchema(TaskSchema):
    id: str  # Usamos str para manejar el ObjectId como string

    class Config:
        orm_mode = True

def task_response_schema(task: dict) -> TaskResponseSchema:
    return TaskResponseSchema(
        id=str(task["_id"]),
        title=task["title"],
        description=task.get("description"),
        completed=task["completed"]
    )


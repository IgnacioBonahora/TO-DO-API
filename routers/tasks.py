from fastapi import APIRouter, HTTPException
from bson import ObjectId
from db.client import db
from db.schemas.task_schema import TaskSchema, TaskUpdateSchema, TaskResponseSchema,task_response_schema

router = APIRouter()

# Obtener todas las tareas
@router.get("/tasks", response_model=list[TaskResponseSchema])
async def get_all_tasks():
    tasks = db["tasks"].find()
    return [task_response_schema(task) for task in tasks]

# Crear una nueva tarea
@router.post("/tasks", response_model=TaskResponseSchema)
async def create_task(task: TaskSchema):
    task_dict = task.dict()
    result = db["tasks"].insert_one(task_dict)
    task_dict["_id"] = str(result.inserted_id)
    return task_response_schema(task_dict)

# Obtener una tarea por ID
@router.get("/tasks/{task_id}", response_model=TaskResponseSchema)
async def get_task(task_id: str):
    task = db["tasks"].find_one({"_id": ObjectId(task_id)})
    if task:
        return task_response_schema(task)
    raise HTTPException(status_code=404, detail="Task not found")

# Actualizar una tarea por ID
@router.put("/tasks/{task_id}", response_model=TaskResponseSchema)
async def update_task(task_id: str, task: TaskUpdateSchema):
    task_dict = {k: v for k, v in task.dict().items() if v is not None}
    if not task_dict:
        raise HTTPException(status_code=400, detail="No fields to update")

    result = db["tasks"].update_one({"_id": ObjectId(task_id)}, {"$set": task_dict})
    if result.modified_count == 1:
        updated_task = db["tasks"].find_one({"_id": ObjectId(task_id)})
        return task_response_schema(updated_task)
    raise HTTPException(status_code=404, detail="Task not found")

# Eliminar una tarea por ID
@router.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    result = db["tasks"].delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 1:
        return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    status: str

class TaskInDB(Task):
    id: int

tasks_db: List[TaskInDB] = []
task_id_counter = 1

@app.get("/tasks", response_model=List[TaskInDB])
def get_tasks():
    return tasks_db

@app.post("/tasks", response_model=TaskInDB)
def create_task(task: Task):
    global task_id_counter
    new_task = TaskInDB(id=task_id_counter, **task.dict())
    tasks_db.append(new_task)
    task_id_counter += 1
    return new_task

@app.put("/tasks/{task_id}", response_model=TaskInDB)
def update_task(task_id: int, updated_task: Task):
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[idx] = TaskInDB(id=task_id, **updated_task.dict())
            return tasks_db[idx]
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            del tasks_db[idx]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

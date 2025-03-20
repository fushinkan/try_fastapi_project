
from fastapi import APIRouter, HTTPException
from app.models.tasks import TaskCreate, Task
from typing import List

router = APIRouter(prefix="/tasks")

tasks: List[Task] = []
new_id = 1


@router.get("/", response_model=List[Task])
async def get_tasks():
    return tasks

@router.post("/", response_model=Task, status_code=201)
async def add_task(task: TaskCreate):
    global new_id
    new_task = Task(id=new_id, **task.dict())
    tasks.append(new_task)

    new_id += 1
    return new_task


@router.put('/{task_id}', response_model=Task)
async def update_task(task_id: int, updated_task: TaskCreate):
    task = next((t for t in tasks if t.id == task_id), None)

    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')

    task.title = updated_task.title
    task.description = updated_task.description
    return task


@router.delete('/{task_id}', status_code=204)
async def delete_task(task_id: int):
    index = next((i for i, t in enumerate(tasks) if t.id == task_id), None)

    if index is None:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks.pop(index)

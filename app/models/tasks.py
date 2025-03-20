from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(..., description='Task name')
    description: str = Field(..., description='Task description')

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int = Field(...)



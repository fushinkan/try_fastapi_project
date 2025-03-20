from fastapi import FastAPI
from app.routers.tasks import router as task_router
import uvicorn

app = FastAPI()
app.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
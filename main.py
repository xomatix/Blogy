from fastapi import FastAPI, Path
from fastapi.routing import APIRouter
from Posts.PostRouter import router as post_router
import threading
import DB.DataBaseConnect as db 
from uvicorn import Server, Config

app = FastAPI()

app.include_router(post_router, prefix="/api/post")

task = threading.Thread(target=db.InitDB())
task.start()
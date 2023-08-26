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

uvicorn_config = Config(app, host="0.0.0.0", port=8000)  # Modify host and port as needed
server = Server(uvicorn_config)
application = server.app
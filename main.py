from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def basic_index():
    return FileResponse('templates/index.html')

@app.get("/upload")
async def uploadFunction():
    return {"message": "Welcome"}
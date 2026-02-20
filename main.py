from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def basic_index():
    return FileResponse('templates/index.html')

@app.get("/upload")
async def uploadFunction():
    return {"message": "Welcome"}
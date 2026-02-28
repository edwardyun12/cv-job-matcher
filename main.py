from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def basic_index():
    return FileResponse('templates/index.html')

@app.post("/upload")
async def uploadFunction(item: Request):
    data = await item.json()
    return {"message": data};
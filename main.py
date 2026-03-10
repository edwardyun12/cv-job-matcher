from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def basic_index():
    return FileResponse('templates/index.html')

@app.post("/upload")
async def uploadFunction(
    file: UploadFile = File(...), 
    text: str = Form(...)
    ):
   content = await file.read()
   print(f"Received file: {file.filename}, size: {len(content)} bytes")
   return {"message": f"File '{file.filename}' uploaded successfully with text: {text}"}
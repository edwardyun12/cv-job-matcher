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
    target_job: str = Form(...)
    ):

   content = await file.read()
   decoded_content = content.decode('utf-8')
   #print(f"Received file: {file.filename}, size: {len(content)} bytes")
   return {"message": f"File content '{decoded_content}' uploaded successfully with target job: {target_job}"}
from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import fitz

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
    pdf_content = await file.read()
   # 2. 파일 경로 대신 'stream'을 사용해 메모리에서 바로 열기
    userCV = fitz.open(stream=pdf_content, filetype="pdf")
    
    # 3. 텍스트 추출 (가장 짧은 코드 버전)
    text = "".join([page.get_text() for page in userCV])
    userCV.close()
    
    # 확인용 출력 (나중에 삭제)
    print(f"추출된 텍스트: {text}")

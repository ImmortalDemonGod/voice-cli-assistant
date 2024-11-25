from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil

app = FastAPI()

@app.post("/upload-recording")
async def upload_recording(file: UploadFile = File(...)):
    try:
        recordings_dir = Path("recordings")
        recordings_dir.mkdir(exist_ok=True)
        file_path = recordings_dir / file.filename
        
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {"filename": file.filename, "status": "success"}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"Upload failed: {str(e)}"}
        )

@app.get("/insights")
async def get_insights(limit: int = 5):
    try:
        from ..processing.analyzer import Analyzer
        analyzer = Analyzer()
        insights = analyzer.get_recent_insights(limit)
        return {"insights": insights}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"Failed to fetch insights: {str(e)}"}
        )
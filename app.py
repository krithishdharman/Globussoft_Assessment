from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import tempfile
from deepface import DeepFace
import os

app = FastAPI(
    title="Globussoft Task 2 - Face Verification API",
    description="Accepts two face images and verifies if they belong to the same person using DeepFace.",
    version="1.0.0"
)

@app.post("/verify", summary="Verify if two faces are of the same person")
async def verify_faces(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    try:
        suffix1 = os.path.splitext(file1.filename)[-1]
        suffix2 = os.path.splitext(file2.filename)[-1]

        with tempfile.NamedTemporaryFile(suffix=suffix1, delete=False) as tmp1, \
             tempfile.NamedTemporaryFile(suffix=suffix2, delete=False) as tmp2:

            tmp1.write(await file1.read())
            tmp2.write(await file2.read())
            tmp1_path, tmp2_path = tmp1.name, tmp2.name

        result = DeepFace.verify(tmp1_path, tmp2_path, enforce_detection=True)

        os.remove(tmp1_path)
        os.remove(tmp2_path)

        response = {
            "verified": result["verified"],
            "distance": result["distance"],
            "model": result["model"]
        }
        return JSONResponse(content=response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

import os
from fastapi import APIRouter, UploadFile, File
from app.services.rag_service import RAGService

router = APIRouter()

os.makedirs("uploads", exist_ok=True)

# Dependency instance (cleaner than globals)
rag_service = RAGService()


@router.post("/upload-policy")
async def upload_policy(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files allowed"}

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    rag_service.upload_policy(file_location)

    return {"message": "Policy uploaded and indexed successfully"}


@router.post("/ask-policy")
async def ask_policy(question: str):
    return rag_service.ask(question)
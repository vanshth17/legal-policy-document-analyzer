from fastapi import APIRouter, UploadFile, File
from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.retriever import get_retriever
from app.rag.chain import build_rag_chain
from app.models.embeddings import get_embeddings
from langchain_community.vectorstores import FAISS

router = APIRouter()

# Global memory (simple version for now)
VECTORSTORE = None


@router.post("/upload-policy")
async def upload_policy(file: UploadFile = File(...)):
    global VECTORSTORE

    # 🔐 Basic file validation
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files allowed"}

    # Save file locally
    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Load & process document
    documents = load_pdf(file_location)
    chunks = split_documents(documents)

    embeddings = get_embeddings()

    VECTORSTORE = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return {"message": "Policy uploaded and indexed successfully"}


@router.post("/ask-policy")
async def ask_policy(question: str):
    global VECTORSTORE

    if VECTORSTORE is None:
        return {"error": "Upload a policy first"}

    retriever = get_retriever(VECTORSTORE)
    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    chain = build_rag_chain()

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return {"answer": response.content}
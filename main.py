from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Legal Policy Document Analyzer API"
)

app.include_router(router)
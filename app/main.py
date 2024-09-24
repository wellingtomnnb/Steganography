from fastapi import FastAPI
from app.api import router

app = FastAPI(version="1.0", redoc_url="/docs", docs_url='/tests')
app.include_router(router, tags=["Steganography"], prefix="/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Steganography API!"}
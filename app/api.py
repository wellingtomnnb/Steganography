from fastapi import APIRouter, HTTPException
from app.steganography import Steganography

router = APIRouter()
steganography = Steganography()

@router.post("/steganography/")
async def apply_steganography(text: str):
    try:
        result = steganography.encode(text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
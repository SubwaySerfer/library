from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/")
async def get_library():
    return {"library": "This is a library"}
from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/")
async def get_library():
    return {"library": "This is a library"}

@router.post("/book")
async def create_book(request: dict):
    print(f"request: {request}")
    return {"book": "Book created successfully"}
from fastapi import FastAPI

from app.routers.library import router as LibraryRouter

app = FastAPI()


app.include_router(LibraryRouter, prefix="/library", tags=["library"])

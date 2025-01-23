from datetime import datetime  # noqa: D104

from pydantic import BaseModel


class Book(BaseModel):
    title: str
    year: datetime.year
    pages: int
    author: str
    price: float

class Author(BaseModel):
    full_name: str
    birth_year: datetime.year

class Reader(BaseModel):
    name: str
    email: str
    registration_date: datetime

class BookLending(BaseModel):
    reader: Reader
    book: Book
    lending_date: datetime
    return_date: datetime


from datetime import date
from typing import Optional

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    bio: str
    books: Optional[list] = []


class AuthorCreate(AuthorBase):
    ...


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date
    author_id: int


class BookCreate(BookBase):
    ...


class Book(BookBase):
    id: int
    author: Author

    class Config:
        orm_mode = True

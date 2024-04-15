from datetime import date
from typing import Optional, Union

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    bio: str
    books: Union[list, None]


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
    author_id: Union[int, None]


class BookCreate(BookBase):
    ...


class Book(BookBase):
    id: int
    author: Author

    class Config:
        orm_mode = True

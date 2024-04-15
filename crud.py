from sqlalchemy.orm import Session
from . import models, schemas


def get_all_authors(db: Session):
    return db.query(models.Author).all()


def get_author_by_id(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
        name=author.name,
        bio=author.bio,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def update_author(db: Session, author_id: int, author: schemas.AuthorCreate):
    db_author = get_author_by_id(db, author_id)
    db_author.name = author.name
    db_author.bio = author.bio
    db.commit()
    db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int):
    db_author = get_author_by_id(db, author_id)
    db.delete(db_author)
    db.commit()
    return db_author


def get_all_books(db: Session):
    return db.query(models.Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = get_book_by_id(db, book_id)
    db_book.title = book.title
    db_book.summary = book.summary
    db_book.publication_date = book.publication_date
    db_book.author_id = book.author_id
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    db.delete(db_book)
    db.commit()
    return db_book

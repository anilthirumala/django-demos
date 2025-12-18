from app.models.book import Book
from app import db

def get_all_books():
    return Book.query.all()

def create_book(data):
    new_book = Book(**data)
    db.session.add(new_book)
    db.session.commit()
    return new_book

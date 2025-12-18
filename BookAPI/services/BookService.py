from Models.Book import Book

class BookService:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, publisher, isbn):
        book = Book(title, author, publisher, isbn)
        self.books.append(book)
        return book

    def get_book_by_id(self, book_id):
        return next((book for book in self.books if book.id == book_id), None)

    def get_all_books(self):
        return self.books

    def update_book(self, book_id, title=None, author=None, publisher=None, isbn=None):
        book = self.get_book_by_id(book_id)
        if book:
            if title: book.Title = title
            if author: book.Author = author
            if publisher: book.Publisher = publisher
            if isbn: book.ISBN = isbn
            return book
        return None

    def delete_book(self, book_id):
        book = self.get_book_by_id(book_id)
        if book:
            self.books.remove(book)
            return True
        return False
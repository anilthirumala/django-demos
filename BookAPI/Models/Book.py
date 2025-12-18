class Book:
    count = 0

    def __init__(self, title="", author="", publisher="", isbn=""):
        self.id = Book.count
        self.Title = title
        self.Author = author
        self.Publisher = publisher
        self.ISBN = isbn
        Book.count += 1

    def to_dict(self):
        return {
            "id": self.id,
            "Title": self.Title,
            "Author": self.Author,
            "Publisher": self.Publisher,
            "ISBN": self.ISBN
        }
class Book:
    def __init__(self):
        self.title = "Book Title"
        self.author = "Author"
        self.price = "Price"

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

    def accept(self):
        print('enter title')
        self.title = input()
        print('enter author')
        self.author = input()
        print('enter price')
        self.price = input()

account = Book()
account.accept()
account.display()

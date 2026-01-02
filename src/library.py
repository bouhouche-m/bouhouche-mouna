from book import Book
from user import User
from loan import Loan

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def loan_book(self, book):
        if book.available:
            book.available = False

    def return_book(self, book):
        book.available = True

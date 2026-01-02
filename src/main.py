from book import Book
from library import Library

library = Library()

book = Book(1, "Python", "Auteur")
library.add_book(book)

library.loan_book(book)
print(book)

library.return_book(book)
print(book)

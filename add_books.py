from utils import books
def add_books():
    name=input("enter name of book ")
    author=input('enter author name ')
    books[name]=author
    print("Book added successfully\n")
from utils import books
def show_books():
    if len(books)==0:
        print("No books available\n")
    else:
        print("Books available\n")
    for b in books:
        print(b)
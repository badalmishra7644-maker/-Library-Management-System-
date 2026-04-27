# from utils import issuedbooks, issuerdetails, books
from utils import *

def issue_books():
    name=input("Enter name of book you want to issue ")
    if name in books:
        nissuer=input("enter name of issuer ")
        date=int(input("enter date of issue "))
        issuerdetails.append((name,nissuer,date))
        issuedbooks[name]=nissuer
        books.pop(name)  
        print(issuerdetails)
        print(issuedbooks)
        print("Book issued\n")
    else:
        print(name,"is not available in library")
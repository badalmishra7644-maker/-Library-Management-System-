from utils import issuedbooks,issuerdetails,books
def book_return():
    name=input("enter book you are returning ") 
    author=input("enter name of author ")
    if name in issuedbooks:
        books[name]=author
        issue_time=("Enter days after you are returning ")

        if issue_time>21:
            fine=(issue_time-21)*60
            print("Total fine =",fine)
            print("Book returned successfully")
        elif issue_time>14:
            fine=(issue_time-14)*20
            print("Total fine =",fine)
            print("Book returned successfully")
        elif issue_time>7:
            fine=(issue_time-7)*10
            print("Total fine =",fine)
            print("Book returned successfully")
        elif issue_time<7:
            print("No fine imposed Book returned successfully")
    else: 
            print("No books returned\n")


 
from add_books import add_books
from issue_books import issue_books
from return_books import book_return
from show_books import show_books

def library():
    while True:
        print(" 1.Add Books\n","2.Show Books\n","3.Issue books\n","4.Return book\n","5.Exit\n")
        choice=int(input("Enter your choice "))
        if choice==1:
            add_books()
        elif choice==2:
            show_books()
        elif choice==3:
            issue_books()
        elif choice==4:
            book_return()
        elif choice==5:
            print("Thank you")
            break
        else:
            print("Invalid choice")

library()
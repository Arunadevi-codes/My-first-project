class Library:
    books = [
    {"id": 1, "book_name": "Python Basics", "author": "John Smith", "copies": 5},
    {"id": 2, "book_name": "Learning Java", "author": "James Gosling", "copies": 3},
    {"id": 3, "book_name": "Web Development", "author": "Mark Thomas", "copies": 7},
    {"id": 4, "book_name": "Data Structures", "author": "Robert Lafore", "copies": 4},
    {"id": 5, "book_name": "Artificial Intelligence", "author": "Stuart Russell", "copies": 2}
    ]
    def __init__(self):
        name = input("Enter your name: ")
        print("Hello", name, "Welcome")

    def menu(self):
        print("\n1. Borrow book")
        print("2. Return book")
        print("3. Display Available books")
        print("4. Exit")
        self.choice = int(input("\nEnter Your Choice: "))
    
    def borrow(self):
        bid = int(input("Enter Book ID:"))
        req = int(input("Enter Number of books to be borrow: "))
        found = False
        for book in Library.books:
            if (bid == book["id"]):
                found = True
                if ( req <= book["copies"]):
                    book["copies"]-=req
                    print("Book borrowed successfully")
                else:
                    print("Book not available")
                break
        if not found:
                print("Enter valid Book ID")

    def returnbook(self):
        rid = int(input("Enter return book ID: "))
        no = int(input("Enter Number of books to be returned: "))
        found = False
        for book in Library.books:
            if (rid == book["id"]):
                found = True
                book["copies"]+=no
                print("Book returned successfully")
                break
        if not found:
            print("Enter valid book ID")

    def display(self):
        for book in Library.books:
            print("\nID: ", book["id"], 
                  "\nBook name: ", book["book_name"],
                  "\nAuthor: ", book["author"],
                  "\nAvailable copies: ", book["copies"])

lib=Library()
while True:

    lib.menu()
    if (lib.choice == 1):
        lib.borrow()
    elif (lib.choice == 2):
        lib.returnbook()
    elif (lib.choice == 3):
        lib. display()
    elif (lib.choice == 4):
        print("Thank you")
        break
    else:
        print("Enter valid choice")
           
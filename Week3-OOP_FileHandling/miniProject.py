'''
Project
Library Management System

Features:
Add books
Search books
Issue books
Return books

Concepts used: OOP and files
'''

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

class Library():

    def __init__(self):
        self.books = []
        self.make_repository()

    def make_repository(self):
        with open("book.txt",'w') as f:
            f.write("101,Python,John,5")
            f.write("\n102,AI,Andrew,3")

    def input_BookDetails(self):
        print("--------------------------------------")
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author: ")
        quantity = int(input("Enter quantity: "))

        return Book(book_id, title, author, quantity)


    def add_Book(self):
        with open("book.txt",'a') as f:
            book=self.input_BookDetails()
            self.books.append(book)
            f.write(f"\n{book.book_id},{book.title},{book.author},{book.quantity}\n")
            print("---- Book Added Successfully ----")

    def search_Book(self):
        print("<==== Search Book ====>")
        bookId = input("Enter book ID to search: ")
        found = False
        with open("book.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == bookId:      # Compare only the book ID
                    print("\nBook Found!")
                    print(f"Book ID      : {data[0]}")
                    print(f"Book Title   : {data[1]}")
                    print(f"Book Author  : {data[2]}")
                    print(f"Quantity     : {data[3]}")
                    print("-----------------------------")
                    found = True
                    break

        if not found:
            print("Book not found!")



    def issue_Book(self):
        bookId = input("Enter Book ID: ")
        found = False
        updated_lines = []
        with open("book.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == bookId:
                    found = True
                    quantity = int(data[3])
                    if quantity > 0:
                        quantity -= 1
                        print("Book Issued Successfully!")
                    else:
                        print("Book is not available.")
                    data[3] = str(quantity)
                updated_lines.append(",".join(data))
        if found:
            with open("book.txt", "w") as f:
                for line in updated_lines:
                    f.write(line + "\n")
        else:
            print("Book not found!")


    def return_Book(self):
        bookId = input("Enter Book ID: ")
        found = False
        updated_lines = []
        with open("book.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == bookId:
                    found = True
                    quantity = int(data[3])
                    if quantity > 0:
                        quantity += 1
                        print("Book Returned Successfully!")
                    else:
                        print("Book is not available.")
                    data[3] = str(quantity)
                updated_lines.append(",".join(data))
        if found:
            with open("book.txt", "w") as f:
                for line in updated_lines:
                    f.write(line + "\n")
        else:
            print("Book not found!")



L=Library()
print("----- Welcome to Library Managemnt System! ----")
while True:
    try:
     choice=int(input("Choose\n1 for Add Books.\n2 for Search Books.\n3 for Issue Books.\n4 for Return Books.\n5 for Exit  "))
    except:
         print("\nInput error. Please try again.")
         continue
    
    if choice==1:
        L.add_Book()
    elif choice==2:
        L.search_Book()
    elif choice==3:
        L.issue_Book()
    elif choice==4:
        L.return_Book()
    elif choice==5:
        print("Exiting the system.")
        break
    else:
        print("Enter a valid choice.")


            


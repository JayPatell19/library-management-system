
list_of_books = []

def add_books():
    book_title = input("Enter book title: ").lower().strip()
    author_name = input("Enter author name: ")
    list_of_books.append({"Title":book_title,"author_name":author_name,"status":"Available"})
    print(f"✅ Book '{book_title}' added!\n")

def view_books():
    if not list_of_books:
        print("\n❌ no books available")
    else:
       print("📚 List of Books:")
       i = 1
       for book in list_of_books:
           print(i, ". Title -", book["Title"], ", Author -", book["author_name"], ", Status -", book["status"])
           i+=1

def issue_books():
    issue_book = input("Enter book title to get a book: ").lower().strip()
    for books in list_of_books:
        if books["Title"] == issue_book:
            if books["status"] == "Available":
                print(f"'{issue_book}' has been issued to you successfully✅")
                books["status"] = "Unavailable"
            else:
                print(f"❌ sorry '{issue_book}' is not Available.\n ")
            return
    
    print(f"❌ There is no book named '{issue_book}'.\n")

def return_books():
    return_book = input("Enter book title to return a book: ").lower().strip()
    for books in list_of_books:
        if books["Title"] == return_book:
            if books["status"] == "Unavailable":
                print(f"Book {return_book} has been successfully returned ✅\n")
                books["status"] = "Available"
            else:
                print(f"❌ Book '{return_book}' was not issued.\n")
            return
    print("❌ Book not found.")

def exit_software():
    print("Thanks for using Library Management System.")
    print("Exiting program...")


print("\n✨Welcome to Library Management System✨\n")

while(True):
    print("----- Library Management Software -----")
    print("\n          1. Add Books ")
    print("          2. View Books")
    print("          3. Issue Books")
    print("          4. Return Books")
    print("          5. Exit Software\n")
    print("----- Library Management Software -----\n")

    user_choise = int(input("Enter your choise: "))

    if (user_choise == 1):
        add_books()
    elif (user_choise == 2):
        view_books()
    elif (user_choise == 3):
        issue_books()
    elif (user_choise == 4):
        return_books()
    elif (user_choise == 5):
        exit_software()
        break
    else:
        print("Enter valid choise")


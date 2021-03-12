# Mini Project - Online Library

class library:

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.d = {}

    def display_books(self):
        return f"The list of books available in our library is - {', '.join(self.list_of_books)}\n"

    def lend_book(self):
        book_name = input("Please enter the name of the book you want to issue.\n")

        if book_name not in self.list_of_books: #  assuming the book is not present in our library.
            print('Sorry, this book is not available. Please enter the correct book name\n')
        else:
            person_name = input("Please enter your name.\n")
            self.d[book_name]  = person_name
            self.list_of_books.remove(book_name)
            print('The book has been issued.\n')


    def add_book(self): #  if someone wants to donate a book
        print("We are glad to know that you are donating a book to our library.\n")
        book_name = input("Please enter the book name.\n")
        self.list_of_books.append(book_name)
        print("You have donated the book successfully.\n")

    def return_book(self):
        name_of_book = input("Please enter the book name\n")
        del self.d[name_of_book]
        self.list_of_books.append(name_of_book)
        print('Thank you for returning the book. You have returned the book successfully.\n')

# Assuming the book names are one, two, three, four, etc.
Books = ['one', 'two','three','four','five','six','seven','eight','nine','ten']
maaz_library = library(list_of_books= Books, library_name= "Maaz")

print('Welcome to Online Library\n')

def choices():
    print('Enter 1 to display the list of books available\n'
          'Enter 2 to issue a book\n'
          'Enter 3 to donate a book\n'
          'Enter 4 to return a book\n'
          'Enter 0 to exit\n')

while True:
    choices()
    choice = int(input('Please enter your choice\n'))
    if choice == 1:
        print(maaz_library.display_books())
    elif choice == 2:
        maaz_library.lend_book()
    elif choice == 3:
        maaz_library.add_book()
    elif choice == 4:
        maaz_library.return_book()
    elif choice == 0:
        break
    else:
        print('\nPlease enter the correct choice\n')
        continue


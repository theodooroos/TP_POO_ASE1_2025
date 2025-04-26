class Person:
    # Class representing a person
    def __init__(self, firstname: str, lastname: str):
        # Constructor
        self.firstname = firstname
        self.lastname = lastname
    
    def __str__(self):
        # String representation
        return f"{self.firstname} {self.lastname}"
    
    def __repr__(self):
        # Return a string
        return f"{self.firstname} {self.lastname}"


class Book:
    # Class representing a book
    def __init__(self, title: str, author: Person):
        # Constructor
        self.title = title
        self.author = author
    
    def __repr__(self):
        # Return a string
        return f"{self.title} ({self.author})"
    
    # String representation as security
    def __str__(self):
        # String representation
        return f"{self.title} ({self.author})"


class LibraryError(Exception):
    # Class representing a library error if books are not available
    def __init__(self, message: str):
        # Constructor
        super().__init__(message)
        self.message = message

    def __str__(self):
        # String representation
        return f"{self.message}"
    
    def __repr__(self):
        # Return a string
        return f"LibraryError({self.message})"
    """Base class for Library errors"""


class Library:
    # Class representing a library
    def __init__(self, name: str):
        # Constructor
        self.name = name
        self._books = []
        self._members = set()
        self._borrowed_books = {}

    def is_book_available(self, book: Book):
        # Check if a book is available if book does not exist return a LibraryError
        if book not in self._books:
            raise LibraryError(f"Book '{book.title}' is not available in the library.")
        # Check if the book is borrowed
        if book in self._borrowed_books:
            result = False
        else:
            result = True
        return result

    def borrow_book(self, book: Book, person: Person):
        # Borrow a book if the book is available
        if book not in self._books:
            raise LibraryError(f"'{book.title}' doesn't exist in the library.")
        if book in self._borrowed_books:
            raise LibraryError(f"'{book.title}' is already borrowed by {self._borrowed_books[book]}.")
        if person not in self._members:
            raise LibraryError(f"'{person}' is not a member of the library.")
        # Add the book to the borrowed books
        self._borrowed_books[book] = person
        return True
    
    def return_book(self, book: Book):
        # Return a book if the book is borrowed
        if book not in self._borrowed_books:
            raise LibraryError(f"'{book.title}' is not part of the borrowed books.")
        # Remove the book from the borrowed books
        del self._borrowed_books[book]
        return True
    
    def add_new_member(self, person: Person):
        # Add a new member to the library
        if person in self._members:
            raise LibraryError(f"Person '{person}' is already a member of the library.")
        self._members.add(person)
        return True
    
    def add_new_book(self, book: Book):
        # Add a new book to the library
        if book in self._books:
            raise LibraryError(f"Book '{book.title}' is already in the library.")
        self._books.append(book)
        return True
    
    def print_status(self):
        # Print the status of the library
        print(f"{self.name} status:")
        print(f"Books catalogue: {self._books}")
        print(f"Members: {self._members}")
        # Print available and borrowed books
        available_books = []
        for book in self._books:
            if book not in self._borrowed_books:
                available_books.append(book)
        print(f"Available books: {available_books}")
        print(f"Borrowed books: {self._borrowed_books}")
        print("-"*5)
        return True

def test_script():
    antoine = Person("Antoine", "Dupont")
    print(antoine)

    julia = Person("Julia", "Roberts")
    print(julia)

    rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
    print(rugby_book)

    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)

    library = Library("Public library")
    library.print_status()

    library.add_new_book(rugby_book)
    library.add_new_book(novel_book)
    library.add_new_member(antoine)
    library.add_new_member(julia)
    library.print_status()

    print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
    library.borrow_book(rugby_book, antoine)
    library.print_status()

    try:
        library.borrow_book(rugby_book, julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(novel_book, Person("Simone", "Veil"))
    except LibraryError as error:
        print(error)

    try:
        library.return_book(novel_book)
    except LibraryError as error:
        print(error)

    library.return_book(rugby_book)
    library.borrow_book(novel_book, julia)
    library.print_status()

    library.borrow_book(rugby_book, julia)
    library.print_status()


def main():
    # Test the Person class : EXO 1
    antoine = Person("Antoine", "Dupont")
    print(antoine)
    # Test the Book class :   EXO 2
    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)
    # Test the Library class : EXO 3
    library = Library("Public library")
    # Test the LibraryError class : EXO 4
    try:
        library.is_book_available(novel_book)
    except LibraryError as e:
        print(e)
    # Test add_new_book : EXO 7
    library.add_new_book(novel_book)
    # Test add_new_member : EXO 7
    library.add_new_member(antoine)
    # Test borrow_book : EXO 5
    # test if the book is available
    absent_book = Book("Le Petit Prince", Person("Antoine", "de Saint-Exupéry"))
    try:
        library.borrow_book(absent_book, antoine)
    except LibraryError as e:
        print(e)
    # test if the person is a member
    absent_person = Person("Jean", "Dupont")
    try:
        library.borrow_book(novel_book, absent_person)
    except LibraryError as e:
        print(e)
    # test to borrow the book
    try:
        library.borrow_book(novel_book, antoine)
        print("pass")
    except LibraryError as e:
        print(e)
    # test to borrow the book again
    try:
        library.borrow_book(novel_book, antoine)
    except LibraryError as e:
        print(e)
    # Test return_book : EXO 6
    # test if the book is borrowed
    try:
        library.return_book(novel_book)
        print("pass")
    except LibraryError as e:
        print(e)
    # test to return the book again
    try:
        library.return_book(novel_book)
    except LibraryError as e:
        print(e)
    # Test to borrow the book again
    try:
        library.borrow_book(novel_book, antoine)
        print("pass")
    except LibraryError as e:
        print(e)
    # Test if everything is ok : EXO 8
    antoine = Person("Antoine", "Dupont")
    print(antoine)

    julia = Person("Julia", "Roberts")
    print(julia)

    rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
    print(rugby_book)

    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)

    library = Library("Public library")
    library.print_status()

    library.add_new_book(rugby_book)
    library.add_new_book(novel_book)
    library.add_new_member(antoine)
    library.add_new_member(julia)
    library.print_status()
    """Test your code here"""
    # Test like asked in the exercice 1.9
    print("Test script \n\n")
    test_script()

if __name__ == "__main__":
    main()

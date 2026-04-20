from book import Book
from user import User


class Admin:
    def __init__(self):
        self.books = []
        self.users = []

    # ---------- BOOK OPERATIONS ----------
    def add_book(self, book_id, name, quantity):
        for book in self.books:
            if book.id == book_id:
                print("Book ID already exists!")
                return
        self.books.append(Book(book_id, name, quantity))
        print("Book is added successfully!")

    def print_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book)

    def print_books_by_prefix(self, prefix):
        found = False
        for book in self.books:
            if book.name.lower().startswith(prefix.lower()):
                print(book)
                found = True
        if not found:
            print("No books found with this prefix.")

    # ---------- USER OPERATIONS ----------
    def add_user(self, user_id, name):
        for user in self.users:
            if user.id == user_id:
                print("User ID already exists!")
                return
        self.users.append(User(user_id, name))
        print("User added successfully!")

    def print_users(self):
        if not self.users:
            print("No users available.")
            return
        for user in self.users:
            print(user)

    # ---------- BORROW / RETURN ----------
    def borrow_book(self, user_id, book_name):
        user = self._find_user(user_id)
        book = self._find_book(book_name)

        if not user or not book:
            return

        if book.quantity == 0:
            print("No copies available.")
            return

        book.quantity -= 1
        user.borrow_book(book.name)
        print("Book borrowed successfully!")

    def return_book(self, user_id, book_name):
        user = self._find_user(user_id)
        book = self._find_book(book_name)

        if not user or not book:
            return

        if book_name not in user.borrowed_books:
            print("User didn't borrow this book.")
            return

        book.quantity += 1
        user.return_book(book_name)
        print("Book returned successfully!")

    def print_user_borrowed_books(self, user_id):
        user = self._find_user(user_id)
        if not user:
            return

        if not user.borrowed_books:
            print("No borrowed books.")
            return

        print(f"{user.name} borrowed:")
        for book in user.borrowed_books:
            print(f"- {book}")

    # ---------- HELPERS ----------
    def _find_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        print("User not found.")
        return None

    def _find_book(self, book_name):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                return book
        print("Book not found.")
        return None
class OperationsManager:
    def __init__(self, admin):
        self.admin = admin

    def menu(self):
        while True:
            print("\nProgram Options:")
            print("1) Add book")
            print("2) Print library books")
            print("3) Print books by prefix")
            print("4) Add user")
            print("5) Borrow book")
            print("6) Return book")
            print("7) Print user's borrowed books")
            print("8) Print users")
            print("9) Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self._add_book()
            elif choice == "2":
                self.admin.print_books()
            elif choice == "3":
                prefix = input("Enter prefix: ")
                self.admin.print_books_by_prefix(prefix)
            elif choice == "4":
                self._add_user()
            elif choice == "5":
                self._borrow_book()
            elif choice == "6":
                self._return_book()
            elif choice == "7":
                user_id = input("Enter user ID: ")
                self.admin.print_user_borrowed_books(user_id)
            elif choice == "8":
                self.admin.print_users()
            elif choice == "9":
                print("Exiting system...")
                break
            else:
                print("Invalid choice!")

    def _add_book(self):
        book_id = input("Enter book ID: ")
        name = input("Enter book name: ")
        quantity = int(input("Enter quantity: "))
        self.admin.add_book(book_id, name, quantity)

    def _add_user(self):
        user_id = input("Enter user ID: ")
        name = input("Enter user name: ")
        self.admin.add_user(user_id, name)

    def _borrow_book(self):
        user_id = input("Enter user ID: ")
        book_name = input("Enter book name: ")
        self.admin.borrow_book(user_id, book_name)

    def _return_book(self):
        user_id = input("Enter user ID: ")
        book_name = input("Enter book name: ")
        self.admin.return_book(user_id, book_name)
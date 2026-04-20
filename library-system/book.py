class Book:
    def __init__(self, book_id, name, quantity):
        self.id = book_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Available: {self.quantity}"
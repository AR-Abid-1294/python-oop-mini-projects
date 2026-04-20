status_dict = {0: "Normal",
               1: "Urgent",
               2: "Super-urgent"}

class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"Patient (Name: {self.name}, Status: {status_dict[self.status]})"
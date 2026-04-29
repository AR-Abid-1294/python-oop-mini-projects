import random

class Acc:
    def __init__(self, acc_id, acc_name, acc_pin):
        self.id = acc_id
        self.name = acc_name
        self.pin = acc_pin
        self.balance = 0
        print(f"New Account Created with acc no ({self.id}) under the name of {self.name}")




class ATM:
    def __init__(self):
        self.accounts = dict()          # acc_id as keys ||| acc object as values

    def createNewAcc(self):
        # create a unique id for the new account
        while True:
            new_acc_id = random.randint(1000, 9999)
            if new_acc_id not in self.accounts:
                break

        # take a name for the account
        new_acc_name = input("Enter your name: ")

        # take a 3-digit PIN for the account
        while True:
            new_acc_pin = input("Enter your 3-digit PIN: ")
            if new_acc_pin.isdigit() and len(new_acc_pin) == 3:
                new_acc_pin = int(new_acc_pin)
                break
            else:
                print("PIN MUST BE A 3-DIGIT INTEGER NUMBER!")

        # create the account and store the details
        new_acc = Acc(new_acc_id, new_acc_name, new_acc_pin)
        self.accounts[new_acc_id] = new_acc

    def accessAcc(self, acc_id, acc_pin):
        if acc_id in self.accounts:
            if self.accounts[acc_id].pin == acc_pin:
                account = self.accounts[acc_id]
                return account
            else:
                print("Wrong PIN")
        else:
            print("No account found with the given id")

    def checkBalance(self, account):
        return account.balance

    def deposit(self, account, amount):
        account.balance += amount
        print(f"{amount} BDT deposited to your account (Acc ID: {account.id}).")

    def withdraw(self, account, amount):
        account.balance -= amount
        print(f"{amount} BDT withdrawn from your account (Acc ID: {account.id}).")


main_menu_options = []

def main():
    while True:
        print("Welcome to the ATM!")
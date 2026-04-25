import random

class Player:
    def __init__(self):
        self.init_balance = int(input("Enter your starting balance: "))
        self.balance = self.init_balance

    def win(self, amount):
        print(f"Congrats! You won ${amount} ;)")
        self.balance += amount

    def lose(self, amount):
        print(f"Bad Luck! You lost ${amount} :(")
        self.balance -= amount


class Machine:
    def __init__(self):
        self.symbols = ['🍒', '⭐', '💎']
        print("\nWelcome to the Slot Machine Game!")

    def bet(self, player):
        print(f"\nCurrent Balance: ${player.balance}")
        bet_amount = int(input("Enter your bet amount ($): "))

        if bet_amount > player.balance:
            print("Sorry, you don't have enough balance.")
        else:
            return bet_amount

    def play(self, player):
        bet_amount = self.bet(player)
        slotA = random.choice(self.symbols)
        slotB = random.choice(self.symbols)
        slotC = random.choice(self.symbols)
        print(f"{slotA} | {slotB} | {slotC}")

        if slotA == slotB == slotC:
            player.win(bet_amount * 10)
        elif len(set([slotA, slotB, slotC])) == 2:
            player.win(bet_amount)
        else:
            player.lose(bet_amount)

        return input("Do you want to play again? (y/n): ").lower() == 'y'
    
    def finish(self, player):
        print("\nThanks for playing!")
        print(f"You started with ${player.init_balance}.")
        print(f"You're finishing with ${player.balance}.")


def main():
    customer = Player()
    slot_machine = Machine()

    play_continue = True
    while play_continue:
        play_continue = slot_machine.play(customer)
    else:
        slot_machine.finish(customer)


if __name__ == "__main__":
    main()
        
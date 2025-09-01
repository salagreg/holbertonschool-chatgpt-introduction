#!/usr/bin/python3
"""
Checkbook Application

This program simulates a simple checkbook, allowing a user to:
- deposit money,
- withdraw money,
- check their balance.

Invalid inputs are safely handled to prevent the program from crashing.
"""


class Checkbook:
    """
    A simple checkbook class to track deposits, withdrawals, and balance.
    """

    def __init__(self):
        """
        Initialize the checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Args:
            amount (float): The amount to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main loop to interact with the user via command-line input.
    Supports: deposit, withdraw, balance, exit.
    Handles invalid numeric inputs safely.
    """
    cb = Checkbook()

    while True:
        action = input("What would you like to do? : ").strip().lower()

        if action == 'exit':
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

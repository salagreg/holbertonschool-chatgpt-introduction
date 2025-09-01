#!/usr/bin/python3


class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    try:
        while True:
            prompt = "What would you like to do? " \
                     "(deposit, withdraw, balance, exit): "
            action = input(prompt)
            if action.lower() == 'exit':
                break
            elif action.lower() == 'deposit':
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    if amount < 0:
                        print("Error: Amount cannot be negative.")
                    else:
                        cb.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                except KeyboardInterrupt:
                    print("\nOperation cancelled.")
                    continue
            elif action.lower() == 'withdraw':
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    if amount < 0:
                        print("Error: Amount cannot be negative.")
                    else:
                        cb.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                except KeyboardInterrupt:
                    print("\nOperation cancelled.")
                    continue
            elif action.lower() == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting program. Goodbye!")
    except EOFError:
        print("\nExiting program. Goodbye!")


if __name__ == "__main__":
    main()

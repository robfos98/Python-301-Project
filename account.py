import time

class Account:
    money = 0.0

    def checkCents(self, x):
        try:
            x = str(float(x))
            if '-' in x:
                if 'e' in x: raise FloatingPointError
                else: raise ArithmeticError
            elif 'e' in x: raise OverflowError
            x = x.split('.')
            if len(x[1]) > 2: raise FloatingPointError
            return float(x[0] + '.' + x[1])
        except ValueError:
            print("That's not a number.")
        except FloatingPointError:
            print("Please use a whole number of cents.")
        except OverflowError:
            print("That sum is beyond the limits of this account.")
        except ArithmeticError:
            print("Please do not enter a negative amount of money.")
        return 0.0

    def deposit(self, x):
        x = self.checkCents(x)
        x += self.money
        if 'e' in str(x):
            print("Your account is too full! Transaction declined.")
        else:
            with open('log.txt', 'a') as log:
                log.write(f"Deposited: ${x - self.money}, {time.ctime(time.time())}\n")
                log.write("Total: " + str(round(x, 2))  + "\n\n")
            self.money = round(x, 2)

    def withdraw(self, x):
        x = self.checkCents(x)
        if x > self.money:
            print("Your account doesn't have that much money. Transaction declined.")
        else:
            with open('log.txt', 'a') as log:
                log.write(f"Withdrawn: ${x}, {time.ctime(time.time())}\n")
                log.write("Total: " + str(round(self.money - x, 2)) + "\n\n")
            self.money -= round(x, 2)

    def __init__(self, dollars = 0.0):
        with open('log.txt', 'w') as log:
            log.write("Account opened:\n")
        self.deposit(dollars)

def app():
    print("Hello!")
    yourAccount = Account()
    print("Congratulations on your new bank account! It lasts as long as this program runs.")
    while True:
        print("\nWould you like to withdraw (w) or deposit (d) money? Press q to quit.")
        decision = input().lower()
        if decision in ['exit', 'leave', 'quit', 'end', 'out', 'over', 'q', 'x']: break
        elif decision in ['withdraw', 'withdrawal', 'w']:
            print("How much money will you be withdrawing?")
            yourAccount.withdraw(input())
        elif decision in ['deposit', 'd']:
            print("How much will you deposit?")
            yourAccount.deposit(input())
        else: print("I'm sorry! That wasn't a valid command.")

app()
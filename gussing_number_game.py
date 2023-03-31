import random

random_number = random.randint(1, 100)
user_guess = input("Guess the number: ")
while True:
    try:
        int(user_guess)
        break
    except ValueError:
        user_guess = input("Its not a number try again: ")
    except Exception:
        user_guess = input("There was a problem please try again: ")


def gussing(random, user):
    pass
import random

random_number = random.randint(1, 100)
user_guess = input("Guess the number: ")
while True:
    try:
        int(user_guess)
        if int(user_guess) < random_number:
            print("Too small!")
            user_guess = input("Guess the number: ")
        elif int(user_guess) > random_number:
            print("Too big!")
            user_guess = input("Guess the number: ")
        else:
            print("You won!")
            break
    except ValueError:
        user_guess = input("Its not a number try again: ")
    except Exception:
        user_guess = input("There was a problem please try again: ")

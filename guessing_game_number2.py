print("Think about a number between 0 and 1000, I will guess it in less then ten tries")

lowest = 0
highest = 1000

while True:
    guess = int((highest - lowest) / 2) + lowest
    print(f"I guess: {guess}")
    print("Is the number too big, too small or I won: ")
    answer = input()
    if answer == "You won":
        print("I won!")
        break
    elif answer == "too big":
        highest = guess
    elif answer == "too small":
        lowest = guess
    else:
        print("don't cheat!")

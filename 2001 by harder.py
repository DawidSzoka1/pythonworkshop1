import random

first_player = 0
computer = 0
print("available dices: D3, D4, D6, D8, D10, D12, D20, D100")


def computer_dices():
    posible_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    computer_dice = []
    for i in range(2):
        a = random.randint(0, 7)
        computer_dice.append(a)
    computer_choice = [posible_dices[computer_dice[0]], posible_dices[computer_dice[1]]]
    return computer_choice


def check_dice(dice1, dice2):
    posible_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    if dice1 in posible_dices and dice2 in posible_dices:
        return True
    else:
        return False


while True:
    first_dice = input("Please choose dice from set: ")
    second_dice = input("Please choose dice from set: ")
    while True:
        if check_dice(first_dice, second_dice):
            break
        elif check_dice(first_dice, second_dice) == False:
            print("one of the dices wasn't in set")
            first_dice = input("Please choose dice from set: ")
            second_dice = input("Please choose dice from set: ")

    computer_dicess = computer_dices()
    check_computer = 0
    check_player = 0
    check_computer += random.randint(1, int(computer_dicess[0][1:]))
    check_computer += random.randint(1, int(computer_dicess[1][1:]))
    if check_computer == 7:
        computer = computer // 7
    elif check_computer == 11:
        computer = computer * 11
    else:
        computer += check_computer

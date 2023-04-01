import random

first_player = 0
computer = 0


def check_dice(dice1, dice2):
    posible_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    computer_dice = []
    for i in range(2):
        a = random.randint(0, 7)
        computer_dice.append(a)
    computer_choice = [posible_dices[computer_dice[0]], posible_dices[computer_dice[1]]]
    if dice1 not in posible_dices or dice2 not in posible_dices:
        return "We don't have dice like that"
    return computer_choice



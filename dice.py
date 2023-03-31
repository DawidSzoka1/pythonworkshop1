import random

def dice(dice):
    posible_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    modifier = ["+", "-"]
    list_dice = [i for i in dice]
    for i in range(len(list_dice)):
        if list_dice[i] == modifier[0]:
            split_dice = dice.split("+")
            throw = split_dice[0]
            modif = split_dice[1]
        elif list_dice[i] == modifier[1]:
            split_dice = dice.split("-")
            throw = split_dice[0]
            modif = split_dice[1]
        else:
            no_modif = True
    for i in range(len(dice)):
        if dice[i] == "D":
            position_of_D = i
    if dice[:position_of_D]:
        numbers_of_throw = int(dice[:position_of_D])

    if no_modif == True:
        if dice[position_of_D:] not in posible_dices:
            return "In our game we don't have this dice"
        else:
            thrown_number = 0
            if dice[:position_of_D]:
                for i in range(numbers_of_throw):
                    thrown_number += random.randint(1, int(dice[position_of_D+1:]))
            else:
                thrown_number += random.randint(1, int(dice[position_of_D+1:]))
            return thrown_number


print(dice("D10"))

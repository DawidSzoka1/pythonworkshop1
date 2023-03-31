import random


def dice(dice):
    posible_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    modifier = ["+", "-"]
    thrown_number = 0
    list_dice = [i for i in dice]
    no_modif = True
    for i in range(len(list_dice)):  # checking if dice have modifierf if yes then spliting dice
        if list_dice[i] == modifier[0]:
            split_dice = dice.split("+")
            throw = split_dice[0]
            modif = split_dice[1]
            modif_type = "+"
            no_modif = False
        elif list_dice[i] == modifier[1]:
            split_dice = dice.split("-")
            throw = split_dice[0]
            modif = split_dice[1]
            modif_type = "-"
            no_modif = False

    for i in range(len(dice)):  # posiotion of D in string
        if dice[i] == "D":
            position_of_D = i
    if dice[:position_of_D]:  # checking if dice is throw multiple times
        numbers_of_throw = int(dice[:position_of_D])

    if no_modif != False:
        if dice[position_of_D:] not in posible_dices:
            return "In our game we don't have this dice"
        else:
            if dice[:position_of_D]:
                for i in range(numbers_of_throw):
                    thrown_number += random.randint(1, int(dice[position_of_D + 1:]))
            else:
                thrown_number += random.randint(1, int(dice[position_of_D + 1:]))
            return thrown_number
    else:
        if dice[:position_of_D]:
            for i in range(numbers_of_throw):
                thrown_number += random.randint(1, int(throw[position_of_D + 1:]))
            if modif_type == "+":
                thrown_number += int(modif)
            else:
                thrown_number -= int(modif)
                            
        else:
            if modif_type == "+":
                thrown_number += random.randint(1, int(throw[position_of_D + 1:]))
                thrown_number += int(modif)
            else:
                thrown_number += random.randint(1, int(throw[position_of_D + 1:]))
                thrown_number -= int(modif)
                
        return thrown_number


print(dice("2D10+10"))
print(dice("D10"))
print(dice("3D10"))
print(dice("6D100-10"))

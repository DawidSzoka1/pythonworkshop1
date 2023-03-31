import random


def dice(dice):
    posible_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    modifier = ["+", "-"]
    thrown_number = 0
    numbers_of_throw = 1
    no_modif = True
    for i in range(len(dice)):  # checking if dice have modifierf if yes then spliting dice
        if dice[i] == modifier[0]:
            split_dice = dice.split("+")
            throw = split_dice[0]
            modif = split_dice[1]
            modif_type = "+"
            no_modif = False
        elif dice[i] == modifier[1]:
            split_dice = dice.split("-")
            throw = split_dice[0]
            modif = split_dice[1]
            modif_type = "-"
            no_modif = False
    try:
        for i in range(len(dice)):  # posiotion of D in string
            if dice[i] == "D":
                position_of_D = i

        if dice[:position_of_D]:  # checking if dice is throw multiple times
            numbers_of_throw = int(dice[:position_of_D])
    except Exception:
        return "There is no D in your dice"

    if no_modif != False:
        if dice[position_of_D:] not in posible_dices:
            return "In our game we don't have this dice"
        else:
            if dice[:position_of_D]:
                for i in range(numbers_of_throw):
                    thrown_number += random.randint(1, int(dice[position_of_D + 1:]))
            else:
                thrown_number += random.randint(1, int(dice[position_of_D + 1:]))
            strin = f"""
Throwing dice type {dice[position_of_D:]}, 
{numbers_of_throw} times without modifier you got: {thrown_number}            
            """
            return strin
    else:
        if throw[position_of_D:] not in posible_dices:
            return "In our game we don't have this dice"

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
        strin = f"""
Throwing dice type {throw[position_of_D:]}, 
{numbers_of_throw} times with modifier {modif_type + modif} you got: {thrown_number}"""
        return strin


print(dice("32D32*10"))
print(dice("D10"))
print(dice("3D10"))
print(dice("D100-10"))

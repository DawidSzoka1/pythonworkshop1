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
        if list_dice[i] == modifier[1]:
            split_dice = dice.split("-")
            throw = split_dice[0]
            modif = split_dice[1]

    # if len(dice) == 5:
    #     if dice[1:3] not in posible_dices:
    #         return "In our game we don't have this dice"
    #     elif dice[3] not in modifier:
    #         return "You can't use this modifier"
    #     try:
    #         int(dice[0])
    #     except Exception:
    #         return "Number of throws need to ba a number"

print(dice("2D10+10"))

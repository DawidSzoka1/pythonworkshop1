def dice(dice):
    posible_dices = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    modifier = ["+", "-"]
    if len(dice) == 5:
        if dice[1:3] not in posible_dices:
            return "In our game we don't have this dice"
        elif dice[3] not in modifier:
            return "You can't use this modifier"
        try:
            int(dice[0])
        except Exception:
            return "Number of throws need to ba a number"


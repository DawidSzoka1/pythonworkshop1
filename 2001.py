import random

first_player = 0
second_player = 0


while True:
    check1 = 0
    check2 = 0
    for i in range(2):
        check1 += random.randint(1, 6)
        check2 += random.randint(1, 6)
    start = input("to throw your dice press enter: ")
    if check1 == 7:
        first_player = first_player // 7
    elif check1 == 11:
        first_player = first_player * 11
    else:
        first_player += check1
    check2 = random.randint(1, 6)
    if check2 == 7:
        second_player = second_player // 7
    elif check2 == 11:
        second_player = second_player * 11
    else:
        second_player += check2
    print(f"first player have {first_player} points")
    print("-------------------")
    print(f"second player have {second_player} points")
    print("-------------------")
    if first_player >= 2001:
        print("first player won")
        break
    elif second_player >= 2001:
        print("second player won")
        break

from play import checking
from os import system
# demo function

def demo(
    r1c1, r1c2, r1c3,
    r2c1, r2c2, r2c3,
    r3c1, r3c2, r3c3
):
    my_list = [r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3]
    demo1 = [my_list[0], "|", my_list[1], "|", my_list[2]]
    demo2 = [my_list[3], "|", my_list[4], "|", my_list[5]]
    demo3 = [my_list[6], "|", my_list[7], "|", my_list[8]]

    var = demo1
    for i in range(3):
        if i == 0:
            var = demo1
        elif i == 1:
            var = demo2
        else:
            var = demo3

        for j in var:
            print(j, end="")

        print()
        if i != 2:
            print("-----")


empt = " "
checks = [empt, empt, empt, empt, empt, empt, empt, empt, empt]


condition = True
while condition:
    user_input = input("X or O: -> ")
    com = ""
    if user_input.lower() == "x":
        user_input = "X"
        com = "O"
        # run code ->
        selected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while True:
            #system("clear")

            demo(checks[0], checks[1], checks[2], checks[3],
                 checks[4], checks[5], checks[6], checks[7], checks[8])
            
            for num in selected:
                print(num, end=" > ")
            position = int(input("index: > "))

            if position in selected:
                selected.remove(position)
                checks[position-1] = "X"
                checks[checking(checks, selected) - 1] = "O"

        # < -
    elif user_input.lower() == "o":
        user_input = "O"
        com = "X"

    else:
        continue

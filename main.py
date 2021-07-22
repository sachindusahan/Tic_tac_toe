
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

empty = " "
demo(empty, "X", empty, "X", empty, "X", "X", "X", "O")



condition = True
while condition:
    user_input = input("X or O: -> ")
    com = ""
    if user_input.lower() == "x":
        user_input = "X"
        com = "O"
    elif user_input.lower() =="o":
        user_input = "O"
        com = "X"
    else:
        continue


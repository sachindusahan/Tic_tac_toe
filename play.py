empt = " "
checks = [empt, empt, empt, empt, empt, empt, empt, empt, empt]
not_selected = [1, 2, 3, 5, 6, 7, 9]
# 0 1 2
# 3 4 5
# 6 7 8
lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def checking(arg1, arg2, arg3, arg4):
    # arg1 = all places
    # arg2 = not_selected
    # arg3 = user input
    # arg4 = com
    index = 1
    for line in lines:
        for i in line:
            if arg1[i] == arg3:
                index += 1

        if index == 2:
            return_value = line.index(empt)
            return return_value
        else:
            for no in arg2:
                return no



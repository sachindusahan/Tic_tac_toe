import random

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
    # arg1 = checks
    # arg2 = available
    # arg3 = user input
    # arg4 = com


    for line in lines:
        count1 = 0
        count2 = 0
        empty = 0
        for i in range(3):
            if arg1[line[i]] == arg3:
                count1 += 1
            if arg1[line[i]] == empt:
                empty += 1
                x = line[i]

        if count1 ==2 and empty == 1:
            return x

    return arg1.index(empt)

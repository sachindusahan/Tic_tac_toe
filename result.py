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


def result(user, computer, checks):
    for line in lines:
        count1 = 0
        count2 = 0
        for i in range(3):
            if checks[line[i]] == user:
                count1 += 1
            if checks[line[i]] == computer:
                count2 += 1
        if count1 == 3:
            return "You won"
        elif count2 == 3:
            return "You loss"
        
        elif " " not in checks:
            return "Draw"

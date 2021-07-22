checks = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
    1, 4, 7], [2, 5, 8], [3, 6, 9], [7, 5, 3], [9, 5, 1]]


check_list1 = []
check_list2 = []
def check_x_o(arg1, arg2):
    # arg1 = i'm (computer)
    for i in checks:
        for j in i:
            if j == arg2:
                check_list1.append(j)
            elif j == arg1:
                check_list2.append(j)




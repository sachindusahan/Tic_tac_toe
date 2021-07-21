def demo(
        r1c1, r1c2, r1c3,
        r2c1, r2c2, r2c3,
        r3c1, r3c2, r3c3
    ):
    all_list = [r1c1, r1c2, r1c3, r2c1, r2c2, r2c3, r3c1, r3c2, r3c3]
    demo1 = [r1c1, "|", r1c2, "|", r1c3]
    for i in range(3):
        for j in demo1:
            print(j, end="")
        print()
        if i != 2:
            print("------")
demo()

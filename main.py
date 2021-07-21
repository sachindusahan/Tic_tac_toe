def demo():
    demo1 = [" ", "|", "  ", "|", " "]
    for i in range(3):
        for j in demo1:
            print(j, end="")
        print()
        if i != 2:
            print("------")
demo()
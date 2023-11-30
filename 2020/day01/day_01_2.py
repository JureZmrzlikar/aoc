for n1 in open("input.txt"):
    n1 = int(n1)
    for n2 in open("input.txt"):
        n2 = int(n2)
        for n3 in open("input.txt"):
            n3 = int(n3)
            if n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
                exit()
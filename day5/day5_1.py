with open("day5.txt", "r") as f:
    lines = f.readlines()

    crates = [[], [], [], [], [], [], [], [], []]
    
    for l in lines:
        if l == " 1   2   3   4   5   6   7   8   9 \n":
            break

        cs = ""
        for i in range(1, len(l), 4):
            cs += l[i] 
            if l[i] != " ": crates[(i-1)//4].insert(0, l[i])

    for _ in lines[10:]:
        l = _[:-1]
        
        n, c1, c2 = 0, 0, 0
        p = ""
        for c in l:
            if c in "1234567890":
                p += c
            elif p:
                if not n:
                    n = int(p)
                elif not c1:
                    c1 = int(p)
                else:
                    c2 = int(p)
                p = ""
        c2 = int(p)
        
        for x in range(n):
            i1 = c1 - 1
            i2 = c2 - 1
            crates[i2].append(crates[i1].pop())

    for c in crates:
        print(c[-1], end="")
    print()

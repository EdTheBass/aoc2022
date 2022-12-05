with open("day2.txt", "r") as f:
    content = f.readlines()
    score = 0
    for r in content:
        elf_move = r[0]
        my_move = r[2]
        if my_move == "X":
            score += 1

            if elf_move == "A":
                score += 3
            elif elf_move == "C":
                score += 6
        elif my_move == "Y":
            score += 2

            if elf_move == "A":
                score += 6
            elif elf_move == "B":
                score += 3
        elif my_move == "Z":
            score += 3

            if elf_move == "B":
                score += 6
            elif elf_move == "C":
                score += 3

    print(score)

        

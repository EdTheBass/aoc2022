def parse_instruction(i):
    op = i[:4]
    if op == "noop":
        return 0, 1
    elif op == "addx":
        return int(i[5:]), 2

with open("day10.txt", "r") as f:
    instructions = f.readlines()

    x_reg = 1
    cycle = 0
    for _ in instructions:
        increment, cs = parse_instruction(_)

        for x in range(cs):
            if abs(cycle - x_reg) <= 1:
                print("#", end="")
            else:
                print(".", end="")

            if x == 1:
                x_reg += increment

            cycle += 1

            if cycle % 40 == 0:
                cycle -= 40
                print()

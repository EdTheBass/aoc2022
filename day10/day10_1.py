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
    total_ss = 0
    for _ in instructions:
        increment, cs = parse_instruction(_)

        for x in range(cs):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                total_ss += cycle * x_reg
        
        x_reg += increment

    print(total_ss)

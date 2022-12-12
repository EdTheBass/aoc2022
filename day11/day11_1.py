class Monkey:
    def __init__(self, num, items, operation, test, tn, fn):
        self.num = num
        self.items = items
        self.operation = operation
        self.test = test
        self.tn = tn
        self.fn = fn
        self.mt = None
        self.mf = None

def parse_monkey(lines):
    n = int(lines[0][7])
    items = []
    for _ in lines[1][18:].split(", "):
        items.append(int(_))
    
    op = lines[2][23]
    n2 = lines[2][25:]
    operation = None
    if n2 == "old\n":
        if op == "*":
            operation = lambda x: x**2
        else:
            operation = lambda x: 2*x
    else:
        n2 = int(n2)
        if op == "*":
            operation = lambda x: x * n2
        else:
            operation = lambda x: x + n2

    test_num = int(lines[3][21:])
    test = lambda x: x % test_num == 0

    tn = int(lines[4][29])
    fn = int(lines[5][30])

    return Monkey(n, items, operation, test, tn, fn)

def monkey_business(inspections):
    max1 = max(inspections)
    inspections.remove(max1)
    max2 = max(inspections)
    return max1 * max2

with open("day11.txt", "r") as f:
    lines = f.readlines()

    monkeys = []
    for m in range(8):
        new_monkey = parse_monkey(lines[7*m:7*m+6])
        monkeys.append(new_monkey)
    
    for m in monkeys:
        true_monkey = monkeys[m.tn]
        false_monkey = monkeys[m.fn]
        m.mt = true_monkey
        m.mf = false_monkey

    inspections = [0] * 8
    for round in range(20):
        for m in monkeys:
            for i in m.items:
                inspections[m.num] += 1
                worry_level = m.operation(i) // 3
                if m.test(worry_level):
                    m.mt.items.append(worry_level)
                else:
                    m.mf.items.append(worry_level)
            m.items = []

    print(monkey_business(inspections))

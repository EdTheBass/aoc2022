with open("day1.txt", "r") as f:
    content = f.read()[:-1]
    content = content.split("\n\n")
    inventories = []
    for inv in content:
        inventories.append(inv.split("\n"))
        for x in range(len(inventories[-1])):
            inventories[-1][x] = int(inventories[-1][x])
    
    totals = []
    for x in inventories:
        totals.append(sum(x))

    top_3_total = 0
    for x in range(3):
        top = max(totals)
        totals.pop(totals.index(top))
        top_3_total += top

    print(top_3_total)

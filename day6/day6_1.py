def get_prev_4(ds, end):
    return ds[end-3:end+1]

def all_different(marker):
    def count(c):
        total = 0
        for x in marker:
            if x == c: total += 1

        return total

    c1, c2, c3, c4 = count(marker[0]), count(marker[1]), count(marker[2]), count(marker[3])
    return (c1 == 1 and c2 == 1 and c3 == 1 and c4 == 1)

with open("day6.txt", "r") as f:
    d_stream = f.read()[:-1]
    
    end = -1
    for x in range(3, len(d_stream)):
        marker = get_prev_4(d_stream, x)
        if all_different(marker):
            end = x+1
            break

    print(end)

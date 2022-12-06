def get_prev_14(ds, end):
    return ds[end-13:end+1]

def all_different(marker):
    def count(c):
        total = 0
        for x in marker:
            if x == c: total += 1

        return total

    for m in marker:
        if count(m) != 1:
            return False

    return True

with open("day6.txt", "r") as f:
    d_stream = f.read()[:-1]
    
    end = -1
    for x in range(13, len(d_stream)):
        marker = get_prev_14(d_stream, x)
        if all_different(marker):
            end = x+1
            break

    print(end)



def form_matrix(lines):
    matrix = []
    for _ in lines:
        l = _.replace("\n", "")
        row = []
        for __ in (l):
            height = int(__)
            row.append(height)
        matrix.append(row)
    return matrix

def get_left(m, i, j):
    return m[i][:j]

def get_right(m, i, j):
    return m[i][j+1:]

def get_up(m, i, j):
    up = []
    for _ in m[:i]:
        up.append(_[j])
    return up

def get_down(m, i, j):
    down = []
    for _ in m[i+1:]:
        down.append(_[j])
    return down

def linear_visibility(l, h, a):
    num_visible = 0
    s_step = 1 if a == "l" else -1
    for t in l[::s_step]:
        num_visible += 1
        if t >= h:
            break
    return num_visible

def visibility(m, i, j):
    height = m[i][j]
    left = get_left(m, i, j)
    right = get_right(m, i, j)
    up = get_up(m, i, j)
    down = get_down(m, i, j)

    if not left or not right or not up or not down:
        return True

    v1, v2, v3, v4 = linear_visibility(left, height, "r"), linear_visibility(right, height, "l"), linear_visibility(up, height, "r"), linear_visibility(down, height, "l")
    return scenic_score(v1, v2, v3, v4)

def scenic_score(v1, v2, v3, v4):
    return v1 * v2 * v3 * v4

with open("day8.txt", "r") as f:
    content = f.readlines()
    
    matrix = form_matrix(content)

    highest = 0
    for i, line in enumerate(matrix):
        for j, tree in enumerate(line):
            v = visibility(matrix, i, j)
            if v > highest:
                highest = v
    
    print(highest)

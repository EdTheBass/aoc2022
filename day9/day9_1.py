def parse_move(move):
    return move[0], int(move[2:-1])

def apply_move(pos, d):
    x, y = pos
    if d == "R":
        return [x+1, y]
    elif d == "L":
        return [x-1, y]
    elif d == "U":
        return [x, y+1]
    else:
        return [x, y-1]

def calc_tail_pos(head_pos, tail_pos):
    hx, hy = head_pos
    tx, ty = tail_pos
    def adjacent():
        dx = tx - hx
        dy = ty - hy
        if abs(dx) <= 1 and abs(dy) <= 1:
            return True, dx, dy
        return False, dx, dy

    a, dx, dy = adjacent()
    if a:
        return tail_pos

    s_dx = (dx//abs(dx)) if dx != 0 else 0
    s_dy = (dy//abs(dy)) if dy != 0 else 0
    
    return [tx-s_dx, ty-s_dy]
    

with open("day9.txt", "r") as f:
    moves = f.readlines()
    
    head_position = [0, 0]
    tail_position = [0, 0]
    visited = []
    for _ in moves:
        direction, magnitude = parse_move(_)
        
        for _ in range(magnitude):
            head_position = apply_move(head_position, direction)
            tail_position = calc_tail_pos(head_position, tail_position)
            
            if tail_position not in visited:
                visited.append(tail_position)

    print(len(visited))


def load_moves(filename):
    """Load the moves file and simplify to a sequence of single UDLR moves"""
    moves = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            direction, count =  line.split()
            moves.extend(direction * int(count))
    return moves

def make_move(move, head_pos, tail_pos):
    if move == 'U':
        head_pos = (head_pos[0], head_pos[1] + 1)
    elif move == 'D':
        head_pos = (head_pos[0], head_pos[1] - 1)
    elif move == 'L':
        head_pos = (head_pos[0] - 1, head_pos[1])
    elif move == 'R':
        head_pos = (head_pos[0] + 1, head_pos[1])
    else:
        raise ValueError(move)

    tail_pos = move_tail(head_pos, tail_pos)
    #print("Move: {0}, Head at: {1}, Tail at {2}".format(move, head_pos, tail_pos))

    return head_pos, tail_pos

def move_tail(head_pos, tail_pos):

    x_diff = head_pos[0] - tail_pos[0]
    y_diff = head_pos[1] - tail_pos[1]
    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return tail_pos
    if x_diff == 2:
        return (head_pos[0]-1, head_pos[1])
    if x_diff == -2:
        return (head_pos[0]+1, head_pos[1])
    if y_diff == 2:
        return (head_pos[0], head_pos[1]-1)
    if y_diff == -2:
        return (head_pos[0], head_pos[1]+1)
    raise(ValueError(head_pos, tail_pos))

def day_nine(filename):
    head_pos = (0, 0)
    tail_pos = (0, 0)
    tail_positions = {tail_pos}
    moves = load_moves(filename)
    
    for move in moves:
        head_pos, tail_pos = make_move(move, head_pos, tail_pos)
        tail_positions.add(tail_pos)

    print(tail_positions)
    return len(tail_positions)

input = 'day_09\\input_day9.txt'
test_input = 'day_09\\test_input_day9.txt'

print("Puzzle 17: {0}".format(day_nine(input)))
#print("Puzzle 18: {0}".format(day_nine(test_input)))
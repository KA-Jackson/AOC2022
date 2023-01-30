
def load_moves(filename):
    """Load the moves file and simplify to a sequence of single UDLR moves"""

    moves = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            direction, count =  line.split()
            moves.extend(direction * int(count))
    return moves

def make_move(move_number, move, knot_positions):
    """Use the move direction to move the head, and then move each following knot"""

    knot_positions[0] = move_headknot(move_number, move, knot_positions[0])

    for knot in range(1, len(knot_positions)):
        knot_positions[knot] = move_knot(move_number, knot_positions[knot - 1], knot_positions[knot])

    return knot_positions

def move_headknot(move_number, move, head_pos):
    """Simply move the headknot one position UDL or R
    Raise a ValueError if the passed move not as expected"""

    if move == 'U':
        head_pos = (head_pos[0], head_pos[1] + 1)
    elif move == 'D':
        head_pos = (head_pos[0], head_pos[1] - 1)
    elif move == 'L':
        head_pos = (head_pos[0] - 1, head_pos[1])
    elif move == 'R':
        head_pos = (head_pos[0] + 1, head_pos[1])
    else:
        raise ValueError(move_number, move)
    return head_pos

def move_knot(move_number, lead_knot_pos, knot_pos):
    """Use the rules to move a knot based on the position of the knot's leading knot.
    Raise error if leading knot and knot are more than 2 spaces out as this should not happen"""
    
    x_diff = lead_knot_pos[0] - knot_pos[0]
    y_diff = lead_knot_pos[1] - knot_pos[1]

    if x_diff > 2 or y_diff > 2:
        raise ValueError(move_number, lead_knot_pos, knot_pos, x_diff, y_diff)

    new_x, new_y = knot_pos
    if abs(x_diff) == 2:
        new_x += x_diff / 2
        if y_diff > 0:
            new_y += 1
        elif y_diff < 0:
            new_y -= 1
    elif abs(y_diff) == 2:
        new_y += y_diff / 2
        if x_diff > 0:
            new_x += 1
        elif x_diff < 0:
            new_x -= 1
    
    return (int(new_x), int(new_y))

def day_nine(filename, knots):
    """Run the day 9 puzzles for the passed input file and number of knots"""

    move_number = 0
    knot_positions = [(0, 0) for x in range(knots)]
    tail_positions = {(0, 0)}
    moves = load_moves(filename)
    
    for move in moves:
        move_number += 1
        knot_positions = make_move(move_number, move, knot_positions)
        tail_positions.add(knot_positions[knots - 1])

    return len(tail_positions)

input = 'day_09\\input_day9.txt'
test_input = 'day_09\\test_input_day9.txt'
test_input2 = 'day_09\\test_input2_day9.txt'

print("Puzzle 17: {0}".format(day_nine(input, 2)))
print("Puzzle 18: {0}".format(day_nine(input, 10)))
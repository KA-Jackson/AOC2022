def get_instructions(filename):
    with open(filename) as f:
        return [l.split() for l in f.readlines()]

def process_instruction(instruction, x):
    if instruction[0] == "noop":
        return [x]
    else:
        return [x, x + int(instruction[1])]

def get_interesting_signal_strengths(cycles):
    """Part 1 of the puzzle. Get the signal during a list of interesting cycles. 
    Cycles is the zero-based list of signals at end of cycles,
    and we need the signal during the cycle, hence - 2"""

    interesting_signals = [20, 60, 100, 140, 180, 220]
    return [n * cycles[n - 2] for n in interesting_signals]

def draw_screen(cycles):
    """Part 2 of the puzzle.  Draw the screen based on the cycle number and its x value.
    The cycles list has the x position as at the end of the cycle, so we need the previous cycle"""

    for row in range(6):
        line = ""
        for pixel in range(40):
            cycle = max(0, row * 40 + pixel - 1)
            x = cycles[cycle]

            if pixel in [x-1, x, x+1]:
                line += "#"
            else:
                line += "."
        print(line)

def day_ten(filename):
    instructions = get_instructions(filename)
    
    cycles, x = [], 1
    for instruction in instructions:
        cycles.extend(process_instruction(instruction, x))
        x = cycles[-1]

    return cycles
    
input = 'day_10\\input_day10.txt'
test_input = 'day_10\\test_input_day10.txt' 

print("Puzzle 19: {0}".format(sum(get_interesting_signal_strengths(day_ten(input)))))
draw_screen(day_ten(input))
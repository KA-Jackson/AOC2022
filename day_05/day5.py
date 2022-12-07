import re

def create_empty_stacks(marker_line):
    stack_count = int(max(marker_line))
    stacks = []
    for i in range(stack_count):
        stacks.append([])
    return stacks

def build_stacks(stack_lines, stacks):
    for line in stack_lines:
        line = line[1::4]
        for stack in range(len(stacks)):
            if line[stack].strip():
                stacks[stack].append(line[stack])
    for stack in stacks:
        stack.reverse()
    return stacks

def do_crate_moves(move_lines, stacks, crate_mover_func):
    for move_line in move_lines:
        instruction = list(map(int, re.findall(r'\d+', move_line)))
        stacks = crate_mover_func(stacks, instruction)
    return stacks

def move_crates_9000(stacks, instruction):
    for _ in range(instruction[0]):
        crate = stacks[instruction[1]-1].pop()
        stacks[instruction[2]-1].append(crate)
    return stacks

def move_crates_9001(stacks, instruction):
    crates = []
    for _ in range(instruction[0]):
        crates.append(stacks[instruction[1]-1].pop())
    crates.reverse()
    stacks[instruction[2]-1].extend(crates)
    return stacks

def top_crates(stacks):
    top = ''
    for stack in stacks:
        top += stack.pop()
    return top

def split_file(filename):
    stack_lines, move_lines, marker_line = [], [], ''
    with open(filename) as file:
        for line in file.readlines():
            if "[" in line:
                stack_lines.append(line)
            elif line.startswith("move"):
                move_lines.append(line)
            elif "1" in line:
                marker_line = line
    return stack_lines, marker_line, move_lines

def day_five(filename, crate_mover_func):
    lines = split_file(filename)
    stacks = create_empty_stacks(lines[1])
    stacks = build_stacks(lines[0], stacks)
    stacks = do_crate_moves(lines[2], stacks, crate_mover_func)
    return top_crates(stacks)

input = 'day_05\\input_day5.txt'
test_input = 'day_05\\test_input_day5.txt'
print("Puzzle 9: " + str(day_five(input, move_crates_9000)))
print("Puzzle 10: " + str(day_five(input, move_crates_9001)))
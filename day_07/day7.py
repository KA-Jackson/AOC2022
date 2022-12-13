from file_directory import file_directory

def process_instruction(root, current, instruction):
    if instruction == '$ ls':
        return current
    elif instruction.startswith('$ cd'):
        if instruction == '$ cd ..':
            return current.move_to_parent_dir()
        elif instruction == '$ cd /':
            return root
        else:
            return current.move_to_sub_dir(instruction.replace('$ cd ', ''))
    elif instruction.startswith('dir'):
        current.add_sub_dir(instruction.replace('dir ', ''))
    else:
        new_file = instruction.split(' ')
        current.add_file(new_file[1], new_file[0])
    return current

def total_size_small_dirs(root, max_size):
    return sum([dir.size() for dir in root.directory_list() if dir.size() < max_size])

def size_of_dir_to_delete(root):
    min_delete_size = 30000000 - (70000000 - root.size())
    return min([dir.size() for dir in root.directory_list() if dir.size() > min_delete_size])

def build_directory(filename):
    root = file_directory('/')
    current = root    
    with open(filename) as file:
        instructions = file.readlines()
        for instruction in instructions:
            current = process_instruction(root, current, instruction.strip())
    return root

def puzzle_13(filename, max_size):
    root = build_directory(filename)
    return total_size_small_dirs(root, max_size)

def puzzle_14(filename):
    root = build_directory(filename)
    return size_of_dir_to_delete(root)

input = 'day_07\\input_day7.txt'
test_input = 'day_07\\test_input_day7.txt'

print("Puzzle 13: " + str(puzzle_13(input, 100000)))
print("Puzzle 14: " + str(puzzle_14(input)))
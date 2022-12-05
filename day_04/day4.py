def build_pair(line):
    elves = line.strip().split(",")
    elf_1 = elves[0].split("-")
    elf_2 = elves[1].split("-")
    elf_1 = int(elf_1[0]), int(elf_1[1])
    elf_2 = int(elf_2[0]), int(elf_2[1])
    return elf_1, elf_2

def check_contained(pair):
    if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        return 1
    if pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
        return 1
    return 0

def check_overlap(pair):
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]:
        return 1
    if pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0]:
        return 1
    return 0

input = 'day_04\\input_day4.txt'

with open(input) as file:
    total = 0
    lines = file.readlines()
    for line in lines:
        pair = build_pair(line)
        total += check_contained(pair)
    print(total)

with open(input) as file:
    total = 0
    lines = file.readlines()
    for line in lines:
        pair = build_pair(line)
        total += check_overlap(pair)
    print(total)

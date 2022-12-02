def get_elves_calories(filename: str):
    elves = []
    elf_calories = 0
    with open(filename) as file:
        while True:
            line = file.readline()
            if not line: #end of file - add last elf
                elves.append(elf_calories)
                break
            item = line.strip()
            if item == "":
                elves.append(elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(item)
    return elves

def sum_list_topn(list: list, n: int):
    sorted_list = sorted(list)
    return sum(sorted_list[-n:])

def puzzle1(filename: str):
    elves_calories = get_elves_calories(filename)
    return sum_list_topn(elves_calories, 1)

def puzzle2(filename: str):
    elves_calories = get_elves_calories(filename)
    return sum_list_topn(elves_calories, 3)

input = 'day_01\\input_day1.txt'

print("Puzzle 1: " + str(puzzle1(input)))
print("Puzzle 2: " + str(puzzle2(input)))
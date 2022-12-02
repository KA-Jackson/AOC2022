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
    sum = 0
    for i in range(-1, -1-n, -1):
        sum += sorted_list[i]
    return sum

def puzzle1(filename: str):
    elves_calories = get_elves_calories(filename)
    return sum_list_topn(elves_calories, 1)

def puzzle2(filename: str):
    elves_calories = get_elves_calories(filename)
    return sum_list_topn(elves_calories, 3)

input = 'day_one\\input_day1.txt'

print(puzzle1(input))
print(puzzle2(input))
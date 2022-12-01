elves = []
elfCalories = 0

with open('./Day1/input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            elves.append(elfCalories)
            break
        item = line.strip()
        if item == "":
            elves.append(elfCalories)
            elfCalories = 0
        else:
            elfCalories = elfCalories + int(item)

#puzzle1
print(max(elves))

#puzzle2
sortedElves = sorted(elves)
print(sortedElves[-1] + sortedElves[-2] + sortedElves[-3])
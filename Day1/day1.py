elves = []
elfCalories = 0

with open('Day1\input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line.strip():
            elfCalories += int(line)
        else:
            elves.append(elfCalories)
            elfCalories = 0

#puzzle1
print(max(elves))

#puzzle2
sortedElves = sorted(elves)
print(sortedElves[-1] + sortedElves[-2] + sortedElves[-3])
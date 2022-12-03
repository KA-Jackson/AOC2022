def sack_compartments_from_line(line: str) -> tuple:
    line = line.strip()
    n = len(line)
    compartment1 = line[0:n//2]
    compartment2 = line[n//2:]
    return set(compartment1), set(compartment2)

def sack_items_from_line(line: str) -> set:
    line = line.strip()
    return set(line)

def shared_item(set1: set, set2: set):
    shared = set1.intersection(set2)
    if len(shared) == 1:
        return shared.pop()
    else:
        raise Exception("Expected only 1 shared item")

def shared_item_3(set1: set, set2: set, set3: set):
    shared = set1.intersection(set2.intersection(set3))
    if len(shared) == 1:
        return shared.pop()
    else:
        raise Exception("Expected only 1 shared item")

def item_priority(item: str):
    if item.upper() == item:
        return ord(item)-38
    else:
        return ord(item)-96

def puzzle_5(filename):
    total_priority = 0
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            sack_compartments = sack_compartments_from_line(line)
            item = shared_item(sack_compartments[0], sack_compartments[1])
            total_priority += item_priority(item)
    return total_priority

def puzzle_6(filename):
    total_priority = 0
    with open(filename) as file:
        lines = file.readlines()
        group = []
        for line in lines:
            group.append(sack_items_from_line(line))
            if len(group) == 3:
                item = shared_item_3(group[0], group[1], group[2])
                group = []
                total_priority += item_priority(item)
    return total_priority

input = 'day_03\\input_day3.txt'

print("Puzzle 5: " + str(puzzle_5(input)))
print("Puzzle 6: " + str(puzzle_6(input)))


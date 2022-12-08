from queue import queue  

def initialise_queue(char_list, size):
    q = queue()
    for n in range(1, size + 1):
        next_char = char_list.pop(0)
        q.enqueue(next_char)
    return q

def list_has_duplicates(list):
    return len(list) > len(set(list))

def find_marker(buffer_string, marker_size):
    char_list = list(buffer_string)
    q = initialise_queue(char_list, marker_size)
    n = marker_size
    while list_has_duplicates(q.items()):
        n += 1
        q.dequeue()
        q.enqueue(char_list.pop(0))
    return n    

def day_six(filename, marker_size):
    with open(filename) as file:
        return find_marker(list(file.read()), marker_size)

input = 'day_06\\input_day6.txt'
test_input = 'day_06\\test_input_day6.txt'

print("Puzzle 11: " + str(day_six(input, 4)))
print("Puzzle 12: " + str(day_six(input, 14)))
def build_grid(filename):
    grid = []
    with open(filename) as file:
        while True:
            line = file.readline().strip()
            if line:
                row = []
                for char in line:
                    row.append(int(char))
                grid.append(row)
            else: break
    return grid

def transpose_grid(grid):
    transposed_grid = []
    for col in range(len(grid[0])):
        column = []
        for row in range(len(grid)):
            column.append(grid[row][col])
        transposed_grid.append(column)
    return transposed_grid

def build_score_grid(grid, transposed_grid, score_func):
    visible_grid = []
    for row in range(len(grid)):
        visible_row = []
        visible_grid.append(visible_row)
        for col in range(len(grid[0])):
            visible_row.append(score_func(grid, transposed_grid, row, col))
    return visible_grid
    
def is_visible(grid, transposed_grid, row, col):
    if is_on_edge(grid, row, col):
        return 1
    if is_visible_left_above(grid[row], col):
        return 1
    if is_visible_right_below(grid[row], col):
        return 1
    if is_visible_left_above(transposed_grid[col], row):
        return 1
    if is_visible_right_below(transposed_grid[col], row):
        return 1
    return 0

def scenic_score(grid, transposed_grid, row, col):
    if is_on_edge(grid, row, col):
        return 0
    left = count_visible_left_above(grid[row], col)
    right = count_visible_right_below(grid[row], col)
    above = count_visible_left_above(transposed_grid[col], row)
    below = count_visible_right_below(transposed_grid[col], row)
    return left * right * above * below

def is_on_edge(grid, row, col):
    if row * col == 0:
        return True
    if row == len(grid)-1:
        return True
    if col == len(grid[0])-1:
        return True
    return False

def is_visible_left_above(list, current):
    return list[current] > max([x for x in list[0:current]])

def is_visible_right_below(list, current):
    return list[current] > max([x for x in list[current+1:]])

def count_visible_left_above(list, current):
    if current == 1: return 1
    count = 0
    for x in range(current-1, -1, -1):
        count += 1
        if list[x] >= list[current]:
            return count
    return count

def count_visible_right_below(list, current):
    if current == len(list)-2: return 1
    count = 0
    for x in range(current+1, len(list)):
        count += 1
        if list[x] >= list[current]:
            return count
    return count

def sum_grid(grid):
    count = 0
    for row in range(len(grid)):
        count += sum(grid[row])
    return count

def max_grid(grid):
    val = 0
    for row in range(len(grid)):
        val = max(max(grid[row]), val)
    return val

def day_eight(filename, score_func, agg_func):
    grid = build_grid(filename)
    transposed_grid = transpose_grid(grid)
    score_grid = build_score_grid(grid, transposed_grid, score_func)
    return agg_func(score_grid)

input = 'day_08\\input_day8.txt'
test_input = 'day_08\\test_input_day8.txt'

print("Puzzle 15: " + str(day_eight(input, is_visible, sum_grid)))
print("Puzzle 16: " + str(day_eight(input, scenic_score, max_grid)))
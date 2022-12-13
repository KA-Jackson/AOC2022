import day7

test_input = 'day_07\\test_input_day7.txt'

def test_13():
    assert day7.puzzle_13(test_input, 100000) == 95437

def test_14():
    assert day7.puzzle_14(test_input) == 24933642
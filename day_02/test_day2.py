import day2

test_input = 'day_02\\test_input_day2.txt'
input = 'day_02\\input_day2.txt'

def test_puzzle3():
    assert day2.puzzle_3(test_input) == 15

def test_3_1():
    assert day2.play_round('A', 'Y', day2.input_to_choice_1) == (1, 8)

def test_3_2():
    assert day2.play_round('B', 'X', day2.input_to_choice_1) == (8, 1)

def test_3_3():
    assert day2.play_round('C', 'Z', day2.input_to_choice_1) == (6, 6)

def test_puzzle4():
    assert day2.puzzle_4(test_input) == 12

def test_4_1():
    assert day2.play_round('A', 'Y', day2.input_to_choice_2) == (4, 4)

def test_4_2():
    assert day2.play_round('B', 'X', day2.input_to_choice_1) == (8, 1)

def test_4_3():
    assert day2.play_round('C', 'Z', day2.input_to_choice_2) == (3, 7)
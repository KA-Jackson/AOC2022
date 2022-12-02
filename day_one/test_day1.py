import day1

test_input = 'day_one\\test_input_day1.txt'
input = 'day_one\\input_day1.txt'

def test_puzzle1():
    assert day1.puzzle1(test_input) == 24000

def test_puzzle2():
    assert day1.puzzle2(test_input) == 45000

def test_firstelf():
    assert day1.get_elves_calories(input)[0] == 50018

def test_lastelf():
    assert day1.get_elves_calories(input)[-1] == 52400

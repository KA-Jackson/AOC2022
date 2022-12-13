import day6

def test_data_11_1():
    assert day6.find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4) == 7

def test_data_11_2():
    assert day6.find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5

def test_data_11_3():
    assert day6.find_marker('nppdvjthqldpwncqszvftbrmjlhg', 4) == 6

def test_data_11_4():
    assert day6.find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10

def test_data_11_5():
    assert day6.find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) == 11

def test_data_12_1():
    assert day6.find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19

def test_data_12_2():
    assert day6.find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23

def test_data_12_3():
    assert day6.find_marker('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23

def test_data_12_4():
    assert day6.find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29

def test_data_12_5():
    assert day6.find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26

input = 'day_05\\input_day5.txt'
test_input = 'day_05\\test_input_day5.txt'
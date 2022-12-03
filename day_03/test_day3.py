import day3

test_input = 'day_03\\test_input_day3.txt'
input = 'day_03\\input_day3.txt'

def test_puzzle5():
    assert day3.puzzle_5(test_input) == 157

def get_line_n(n):
    with open(test_input, 'r') as fp:
        for i, line in enumerate(fp):
            if i == n-1:
                return line
            elif i == n:
                break

def test_sack_compartments_1():
    line = get_line_n(1)
    assert day3.sack_compartments_from_line(line) == (
        {"v","J","r","w","p","W","t","w","J","g","W","r"},
        {"h","c","s","F","M","M","f","F","F","h","F","p"})

def test_sack_compartments_2():
    line = get_line_n(2)
    assert day3.sack_compartments_from_line(line) == (
        {"j","q","H","R","N","q","R","j","q","z","j","G","D","L","G","L"},
        {"r","s","F","M","f","F","Z","S","r","L","r","F","Z","s","S","L"})

def test_sack_compartments_3():
    line = get_line_n(3)
    assert day3.sack_compartments_from_line(line) == (
        {"P","m","m","d","z","q","P","r","V"},
        {"v","P","w","w","T","W","B","w","g"})

def get_shared_item_line_n(n):
    line = get_line_n(n)
    sack_compartments = day3.sack_compartments_from_line(line)
    return day3.shared_item(sack_compartments[0], sack_compartments[1])

def test_shared_item_4():
    assert get_shared_item_line_n(4) == "v"
    
def test_shared_item_5():
    assert get_shared_item_line_n(5) == "t"

def test_shared_item_6():
    assert get_shared_item_line_n(6) == "s"

def get_letter_priority(letter):
    return day3.item_priority(letter);

def test_letter_priority_p():
    assert get_letter_priority("p") == 16

def test_letter_priority_L():
    assert get_letter_priority("L") == 38

def test_letter_priority_P():
    assert get_letter_priority("P") == 42

def test_letter_priority_v():
    assert get_letter_priority("v") == 22

def test_letter_priority_t():
    assert get_letter_priority("t") == 20

def test_letter_priority_s():
    assert get_letter_priority("s") == 19

def test_puzzle6():
    assert day3.puzzle_6(test_input) == 70

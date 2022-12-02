def play_game(filename: str, input_to_choice_func):
    opponent_score = 0
    player_score = 0
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            opponent_input = line[0]
            player_input = line[2]            
            scores = play_round(opponent_input, player_input, input_to_choice_func)
            opponent_score += scores[0]
            player_score += scores[1]
    return player_score

def play_round(opponent_input, player_input, input_to_choice_func):
    choices = input_to_choice_func(opponent_input, player_input)
    opponent_choice = choices[0]
    player_choice = choices[1]    
    score_opponent = choice_score(opponent_choice)
    score_player = choice_score(player_choice)
    results = result_scores(opponent_choice, player_choice)
    score_opponent += results[0]
    score_player += results[1]
    return score_opponent, score_player

def input_to_choice_1(opponent_input, player_input):
    rules = {
        "A": "R",
        "B": "P",
        "C": "S",
        "X": "R",
        "Y": "P",
        "Z": "S"
    }
    return rules[opponent_input], rules[player_input]

def input_to_choice_2(opponent_input, player_input):
    opponent_rules = {
        "A": "R",
        "B": "P",
        "C": "S"
    }
    player_rules = {
        "AX": "S",
        "AY": "R",
        "AZ": "P",
        "BX": "R",
        "BY": "P",
        "BZ": "S",
        "CX": "P",
        "CY": "S",
        "CZ": "R"
    }
    return opponent_rules[opponent_input], player_rules[opponent_input + player_input]

def choice_score(choice: str):
    choices = {
        "R": 1,
        "P": 2,
        "S": 3
    }
    return choices[choice]

def result_scores(opponent, player):
    win = 6
    draw = 3
    lose = 0
    scores = {
        "RR": (draw, draw),
        "RP": (lose, win),
        "RS": (win, lose),
        "PR": (win, lose),
        "PP": (draw, draw),
        "PS": (lose, win),
        "SR": (lose, win),
        "SP": (win, lose),
        "SS": (draw, draw)
    }
    return scores[opponent + player]

input = 'day_02\\input_day2.txt'

def puzzle_3(filename):
    return play_game(filename, input_to_choice_1)

def puzzle_4(filename):
    return play_game(filename, input_to_choice_2)

print("Puzzle 3: " + str(puzzle_3(input)))
print("Puzzle 4: " + str(puzzle_4(input)))
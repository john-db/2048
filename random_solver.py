from random import randint
from solver import process_left_board, process_down_board, process_right_board, process_up_board
from logic import add_rand_tile, legal_moves

def next_move_mash():
    moves = ["w","a","s","d"]
    return moves[randint(0, len(moves) - 1)]

def play_random_game(game):
    while True:
        moves = legal_moves(game)
        if len(moves) == 0:
            break
        move = next_move_mash()
        if move == 'a':
            if moves.count("a") > 0:
                process_left_board(game)
                add_rand_tile(game)
        elif move == 'w':
            if moves.count("w") > 0:
                process_up_board(game)
                add_rand_tile(game)
        elif move == 'd':
            if moves.count("d") > 0:
                process_right_board(game)
                add_rand_tile(game)
        elif move == 's':
            if moves.count("s") > 0:
                process_down_board(game)
                add_rand_tile(game)
    return game[1]

def next_move_rand_alg(game):
    num_of_games = 1000

    up_value = 0
    left_value = 0
    down_value = 0
    right_value = 0

    moves = legal_moves(game)

    if moves.count("w") > 0:
        up = [[row[:] for row in game[0]], game[1]]
        process_up_board(up)
        for i in range(num_of_games):
            temp = [[row[:] for row in up[0]], up[1]]
            play_random_game(temp)
            up_value += temp[1]

    if moves.count("a") > 0:
        left = [[row[:] for row in game[0]], game[1]]
        process_left_board(left)
        for i in range(num_of_games):
            temp = [[row[:] for row in left[0]], left[1]]
            play_random_game(temp)
            left_value += temp[1]

    if moves.count("s") > 0:
        down = [[row[:] for row in game[0]], game[1]]
        process_down_board(down)
        for i in range(num_of_games):
            temp = [[row[:] for row in down[0]], down[1]]
            play_random_game(temp)
            down_value += temp[1]

    if moves.count("d") > 0:
        right = [[row[:] for row in game[0]], game[1]]
        process_right_board(right)
        for i in range(num_of_games):
            temp = [[row[:] for row in right[0]], right[1]]
            play_random_game(temp)
            right_value += temp[1]

    if up_value >= down_value and up_value >= left_value and up_value >= right_value:
        return "w"
    elif right_value >= up_value and right_value >= left_value and right_value >= down_value:
        return "d"
    elif down_value >= up_value and down_value >= left_value and down_value >= right_value:
        return "s"
    else:
        return "a"


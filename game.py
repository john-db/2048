from sys import stdin

from time import sleep
from random_solver import next_move_mash, next_move_rand_alg
from solver import next_move_algo
from logic import add_rand_tile, process_down_board, process_left_board, \
    process_right_board, process_up_board, check_for_2048, legal_moves

def print_board(game):
    result = "SCORE: " + str(game[1]) + "\n"
    for i in range(4):
        for j in range(4):
            result += str(game[0][i][j])
            if j != 3:
                result += ' '
        result += '\n'

    print(result)

def play_game(game):
    print('enter w/a/s/d to move up/left/down/right')
    print('enter "exit" to exit the game')
    while True:
        print_board(game)
        if check_for_2048(game):
            print("you win!")
            break
        moves = legal_moves(game)
        if len(moves) == 0:
            print("no legal moves")
            break

        input = stdin.readline()
        if input == 'exit\n':
            break
        dir = input.strip("\n")
        if dir == 'a':
            if moves.count("a") > 0:
                process_left_board(game)
                add_rand_tile(game)
        elif dir == 'w':
            if moves.count("w") > 0:
                process_up_board(game)
                add_rand_tile(game)
        elif dir == 'd':
            if moves.count("d") > 0:
                process_right_board(game)
                add_rand_tile(game)
        elif dir == 's':
            if moves.count("s") > 0:
                process_down_board(game)
                add_rand_tile(game)

def watch_game(game, alg_type):
    while True:
        print_board(game)
        if check_for_2048(game):
            print("you win!")
            break
        moves = legal_moves(game)
        if len(moves) == 0:
            print("no legal moves")
            break
        
        if alg_type == "1\n":
            move = next_move_algo(game)
        elif alg_type == "2\n":
            move = next_move_rand_alg(game)
        else:
            move = next_move_mash()
        #sleep(.5)
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

board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
game = [board, 0]
add_rand_tile(game)
add_rand_tile(game)

print('Enter "y" if you want to play, enter anything else if you want to see the computer play')
input = stdin.readline()
if input == 'y\n':
    play_game(game)
else:
    print('Enter 1 (lookahead + heuristic), 2 (best-random alg), or anything else (random keys)')
    alg_type = stdin.readline()
    if alg_type == "1\n":
        print("will use the lookahead/heuristic algorithm")
    elif alg_type == "2\n":
        print("will use the randomized algorithm")
    else:
        print("will button mash (control, spamming random keys)")
    watch_game(game, alg_type)





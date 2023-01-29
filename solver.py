from random import randint
from logic import process_left_board, process_right_board, process_down_board, \
    process_up_board, legal_moves, empty_spaces

def next_move_algo(game):
    up_val = None
    left_val = None
    down_val = None
    right_val = None
    current_move = (None, None)

    left = [[row[:] for row in game[0]], game[1]]
    process_left_board(left)
    if left[0] != game[0]:
        left_val = eval_board(left, 0)
        if current_move[1] == None or left_val > current_move[1]:
                    current_move = ("a", left_val)


    right = [[row[:] for row in game[0]], game[1]]
    process_right_board(right)
    if right[0] != game[0]:
        right_val = eval_board(right, 0)
        if current_move[1] == None or right_val > current_move[1]:
            current_move = ("d", right_val)

    up = [[row[:] for row in game[0]], game[1]]
    process_up_board(up)
    if up[0] != game[0]:
        up_val = eval_board(up, 0)
        if current_move[1] == None or up_val > current_move[1]:
            current_move = ("w", up_val)
    
    down = [[row[:] for row in game[0]], game[1]]
    process_down_board(down)
    if down[0] != game[0]:
        down_val = eval_board(down, 0)
        if current_move[1] == None or down_val > current_move[1]:
            current_move = ("s", down_val)
    
    return current_move[0]

def eval_board(game, depth):
    if depth == 3:
        return heuristic(game)
    else:
        legals = legal_moves(game)
        if len(legals) == 0:
            return -1000
        up_value = None
        left_value = None
        right_value = None
        down_value = None
        if legals.count("w") > 0:
            up_value = 0
            up = [[row[:] for row in game[0]], game[1]]
            process_up_board(up)
            empties = empty_spaces(up)
            num_empties = len(empties)
            for i in range(num_empties):
                coords = empties[i]
                up[0][coords[0]][coords[1]] = 2
                up_value += (0.9) * (1/num_empties) * eval_board(up, depth + 1)

                up[0][coords[0]][coords[1]] = 4
                up_value += (0.1) * (1/num_empties) * eval_board(up, depth + 1)

                up[0][coords[0]][coords[1]] = 0
        if legals.count("a") > 0:
            left_value = 0
            left = [[row[:] for row in game[0]], game[1]]
            process_left_board(left)
            empties = empty_spaces(left)
            num_empties = len(empties)
            for i in range(num_empties):
                coords = empties[i]
                left[0][coords[0]][coords[1]] = 2
                left_value += (0.9) * (1/num_empties) * eval_board(left, depth + 1)

                left[0][coords[0]][coords[1]] = 4
                left_value += (0.1) * (1/num_empties) * eval_board(left, depth + 1)

                left[0][coords[0]][coords[1]] = 0
        if legals.count("s") > 0:
            down_value = 0
            down = [[row[:] for row in game[0]], game[1]]
            process_down_board(down)
            empties = empty_spaces(down)
            num_empties = len(empties)
            for i in range(num_empties):
                coords = empties[i]
                down[0][coords[0]][coords[1]] = 2
                down_value += (0.9) * (1/num_empties) * eval_board(down, depth + 1)

                down[0][coords[0]][coords[1]] = 4
                down_value += (0.1) * (1/num_empties) * eval_board(down, depth + 1)

                down[0][coords[0]][coords[1]] = 0
        if legals.count("d") > 0:
            right_value = 0
            right = [[row[:] for row in game[0]], game[1]]
            process_right_board(right)
            empties = empty_spaces(right)
            num_empties = len(empties)
            for i in range(num_empties):
                coords = empties[i]
                right[0][coords[0]][coords[1]] = 2
                right_value += (0.9) * (1/num_empties) * eval_board(right, depth + 1)

                right[0][coords[0]][coords[1]] = 4
                right_value += (0.1) * (1/num_empties) * eval_board(right, depth + 1)

                right[0][coords[0]][coords[1]] = 0
        
        values = [up_value, left_value, right_value, down_value]
        real_values = []
        for i in range(4):
            if values[i] != None:
                real_values.append(values[i])
        return max(real_values)

def heuristic(game): 
    if len(legal_moves(game)) == 0:
        return -100000
    num_empties = len(empty_spaces(game))
    max_tile = 2
    for i in range(4):
        for j in range(4):
            if game[0][i][j] > max_tile:
                max_tile = game[0][i][j]
    return max_tile + 100 * num_empties
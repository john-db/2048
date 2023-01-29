from random import randint

def empty_spaces(game):
    empties = []
    for row in range(len(game[0])):
        for col in range(len(game[0][row])):
            if game[0][row][col] == 0:
                empties.append((row, col))
    return empties    

def add_rand_tile(game):
    empties = empty_spaces(game)
    length = len(empties)
    if length == 0:
        return
    #pick random empty tile
    coords = empties[randint(0, length - 1)]
    #90% chance new tile is a 2, 10% chance it is a 4
    if randint(0,9) == 0:
        game[0][coords[0]][coords[1]] = 4
    else:
        game[0][coords[0]][coords[1]] = 2
    return

def process_left_board(game):
    for i in range(4):
        process_left(game[0][i], 0, game)

def process_left(row, idx, game):
    if idx == 3:
        return
    all_zero = True
    j = idx + 1
    while j < 4:
        if row[j] != 0:
            all_zero = False
        j = j + 1
    if all_zero:
        return
    
    if row[idx] == 0:
        i = idx
        while i < 3:
            row[i] = row[i + 1]
            i = i + 1
        row[i] = 0
        process_left(row, idx, game)
    elif row[idx + 1] == 0:
        i = idx + 1
        while i < 3:
            row[i] = row[i + 1]
            i = i + 1
        row[i] = 0
        process_left(row, idx, game)
    elif row[idx + 1] == row[idx]:
        row[idx] = 2 * row[idx]
        game[1] += row[idx]
        i = idx + 1
        while i < 3:
            row[i] = row[i + 1]
            i = i + 1
        row[i] = 0
        process_left(row, idx + 1, game)
    else:
        process_left(row, idx + 1, game)

def process_up_board(game):
    for i in range(4):
        process_up(game, i, 0)

def process_up(game, col, idx):
    if idx == 3:
        return
    all_zero = True
    j = idx + 1
    while j < 4:
        if game[0][j][col] != 0:
            all_zero = False
        j = j + 1
    if all_zero:
        return
    
    if game[0][idx][col] == 0:
        i = idx
        while i < 3:
            game[0][i][col] = game[0][i + 1][col]
            i = i + 1
        game[0][i][col] = 0
        process_up(game, col, idx)
    elif game[0][idx + 1][col] == 0:
        i = idx + 1
        while i < 3:
            game[0][i][col] = game[0][i + 1][col]
            i = i + 1
        game[0][i][col] = 0
        process_up(game, col, idx)
    elif game[0][idx + 1][col] == game[0][idx][col]:
        game[0][idx][col] = 2 * game[0][idx][col]
        game[1] += game[0][idx][col]
        i = idx + 1
        while i < 3:
            game[0][i][col] = game[0][i + 1][col]
            i = i + 1
        game[0][i][col] = 0
        process_up(game, col, idx + 1)
    else:
        process_up(game, col, idx + 1)
    
def process_right_board(game):
    for i in range(4):
            process_right(game[0][i], 3, game)

def process_right(row, idx, game):
    if idx == 0:
        return
    all_zero = True
    j = idx - 1
    while j > -1:
        if row[j] != 0:
            all_zero = False
        j = j - 1
    if all_zero:
        return
    
    if row[idx] == 0:
        i = idx
        while i > 0:
            row[i] = row[i - 1]
            i = i - 1
        row[i] = 0
        process_right(row, idx, game)
    elif row[idx - 1] == 0:
        i = idx - 1
        while i > 0:
            row[i] = row[i - 1]
            i = i - 1
        row[i] = 0
        process_right(row, idx, game)
    elif row[idx - 1] == row[idx]:
        row[idx] = 2 * row[idx]
        game[1] += row[idx]
        i = idx - 1
        while i > 0:
            row[i] = row[i - 1]
            i = i - 1
        row[i] = 0
        process_right(row, idx - 1, game)
    else:
        process_right(row, idx - 1, game)

def process_down_board(game):
    for i in range(4):
        process_down(game, i, 3)

def process_down(game, col, idx):
    if idx == 0:
        return
    all_zero = True
    j = idx - 1
    while j > -1:
        if game[0][j][col] != 0:
            all_zero = False
        j = j - 1
    if all_zero:
        return
    
    if game[0][idx][col] == 0:
        i = idx
        while i > 0:
            game[0][i][col] = game[0][i - 1][col]
            i = i - 1
        game[0][i][col] = 0
        process_down(game, col, idx)
    elif game[0][idx - 1][col] == 0:
        i = idx - 1
        while i > 0:
            game[0][i][col] = game[0][i - 1][col]
            i = i - 1
        game[0][i][col] = 0
        process_down(game, col, idx)
    elif game[0][idx - 1][col] == game[0][idx][col]:
        game[0][idx][col] = 2 * game[0][idx][col]
        game[1] += game[0][idx][col]
        i = idx - 1
        while i > 0:
            game[0][i][col] = game[0][i - 1][col]
            i = i - 1
        game[0][i][col] = 0
        process_down(game, col, idx - 1)
    else:
        process_down(game, col, idx - 1)

def legal_moves(game):
    left = [[row[:] for row in game[0]], game[1]]
    process_left_board(left)

    right = [[row[:] for row in game[0]], game[1]]
    process_right_board(right)

    up = [[row[:] for row in game[0]], game[1]]
    process_up_board(up)
    
    down = [[row[:] for row in game[0]], game[1]]
    process_down_board(down)

    moves = []
    if left[0] != game[0]:
        moves.append("a")
    if right[0] != game[0]:
        moves.append("d")
    if up[0] != game[0]:
        moves.append("w")
    if down[0] != game[0]:
        moves.append("s")   
    return moves

def check_for_2048(game):
    for i in range(4):
        for j in range(4):
            if game[0][i][j] == 2048:
                return True
    
    return False
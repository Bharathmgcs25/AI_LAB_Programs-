# Tic-Tac-Toe using Minimax AI

board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('--+---+--')
    print()

def check_winner(player):
    winning = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in winning:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -1000

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)

        return best_score

def ai_move():
    best_score = -1000
    best_move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'

# Main program
print("TIC-TAC-TOE")
print("You are X, AI is O")

while True:
    print_board()

    # User move
    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != ' ':
        print("Invalid move!")
        continue

    board[move] = 'X'

    if check_winner('X'):
        print_board()
        print("You Win!")
        break

    if ' ' not in board:
        print_board()
        print("Draw!")
        break

    # AI move
    ai_move()

    if check_winner('O'):
        print_board()
        print("AI Wins!")
        break

    if ' ' not in board:
        print_board()
        print("Draw!")
        break
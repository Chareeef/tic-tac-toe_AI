''' Helper Functions for Tic_Tac_Toe '''

def print_board(board):
    ''' Print The Tic_Tac_Toe board '''

    print('\n')

    for i in range(9):
        if i % 3 == 0 and i > 0:
            print()

        if board[i] == 0:
            print('_', end=' ')
        elif board[i] == 1:
            print('X', end=' ')
        elif board[i] == 2:
            print('O', end=' ')
    print('\n')


def game_outcome(outcome):
    ''' Display the final result '''
    
    if outcome == 0:
        print('Draw')
    elif outcome == 1:
        print('Player X Wins !')
    elif outcome == 2:
        print('Player O Wins !')
    print('\n')


def analyze_board(board):
    '''
    Check the current status of the game,
    i.e. if someone has won or no
    '''

    # Check Rows:
    for i in [0, 3, 6]:
        if board[i] != 0 and board[i] == board[i + 1] == board[i + 2]:
            return board[i]

    # Check Columns:
    for i in [0, 1, 2]:
        if board[i] != 0 and board[i] == board[i + 3] == board[i + 6]:
            return board[i]

    # Check Diagonals:
    if board[4] != 0:
            if board[0] == board[4] == board[8]:
                return board[4]
            elif board[2] == board[4] == board[6]:
                return board[4]

    # Still a Draw:
    return 0

def is_draw(board):
    ''' Check if a game Final State is a Draw '''

    for i in range(9):
        if board[i] == 0:
            break
        if i == 8:
            return True
    return False

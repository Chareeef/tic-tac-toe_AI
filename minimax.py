''' The Minimax Algorithm '''

from XO_tools import analyze_board, is_draw

def minimax(board, is_maximizing, AI_Human_dict):
    '''
    An implementation of the minimax
    algorithm for the Tic-Tac-Toe game
    '''

    outcome = analyze_board(board)
    if outcome == AI_Human_dict['AI']:
        return 1
    elif outcome == AI_Human_dict['Human']:
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        optimal_score = -2

        for i in range(9):
            if board[i] != 0:
                continue
            board[i] = AI_Human_dict['AI']
            test_score = minimax(board, False, AI_Human_dict)
            board[i] = 0

            optimal_score = max(test_score, optimal_score)

        return optimal_score
    else:
        optimal_score = 2

        for i in range(9):
            if board[i] != 0:
                continue
            board[i] = AI_Human_dict['Human']
            test_score = minimax(board, True, AI_Human_dict)
            board[i] = 0

            optimal_score = min(test_score, optimal_score)

        return optimal_score

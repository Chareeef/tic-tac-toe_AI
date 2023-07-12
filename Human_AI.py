''' Human and AI Players Classes '''

from minimax import minimax

class Human:
    '''Player's class

    Attribute:
        scheme: 1: 'X' or 2: 'O'
    Methods:
        play: Player's turn process
    
    '''

    def __init__(self, scheme):
        self.scheme = scheme

    def play(self, board):
        '''User 1's chance to play'''

        XO = 'X' if self.scheme == 1 else 'O'

        try:
            case_number = int(input(f'Player {XO}, enter a case ' +\
                    'from 1 to 9: ')) - 1
            if board[case_number] != 0 or case_number < 0:
                raise ValueError
            board[case_number] = self.scheme
        except (ValueError, IndexError):
            print('Invalid case')
            self.play(board)

class AI:
    '''AI's class

    Attribute:
        scheme: 1: 'X' or 2: 'O'
    Methods:
        play: AI's turn process
    
    '''

    def __init__(self, scheme):
        self.scheme = scheme

    def play(self, board, AI_Human_dict):
        '''AI's chance to play
        suppported by the minimax algorithm'''

        optimal_score = -2
        best_case = -10

        for i in range(9):
            if board[i] != 0:
                continue
            board[i] = self.scheme
            test_score = minimax(board, False, AI_Human_dict)
            board[i] = 0

            if test_score > optimal_score:
                optimal_score = test_score
                best_case = i

        board[best_case] = self.scheme

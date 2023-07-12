''' The main Tic_Tac_Toe project's file '''

from Human_AI import Human, AI 
from XO_tools import print_board, analyze_board, game_outcome
from time import sleep


def main():
    '''Tic_Tac_Toe game's main procedure'''

    # Ask for the wanted game mode:
    while True:
        try:
            solo_or_multi = int(input('You want to play:\n' +\
                    '\tAgainst AI: 1  /  With a friend: 2\n' +\
                    '\t\tChoice: '))
            if solo_or_multi not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print('\nInvalid Command\n')

    # If Against an AI, ask the user if he wants to play first or not:
    if solo_or_multi == 1:
        print()
        while True:
            try:
                first_or_second = int(input('Enter 1 to play first, ' +\
                        '2 otherwise:\n\t\tChoice: '))
                if first_or_second not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print('\nInvalid Command\n')
    print()

    # Ask the user whether he wants to play with "X" or "O":
    while True:
        try:
            scheme = int(input("Choose 1: 'X' or 2: 'O'\n\t\tChoice: "))
            if scheme not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print('\nInvalid Command\n')

    # Set up the Players Classes:
    user1 = Human(scheme)
    if solo_or_multi == 2:
        user2 = Human(1) if scheme == 2 else Human(2)
    else:
        bot = AI(1) if scheme == 2 else AI(2)
        AI_Human_dict = {'AI': bot.scheme, 'Human': user1.scheme}

    # Initialize the game board:
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Play against the AI:
    if solo_or_multi == 1:
        for i in range(9):
            if analyze_board(board) != 0:
                break
            if (i + first_or_second) % 2 == 0:
                if i == 0:
                    board[0] = bot.scheme
                    continue
                bot.play(board, AI_Human_dict)
            else:
                print_board(board)
                user1.play(board)

    # Play against another Human Player:
    elif solo_or_multi == 2:
        for i in range(9):
            if analyze_board(board) != 0:
                break
            if i % 2 == 0:
                print_board(board)
                user1.play(board)
            else:
                print_board(board)
                user2.play(board)

    # Print the final board and announce the result
    print_board(board)
    game_outcome(analyze_board(board))
    sleep(1)

    # Ask for a new game:
    while True:
        try:
            restart = int(input('Another game?\n\t' +\
                    '\t1: Yes / 0: No\n\t\tChoice: '))
            if restart == 1:
                print()
                main()
                break
            elif restart == 0:
                print('\nSee You !')
                break
            else:
                raise ValueError
        except ValueError:
            print('\nInvalid Command\n')

# Run the Tic_Tac_Toe game:
main()

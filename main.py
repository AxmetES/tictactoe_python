board = [' '] * 10


def play_again():
    print('Do you want play again ? :')
    inp = input('')
    if inp == 'y':
        game_play(player_marker)
    else:
        exit()


def clearDisplay():
    print('\n' * 80)


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print('-------')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('-------')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])


def place_marker(board, marker, pos):
    board[pos] = marker


# Check for winner True of False
def winCheck(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[7] == board[5] == board[3] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[7] == board[4] == board[1] == marker) or
            (board[8] == board[5] == board[2] == marker) or
            (board[3] == board[6] == board[9] == marker))


def isBoardFull(board):
    if board.count(' ') < 1:
        return True
    else:
        return False


def playerMove(player_marker):
    run = True
    while run:
        move = input('Plz select position to number between 1-9: ')
        try:
            move = int(move)
            if (move > 0) and (move < 10):
                if spaceIsFree(move):
                    run = False
                    place_marker(board, player_marker, move)
                else:
                    print('Sorry this space isn\'t free')

            else:
                print('Inserted number not in rage (1-9)')

        except:
            print('Plz type a number!')


def game_play(player_marker):
    print('Welcome to game Tic Tac Toe')
    printBoard(board)

    while not (isBoardFull(board)):
        playerMove(player_marker)
        clearDisplay()
        printBoard(board)
        if player_marker == 'x':
            if winCheck(board, player_marker):
                clearDisplay()
                print('{} IS WINNER!!!'.format(player_marker))
                play_again()
            player_marker = 'o'
        else:
            if winCheck(board, player_marker):
                clearDisplay()
                print('{} IS WINNER!!!'.format(player_marker))
                play_again()
            player_marker = 'x'

        if isBoardFull(board):
            clearDisplay()
            print('TIE no winner!!!')


# test_board = ['#', 'x', 'o', 'x', 'x', 'x', 'x', 'x', 'o', 'o']
# printBoard(test_board)
# winCheck(test_board, 'x')

player_marker = 'x'
game_play(player_marker)

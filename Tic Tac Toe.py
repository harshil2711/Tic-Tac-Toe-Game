import sys

winner = None

game_is_still_going = True

current_player = "X"

main_board = ['_','_','_','_','_','_','_','_','_']

def display_board():
    print(main_board[0] + ' | ' + main_board[1] + ' | ' + main_board[2])
    print(main_board[3] + ' | ' + main_board[4] + ' | ' + main_board[5])
    print(main_board[6] + ' | ' + main_board[7] + ' | ' + main_board[8])


def handle_turn(current_player):
    try:
        print(current_player + "'s turn")
        position = input("enter the number 1-9 :")
        position = int(position) - 1
        main_board[position] = current_player
        display_board()
    except:
        if position == "clear":
            quit()

        else:
            print("enter the valid input")


def check_if_gameover():
    check_if_win()
    check_if_tie()



def check_if_win():
    check_rows()
    check_column()
    check_diag()


def check_if_tie():
       if "_" not in main_board:
            print("match is tie")
            sys.exit()


def flip():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_rows():
    row1 = main_board[0] == main_board[1] == main_board[2] != "_"
    row2 = main_board[3] == main_board[4] == main_board[5] != "_"
    row3 = main_board[6] == main_board[7] == main_board[8] != "_"

    if row1:
        print(f"hurray....{current_player} wins the match")
        sys.exit()
    if row2:
        print(f"hurray....{current_player} wins the match")
        sys.exit()
    if row3:
        print(f"hurray....{current_player} wins the match")
        sys.exit()


def check_column():
    col1 = main_board[0] == main_board[3] == main_board[6] != "_"
    col2 = main_board[1] == main_board[4] == main_board[7] != "_"
    col3 = main_board[2] == main_board[5] == main_board[8] != "_"

    if col1:
        print(f"hurray....{current_player} wins the match")
        sys.exit()
    if col2:
        print(f"hurray....{current_player} wins the match")
        sys.exit()
    if col3:
        print(f"hurray....{current_player} wins the match")
        sys.exit()

def check_diag():
    diag1 = main_board[0] == main_board[4] == main_board[8] != "_"
    diag2 = main_board[2] == main_board[4] == main_board[6] != "_"

    if diag1:
        print(f"hurray....{current_player} wins the match")
        sys.exit()
    if diag2:
        print(f"hurray....{current_player} wins the match")
        sys.exit()


def play_game():
    display_board()
    while game_is_still_going:
        handle_turn(current_player)
        check_if_gameover()
        flip()
play_game()

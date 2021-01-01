main_board = ['_','_','_','_','_','_','_','_','_']


current_player = 'X'
game_is_still_going =True
winner = None

def board():
    print(main_board[0]+' | '+main_board[1]+' | '+main_board[2])
    print(main_board[3]+' | '+main_board[4]+' | '+main_board[5])
    print(main_board[6]+' | '+main_board[7]+' | '+main_board[8])

def handle_turn(current_player):
    try:
        print(f"{current_player}'s turn")
        position = int(input("enter value 1-9"))
        position = position-1
        main_board[position]=current_player
        board()
    except:
        if position == "quit":
            quit()
        else:
            print(f"sorry i don't understand {position}")

def playgame()


# Switch player moves
def flip():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def if_game_over():
    pass


def check_if_win():
    while winner:
        if main_board[0]==main_board[1]==main_board[2]:
            print(f"hurray!! {current_player} win the match")


        elif main_board[3]==main_board[4]==main_board[5]:
            print(f"{current_player} win the match")

        elif main_board[6]==main_board[7]==main_board[8]:
            print(f"{current_player} win the match")

        elif main_board[0]==main_board[3]==main_board[6]:
            print(f"{current_player} win the match")


        elif main_board[1]==main_board[4]==main_board[7]:
            print(f"{current_player} win the match")

        elif main_board[2] == main_board[5] == main_board[8]:
            print(f"{current_player} win the match")


        elif main_board[0] == main_board[4] == main_board[8]:
            print(f"{current_player} win the match")


        elif main_board[2] == main_board[4] == main_board[6]:
            print(f"{current_player} win the match")


        else:
            print(" match tie ")



def check_if_tie():
    pass



def play():
    board()
    while game_is_still_going:
        hadle_input(current_player)
        if_game_over()
        flip()
play()

#tic tac toe game with an AI
board=[' ' for x in range(10)]

def insertletter(letter,pos):
    board[pos]=letter

def free_space(pos):
    return board[pos]==' '


def show_board(board):
    print(board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('------------------------------------------------------')
    print(board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('------------------------------------------------------')
    print(board[7] + '  |  ' + board[8] + '  |  ' + board[9])


def winner(board,letter):
     if  board[1]==letter and board[2]==letter and board[3]==letter :
         return True
     if board[4]==letter and board[5]==letter and board[6]==letter:
         return True
     if board[7]==letter and board[8]==letter and board[9]==letter:
         return True
     if board[1]==letter and board[4]==letter and board[7]==letter:
         return True
     if board[2]==letter and board[5]==letter and board[8]==letter:
         return True
     if board[3]==letter and board[6]==letter and board[9]==letter:
         return True
     if board[1]==letter and board[5]==letter and board[9]==letter:
         return True
     if board[3]==letter and board[5]==letter and board[7]==letter:
         return True
     else:
         return False


def opponent():
    flag=True
    move=input('enter the position where you want to place X  :')

    while flag:
        try:
            move=int(move)
            if move>0 and move<10:
                if free_space(move):
                    flag=False
                    insertletter('x',move)
                else:
                    print('sorry the position entered is not free. ')
            else:
                print('the move should be between 1 to 9 !!')
        except:
            print('enter an integer!!')


def computer_move(board):
    empty=[i for i,letter in enumerate(board) if letter==' ' and i!=0]
    move = 0

    for letter in ['o','x']:
        for x in empty:
            temp_board=board[:]
            temp_board[x]=letter
            if winner(temp_board,letter):
                move=x
                return move

    corner=[]
    for i in empty:
        if i==1 or i==3 or i==7 or i==9:
            corner.append(i)
    if len(corner)>0:
        move=any_random(corner)
        return move

    if free_space(5):
        move=5
        return move

    edge=[]
    for i in empty:
        if i in [2,4,6,8]:
            edge.append(i)
    if len(edge)>0:
        move=any_random(edge)
    return move

def any_random(list1):
    import random
    length=len(list1)
    x = random.randrange(0,length)
    return list1[x]

def board_full(board):
    if board.count(' ')>1:
        return False
    else:
        return True


def main():
    print('hey im an AI, ready to play tic-tac-toe with me ?')
    show_board(board)

    while not (board_full(board)):
        if not winner(board,'o'):
            opponent()
            show_board(board)
        else:
            print(' I win the game , wanna play once more ?')
            break
        if not winner(board,'x'):
            move = computer_move(board)
             if move == 0:
                print('there is a tie :( ')
            insertletter('o',move)
            print('my turn')
            show_board(board)
            print('i place the o at position:',move)
        else:
            print('congrats ! you win the game :) ')
            break

    if board_full(board):
        print('there is a tie :( ')
        print('--------  Thankyou :)  ---------')

if __name__== '__main__':
    main()











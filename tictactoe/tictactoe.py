"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
rows=3
cols=3


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount=0
    ocount=0
    for i in range(rows):
        for j in range(cols):
            if(board[i][j]==X):
                xcount+=1
            if(board[i][j]==O):
                ocount+=1
    if xcount>ocount:
        return O
    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # actions=set()
    # for i in range(rows):
    #     for j in range(cols):
    #         if(board[i][j]==EMPTY):
    #             actions.add((i,j))
    # return actions

    actions = []
    row_num = 0
    col_num = 0

    for row in board:
        for col in row:
            if col == EMPTY:
                actions.append((row_num, col_num))
            col_num += 1
        row_num += 1
        col_num = 0

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError('Invalid Action')

    p=player(board)
    board_copy=copy.deepcopy(board)
    (i,j)=action
    board_copy[i][j] = p
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for r in board:
        values_row=set()
        for c in r:
            values_row.add(c)
        if values_row=={X}:
            return X
        elif values_row=={O}:
            return O
        else:
            pass

    for c in range(len(board)):
        values_col=set()
        for r in board:
            values_col.add(r[c])
        if values_col=={X}:
            return X
        elif values_col=={O}:
            return O
        else:
            pass

    values_diag1=set()
    values_daig2=set()

    for i in range(rows):
        for j in range(cols):
            if i==j:
                values_diag1.add(board[i][j])
            if j==3-1-i:
                values_daig2.add(board[i][j])
    if values_daig2=={X} or values_diag1=={X}:
        return X
    elif values_diag1=={O} or values_daig2=={O}:
        return O
    else:
        pass

    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for col in row:
            if col is None:
                return  False

    return  True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) ==X:
        return 1
    elif winner(board)== O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimum_action=None

    def min_values(board):
        if terminal(board):
            utility_board=utility(board)
            return utility_board
        v=math.inf
        for action in actions(board):
            m=max_values(result(board,action))
            v=min(v,m)
        return v

    def max_values(board):
        if terminal(board):
            utility_board = utility(board)
            return utility_board
        v = -math.inf
        for action in actions(board):
            m = min_values(result(board, action))
            v = max(v, m)
        return v

    if player(board)==X:
        utility_list=[]
        for action in actions(board):
            current_utility=min_values(result(board,action))
            utility_list.append(current_utility)
        optimum_utility=max(utility_list)
        index_optimum_utility=utility_list.index(optimum_utility)

        optimum_action=actions(board)[index_optimum_utility]

    else :
        utility_list=[]
        for action in actions(board):
            current_utility=max_values(result(board,action))
            utility_list.append(current_utility)

        optimum_utility=min(utility_list)
        index_optimum_utility=utility_list.index(optimum_utility)

        optimum_action=actions(board)[index_optimum_utility]

    return optimum_action


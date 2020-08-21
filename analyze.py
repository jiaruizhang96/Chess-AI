
def GenBoard():
    board = [13,11,12,15,14,12,11,13,
             10,10,10,10,10,10,10,10,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             20,20,20,20,20,20,20,20,
             23,21,22,25,24,22,21,23]
    return board

def printBoard(b):
    board = []
    for i in b:
        if i == 0:
            board += [str(i)+" "]
        else:
            board += [str(i)]
    if len(board) == 64:
        print("--------------BLACK SIDE--------------")
        print(board[63] + " | " + board[62] + " | " + board[61] + " | " + board[60] + " | " + board[59] + " | " + board[58] + " | " + board[57] + " | " + board[56])
        print("--------------------------------------")
        print(board[55] + " | " + board[54] + " | " + board[53] + " | " + board[52] + " | " + board[51] + " | " + board[50] + " | " + board[49] + " | " + board[48])
        print("--------------------------------------")
        print(board[47] + " | " + board[46] + " | " + board[45] + " | " + board[44] + " | " + board[43] + " | " + board[42] + " | " + board[41] + " | " + board[40])
        print("--------------------------------------")
        print(board[39] + " | " + board[38] + " | " + board[37] + " | " + board[36] + " | " + board[35] + " | " + board[34] + " | " + board[33] + " | " + board[32])
        print("--------------------------------------")
        print(board[31] + " | " + board[30] + " | " + board[29] + " | " + board[28] + " | " + board[27] + " | " + board[26] + " | " + board[25] + " | " + board[24])
        print("--------------------------------------")
        print(board[23] + " | " + board[22] + " | " + board[21] + " | " + board[20] + " | " + board[19] + " | " + board[18] + " | " + board[17] + " | " + board[16])
        print("--------------------------------------")
        print(board[15] + " | " + board[14] + " | " + board[13] + " | " + board[12] + " | " + board[11] + " | " + board[10] + " | " + board[9] + " | " + board[8])
        print("--------------------------------------")
        print(board[7] + " | " + board[6] + " | " + board[5] + " | " + board[4] + " | " + board[3] + " | " + board[2] + " | " + board[1] + " | " + board[0])
        print("--------------WHITE SIDE--------------")
        return True
    return False


def GetPlayerPositions(board,player):  # 10 for white, 20 for black
    pos = []
    if len(board) == 64:
        for i in range(64):
            if ( board[i] >= player ) and (abs(board[i]-player) <= 5):
                pos += [i]
        return pos
    else:
        return -1

def GetPieceLegalMoves(board,position):
    if len(board) == 64:
        piece = GetPiece(position,board)
        moves = []
        player = GetPlayer(board[position]) # 20 black 10 white -1 non
        ######## pawns, 0 #########
        if (piece == 0) and (player == 10): # white
            if GoRightUp(position,board,True,player):
                moves += [GoRightUp(position,board,True,player)]
            if GoLeftUp(position,board,True,player):
                moves += [GoLeftUp(position,board,True,player)]
            if GoUp(position,board,False,player):
                moves += [GoUp(position,board,False,player)]
            return moves
        if (piece == 0) and (player == 20): # black
            if GoRightDown(position,board,True,player):
                moves += [GoRightDown(position,board,True,player)]
            if GoLeftDown(position,board,True,player):
                moves += [GoLeftDown(position,board,True,player)]
            if GoDown(position,board,False,player):
                moves += [GoDown(position,board,False,player)]
            return moves
        ######## knight, 1 #########
        if piece == 1:
            if LRightUp(position, board, player):
                moves += [LRightUp(position, board, player)]
            if LRightDown(position, board, player):
                moves += [LRightDown(position, board, player)]
            if LLeftUp(position, board, player):
                moves += [LLeftUp(position, board, player)]
            if LLeftDown(position, board, player):
                moves += [LLeftDown(position, board, player)]
            return moves

        ######## bishop, 2 #########
        if piece == 2:
            temp = position
            while temp < 56:
                if GoRightUp(temp,board,False,player):
                    moves += [GoRightUp(temp,board,False,player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp],player):
                        break
                break
            temp = position
            while temp < 55:
                if GoLeftUp(temp,board,False,player):
                    moves += [GoLeftUp(temp,board,False,player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp],player):
                        break
                break
            temp = position
            while temp > 8:
                if GoRightDown(temp, board, False, player):
                    moves += [GoRightDown(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp],player):
                        break
                break
            temp = position
            while temp > 7:
                if GoLeftDown(temp, board, False, player):
                    moves += [GoLeftDown(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp],player):
                        break
                break
            return moves
        ######## rook, 3 ########
        if piece == 3:
            temp = position
            while temp < 56:
                if GoUp(temp, board, False, player):
                    moves += [GoUp(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp],player):
                        break
                break

            temp = position
            while temp > 7:
                if GoDown(temp, board, False, player):
                    moves += [GoDown(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp], player):
                        break
                break
            return moves
        ######## queen, 4 ########
        if piece == 4:
            temp = position
            while (temp < 56) and (temp > -1):
                if GoUp(temp, board, False, player):
                    moves += [GoUp(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp],player):
                        break
                break
            temp = position
            while (temp > 7) and (temp < 64):
                if GoDown(temp, board, False, player):
                    moves += [GoDown(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp], player):
                        break
                break
            temp = position
            while (temp < 56) and (temp > -1):
                if GoRightUp(temp, board, False, player):
                    moves += [GoRightUp(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp], player):
                        break
                break
            temp = position
            while (temp < 55) and (temp > -1):
                if GoLeftUp(temp, board, False, player):
                    moves += [GoLeftUp(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp], player):
                        break
                break
            temp = position
            while (temp > 8) and (temp > -1):
                if GoRightDown(temp, board, False, player):
                    moves += [GoRightDown(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp], player):
                        break
                break
            temp = position
            while (temp > 7) and (temp < 64):
                if GoLeftDown(temp, board, False, player):
                    moves += [GoLeftDown(temp, board, False, player)]
                    temp = moves[-1]
                    if IsOpponent(board[temp], player):
                        break
                break
            return moves
        ######## king, 5 ########
        if piece == 5:
            if GoUp(position, board, False, player):
                moves += [GoUp(position, board, False, player)]
            if GoDown(position, board, False, player):
                moves += [GoDown(position, board, False, player)]
            if GoRightUp(position, board, False, player):
                moves += [GoRightUp(position, board, False, player)]
            if GoLeftUp(position, board, False, player):
                moves += [GoLeftUp(position, board, False, player)]
            if GoRightDown(position, board, False, player):
                moves += [GoRightDown(position, board, False, player)]
            if GoLeftDown(position, board, False, player):
                moves += [GoLeftDown(position, board, False, player)]
            return moves
    else:
        return -1

def IsPositionUnderThreat(board,position,player):
    piece = GetPiece(position,board)
    for i in range(64):
        if IsOpponent(board[i],player) == True:
            moves = GetPieceLegalMoves(board,i)
            if position in moves:
                if GetPiece(i,board) == 0:
                    if abs(position-i) == 8:
                        return False
                    return True
                else:
                    return True
    return False

############################################### helper functions #######################################################
def GetPiece(position,board):
    piece = board[position]
    if piece == 0:
        return -1
    elif piece >= 20:
        return (piece-20)
    return (piece-10)

def GetPlayer(piece):
    if piece == 0:
        return -1
    if (piece-16) > 0:
        return 20
    else:
        return 10

def IsOpponent(piece,player):
    if piece == 0:
        return -1
    num = GetPlayer(piece)
    if num == player:
        return False
    return True

def GoUp(position,board,capture,player): # capture = True : record the position when there is an opponent, else: record the position when it's empty, baseline player = white
    if (position < 56):
        pos = position + 8
        if (capture == True) and (IsOpponent(board[pos],player) == True):
            return pos
        if (capture == False) and (IsOpponent(board[pos],player) == True):
            return pos
        if (capture == False) and (IsOpponent(board[pos],player) == -1):
            return pos
        return False
    else:
        return False

def GoDown(position,board,capture,player): # capture = True : record the position when there is an opponent, else: record the position when it's empty, baseline player = white
    if (position > 7):
        pos = position - 8
        if (capture == True) and (IsOpponent(board[pos],player) == True):
            return pos
        if (capture == False) and (IsOpponent(board[pos],player) == True):
            return pos
        if (capture == False) and (IsOpponent(board[pos],player) == -1):
            return pos
        return False
    else:
        return False

def GoRightUp(position,board,capture,player): # capture = True : record the position when there is an opponent, else: record the position when it's empty, baseline player = white
    if (position % 8) != 0:
        pos = position + 7
        if pos < 63:
            if (capture == True) and (IsOpponent(board[pos],player) == True):
                return pos
            if (capture == False) and (IsOpponent(board[pos],player) == True):
                return pos
            if (capture == False) and (IsOpponent(board[pos],player) == -1):
                return pos

        return False
    else:
        return False

def GoLeftUp(position,board,capture,player): # capture = True : record the position when there is an opponent, else: record the position when it's empty
    if (position % 8) != 7:
        pos = position + 9
        if pos < 64:
            if (capture == True) and (IsOpponent(board[pos],player) == True):
                return pos
            if (capture == False) and (IsOpponent(board[pos],player) == True):
                return pos
            if (capture == False) and (IsOpponent(board[pos],player) == -1):
                return pos
        return False
    else:
        return False

def GoRightDown(position,board,capture,player): # capture = True : record the position when there is an opponent, else: record the position when it's empty
    if (position % 8) != 0:
        pos = position - 9
        if pos > -1:
            if (capture == True) and (IsOpponent(board[pos],player) == True):
                return pos
            if (capture == False) and (IsOpponent(board[pos],player) == True):
                return pos
            if (capture == False) and (IsOpponent(board[pos],player) == -1):
                return pos
        return False
    else:
        return False

def GoLeftDown(position,board,capture,player):  # capture = True : record the position when there is an opponent, else: record the position when it's empty
    if (position % 8) != 7:
        pos = position - 7
        if pos > 0:
            if (capture == True) and (IsOpponent(board[pos],player) == True):
                return pos
            if (capture == False) and (IsOpponent(board[pos],player) == True):
                return pos
            if (capture == False) and (IsOpponent(board[pos],player) == -1):
                return pos
        return False
    else:
        return False

def LRightUp(position,board,player):
    if ((position % 8) != 0) and (position < 48):
        pos = position + 15
        if IsOpponent(board[pos],player) != False:
            return pos
        return False
    return False

def LRightDown(position,board,player):
    if ((position % 8) != 0) and (position > 16):
        pos = position - 17
        if IsOpponent(board[pos],player) != False:
            return pos
        return False
    return False

def LLeftUp(position,board,player):
    if ((position % 8) != 7) and (position < 47):
        pos = position + 17
        if IsOpponent(board[pos],player) != False:
            return pos
        return False
    return False

def LLeftDown(position,board,player):
    if ((position % 8) != 7) and (position > 15):
        pos = position - 15
        if IsOpponent(board[pos],player) != False:
            return pos
        return False
    return False

def AnalyzeBoard(board):
    black = 25
    white = 15
    if black not in board:
        return 20
    if white not in board:
        return 10
    else:
        return False





#def main():
    board = GenBoard()
    #tree.GenNode(board,10)
   # return True
#main()
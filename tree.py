import analyze


def EvalPiece(piece, position):
    if piece == 0:
        score = [0, 0, 0, 0, 0, 0, 0, 0,
                 0.5, 1, 1, -2, -2, 1, 1, 0.5,
                 0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5,
                 0, 0, 0, 2, 2, 0, 0, 0,
                 0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5,
                 1, 1, 2, 3, 3, 2, 1, 1,
                 5, 5, 5, 5, 5, 5, 5, 5,
                 0, 0, 0, 0, 0, 0, 0, 0]
        return 10 * score[position]
    if piece == 1:
        score = [-5, -4, -3, -3, -3, -3, -4, -5,
                 -4, -2, 0, 0.5, 0.5, 0, -2, -4,
                 -3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3,
                 -3, 0, 1.5, 2, 2, 1.5, 0, -3,
                 -3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3,
                 -3, 0, 1, 1.5, 1.5, 1, 0, -3,
                 -4, -2, 0, 0, 0, 0, -2, -4,
                 -5, -4, -3, -3, -3, -3, -4, -5]
        return 30 * score[position]
    if piece == 2:
        score = [-2, -1, -1, -1, -1, -1, -1, -2,
                 -1, 0.5, 0, 0, 0, 0, 0.5, -1,
                 -1, 1, 1, 1, 1, 1, 1, -1,
                 -1, 0, 1, 1, 1, 1, 0, -1,
                 -1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1,
                 -1, 0, 0.5, 1, 1, 0.5, 0, -1,
                 -1, 0, 0, 0, 0, 0, 0, -1,
                 -2, -1, -1, -1, -1, -1, -1, -2]
        return 30 * score[position]
    if piece == 3:
        score = [0, 0, 0, 0.5, 0.5, 0, 0, 0,
                 -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                 -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                 -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                 -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                 -0.5, 0, 0, 0, 0, 0, 0, -0.5,
                 0.5, 1, 1, 1, 1, 1, 1, 0.5,
                 0, 0, 0, 0, 0, 0, 0, 0]
        return 50 * score[position]
    if piece == 4:
        score = [-2, -1, -1, -0.5, -0.5, -1, -1, -2,
                 -1, 0, 0, 0, 0, 0.5, 0, -1,
                 -1, 0, 0.5, 0.5, 0.5, 0.5, 0.5, -1,
                 -0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, 0,
                 -0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5,
                 -1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1,
                 -1, 0, 0, 0, 0, 0, 0, -1,
                 -2, -1, -1, -0.5, -0.5, -1, -1, -2]
        return 90 * score[position]
    if piece == 5:
        score = [2, 3, 1, 0, 0, 1, 3, 2,
                 2, 2, 0, 0, 0, 0, 2, 2,
                 -1, -2, -2, -2, -2, -2, -2, -1,
                 -2, -3, -3, -4, -4, -3, -3, -2,
                 -3, -4, -4, -5, -5, -4, -4, -3,
                 -3, -4, -4, -5, -5, -4, -4, -3,
                 -3, -4, -4, -5, -5, -4, -4, -3,
                 -3, -4, -4, -5, -5, -4, -4, -3]
        return 900 * score[position]
    return False


def EvalBoard(board):
    if len(board) == 64:
        score = 0
        for i in range(64):
            if (analyze.GetPlayer(board[i]) == 10) and (analyze.GetPiece(i, board) != -1):
                score += float(EvalPiece(analyze.GetPiece(i, board), i))
        return score
    else:
        return False


class Node(object):
    def __init__(self):
        self.val = None # score
        self.board = None # board after moving
        self.pos = None # move which one (index)
        self.move = None # move to where (index)
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


def GenNewBoardScore(b,before,after):
    board = b.copy()
    piece = board[before]
    if analyze.GetPlayer(piece) != -1:
        moves = analyze.GetPieceLegalMoves(board, before)
        if after in moves:
            board[after] = piece
            board[before] = 0
    score = EvalBoard(board)
    return score

def GenNewBoard(b,before,after):
    board = b.copy()
    temp = board[before]
    board[after] = temp
    board[before] = 0
    return board

def GenNode(board,player):
    parent = Node()
    for i in range(64):
        if int(analyze.GetPlayer(board[i])) == player:
            temp = analyze.GetPieceLegalMoves(board,i)
            if len(temp) > 0:
                for j in temp:
                    child = Node()
                    child.board = GenNewBoard(board,i,j)
                    child.pos = i
                    child.move = j
                    parent.add_child(child)
    return parent


def minimax(board,depth,maximizer,a,b):
    if depth == 0:
        return (EvalBoard(board),None)
    bestmove = None
    if maximizer == True:
        val = -10**5 # smaller than the lowest score
        for child in GenNode(board,10).children:
            m = float(minimax(child.board,depth-1,False,a,b)[0])
            value = max(val,m)
            if value > a:
                bestmove = child
                a = value
                if a >= b:
                    break
    else:
        val = 10**5 #larger than the highest score
        for child in GenNode(board,20).children:
            m = float(minimax(child.board,depth-1,True,a,b)[0])
            value = min(val,m)
            if value < b:
                bestmove = child
                b = value
                if a >= b:
                    break
    return (value,bestmove)

def GetBestMove(board):
    level = 2
    value, best = minimax(board, level, True, -10 ** 5, 10 ** 5)
    return (best.pos,best.move,best.board)

def main():
    board = analyze.GenBoard()
    analyze.printBoard(board)
    while True:
        #analyze.printBoard(board)
        movewhitefrom, movewhiteto,new_board = GetBestMove(board)
        #whitepiece = board[movewhitefrom]
        #if GetPlayer(whitepiece) == 10:
            #moves = GetPieceLegalMoves(board, movewhitefrom)
            #print(moves)
            #if movewhiteto in moves:
              #  board[movewhiteto] = whitepiece
              #  board[movewhitefrom] = 0
        board = new_board
        state = analyze.AnalyzeBoard(board)
        if state == 10:
            print('White won')
            return True
        print('After White Move')
        analyze.printBoard(board)
        moveblackfrom = int(input("Move Black: Which One?"))
        moveblackto = int(input("Move Black: Where To?"))
        blackpiece = board[moveblackfrom]
        if analyze.GetPlayer(blackpiece) == 20:
            moves = analyze.GetPieceLegalMoves(board, moveblackfrom)
            if moveblackto in moves:
                board[moveblackto] = blackpiece
                board[moveblackfrom] = 0
        state = analyze.AnalyzeBoard(board)
        if state == 20:
            print('Black won')
            return True

    return True
main()

N = 4

def printBoard(board):
    for row in board:
        print(" ".join(row))

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == "Q": return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):#zip functoion is used for pairs l
        if board[i][j] == "Q": return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == "Q": return False
    return True

def solveNQueens(board, col=0):
    if col == N: return True
    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = "Q"
            if solveNQueens(board, col + 1): return True
            board[row][col] = "0"
    return False

board = [["0"] * N for _ in range(N)]
if solveNQueens(board): printBoard(board)
else: print("No solution")

"""Rekurzivni algoritam za trazenje stringa u 2D arrayu, tako da je svaki char
susjed prethodnom charu(max 8 mogucnosti)"""
def find_word(board, word):
    if len(word) == 1:
        for row in board:
            if word[0] in row:
                return True
        return False
    return find(board,word,-1,-1)

def find(board,word,curr_row,curr_col):
    if len(word)==0:
        return True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == word[0] and curr_row == -1:
                print(board[i][j], word, i, j,len(word[1:]))
                if find(board,word[1:],i,j):
                    return True
            elif board[i][j] == word[0] and abs(i-curr_row)<=1 and abs(j-curr_col)<=1:
                if i==curr_row and j==curr_col:
                    pass
                else:
                    print(board[i][j],word,i,j,len(word[1:]))
                    board[i][j] = -1
                    if find(board,word[1:],i,j):
                        return True
    return False

testBoard = [
      ["E","A","R","A"],
      ["N","L","E","C"],
      ["I","A","I","S"],
      ["B","Y","O","R"]
    ]
print(find_word(testBoard, 'BAILER'))
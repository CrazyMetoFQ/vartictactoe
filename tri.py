import numpy as np

board = np.array([
    [1,0,0,0,0],
    [0,1,0,0,1],
    [0,0,1,0,0],
    [1,0,0,1,0],
    [0,1,0,0,1]
])


def getDiags_right_downwards(board):
    
    diags = []    
    ws,hs = board.shape
    for col in range(ws):

        ncol = col
        curr_diag = []
        for row in range(hs):
            
            if ncol+1 > ws:
                break
            
            # print(f"{col} ( {row},{ncol} )  =  {board[row][ncol]}")
            curr_diag.append((board[row][ncol]))
            ncol += 1  
        
        diags.append(curr_diag)
        
    return diags


for row in board:
    print(row)

print()


print(getDiags_right_downwards(board)) # top right
print(getDiags_right_downwards(board.transpose()))  # bottom right

print(getDiags_right_downwards(np.array([row[::-1] for row in board])))  # top left 
print(getDiags_right_downwards(np.array([row[::-1] for row in board]).transpose()))  # bottom left


    
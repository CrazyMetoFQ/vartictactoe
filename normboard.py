import numpy as np


def get_all_sublists(l):
    
    # only forwawrd
    
    ln = range(len(l))
    suls = [[l[i:i+j+1] for j in ln] for i in ln]
    
    return suls


class Board:
    
    
    def create_board(size:tuple[int,int], fill = "*"):
        
        h,w = size
        
        return [[fill for _ in range(w)] for _ in range(h)]        
        
        
    
    def __init__(self, size:tuple[int,int]) -> None:
        
        
        self.board = np.array(Board.create_board(size))
        
        
        
    def pprintBoard(self):
        
        for r in self.board:
            
            rs = " | ".join([str(i) for i in r])
            rs = rs.replace("0", " ")
            print(rs)
            print("-"*len(rs))
    
    
    def play_move(self, puck, pos):
        
        self.board[pos[0]][pos[1]]  = puck
    
    
    def winCheck(self, lench=3, checkFor = "X"):
        
        def lsCheck(ls:list[list], checkFor= checkFor, filler="*"):
        
            for r in ls:
                
                all_pos = get_all_sublists(r)
                all_pos = [j for i in all_pos for j in i if (len(j)==lench and filler not in j and checkFor in j)]
                
                res = any(all(i==l[0] for i in l) for l in all_pos)
                
                if res:
                    return res
                else:
                    pass
                
            return False
        
        def getDiags_right_downwards(board):
            
            diags = []
            ws,hs = board.shape # (len(board[0]),len(board))
            
            for col in range(ws):
                ncol = col

                curr_diag = []
                for row in range(hs):

                    if ncol+1 > ws:
                        break
                    curr_diag.append((board[row][ncol]))

                    ncol += 1  
                diags.append(curr_diag)
            
            return diags
        

        checks = [lsCheck(self.board), # Rows
                    lsCheck(np.array(self.board).transpose().tolist()), # Cols
                    
                    lsCheck(getDiags_right_downwards(self.board)), # top right
                    lsCheck(getDiags_right_downwards(self.board.transpose())),  # bottom right

                    lsCheck(getDiags_right_downwards(np.array([row[::-1] for row in self.board]))),  # top left 
                    lsCheck(getDiags_right_downwards(np.array([row[::-1] for row in self.board]).transpose()))]  # bottom left
                
        return any(checks)
        
            
            
board = Board((5,5))

board.pprintBoard()            
print("----------------------")


board.play_move("O", (0,0))
board.play_move("O", (1,1))
board.play_move("O", (2,2))
board.play_move("O", (3,3))

board.pprintBoard()            

print(board.winCheck(4, "O"))
        

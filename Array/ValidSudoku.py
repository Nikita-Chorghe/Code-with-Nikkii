class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            a = []
            for i in row:
                if(i!="."):
                    if i in a:
                        return False
                    else:
                        a.append(i)
                        
        for j in range(len(board)):
            b = []
            for i in range(9):
                if(board[i][j] not in b and board[i][j]!="."):
                    b.append(board[i][j])
                elif (board[i][j]!="."):
                    return False
                
        for i in range(0,9,3):   
            for j in range(0,9,3) :
                c=[]
                for k in range(i,i+3):                    
                    for l in range(j,j+3):
                        if(board[k][l] not in c and board[k][l]!="."):
                            c.append(board[k][l])
                        elif (board[k][l]!="."):
                            return False
        return True
                        
       
        
                
           
                       
        
        
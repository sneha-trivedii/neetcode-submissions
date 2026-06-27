class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Approach: Brute Force Approach

        # Validate Rows 
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                if board[i][j] == ".":
                    continue
                s.add(board[i][j])
                
        # Validate Columns
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                if board[j][i] == ".":
                    continue
                s.add(board[j][i])

        # Validate Squares
        for square in range(9):
            s = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in s:
                        return False
                    if board[row][col] == ".":
                        continue
                    s.add(board[row][col])
        
        return True        
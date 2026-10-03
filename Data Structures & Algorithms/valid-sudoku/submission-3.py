class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Approach: Use 2D arrays to store already seen elements 
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        box = [[]for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # row
                if board[r][c] in rows[r]:
                    return False
                rows[r].append(board[r][c])

                # column
                if board[r][c] in cols[c]:
                    return False
                cols[c].append(board[r][c])

                # grid
                box_idx = 3*(r//3)+(c//3)
                if board[r][c] in box[box_idx]:
                    return False
                box[box_idx].append(board[r][c])
            
        return True
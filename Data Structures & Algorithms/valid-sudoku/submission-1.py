class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Approach: Using a list of sets

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                # represent the number by it's position on the board
                number = board[r][c]
                # box represents which square the number belongs to
                box = (r // 3) * 3 + (c // 3)

                if number == ".":
                    continue
                # Check if the number is in rth set in rows or cth set in cols or box'th set in boxes
                if number in rows[r] or number in cols[c] or number in boxes[box]:
                    return False

                # Add number to the rth set in rows, cth set in cols and boxth set in boxes
                rows[r].add(number)
                cols[c].add(number)
                boxes[box].add(number)
        return True
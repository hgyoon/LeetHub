class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Go through row
        for i in range(9):
            #create a set for each row for duplicate
            unique_set = set()
            unique_set_col = set()
            unique_set_grid = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in unique_set:
                        return False
                    elif board[i][j] not in unique_set:
                        unique_set.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in unique_set_col:
                        return False
                    elif board[j][i] not in unique_set_col:
                        unique_set_col.add(board[j][i])
                box_row = (i // 3) * 3 + (j // 3)
                box_col = (i % 3) * 3 + (j % 3)
                box_char = board[box_row][box_col]
                if box_char != ".":
                    if box_char in unique_set_grid:
                        return False
                    elif box_char not in unique_set_grid:
                        unique_set_grid.add(box_char)
        return True



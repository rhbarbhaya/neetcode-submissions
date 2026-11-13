class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_check = {}
        box_check = {}
        for i in range(0, 9, 1):
            rows_check[i] = []
            box_check[i] = []
        for row_index, row in enumerate(board):
            cleaned_row = [j for j in row if j != "."]
            if len(set(cleaned_row)) != len(cleaned_row):
                return False
            for col_index, col in enumerate(row):
                if col != ".":
                    rows_check[col_index].append(col)
                if row_index in range(0, 3) and col_index in range(0, 3) and col != ".":
                    box_check[0].append(col)
                if row_index in range(0, 3) and col_index in range(3, 6) and col != ".":
                    box_check[1].append(col)
                if row_index in range(0, 3) and col_index in range(6, 9) and col != ".":
                    box_check[2].append(col)
                if row_index in range(3, 6) and col_index in range(0, 3) and col != ".":
                    box_check[3].append(col)
                if row_index in range(3, 6) and col_index in range(3, 6) and col != ".":
                    box_check[4].append(col)
                if row_index in range(3, 6) and col_index in range(6, 9) and col != ".":
                    box_check[5].append(col)
                if row_index in range(6, 9) and col_index in range(0, 3) and col != ".":
                    box_check[6].append(col)
                if row_index in range(6, 9) and col_index in range(3, 6) and col != ".":
                    box_check[7].append(col)
                if row_index in range(6, 9) and col_index in range(6, 9) and col != ".":
                    box_check[8].append(col)
        for _, value in rows_check.items():
            if len(value) != len(set(value)):
                return False
        for _, value in box_check.items():
            if len(value) != len(set(value)):
                return False
        return True
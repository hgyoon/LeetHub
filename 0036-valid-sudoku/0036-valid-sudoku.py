class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # i: 검사할 Row, Column, 3x3 Box의 번호 (0~8)
        # j: 해당 Row, Column, Box 내부의 각 칸을 순회 (0~8)
        for i in range(9):

            # 각 Row, Column, Box의 중복 숫자를 확인하기 위한 Set
            # i가 증가할 때마다 새로운 Set 생성 (이전 검사 기록 초기화)
            row_seen = set()
            col_seen = set()
            box_seen = set()

            for j in range(9):

                # ==========================================
                # 1. Row 검사 (가로 방향)
                # ==========================================

                # i는 고정, j가 0~8까지 증가
                # board[0][0], board[0][1], ... board[0][8]
                row_num = board[i][j]

                if row_num != ".":
                    if row_num in row_seen:
                        return False

                    row_seen.add(row_num)

                # ==========================================
                # 2. Column 검사 (세로 방향)
                # ==========================================

                # j는 Row 인덱스, i는 Column 인덱스
                # board[0][0], board[1][0], ... board[8][0]
                col_num = board[j][i]

                if col_num != ".":
                    if col_num in col_seen:
                        return False

                    col_seen.add(col_num)

                # ==========================================
                # 3. 3x3 Box 검사
                # ==========================================

                # Sudoku에는 총 9개의 3x3 Box가 존재
                #
                # Box 번호 (i):
                #   0 | 1 | 2
                #  ---+---+---
                #   3 | 4 | 5
                #  ---+---+---
                #   6 | 7 | 8
                #
                # i: 어떤 Box를 검사할지 결정
                # j: 선택한 Box 내부의 9칸을 순회
                #
                # // : 몇 번째 그룹인지 계산 (몫)
                # %  : 해당 그룹 안에서의 위치 계산 (나머지)
                #
                # 시간으로 비유하면:
                # 135 // 60 = 2  -> 2시간
                # 135 % 60  = 15 -> 15분
                #
                # 마찬가지로:
                # i // 3 -> 몇 번째 Box 줄인지 (0, 1, 2)
                # i % 3  -> 그 줄에서 몇 번째 Box인지 (0, 1, 2)
                #
                # 각 Box는 3칸씩 차지하므로 * 3으로 시작 좌표 계산
                #
                # i = 4라면:
                # (4 // 3) * 3 = 3 -> 시작 Row
                # (4 % 3) * 3  = 3 -> 시작 Column
                # 따라서 가운데 Box의 시작 좌표는 (3, 3)

                # j // 3 -> Box 내부에서 몇 번째 Row인지
                #           0, 0, 0, 1, 1, 1, 2, 2, 2
                #
                # j % 3  -> Box 내부에서 몇 번째 Column인지
                #           0, 1, 2, 0, 1, 2, 0, 1, 2
                #
                # 시작 좌표 + 내부 이동량 = 실제 Board 좌표

                box_row = (i // 3) * 3 + (j // 3)
                box_col = (i % 3) * 3 + (j % 3)

                box_num = board[box_row][box_col]

                if box_num != ".":
                    if box_num in box_seen:
                        return False

                    box_seen.add(box_num)

        # 모든 Row, Column, Box에서 중복이 없으면 Valid
        return True
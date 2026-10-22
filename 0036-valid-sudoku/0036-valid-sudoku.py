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

                # i는 고정, j가 0~8까지 증가
                # board[0][0], board[1][0], ... board[8][0]
                col_num = board[j][i]

                if col_num != ".":
                    if col_num in col_seen:
                        return False

                    col_seen.add(col_num)

                # ==========================================
                # 3. 3x3 Box 검사 (가로 우선 순회)
                # ==========================================

                # 총 9개의 3x3 Box가 존재
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
                # [핵심 원리]
                # 가로로 먼저 이동하므로:
                #
                # // : 천천히 증가하는 인덱스
                #      일정 횟수 동안 같은 값을 유지한 뒤 증가
                #
                # %  : 빠르게 순환하는 인덱스
                #      매번 증가하다가 일정 범위에 도달하면 0으로 복귀
                #
                # 예시: j = 0~8
                # j // 3 -> 0, 0, 0, 1, 1, 1, 2, 2, 2 (느림)
                # j % 3  -> 0, 1, 2, 0, 1, 2, 0, 1, 2 (빠름)
                #
                # 시간으로 비유하면:
                # total_minutes = 135
                # 135 // 60 = 2  -> 몇 시간이 지났는가?
                # 135 % 60  = 15 -> 현재 시간 안에서 몇 분인가?
                #
                # [i: Box의 시작 좌표]
                #
                # Row는 천천히 증가하므로 //
                # i = 0~2 -> Row 0
                # i = 3~5 -> Row 3
                # i = 6~8 -> Row 6
                #
                # Column은 빠르게 순환하므로 %
                # i = 0, 3, 6 -> Col 0
                # i = 1, 4, 7 -> Col 3
                # i = 2, 5, 8 -> Col 6
                #
                # 각 Box의 크기가 3이므로 시작 좌표에 * 3
                #
                # [j: Box 내부의 이동 좌표]
                #
                # Row는 천천히 이동하므로 j // 3
                # Column은 빠르게 이동하므로 j % 3
                #
                # 따라서:
                # 실제 좌표 = Box 시작 좌표 + Box 내부 이동량
                #
                # 주의: 세로 우선 순회라면 //와 %의 역할이 반대가 됨

                box_row = (i // 3) * 3 + (j // 3)
                box_col = (i % 3) * 3 + (j % 3)

                box_num = board[box_row][box_col]

                if box_num != ".":
                    if box_num in box_seen:
                        return False

                    box_seen.add(box_num)

        # 모든 Row, Column, Box에서 중복이 없으면 Valid
        return True
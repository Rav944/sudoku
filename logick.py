import pygame

grid_1 = [[7, 3, 0, 4, 6, 5, 0, 0, 8],
          [0, 0, 0, 3, 9, 2, 4, 0, 7],
          [5, 0, 0, 0, 0, 0, 0, 6, 9],
          [0, 0, 7, 0, 0, 0, 8, 4, 0],
          [0, 5, 0, 8, 0, 4, 0, 3, 0],
          [0, 9, 0, 2, 0, 3, 0, 0, 0],
          [2, 0, 0, 0, 0, 9, 1, 0, 0],
          [9, 0, 3, 5, 0, 0, 7, 0, 0],
          [0, 8, 4, 7, 2, 0, 0, 0, 0]]

grid_2 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

#
# [[7, 8, 5, 4, 3, 9, 1, 2, 6],
#  [6, 1, 2, 8, 7, 5, 3, 4, 9],
#  [4, 9, 3, 6, 2, 1, 5, 7, 8],
#  [8, 5, 7, 9, 4, 3, 2, 6, 1],
#  [2, 6, 1, 7, 5, 8, 9, 3, 4],
#  [9, 3, 4, 1, 6, 2, 7, 8, 5],
#  [5, 7, 8, 3, 9, 4, 6, 1, 2],
#  [1, 2, 6, 5, 8, 7, 4, 9, 3],
#  [3, 4, 9, 2, 1, 6, 8, 5, 7]]


def solve(bo, redraw_window, win, play_time, strikes):
    find = find_empty(bo.board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if check_value(bo.board, i, (row, col)):
            cube = bo.cubes[row][col]
            gap = cube.width / 9
            x = cube.col * gap
            y = cube.row * gap
            bo.cubes[row][col].set(i)
            bo.board[row][col] = i
            bo.update_model()
            redraw_window(win, bo, play_time, strikes)
            pygame.draw.rect(win, pygame.Color("green"), (x, y, gap, gap), 3)
            pygame.display.update()
            if solve(bo, redraw_window, win, play_time, strikes):
                return True

            bo.cubes[row][col].set(0)
            bo.board[row][col] = 0
            pygame.draw.rect(win, pygame.Color("red"), (x, y, gap, gap), 3)
            bo.update_model()
            pygame.display.update()

    return False


def check_value(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

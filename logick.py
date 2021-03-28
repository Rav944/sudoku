import pygame

from settings import CORRECT_SUMMARY, INCORRECT_SUMMARY
from utils import redraw_window


def solve(bo, win: pygame.Surface, play_time: int, strikes: int) -> bool:
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
            pygame.draw.rect(win, CORRECT_SUMMARY, (x, y, gap, gap), 3)
            pygame.display.update()
            if solve(bo, win, play_time, strikes):
                return True

            bo.cubes[row][col].set(0)
            bo.board[row][col] = 0
            pygame.draw.rect(win, INCORRECT_SUMMARY, (x, y, gap, gap), 3)
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

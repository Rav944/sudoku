import pygame

from settings import FONT


def redraw_window(win: pygame.Surface, board, game_time: float, strikes: int):
    win.fill((255, 255, 255))
    fnt = pygame.font.SysFont(FONT, 40)
    text = fnt.render("Time: " + format_time(game_time), True, (0, 0, 0))
    win.blit(text, (540 - 160, 560))
    text = fnt.render("X " * strikes, True, (255, 0, 0))
    win.blit(text, (20, 560))
    board.draw(win)


def format_time(secs: float) -> str:
    sec = secs % 60
    minute = secs // 60
    mat = " " + str(minute) + ":" + str(sec)
    return mat

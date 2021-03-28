import pygame
from settings import SELECTED_BACKGROUND, FONT


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value: int, row: int, col: int, width: int, height: int):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win: pygame.Surface):
        fnt = pygame.font.SysFont(FONT, 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), True, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        elif not self.value == 0:
            text = fnt.render(str(self.value), True, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(win, SELECTED_BACKGROUND, (x, y, gap, gap), 3)

    def set(self, val: int):
        self.value = val

    def set_temp(self, val: int):
        self.temp = val

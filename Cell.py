
import pygame
from const import *


class Cell:  # This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.initial = value
        self.sketch = False

        # determine which cell are preset and which cell take input
        if self.initial > 0:
            self.can_be_cleared = False
        else:
            self.can_be_cleared = True

        # self.value = value
        # self.row = row
        # self.col = col
        # self.screen = screen
        # cell_size = width // 9
        # self.rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
        # self.is_given = True if value != 0 else False
        # self.font = pygame.font.Font(None, int(cell_size * 0.6))  # Font for displaying text
        # self.sketched_value = None  # Initialize sketched_value attribute to None

    def draw(self, screen):
        # pygame.draw.rect(screen, BLACK, self.rect, 1)  # Draw cell outline
        #
        # if self.value != 0:
        #     text_surface = self.font.render(str(self.value), True, BLACK)  # Render cell value
        #     screen.blit(text_surface, (self.rect.x + 20, self.rect.y + 15))  # Draw cell value
        # else:
        #     if self.sketched_value is not None:
        #         # Render sketched value if exists
        #         sketched_text_surface = self.font.render(str(self.sketched_value), True, GRAY)
        #         screen.blit(sketched_text_surface, (self.rect.x + 5, self.rect.y + 5))

        font = pygame.font.Font(None, 50)

        # preset numbers are black
        if self.value != 0 and not self.sketch:
            surface = font.render(str(self.value), 0, PRESET) # Render cell value
            rectangle = surface.get_rect(center=((self.row * (width / 9) + (width / 18)), (self.col * (width / 9) + (width / 18))))
            self.screen.blit(surface, rectangle) # Draw cell value

        # input numbers will be gray
        if self.value != 0 and self.sketch:
            surface = font.render(str(self.value), 0, USER) # Render cell value
            rectangle = surface.get_rect(center=((self.row * (width / 9) + (width / 18)), (self.col * (width / 9) + (width / 18))))
            self.screen.blit(surface, rectangle) # Draw cell value

        # if 0 is enter, nothing will display
        if self.value == 0:
            surface = font.render(' ', True, BACKGROUND) # Render cell value
            rectangle = surface.get_rect(center=((self.row * (width / 9) + (width / 18)), (self.col * (width / 9) + (width / 18))))
            self.screen.blit(surface, rectangle) # Draw cell value

    def set_value(self, value):
        self.value = value

    def set_sketched_value(self, value):  # Set the sketched value
        self.value = value
        self.sketch = True

    def update(self):  # Update cell appearance if needed
        pass

import pygame
from const import *

class Cell: # This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.rect = pygame.Rect(50 + col * 50, 50 + row * 50, 50, 50)
        self.is_given = True if value != 0 else False
        self.font = pygame.font.Font(None, 36)  # Font for displaying text
        self.sketched_value = None  # Initialize sketched_value attribute to None

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect, 1)  # Draw cell outline
        if self.value != 0:
            text_surface = self.font.render(str(self.value), True, BLACK)  # Render cell value
            screen.blit(text_surface, (self.rect.x + 20, self.rect.y + 15))  # Draw cell value
        else:
            if self.sketched_value is not None:
                # Render sketched value if exists
                sketched_text_surface = self.font.render(str(self.sketched_value), True, GRAY)
                screen.blit(sketched_text_surface, (self.rect.x + 5, self.rect.y + 5))

    def set_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        # Set the sketched value
        self.sketched_value = value

    def update(self):
        pass  # Update cell appearance if needed

import pygame
import sys
from Board import Board
from const import *

# pygame.init()


def game_start():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(CAPTION)
    screen.fill(WHITE)

    title_surface = start_title_font.render('SUDOKU', True, BLACK)
    title_rectangle = title_surface.get_rect(center=(width // 2, 100))
    screen.blit(title_surface, title_rectangle)

    game_surface = game_font.render('Select Game Mode:', True, BLACK)
    game_rectangle = game_surface.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(game_surface, game_rectangle)

    easy_text = button_font.render('Easy', 0, WHITE)
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(BLACK)
    easy_surface.blit(easy_text, (10, 10))
    easy_rectangle = easy_surface.get_rect(center=(width // 2 - 200, height // 2 + 200))
    screen.blit(easy_surface, easy_rectangle)

    medium_text = button_font.render('Medium', 0, WHITE)
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(BLACK)
    medium_surface.blit(medium_text, (10, 10))
    medium_rectangle = medium_surface.get_rect(center=(width // 2, height // 2 + 200))
    screen.blit(medium_surface, medium_rectangle)

    hard_text = button_font.render('Hard', 0, WHITE)
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(BLACK)
    hard_surface.blit(hard_text, (10, 10))
    hard_rectangle = hard_surface.get_rect(center=(width // 2 + 200, height // 2 + 200))
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 'EASY'
                elif medium_rectangle.collidepoint(event.pos):
                    return 'MEDIUM'
                elif hard_rectangle.collidepoint(event.pos):
                    return 'HARD'

        pygame.display.update()


def game_over():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(CAPTION)
    screen.fill(WHITE)

    # Game Over message
    title_surface = start_title_font.render('Game Over D:', 0, BLACK)
    title_rectangle = title_surface.get_rect(center=(width // 2, height // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Restart button
    restart_text = button_font.render('RESTART', 0, WHITE)
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(BLACK)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(center=(width // 2, height // 2 + 100))
    screen.blit(restart_surface, restart_rectangle)

    # Update display
    pygame.display.update()

    YAY = True
    while YAY:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if restart_rectangle.collidepoint(event.pos):
        #             return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() # exit

            if event.type == pygame.MOUSEBUTTONDOWN: # restart selection
                if restart_rectangle.collidepoint(event.pos): # reset display
                    difficulty = game_start()
                    screen = pygame.display.set_mode((width, height))
                    pygame.display.set_caption(CAPTION)
                    screen.fill(WHITE)

                    current_board = Board(width, width, screen, difficulty)
                    current_board.draw()
                    buttons(screen)
                    pygame.display.update()
                    YAY = False


def game_win():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(CAPTION)
    screen.fill(WHITE)

    title_surface = start_title_font.render('You Win!', 0, BLACK)
    title_rectangle = title_surface.get_rect(center=(width // 2, height // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    exit_text = button_font.render('EXIT', 0, WHITE)
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(BLACK)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center=(width // 2, height // 2 + 100))
    screen.blit(exit_surface, exit_rectangle)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    sys.exit()


def buttons(screen):
    button_font = pygame.font.Font(None, 25)

    # reset button
    reset_text = button_font.render('RESET', True, WHITE)
    reset_surface = pygame.Surface((65, 31))
    reset_surface.fill(BLACK)
    reset_surface.blit(reset_text, (5, 5))
    reset_rectangle = reset_surface.get_rect(center=(200, 650))
    # reset_rectangle = reset_surface.get_rect(topleft=(10, height - 60))
    screen.blit(reset_surface, reset_rectangle)

    # restart button
    restart_text = button_font.render('RESTART', 0, WHITE)
    restart_surface = pygame.Surface((85, 31))
    restart_surface.fill(BLACK)
    restart_surface.blit(restart_text, (5, 5))
    restart_rectangle = restart_surface.get_rect(center=(300, 650))
    # restart_rectangle = restart_surface.get_rect(topleft=(100, height - 60))
    screen.blit(restart_surface, restart_rectangle)

    # exit button
    exit_text = button_font.render('EXIT', 0, WHITE)
    exit_surface = pygame.Surface((50, 31))
    exit_surface.fill(BLACK)
    exit_surface.blit(exit_text, (5, 5))
    exit_rectangle = exit_surface.get_rect(center=(400, 650))
    # exit_rectangle = exit_surface.get_rect(topleft=(210, height - 60))
    screen.blit(exit_surface, exit_rectangle)

    pygame.display.update()

pygame.init()
start_title_font = pygame.font.Font(None, 100)
game_font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 70)

difficulty = game_start()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(CAPTION)
screen.fill(WHITE)

current_board = Board(width, width, screen, difficulty)
current_board.draw()
buttons(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(WHITE)
            current_board.draw()
            x, y = event.pos

            if 375 <= x <= 425 and 614.5 <= y <= 645.5:  # user press exit
                pygame.quit()
                sys.exit()

            elif 257.5 <= x <= 347.5 and 614.5 <= y <= 645.5:  # user press restart
                difficulty = game_start()
                screen = pygame.display.set_mode((width, height))
                pygame.display.set_caption(CAPTION)
                screen.fill(WHITE)

                current_board = Board(width, width, screen, difficulty)
                current_board.draw()
                buttons(screen)
                pygame.display.update()


            elif 167.5 <= x <= 232.5 and 614.5 <= y <= 645.5:  # user press reset
                current_board.reset_to_original()
                screen.fill(WHITE)
                current_board.draw()
                buttons(screen)
                pygame.display.update()

            else:
                try:
                    coordinates = current_board.click(x, y)
                    current_board.select(coordinates[0], coordinates[1])
                    buttons(screen)
                    pygame.display.update()
                except:
                    pass

        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_BACKSPACE:
                    current_board.clear()
                    screen.fill(WHITE)
                    current_board.draw()
                    buttons(screen)
                    pygame.display.update()

                elif 1 <= int(pygame.key.name(event.key)[-1]) <= 9:
                    guess = int(pygame.key.name(event.key)[-1])
                    current_board.sketch(guess)
                    current_board.place_number(guess)
                    current_board.update_board()
                    screen.fill(WHITE)
                    current_board.draw()
                    buttons(screen)
                    pygame.display.update()
            except:
                pass

        current_board.update_board()
        if current_board.is_full():
            if current_board.check_board():
                game_win()
            else:
                game_over()
                screen = pygame.display.set_mode((width, height))
                pygame.display.set_caption(CAPTION)
                screen.fill(WHITE)
                current_board = Board(width, width, screen, difficulty)
                current_board.draw()
                buttons(screen)
                pygame.display.update()

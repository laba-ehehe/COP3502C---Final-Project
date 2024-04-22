import pygame, sys
from Board import Board

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
width, height = 600, 700

def game_start():
    # screen, caption, background
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('( ͡° ͜ʖ ͡°) SUDOKU ( ͡° ͜ʖ ͡°)')
    screen.fill((255, 255, 255))

    # title, game modes
    title_surface = start_title_font.render('Sudoku', 0, BLACK)
    title_rectangle = title_surface.get_rect(center=(width // 2, height // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    game_surface = game_font.render('Select Game Mode:', 0, BLACK)
    game_rectangle = game_surface.get_rect(center=(width // 2, height // 2 + 50))
    screen.blit(game_surface, game_rectangle)

    # game modes text
    easy_text = button_font.render('Easy', 0, WHITE)
    medium_text = button_font.render('Medium', 0, WHITE)
    hard_text = button_font.render('Hard', 0, WHITE)

    # game modes button
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(BLACK)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(BLACK)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(BLACK)
    hard_surface.blit(hard_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(center=(width // 2 - 200, height // 2 + 200))
    medium_rectangle = medium_surface.get_rect(center=(width // 2, height // 2 + 200))
    hard_rectangle = hard_surface.get_rect(center=(width // 2 + 200, height // 2 + 200))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    # get actions from the player
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

        pygame.display.update() # update display


def game_over():
    # screen, caption, background
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('( ͡° ͜ʖ ͡°) SUDOKU ( ͡° ͜ʖ ͡°)')
    screen.fill(WHITE)

    # title, game over message
    title_surface = start_title_font.render('Game Over :(', 0, BLACK)
    title_rectangle = title_surface.get_rect(center=(width // 2, height // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    restart_text = button_font.render('RESTART', 0, WHITE)

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(BLACK)
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(center=(width // 2, height // 2 + 100))

    screen.blit(restart_surface, restart_rectangle)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos): # resets screen display.
                    difficulty = game_start()
                    screen = pygame.display.set_mode((600, 700))
                    pygame.display.set_caption('( ͡° ͜ʖ ͡°) SUDOKU ( ͡° ͜ʖ ͡°)')
                    screen.fill(WHITE)
                    # Calls Board class to create a new current_board.
                    current_board = Board(600, 700, screen, difficulty)
                    current_board.draw()
                    create_in_game_buttons(screen)
                    pygame.display.update()
                    break


def game_win():
    # screen, caption, background
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption('( ͡° ͜ʖ ͡°) SUDOKU ( ͡° ͜ʖ ͡°)')
    screen.fill(WHITE)

    # title, game won & exit message
    title_surface = start_title_font.render('Game Won!', 0, BLACK)
    title_rectangle = title_surface.get_rect(center=(width // 2, height // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    exit_text = button_font.render('EXIT', 0, WHITE)

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(BLACK)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(center=(width // 2, height // 2 + 100))

    screen.blit(exit_surface, exit_rectangle)

    pygame.display.update()

    while True: # continue until the program closes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    sys.exit()


def buttons(screen):
    # Creates the font used for in_game_buttons
    in_game_button_font = pygame.font.Font(None, 25)

    # Creates the reset button.
    reset_text = in_game_button_font.render('RESET', 0, WHITE)
    reset_surface = pygame.Surface((65, 31))
    reset_surface.fill(BLACK)
    reset_surface.blit(reset_text, (5, 5))
    reset_rectangle = reset_surface.get_rect(center=(200, 630))
    screen.blit(reset_surface, reset_rectangle)

    # Creates the restart button.
    restart_text = in_game_button_font.render('RESTART', 0, WHITE)
    restart_surface = pygame.Surface((85, 31))
    restart_surface.fill(BLACK)
    restart_surface.blit(restart_text, (5, 5))
    restart_rectangle = restart_surface.get_rect(center=(300, 630))
    screen.blit(restart_surface, restart_rectangle)

    # Creates the exit button.
    exit_text = in_game_button_font.render('EXIT', 0, WHITE)
    exit_surface = pygame.Surface((50, 31))
    exit_surface.fill(BLACK)
    exit_surface.blit(exit_text, (5, 5))
    exit_rectangle = exit_surface.get_rect(center=(400, 630))
    screen.blit(exit_surface, exit_rectangle)

    # Updates display to conform with changes.
    pygame.display.update()


pygame.init()
start_title_font = pygame.font.Font(None, 100)
game_font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 70)
# Calls start menu and the selected difficulty level is returned.
difficulty = game_start()
# Creates screen, adds caption, and fills with a white background.
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('( ͡° ͜ʖ ͡°) SUDOKU ( ͡° ͜ʖ ͡°)')
screen.fill(WHITE)
# Calls Board class to create current_board.
current_board = Board(600, 600, screen, difficulty)
# Draws current_board.
current_board.draw()
buttons(screen)

# Loop used to evaluate events.
while True:
    for event in pygame.event.get():
        # Exits the program if the 'x' is clicked.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Addresses mouse button down events.
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(WHITE)
            current_board.draw()
            x, y = event.pos
            # Exits the game if exit is pressed.
            if 375 <= x <= 425 and 614.5 <= y <= 645.5:
                pygame.quit()
                sys.exit()
            # Restarts the game menu and initial steps if restart is selected.
            elif 257.5 <= x <= 347.5 and 614.5 <= y <= 645.5:
                difficulty = game_start()
                screen = pygame.display.set_mode((width, height))
                pygame.display.set_caption('Sudoku')
                screen.fill([255, 255, 245])
                # Calls Board class to create a new current_board.
                current_board = Board(600, 600, screen, difficulty)
                current_board.draw()
                buttons(screen)
                pygame.display.update()
            # Calls method to replace current list of cells with original version.
            elif 167.5 <= x <= 232.5 and 614.5 <= y <= 645.5:
                current_board.reset_to_original()
                screen.fill([255, 255, 245])
                current_board.draw()
                buttons(screen)
                pygame.display.update()
            # Addresses other clicks.
            else:
                # Tries to proceed like a cell was selected.
                try:
                    coordinates = current_board.click(x, y)
                    current_board.select(coordinates[0], coordinates[1])
                    buttons(screen)
                    pygame.display.update()
                # Otherwise, takes no action.
                except:
                    pass
        # Used https://www.geeksforgeeks.org/how-to-get-keyboard-input-in-pygame/ for information on setting up loop.
        if event.type == pygame.KEYDOWN:
            # if there is a valid cell to delete it will pass
            try:
                if event.key == pygame.K_BACKSPACE:
                    current_board.clear()
                    screen.fill(WHITE)
                    current_board.draw()
                    buttons(screen)
                    pygame.display.update()
                # If 1-9 is pressed for a valid cell, board, list, and screen display are updated.
                # For any input using pygame and a number it will be inputted into the cell
                elif 1 <= int(pygame.key.name(event.key)[-1]) <= 9:
                    guess = int(pygame.key.name(event.key)[-1])
                    current_board.sketch(guess)
                    current_board.place_number(guess)
                    current_board.update_board()
                    screen.fill(WHITE)
                    current_board.draw()
                    buttons(screen)
                    pygame.display.update()
            # If a number is pressed for a valid cell, board, list, and screen display are updated.
            except:
                pass
        current_board.update_board()
        # Checks whether the board is full.
        if current_board.is_full():
            # Credit to OH TA Wednesday 3:22 ET for debugging. Originally missing "()".
            if current_board.check_board():
                game_win()
            else:
                # Calls game over function and initiates new game.
                game_over()
                screen = pygame.display.set_mode((width, height))
                pygame.display.set_caption('Sudoku')
                screen.fill(WHITE)
                # Calls Board class to create a new current_board.
                current_board = Board(600, 600, screen, difficulty)
                current_board.draw()
                buttons(screen)
                pygame.display.update()

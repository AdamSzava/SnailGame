import pygame
import sys
import random

#macros
GAME_TITLE = 'Snail Game'
WINDOW_SIZE = (1280,720)


def startGame() -> None:
    # initialize pygame and the game window
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(GAME_TITLE)

    # create a clock to control frame rate
    clock = pygame.time.Clock()

    # main game loop
    while True:
        # check if close window button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # run the step function for valid entities

        pygame.display.update()# update the screen with all the new information
        clock.tick(60)#


if __name__ == '__main__':
    startGame()

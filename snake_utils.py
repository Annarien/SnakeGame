"""
This python file contains all the methods and functions are created and need for a successful snake gaming
experience.
"""
# imports
import pygame
import time
import random

# global variables
display_height = 600
display_width = 800
display_screen = pygame.display.set_mode((display_width, display_height))
# x1_change = 0
# y1_change = 0
# x1 = display_width / 2
# y1 = display_height / 2
snake_block = 10
snake_speed = 30
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

clock = pygame.time.Clock()


class GameProcess:

    # the different functions of playing the snake game is place here.
    @staticmethod
    def message(msg, color):
        font_style = pygame.font.SysFont(None, 50)

        mesg = font_style.render(msg, True, color)
        display_screen.blit(mesg, [display_width/3, display_height/3])

    @staticmethod
    def gameLoop():
        game_over = False
        game_close = False

        x1 = display_width / 2
        y1 = display_height / 2

        x1_change = 0
        y1_change = 0

        foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0

        while not game_over:
            while game_close:
                display_screen.fill(white)
                GameProcess.message('You Lost!  Press Q-Quit or C-Play Again', red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            GameProcess.gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            display_screen.fill(white)
            pygame.draw.rect(display_screen, blue, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(display_screen, black, [x1, y1, snake_block, snake_block])
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                print("Yummy!!")
            clock.tick(snake_speed)

        pygame.quit()
        quit()



"""
The snake game follows work from: https://www.edureka.co/blog/snake-game-with-pygame/

This is the the traditional snake game. The snake moves up or down, left or right, and is able to eat an apple.
If the apple is eaten, the length of the snake increases by one.
If the snake eats itself or bumps into a wall => Game Over.
"""

# imports
from snake_utils import GameProcess

GameProcess.gameLoop()
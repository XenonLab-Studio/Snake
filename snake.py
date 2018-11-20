#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Copyright (C) 2018 Stefano Peris <xenonlab.develop@gmail.com>

Github repository: <https://github.com/XenonLab-Studio/Snake.git>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

# Define some variables
WIDTH = 35 # total game cell width and height
HEIGHT = 20
MAX_X = WIDTH - 2 # sets max inside the game, so the snake wont hit the border
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 5 # Starting snake length
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100 # this controls the speed of the game

# Make Snake Oject
class Snake(object):
    def __init__(self):
        self.x = 'Hisss!'

    def method_a(self, foo):
        print self.x + ' ' + foo

snake = Snake() # We do not pass any argument to the __init__ method
snake.method_a('Says the snake') # We only pass a single argument

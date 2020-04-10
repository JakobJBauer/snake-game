import pygame
import random
from snake_body import SnakeBody
from frame import Frame
from snake import Snake


class Food(SnakeBody):
    def __init__(self, width: int, window, frame: Frame, color: pygame.Color, snake: Snake):
        super().__init__(0, 0, width)
        self.display = window
        self.color = color
        self.frame = frame
        self.snake = snake

    def spawn(self):
        self.x = random.randint(1, (self.frame.get_width() // self.width) - 1) * self.width
        self.y = random.randint(1, (self.frame.get_height() // self.height) - 1) * self.height

    def redraw(self):
        pygame.draw.rect(self.display, self.color, pygame.Rect(*self.properties()))

    def get_eaten(self):
        self.spawn()
        self.redraw()

    def eating_process(self) -> bool:
        if self.snake.get_head().coordinates() == self.coordinates():
            self.get_eaten()
            self.snake.grow()
            return True
        return False

    def set_food_color(self, color):
        self.color = color

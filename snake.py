import pygame
from .frame import Frame
from .snake_body import SnakeBody
from .main import PIXEL_SIZE


class Snake:
    def __init__(self, frame: Frame, color: pygame.color):
        self.frame = frame
        self.x = frame.get_width() // 2
        self.y = frame.get_height() // 2
        self.body = [
            SnakeBody(self.x - 2, self.y),
            SnakeBody(self.x - 1, self.y),
            SnakeBody(self.x, self.y)
        ]
        self.color = color
        self.growth = 0
        self.direction = "right"

    def get_snake(self):
        return self.body

    def grow(self, factor: int = 1):
        self.growth += factor

    def move(self):
        if self.growth > 0:
            self.growth -= 1
        else:
            self.body.pop()
        self.body.append(self._get_new_coordinate())

    def draw(self):
        for body_sequence in self.get_snake():
            pygame.draw.rect(self.frame, self.color, body_sequence.coordinates())

    def _get_new_coordinate(self):
        x, y = self.body[-1].coordinates()

        if self.direction == "up":
            y -= PIXEL_SIZE
        elif self.direction == "down":
            y += PIXEL_SIZE
        elif self.direction == "left":
            x -= PIXEL_SIZE
        elif self.direction == "right":
            x += PIXEL_SIZE

        return SnakeBody(x, y)

    def set_direction(self, direction: str):
        if direction not in ("up", "down", "left", "right"):
            raise ValueError("Direction must be 'up', 'down', 'left' or 'right'")
        self.direction = direction

    def is_dead(self):
        return self._bite_itself() and self._hit_obstacle()

    def _bite_itself(self):
        snake_bodies = self.get_snake()
        for body in snake_bodies:
            temp_bodies = snake_bodies.copy()
            temp_bodies.remove(body)
            if body in temp_bodies:
                return True
        return False

    def _hit_obstacle(self):
        x, y = self.get_snake()[-1].coordinates()
        if x < 0 or x > self.frame.get_width():
            return True
        if y < 0 or y > self.frame.get_height():
            return True
        return False

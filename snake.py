import pygame
from frame import Frame
from snake_body import SnakeBody


class Snake:
    def __init__(self, frame: Frame, color: pygame.color, pixel_size: int):
        self.frame = frame
        self.x = frame.get_width() // 2
        self.y = frame.get_height() // 2
        self.body = [
            SnakeBody(self.x - 2 * pixel_size, self.y, pixel_size),
            SnakeBody(self.x - pixel_size, self.y, pixel_size),
            SnakeBody(self.x, self.y, pixel_size)
        ]
        self.color = color
        self.growth = 0
        self.direction = "hold"
        self.pixel_size = pixel_size
        self.display = frame.get_display()
        self.score = 0

    def get_snake(self):
        return self.body

    def get_head(self):
        return self.get_snake()[-1]

    def grow(self, factor: int = 1):
        self.growth += factor
        self.score += factor

    def move(self):
        if not self.is_dead():
            if self.growth > 0:
                self.growth -= 1
            else:
                self.body.pop(0)
            self.body.append(self._get_new_coordinate())

    def draw(self):
        for body_sequence in self.get_snake():
            pygame.draw.rect(self.display, self.color, pygame.Rect(*body_sequence.properties()))

    def _get_new_coordinate(self):
        x, y = self.body[-1].coordinates()

        if self.direction == "up":
            y -= self.pixel_size
        elif self.direction == "down":
            y += self.pixel_size
        elif self.direction == "left":
            x -= self.pixel_size
        elif self.direction == "right":
            x += self.pixel_size

        return SnakeBody(x, y, self.pixel_size)

    def set_direction(self, direction: str):
        if direction not in ("up", "down", "left", "right"):
            raise ValueError("Direction must be 'up', 'down', 'left' or 'right'")
        self.direction = direction

    def is_dead(self):
        return self._bite_itself() or self._hit_obstacle()

    def revive(self):
        self.body = [
            SnakeBody(self.x - 2 * self.pixel_size, self.y, self.pixel_size),
            SnakeBody(self.x - self.pixel_size, self.y, self.pixel_size),
            SnakeBody(self.x, self.y, self.pixel_size)
        ]
        self.set_direction("left")
        self.score = 0

    def _bite_itself(self):
        snake_bodies = self.get_snake().copy()
        for i in range(len(snake_bodies)):
            current_body = snake_bodies.pop(0)
            for snake_body in snake_bodies:
                if current_body.coordinates() == snake_body.coordinates():
                    return True
        return False

    def _hit_obstacle(self):
        x, y = self.get_snake()[-1].coordinates()
        if x < 0 or x > self.frame.get_width()-1:
            return True
        if y < 0 or y > self.frame.get_height()-1:
            return True
        return False

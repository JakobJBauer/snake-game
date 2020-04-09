import pygame


class Frame:
    def __init__(self, width: int, height: int, caption: str):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_frame(self):
        return self.window

    def get_display(self):
        return self.window

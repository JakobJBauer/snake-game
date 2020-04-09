class SnakeBody:
    def __init__(self, x: int, y: int, width: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = width

    def coordinates(self):
        return self.x, self.y

    def properties(self):
        return self.x, self.y, self.width, self.height

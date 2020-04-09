class SnakeBody:
    def __init__(self, x: int, y: int, _width: int):
        self.x = x
        self.y = y
        self.width = _width
        self.height = _width

    def coordinates(self):
        return self.x, self.y

    def properties(self):
        return self.x, self.y, self.width, self.height

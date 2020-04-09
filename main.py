import pygame
from .frame import Frame
from .snake import Snake

# region define constants
FRAME_WIDTH = 500
FRAME_HEIGHT = 500
COLOR = 'red3'
FPS = 60
PIXEL_SIZE = 10
# endregion

pygame.init()

frame = Frame(FRAME_WIDTH, FRAME_HEIGHT, "Snake - by Jakob J. Bauer")
snake = Snake(frame, pygame.color.THECOLORS.get(COLOR, (255, 0, 0, 0)))
pygame.time.Clock().tick(FPS)  # Set framerate


"""while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x - velocity >= 0:
            x -= velocity
        else:
            x = 0
    if keys[pygame.K_RIGHT]:
        if x + width + velocity <= max_x:
            x += velocity
        else:
            x = max_x - width

    if not is_jumping:
        if keys[pygame.K_DOWN]:
            if y + height + velocity <= max_y:
                y += velocity
            else:
                y = max_y - height
        if keys[pygame.K_UP]:
            if y - velocity >= 0:
                y -= velocity
            else:
                y = 0
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1

            y -= jump_count ** 2 * neg * gravity
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()"""

pygame.quit()

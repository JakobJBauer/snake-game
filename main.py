import pygame
import time
import random
from frame import Frame
from snake import Snake
from food import Food

# region define constants
FRAME_WIDTH = 500
FRAME_HEIGHT = 500
COLOR = 'red3'
FPS = 30
PIXEL_SIZE = 10
# endregion

pygame.init()

frame = Frame(FRAME_WIDTH, FRAME_HEIGHT, "Snake - by Jakob J. Bauer")
display = frame.get_display()
snake = Snake(frame, pygame.color.THECOLORS.get(COLOR, (255, 0, 0)), PIXEL_SIZE)
food = Food(PIXEL_SIZE, display, frame, pygame.color.THECOLORS[COLOR], snake)
clock = pygame.time.Clock()

loosing_text = pygame.font.SysFont("Comic Sans MS", 30).render("You died!", False, (0, 255, 0))

t0 = time.time()
food.get_eaten()

run = True
while run:
    tn = time.time()
    clock.tick(FPS * ((tn - t0) * 0.01 + 0.8))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snake.set_direction("left")
    if keys[pygame.K_RIGHT]:
        snake.set_direction("right")
    if keys[pygame.K_DOWN]:
        snake.set_direction("down")
    if keys[pygame.K_UP]:
        snake.set_direction("up")

    frame.window.fill((0, 0, 0))
    snake.move()

    eaten = food.eating_process()
    if eaten:
        food.set_food_color((random.randint(0, 222), random.randint(0, 222), random.randint(0, 222)))

    snake.draw()
    food.redraw()

    if snake.is_dead():
        display.blit(loosing_text, (200, 200))

    pygame.display.update()

pygame.quit()

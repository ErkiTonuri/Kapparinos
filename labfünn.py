import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Rectangle():
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)
        self.height = random.randint(20, 70)
        self.width = random.randint(20, 70)
        self.move_x = random.randint(-3, 3)
        self.move_y = random.randint(-3, 3)
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def move(self):
        self.x += self.move_x
        self.y += self.move_y
        if 1000 < self.x or 0 > self.x:
            self.move_x *= -1
        if 700 < self.y or 0 > self.y:
            self.move_y *= -1

    def draw(self):
        pygame.draw.rect(screen, (self.r, self.g, self.b), (self.x, self.y, self.height, self.width))


class Ellipse(Rectangle):
    def __init__(self):
        super().__init__()

    def draw(self):
        pygame.draw.ellipse(screen, (self.r, self.g, self.b), (self.x, self.y, self.height, self.width))


pygame.init()

size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

my_list = []

for i in range(500):
    my_object = Rectangle()
    my_list.append(my_object)
    my_object = Ellipse()
    my_list.append(my_object)


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    p = len(my_list)
    for i in range(p):
        my_object = my_list[i]
        my_object.move()
        my_object.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
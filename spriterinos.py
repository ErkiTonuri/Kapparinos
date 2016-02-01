import pygame
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 30])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # Draw the ellipse

    def draw(self):
        pygame.draw.ellipse(self.image, BLACK, [0, 0, 50, 100])

pygame.init()

size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

my_list = []

clock = pygame.time.Clock()

done = False

for i in range(500):
    my_object = Block()
    my_list.append(my_object)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    p = len(my_list)
    for i in range(p):
        my_object = my_list[i]
        #my_object.move()
        my_object.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
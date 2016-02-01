import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

size = (320, 420)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MÄNG")

done = False
clock = pygame.time.Clock()


class Ball():
    def __init__(self):
        # Ball location
        self.x = 0
        self.y = 0

        # Ball's movement
        self.change_x = 0
        self.change_y = 0

        # Ball size
        self.size = 10

        # Ball colour
        self.color = [255, 255, 255]

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)


theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 2
theBall.change_y = 1
theBall.color = [255, 0, 0]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLUE)
    theBall.move()
    theBall.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

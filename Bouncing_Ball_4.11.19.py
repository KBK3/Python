import pygame
import random
class Ball():
        # --- Атрибуты класса ---
        # Ball position
        x=0
        y=0
        # Ball's vector
        change_x=0
        change_y=0
        # Ball size
        size=80
        # Ball color
        color=[255,255,255]
        # --- Методы класса ---
        def move(self):
            self.x += self.change_x
            self.y += self.change_y
        def draw(self, screen):
            pygame.draw.circle(screen, self.color, [self.x, self.y], self.size )
pygame.init()
FPS=60
white = [255,255,255]
green = [0, 255, 0]
red = [255, 0, 0]
yellow = [255,255,0]
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pinball")
clock = pygame.time.Clock()
done = True
k=1
w=1
s=1
theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 2
theBall.change_y = 1
theBall.color = [255,0,0]
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    screen.fill(white)
    # Этот код находится в главном цикле чтобы двигать и рисовать шар:
    if theBall.y > 600 - 80 or theBall.y < 80:
        theBall.change_y *= -1
    if theBall.x > 600 or theBall.x < 80:
        theBall.change_x *= -1
    theBall.move()
    theBall.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

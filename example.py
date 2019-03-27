import pygame
import random
size=[800,600]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("pygame_Muntjan")
done=False
#Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
#rgb
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
color=[r,g,b]
#position

clock=pygame.time.Clock()
screen.fill(white)
pygame.display.flip()
for circle1 in range(1,50,2):
    pygame.draw.circle(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,800),random.randint(0,600)),random.randint(10,40),2)
    pygame.display.flip()
    clock.tick(20)
while done==False:
     for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True

pygame.quit()

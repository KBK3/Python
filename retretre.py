import pygame
pygame.init()
white = [255,255,255]
green = [0, 255, 0]
red = [255, 0, 0]
yellow = [255,255,0]
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Work_Animaton")
x=50
y=350
x1=400
y1=-50
run = True
while run:
    for a in pygame.event.get():
        if a.type == pygame.QUIT:
            run=False
    screen.fill(white)
    pygame.draw.circle(screen,yellow,(x,y),60,0)
    pygame.draw.circle(screen,red,(x1,y1),60,0)
    #pygame.draw.circle(screen,green,(x,y),60,0)
    pygame.display.flip()
    x=x+5
    if x<860:
        x=-60
    y1=y1+5
    if y1> 660:
        y1=-60

    pygame.time.delay(10)

pygame.quit()

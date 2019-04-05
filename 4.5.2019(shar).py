import pygame
pygame.init()
white = [255,255,255]
green = [0, 255, 0]
red = [255, 0, 0]
yellow = [255,255,0]
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Animation")
x = 100
y = 100
x1 = 400
y1 = 100
x2 = 100
y2 = 100
#screen.fill(white)
#pygame.draw.circle(screen,green,[x,y],100,0)
#pygame.display.flip()
done = True
#clock = pygame.time.Clock()
k = 1
w = 1
s = 1
while done:
    #clock.tick(1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=False
    screen.fill(white)
    pygame.draw.circle(screen,green,[x,y],100,0)
    pygame.draw.circle(screen,red,[x1,y1],100,0)
    pygame.draw.circle(screen,yellow,[x2,y2],100,0)
    pygame.display.flip()
    #x += 5
    if x>800:
        k = -1
    if x<0:
        k = 1
    x = x+5*k
    if y1>600:
        w = -1
    if y1<0:
        w = 1
    y1 = y1+5*w

    if x2>800:
        s = -1
    x2 = x2+5*s
    if y2>600:
        s = -1
    y2 = y2+5*s

    if x2<100:
        s = 1
    x2 = x2+5*s
    if y2<100:
        s = 1
    y2 = y2+5*s
    
        
        
        
    pygame.time.delay(10)
pygame.quit()

import pygame, sys
pygame.init()
white=(255,255,255)
screen = pygame.display.set_mode([800, 600])
image1 = pygame.image.load("put.jpg") 
#image = pygame.transform.scale(image, (200, 200)).convert()
image2 = pygame.image.load("pu1.jpg") 
#image2 = pygame.transform.scale(image1, (200, 200)).convert()
image=image1
x=5
y=90
k=1
screen.blit(image, (x,y))
pygame.display.flip()
running = True
while running:
    for i in pygame.event.get():
        if  i.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    screen.fill(white)
    screen.blit(image, (x,y))
    x+=5*k
    if x >800:
        k=-1
        image=image2
    if x<0:
        k=1
        image=image1

    pygame.time.delay(10)
pygame.quit()

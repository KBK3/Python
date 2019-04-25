import pygame
pygame.init()
FPS = 60
W = 1060 # ширина экрана
H = 644 # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
#Фон
bg=pygame.image.load("backg.png")
#Персонажи
static=pygame.image.load("static_1.png")
start=pygame.image.load("start.png")
process=pygame.image.load("process.png")
zercal_static=pygame.image.load("zercal_static.png")
zercal_start=pygame.image.load("zercal_start.png")
zercal_process=pygame.image.load("zercal_process.png")
Char=static
go=0
x=10
y=523
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.key.set_repeat(1,1)
done = True
while done:
    sc.blit(bg,(0,0))
    sc.blit(static,(x,y))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 3
            elif i.key == pygame.K_RIGHT:
                x += 3
    clock.tick(FPS)
pygame.quit()

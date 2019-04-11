import pygame
'''
FPS = 60
W = 700 # ширина экрана
H = 300 # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50
done = True
while done:
    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
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
'''
#2
'''
FPS = 60
W = 800 # ширина экрана
H = 600 # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50
motion = STOP
done = True
while done:
    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                motion = STOP
    if motion == LEFT:
        x -= 3
    elif motion == RIGHT:
        x += 3
    clock.tick(FPS)
pygame.quit()
'''
#3
'''
x = 200
y = 200
ekraan = pygame.display.set_mode([1366, 766])
pilt = pygame.image.load("android.png") 
samm = 10
running = True
while running:
    ekraan.fill([255, 255, 255])
    ekraan.blit(pilt, (x,y))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        # Kui sündmuseks on klahvi allavajutamine...
        elif i.type == pygame.KEYDOWN:
            # ... ja klahviks on nooleklahv üles liikumiseks,...
            if i.key == pygame.K_UP:
                # ... siis vähendame y-koordinaati
                    y = y - samm
            elif i.key == pygame.K_DOWN:
                y = y + samm
            elif i.key == pygame.K_LEFT:
                x = x - samm
            elif i.key == pygame.K_RIGHT:
                x = x + samm
pygame.quit()
'''
#4
import pygame
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
pygame.init()
sc = pygame.display.set_mode((400, 300))
sc.fill(WHITE)
pygame.display.update()
done = True
while done: for i in pygame.event.get():
    if i.type == pygame.QUIT:
        done = False
    if i.type == pygame.MOUSEBUTTONDOWN:
        if i.button == 1:
            pygame.draw.circle(sc, RED, i.pos, 20)
            pygame.display.update()
        elif i.button == 3:
            pygame.draw.circle(sc, BLUE, i.pos, 20)
            pygame.draw.rect(sc, GREEN, (i.pos[0]-10, i.pos[1]-10, 20,20))
            pygame.display.update()
        elif i.button == 2:
            sc.fill(WHITE)
            pygame.display.update()
pygame.time.delay(20)
'''
while done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if pressed[0]:
        pygame.draw.circle(sc, BLUE, pos, 5)
        pygame.display.update()
pygame.time.delay(20)
pygame.mouse.set_visible(False)
while done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
    sc.fill(WHITE)
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(sc, BLUE, (pos[0]-10, pos[1]-10, 20, 20))
        pygame.display.update()
pygame.time.delay(20)
'''
pygame.quit()

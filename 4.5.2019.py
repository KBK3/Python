#Клетка
import pygame
pygame.init()
black = [0,0,0]
white = [255,255,255]
size =  [600,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

screen.fill(white)
pygame.draw.line(screen,black,[0,0],[600,0],3)
pygame.draw.line(screen,black,[200,0],[200,600],3)
pygame.draw.line(screen,black,[400,0],[400,600],3)
pygame.draw.line(screen,black,[0,0],[0,800],3)
#pygame.draw.line(screen,black,[600,0],[600,600],3)
pygame.draw.line(screen,black,[0,200],[600,200],3)
pygame.draw.line(screen,black,[0,400],[600,400],3)
pygame.draw.line(screen,black,[0,600],[600,600],3)
pygame.display.flip()
done = True
clock = pygame.time.Clock()
while done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
pygame.quit()

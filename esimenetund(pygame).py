# Импортировать библиотеку под названием 'pygame'
import pygame
# Инициализировать игровой движок
'''
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
'''
red = ( 255,   0,   0)
green    = (   0, 255,   0)
black=(0,0,0)
# Задать ширину и высоту и цвет экрана
size=[800,600]
screen=pygame.display.set_mode(size)
yellow=(255,255,0)
#Задать заголовок окну
pygame.display.set_caption("siseveeb.exe")
#Оставаться в цикле, пока пользователь не нажмёт на кнопку закрытия окна
done=False
#Фон
screen.fill(yellow)
# Обновить экран, выведя то, что мы нарисовали
pygame.display.flip()
# Используется для контроля частоты обновления экрана
clock=pygame.time.Clock()
 
# -------- Основной цикл программы -----------
while done==False:
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
 
 
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
 
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
 
 
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
    # Нарисовать на экране зелёную линию от (0,0) до (100,100)
    # шириной в пять пикселей.
    pygame.draw.line(screen,red,[0,0],[800,600],30)
    pygame.draw.line(screen,green,[0,600],[800,0],30)
    pygame.draw.rect(screen,black,[120,120,250,200],2)
    # Нарисовать эллипс, используя прямоугольник для задания внешних границ
    pygame.draw.ellipse(screen,black,[120,120,250,200],2)
    pygame.display.flip()
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
    for y_offset in range(0,150,20):
        pygame.draw.line(screen,green,[0,10+y_offset],[100,110+y_offset],5)
        pygame.display.flip()
        clock.tick(20)
    # Ограничить до 20 кадров в секунду
    clock.tick(30)
pygame.quit()

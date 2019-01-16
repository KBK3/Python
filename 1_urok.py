
# http://zpirittutorials.blogspot.com.ee/2011/04/pygame_11.html


# Наша первая программа - PYGAME

# Импорт библиотеки pygame
import pygame

# Инициализируем движок pygame
pygame.init()

# Определяем несколько цветов, которые мы будем
# использовать (RGB)
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
color = [153, 0, 153]

pi = 3.141592653

# Устанавливаем размеры окна
size = [800, 600]
screen = pygame.display.set_mode(size)

# Устанавливаем заголовок окна
pygame.display.set_caption("Game")

# Цикл работает пока пользователь не закроет окно
done = False
clock = pygame.time.Clock()

while done == False:
 # Следующяя строка ограничивает наш цикл 10 кадрами в секунду.
 # Если этого не сделать, то игра будет использовать
 # максимальное колличество ресурсов.
 clock.tick(10)
 for event in pygame.event.get():  # Проходимся по событиям
  if event.type == pygame.QUIT: # Если пользователь закрыл окно
   done = True # Сигнализируем что цикл пора завершать
 
 # Все рисование происходит после нашего for-цикла,
 # но внутри главного цикла ( while done==False ).
 
 # Заливаем  экран
 screen.fill(white)
 
 # Рисуем на экране зеленую линию из левого верхнего угла (0, 0)
 # в точку (100, 100) шириной 5 пикселей
 pygame.draw.line(screen, green, [0,0], [800,600], 5)
 
 # Рисуем несколько красных линий из точки (0,10) в точку (200, 210)
 # используя цикл
 y_offset = 0
 while y_offset < 200 :
  pygame.draw.line(screen, red, [0, 10+y_offset], [200, 210+y_offset], 5)
  y_offset += 20
  
 # Выбираем шрифт, который мы будем использовать.
 # Стандартный шрифт, 25 точек.
 
 font = pygame.font.Font(None, 55)
 font2 = pygame.font.SysFont('Constantia', 30)
 
 # Рисуем текст. "True" означает использовать сглаживание
 # Black -- цвет текста. Следующая строка создает образ текста
 # но не рисует его на экране.
 text = font.render("Первый рисунок", True, blue)
 text2 = font2.render ("Графические примитивы", True, color)
 
 #Рисуем изображение текста на экран в точке (250, 250)
 screen.blit(text, [400, 150] )
 screen.blit(text2, [220, 65] )
 
 # Рисуем прямоугольник (верхний угол, ширина, высота
 pygame.draw.rect(screen, blue, [200,200, 500,350], 5)
 
 # Рисуем эллипс. При рисовании эллипса используется
 # прямоугольник, в который этот эллипс вписывается
 pygame.draw.ellipse(screen, green, [200,20, 400, 100], 4)
 
 # Рисуем дугу как часть эллипса. Координаты угла
 # задаются в радианах
 pygame.draw.arc(screen,black,[20,220,250,200], 0, pi/2, 5)
 pygame.draw.arc(screen,green,[20,220,250,200], pi/2, pi, 5)
 pygame.draw.arc(screen,blue, [20,220,250,200], pi,3*pi/2, 5)
 pygame.draw.arc(screen,red, [20,220,250,200],3*pi/2, 2*pi, 5)
 
 # Эта строчка рисует треугольник используя функцию "polygon"
 pygame.draw.polygon(screen,red,[[400,400],[300,500],[500,500]],5)

 # дополнила окружность   
 pygame.draw.circle(screen,color,[550,300],50,0)
 pygame.draw.circle(screen,white,[550,300],30,0)
 
 
 # Теперь обновляем окно чтобы все наше рисование
 # отобразилось на экране. Это надо делать ПОСЛЕ ТОГО
 # как все нарисовали
 pygame.display.flip()

pygame.quit()

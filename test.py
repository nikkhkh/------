import pygame
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Змейка')
 
game_over = False
x1 = 300 #Указываем начальное значение положения змейки по оси х.
y1 = 300 #Указываем начальное значение положения змейки по оси y.
x1_change = 0 #Создаём переменную, которой в цикле while будут
#присваиваться значения изменения положения змейки по оси х.
y1_change = 0 #создаём переменную, которой в цикле while будут
#присваиваться значения изменения положения змейки по оси y.
clock = pygame.time.Clock()
 
while not game_over:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           game_over = True
       if event.type == pygame.KEYDOWN: #Добавляем считывание направления
#движений с клавиатуры.
           if event.key == pygame.K_LEFT:
               x1_change = -10 #Указываем шаг изменения положения змейки
#в 10 пикселей.
               y1_change = 0
           elif event.key == pygame.K_RIGHT:
               x1_change = 10
               y1_change = 0
           elif event.key == pygame.K_UP:
               y1_change = -10
               x1_change = 0
           elif event.key == pygame.K_DOWN:
               y1_change = 10
               x1_change = 0
   x1 += x1_change #Записываем новое значение положения змейки по оси х.
   y1 += y1_change #Записываем новое значение положения змейки по оси y.
   dis.fill(white)
   
   pygame.draw.rect(dis, black, [x1, y1, 10, 10])
   pygame.display.update()
   clock.tick(30)
 
pygame.quit()
quit()
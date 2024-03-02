import pygame as pg

black = (0, 0, 0)

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 200
        self.y = 200
        self.y1_change = 10
        self.x1_change = 0

    def draw(self):
        pg.draw.rect(self.screen, black, [self.x, self.y, 10, 10])

    def move (self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                x1_change = -10 #Указываем шаг изменения положения змейки в 10 пикселей.
                y1_change = 0   
            elif event.key == pg.K_d:
                x1_change = 10
                y1_change = 0
            elif event.key == pg.K_w:
                y1_change = -10
                x1_change = 0
            elif event.key == pg.K_s:
                self.y1_change = 10
                self.x1_change = 0
        self.x += self.x1_change #Записываем новое значение положения змейки по оси х.
        self.y += self.y1_change #Записываем новое значение положения змейки по оси y.

    def update(self):
        pass
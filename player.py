import pygame as pg

dis_width = 800
dis_height = 600

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 300
        self.y = 300

    def draw(self):
        pg.draw.rect(self.screen, 'black', (self.x, self.y), 10)

    def move (self, x1_change, y1_change, key):
        game_over = False
        x1_change = 0
        y1_change = 0
        while not game_over:
                if type == pg.KEYDOWN: #Добавляем считывание направления
                                            #движений с клавиатуры.
                    if key == pg.K_LEFT:
                        self.x1_change = -10 #Указываем шаг изменения положения змейки
                                            #в 10 пикселей.
                        self.y1_change = 0
                    elif key == pg.K_RIGHT:
                        self.x1_change = 10
                        self.y1_change = 0
                    elif key == pg.K_UP:
                        self.y1_change = -10
                        self.x1_change = 0
                    elif key == pg.K_DOWN:
                        self.y1_change = 10
                        self.x1_change = 0
        self.x += x1_change #Записываем новое значение положения змейки по оси х.
        self.y += y1_change #Записываем новое значение положения змейки по оси y.
        if self.x >= dis_width or self.x < 0 or self.y >= dis_height or self.y < 0:
            game_over = True

    def update(self):
        pass
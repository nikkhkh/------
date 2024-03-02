import pygame as pg
from player import Player

HEIGHT = 800
WEIGHT = 600

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((HEIGHT, WEIGHT))
        self.back_surf = pg.image.load('image.jpg')
        self.clock = pg.time.Clock()
        self.player = Player(self.screen)

    def game(self, x1_change, y1_change):
        while True:
            self.draw()
            self.move()
            self.update()
            self.clock.tick(30)
            x1_change()
            y1_change()
    
    def draw(self):
        self.screen.blit(self.back_surf, (0, 0))
        self.player.draw()

    def move(self, x1_change, y1_change, key):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        keys_pressed = pg.key.get_pressed()
        self.player.move(keys_pressed)

    def update(self):
        pg.display.update()

game = Game()
game.game()
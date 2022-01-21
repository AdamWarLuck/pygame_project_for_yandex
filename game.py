import pygame
import sys

from start import Screen_for_start
from settings import Settings
from image import Image
from maps import Map
from fight import Fight
from end import Screen_for_end
#from module1 import Screen_for_start


class Game:
    def __init__(self): 
        pygame.init()
        self.settings = Settings()
        self.start = Screen_for_start(self)
        self.image = Image(self)
        self.map = Map(self)
        self.end = Screen_for_end(self)
        self.fight = Fight(self)
        
        self.screen = pygame.display.set_mode(self.settings.proportions_game_screen)
        self.sprite = pygame.sprite.Sprite()
        self.all_sprite = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Квест Арион')


    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                else:
                    if event.type == pygame.KEYDOWN:
                        self.map.move_your_hero(event)

                    for i in self.map.mapping_of_forest():
                        self.screen.blit(i[0], i[1])

            self.clock.tick(self.settings.FPS)
            pygame.display.flip()


t = Game()

t.start.start_screen()
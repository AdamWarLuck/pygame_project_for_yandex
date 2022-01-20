import random
import pygame
import sys


from settings import Settings
from image import Image
from maps import Map


class Game():
    def __init__(self): 
        self.settings = Settings()
        self.map = Map(self)
        self.image = Image()

        pygame.init()
        #self.keys = pygame.key.get_pressed()
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

                    map = self.map.mapping_of_forest()
                    for i in map:
                        self.screen.blit(i[0], i[1])


            self.clock.tick(self.settings.FPS)
            pygame.display.flip()


t = Game()

t.start_game()
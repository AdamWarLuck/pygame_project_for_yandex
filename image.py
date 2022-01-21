import pygame
from settings import Settings

class Image:
    def __init__(self, game):
        self.game = game

        self.back_ground_of_forest = pygame.image.load('data/forest_background.png')

        self.grass = pygame.image.load('data/grass.png')
        self.grass = pygame.transform.scale(self.grass, self.game.settings.proportions_for_map)

        self.goblin = pygame.image.load('data/goblin.png')
        
        self.goblin.set_colorkey(self.goblin.get_at((0, 0)))

        self.knight_hero = pygame.image.load('data/knight.png')
        self.knight_hero.set_colorkey(self.knight_hero.get_at((0, 0)))

        self.tree = pygame.image.load('data/tree.png')
        self.tree = pygame.transform.scale(self.tree, self.game.settings.proportions_for_map)
        self.tree.set_colorkey(self.tree.get_at((0, 0)))

        self.ent = pygame.image.load('data/ent.png')
        
        self.ent.set_colorkey(self.ent.get_at((0, 0)))

        self.slime = pygame.image.load('data/monstr_slime.png')
        
        self.slime.set_colorkey(self.slime.get_at((0, 0)))
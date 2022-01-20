import pygame
from settings import Settings

class Image:
    def __init__(self):
        self.settings = Settings()

        self.back_ground_of_forest = pygame.image.load('data/forest_background.png')

        self.sword = pygame.image.load('data/sword.png')
        self.sword.set_colorkey(self.sword.get_at((0, 0)))

        self.sword_with_fire = pygame.image.load('data/sword_with_fire.png')
        self.sword_with_fire.set_colorkey(self.sword_with_fire.get_at((0, 0)))
        
        self.shield = pygame.image.load('data/shield.png')
        self.shield.set_colorkey(self.shield.get_at((0, 0)))

        self.gold_shield = pygame.image.load('data/strong_shield.png')
        self.gold_shield.set_colorkey(self.gold_shield.get_at((0, 0)))

        self.chest = pygame.image.load('data/chest.png')
        self.chest = pygame.transform.scale(self.chest, self.settings.proportions_for_map_of_chest_and_heal)
        self.chest.set_colorkey(self.chest.get_at((0, 0)))

        self.grass = pygame.image.load('data/grass.png')
        self.grass = pygame.transform.scale(self.grass, self.settings.proportions_for_map)

        self.goblin = pygame.image.load('data/goblin.png')
        self.goblin = pygame.transform.scale(self.goblin, self.settings.proportions_of_goblin)
        self.goblin.set_colorkey(self.goblin.get_at((0, 0)))

        self.knight_hero = pygame.image.load('data/knight.png')
        self.knight_hero = pygame.transform.scale(self.knight_hero, self.settings.proportions_for_map)
        self.knight_hero.set_colorkey(self.knight_hero.get_at((0, 0)))

        self.tree = pygame.image.load('data/tree.png')
        self.tree = pygame.transform.scale(self.tree, self.settings.proportions_for_map)
        self.tree.set_colorkey(self.tree.get_at((0, 0)))

        self.heal = pygame.image.load('data/heal.png')
        self.heal = pygame.transform.scale(self.heal, self.settings.proportions_for_map_of_chest_and_heal)
        self.heal.set_colorkey(self.heal.get_at((0, 0)))

        self.dark_knight = pygame.image.load('data/dark_knight.png')
        self.dark_knight = pygame.transform.scale(self.dark_knight, self.settings.proportions_for_map)
        self.dark_knight.set_colorkey(self.dark_knight.get_at((0, 0)))

        self.ent = pygame.image.load('data/ent.png')
        self.ent = pygame.transform.scale(self.ent, self.settings.proportions_for_map)
        self.ent.set_colorkey(self.ent.get_at((0, 0)))

        self.slime = pygame.image.load('data/monstr_slime.png')
        self.slime = pygame.transform.scale(self.slime, self.settings.proportions_for_map)
        self.slime.set_colorkey(self.slime.get_at((0, 0)))

        self.box = pygame.image.load('data/box.png')
        self.river = pygame.image.load('data/river.png')
        self.rock = pygame.image.load('data/rock.png') 
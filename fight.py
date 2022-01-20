import pygame
from random import randint

from settings import Settings 
from image import Image

class Fight:
    def __init__(self):
        self.settings = Settings()
        self.image = Image()

        pygame.init()

        self.image.back_ground_of_forest = pygame.transform.scale(self.image.back_ground_of_forest, self.settings.proportions_game_screen)
        self.screen = pygame.display.set_mode(self.settings.proportions_game_screen)
        self.sprite = pygame.sprite.Sprite()
        self.all_sprite = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Квест Арион')

        self.hp_of_your_hero = "100"
        self.hp_of_your_enemy = "100"
        self.armor_your_hero = "0"

        self.number_of_attak_your_hero = str(randint(1, 10))
        self.number_of_armor_your_hero = str(randint(1, 10))

        self.font = pygame.font.Font(None, 40)

        self.text_for_attack = self.font.render(self.number_of_attak_your_hero, True, (255, 255, 255))
        self.text_for_armor = self.font.render(self.number_of_armor_your_hero, True, (255, 255, 255))

        self.text_of_your_hp = self.font.render(self.hp_of_your_hero, True, (255, 255, 255))
        self.text_of_your_enemy_hp = self.font.render(self.hp_of_your_enemy, True, (255, 255, 255))
        self.text_armor = self.font.render(self.armor_your_hero, True, (255, 255, 255))

        self.armor = 0
        self.hp = 300
        self.hp_enemy = 300 
        
        self.monstr = "goblin"
        self.location = "forest"

    def draw_field(self):
        
        if self.location == "forest":
            self.image.back_ground_of_forest = pygame.transform.scale(self.image.back_ground_of_forest, self.settings.proportions_game_screen)
            self.screen.blit(self.image.back_ground_of_forest, (0, 0))

            self.image.knight_hero = pygame.transform.scale(self.image.knight_hero, self.settings.proportions_of_knight_in_fight)
            self.screen.blit(self.image.knight_hero, self.settings.proportions_knight_in_fight)

            if self.monstr == "goblin":
                self.image.goblin = pygame.transform.scale(self.image.goblin, self.settings.proportions_of_goblin_in_fight)
                self.screen.blit(self.image.goblin, self.settings.positions_goblin_in_fight)

            if self.monstr == "ent":
                self.image.ent = pygame.transform.scale(self.image.ent, self.settings.proportions_of_ent_in_fight)
                self.screen.blit(self.image.ent, self.settings.proportions_ent_in_fight)
                self.image.ent.set_colorkey(self.image.ent.get_at((0, 0)))
            

        pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, 300, 60), 1)
        pygame.draw.rect(self.screen, (255, 0, 0), (1, 1, self.hp, 60))

        pygame.draw.rect(self.screen, (150, 150, 150), (308, 0, 100, 60), 1)
        pygame.draw.rect(self.screen, (150, 150, 150), (308, 1, self.armor, 60))

        pygame.draw.rect(self.screen, (255, 0, 0), (580, 0, 300, 60), 1)
        pygame.draw.rect(self.screen, (255, 0, 0), (580, 1, self.hp_enemy, 60))

        pygame.draw.rect(self.screen, (255, 0, 0), (300, 300, 40, 60))
        pygame.draw.rect(self.screen, (150, 150, 150), (300, 400, 40, 60))

        pygame.draw.rect(self.screen, (0, 0, 0), (0, 65, 100, 100), 1)
        pygame.draw.rect(self.screen, (0, 0, 0), (110, 65, 100, 100), 1)

        self.screen.blit(self.text_for_attack, (302, 310))
        self.screen.blit(self.text_for_armor, (302, 410))
        self.screen.blit(self.text_of_your_hp, (130, 17))
        self.screen.blit(self.text_of_your_enemy_hp, (710, 17))
        self.screen.blit(self.text_armor, (340, 17))

    def feature_update(self):
        self.text_for_armor = self.font.render(self.number_of_armor_your_hero, True, (255, 255, 255))
        self.text_for_attack = self.font.render(self.number_of_attak_your_hero, True, (255, 255, 255))

        self.text_of_your_hp = self.font.render(self.hp_of_your_hero, True, (255, 255, 255))

        self.text_of_your_enemy_hp = self.font.render(self.hp_of_your_enemy, True, (255, 255, 255))

        self.text_armor = self.font.render(self.armor_your_hero, True, (255, 255, 255))

    def attack(self):
        self.hp_enemy -= int(self.number_of_attak_your_hero) * 3
        self.hp_of_your_enemy = str(int(self.hp_of_your_enemy) - int(self.number_of_attak_your_hero))
        self.number_of_attak_your_hero = str(randint(1, 10))
        self.number_of_armor_your_hero = str(randint(1, 10))

    def defense(self):
        self.armor =  int(self.number_of_armor_your_hero) * 10
        self.armor_your_hero = str(self.number_of_armor_your_hero)
        self.number_of_armor_your_hero = str(randint(1, 10))
        self.number_of_attak_your_hero = str(randint(1, 10))

    def turn_enemy(self):
        pass

    def start_fight(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.attack()
                        self.feature_update()

                    elif event.button == 3:
                        self.defense()
                        self.feature_update()

            self.draw_field()

            pygame.display.flip()


t = Fight()
t.start_fight()
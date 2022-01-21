import pygame
from random import randint


class Fight:
    def __init__(self, game):
        self.game = game

        self.screen = pygame.display.set_mode(self.game.settings.proportions_game_screen)
        self.sprite = pygame.sprite.Sprite()
        self.all_sprite = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Квест Арион')

        self.hp_of_your_hero = "100"
        self.hp_of_your_enemy = "100"
        self.armor_your_hero = "0"

        self.number_of_attak_your_hero = str(randint(1, 10))
        self.number_of_armor_your_hero = str(randint(1, 3))
        

        self.font = pygame.font.Font(None, 40)

        self.text_for_attack = self.font.render(self.number_of_attak_your_hero, True, (255, 255, 255))
        self.text_for_armor = self.font.render(self.number_of_armor_your_hero, True, (255, 255, 255))

        self.text_of_your_hp = self.font.render(self.hp_of_your_hero, True, (255, 255, 255))
        self.text_of_your_enemy_hp = self.font.render(self.hp_of_your_enemy, True, (255, 255, 255))
        self.text_armor = self.font.render(self.armor_your_hero, True, (255, 255, 255))
        

        self.hp = 300
        self.hp_enemy = 300 
        
        #self.monstr = "slime"
        #self.location = "forest"

    def draw_field(self, monstr, location):
        self.monstr = monstr
        self.location = location

        if location == "forest":
            self.game.image.back_ground_of_forest = pygame.transform.scale(self.game.image.back_ground_of_forest, self.game.settings.proportions_game_screen)
            self.screen.blit(self.game.image.back_ground_of_forest, (0, 0))

            self.game.image.knight_hero = pygame.transform.scale(self.game.image.knight_hero, self.game.settings.proportions_of_knight_in_fight)
            self.screen.blit(self.game.image.knight_hero, self.game.settings.proportions_knight_in_fight)


            if monstr == "goblin":
                self.game.image.goblin = pygame.transform.scale(self.game.image.goblin, self.game.settings.proportions_of_goblin_in_fight)
                self.screen.blit(self.game.image.goblin, self.game.settings.positions_goblin_in_fight)
                self.armor_ememy = 0
                self.text_armor_enemy = self.font.render(str(self.armor_ememy), True, (255, 255, 255))
                

            elif monstr == "ent":
                self.game.image.ent = pygame.transform.scale(self.game.image.ent, self.game.settings.proportions_of_ent_in_fight)
                self.screen.blit(self.game.image.ent, self.game.settings.proportions_ent_in_fight)
                self.armor_ememy = 2
                self.text_armor_enemy = self.font.render(str(self.armor_ememy), True, (255, 255, 255))
                

            elif monstr == "slime":
                self.game.image.slime = pygame.transform.scale(self.game.image.slime, self.game.settings.proportions_of_slime_in_fight)
                self.screen.blit(self.game.image.slime, self.game.settings.proportions_slime_in_fight)
                self.text_armor_enemy = self.font.render("50%", True, (255, 255, 255))
                self.armor_ememy = round(int(self.number_of_attak_your_hero) / 2)

        pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, 300, 60), 1)
        pygame.draw.rect(self.screen, (255, 0, 0), (1, 1, self.hp, 60))

        pygame.draw.rect(self.screen, (150, 150, 150), (308, 0, 100, 60))

        pygame.draw.rect(self.screen, (150, 150, 150), (472, 0, 100, 60))

        pygame.draw.rect(self.screen, (255, 0, 0), (580, 0, 300, 60), 1)
        pygame.draw.rect(self.screen, (255, 0, 0), (580, 1, self.hp_enemy, 60))

        pygame.draw.rect(self.screen, (255, 0, 0), (300, 300, 40, 60))
        pygame.draw.rect(self.screen, (150, 150, 150), (300, 400, 40, 60))

        pygame.draw.rect(self.screen, (0, 0, 0), (0, 65, 100, 100), 1)
        pygame.draw.rect(self.screen, (0, 0, 0), (110, 65, 100, 100), 1)


        self.screen.blit(self.text_for_attack, (302, 310))
        self.screen.blit(self.text_armor_enemy, (510, 17))
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
        if int(self.number_of_attak_your_hero) * 3 - self.armor_ememy >= 0:
            self.hp_enemy -= int(self.number_of_attak_your_hero) * 3 - self.armor_ememy
            self.hp_of_your_enemy = str(int(self.hp_of_your_enemy) - int(self.number_of_attak_your_hero) + self.armor_ememy)

        self.number_of_attak_your_hero = str(randint(1, 10))
        self.number_of_armor_your_hero = str(randint(1, 3))

        if int(self.hp_of_your_enemy) <= 0:
            self.game.image.goblin = pygame.transform.scale(self.game.image.goblin, self.game.settings.proportions_of_goblin)
            self.game.image.knight_hero = pygame.transform.scale(self.game.image.knight_hero, self.game.settings.proportions_for_map)
            self.game.image.ent = pygame.transform.scale(self.game.image.ent, self.game.settings.proportions_for_map)
            self.game.image.slime = pygame.transform.scale(self.game.image.slime, self.game.settings.proportions_for_map)

            self.hp_of_your_hero = "100"
            self.hp_of_your_enemy = "100"
            self.armor_your_hero = "0"

            self.number_of_attak_your_hero = str(randint(1, 10))
            self.number_of_armor_your_hero = str(randint(1, 3))
        
            self.text_for_attack = self.font.render(self.number_of_attak_your_hero, True, (255, 255, 255))
            self.text_for_armor = self.font.render(self.number_of_armor_your_hero, True, (255, 255, 255))

            self.text_of_your_hp = self.font.render(self.hp_of_your_hero, True, (255, 255, 255))
            self.text_of_your_enemy_hp = self.font.render(self.hp_of_your_enemy, True, (255, 255, 255))
            self.text_armor = self.font.render(self.armor_your_hero, True, (255, 255, 255))
        
            self.hp = 300
            self.hp_enemy = 300
            if "-" not in self.game.map.map_of_forest[5] and "!" not in self.game.map.map_of_forest[1] and "*" not in self.game.map.map_of_forest[3]:
                self.game.end.end_screen()

            else:
                self.game.map.mapping_of_forest()
                self.game.start_game()
            

    def defense(self):
        self.armor_your_hero = self.number_of_armor_your_hero
        self.number_of_armor_your_hero = str(randint(1, 3))
        self.number_of_attak_your_hero = str(randint(1, 10))

    def turn_enemy(self):
        self.attack_enemy = randint(1, 5)
        
        if self.hp - self.attack_enemy <= 0:
            self.game.end.end_screen()

        elif self.attack_enemy - int(self.armor_your_hero) >= 0:
            self.hp -= self.attack_enemy * 3 - int(self.armor_your_hero)
            self.hp_of_your_hero = str(int(self.hp_of_your_hero) - self.attack_enemy)

        

    def start_fight(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.attack()
                        self.turn_enemy()
                        self.feature_update()

                    elif event.button == 3:
                        self.defense()
                        self.turn_enemy()
                        self.feature_update()

            self.draw_field(self.monstr, self.location)

            pygame.display.flip()


#t = Fight()
#t.draw_field("goblin", "forest")
#t.start_fight()
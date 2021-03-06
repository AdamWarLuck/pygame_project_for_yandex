import pygame


class Map():
    def __init__(self, game):
        self.game = game
        self.map_with_image = []
        
        self.game.image.goblin = pygame.transform.scale(self.game.image.goblin, self.game.settings.proportions_of_goblin)
        self.game.image.knight_hero = pygame.transform.scale(self.game.image.knight_hero, self.game.settings.proportions_for_map)
        self.game.image.ent = pygame.transform.scale(self.game.image.ent, self.game.settings.proportions_for_map)
        self.game.image.slime = pygame.transform.scale(self.game.image.slime, self.game.settings.proportions_for_map)

        self.start_pos_your_hero = [1, 1]

        with open('forest.txt', 'r') as f:
            self.map_of_forest = f.read().split('\n')

        self.map_of_forest = [list(i) for i in self.map_of_forest]

        self.y = 0

    def move_your_hero(self, event):
        if event.key == pygame.K_w and self.map_of_forest[self.start_pos_your_hero[1] - 1][self.start_pos_your_hero[0]] == '.':

            self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0]] = '.'
            self.map_of_forest[self.start_pos_your_hero[1] - 1][self.start_pos_your_hero[0]] = '@'
            self.start_pos_your_hero[1] -= 1

        elif event.key == pygame.K_s and self.map_of_forest[self.start_pos_your_hero[1] + 1][self.start_pos_your_hero[0]] == '.':

            self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0]] = '.'
            self.map_of_forest[self.start_pos_your_hero[1] + 1][self.start_pos_your_hero[0]] = '@'
            self.start_pos_your_hero[1] += 1

        elif event.key == pygame.K_d and self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] + 1] in ('.', "!", "*", "-"):

            if self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] + 1] == "!":

                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0]] = '.'
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] + 1] = '.'
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] + 1] = '@'
                self.start_pos_your_hero[0] += 1
               
                self.game.fight.draw_field("goblin", "forest")
                self.game.fight.start_fight()

            elif self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] + 1] == "-":

                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0]] = '.'
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] + 1] = '.'
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] + 1] = '@'
                self.start_pos_your_hero[0] += 1

                self.game.fight.draw_field("slime", "forest")
                self.game.fight.start_fight()


            elif self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] + 1] == '.':
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0]] = '.'
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] + 1] = '@'
                self.start_pos_your_hero[0] += 1

        elif event.key == pygame.K_a and self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] - 1] in ('.', "!", "*", "-"):

            if self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] - 1] == "*":

                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0]] = '.'
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] - 1] = '.'
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] - 1] = '@'
                self.start_pos_your_hero[0] -= 1

                self.game.fight.draw_field("ent", "forest")
                self.game.fight.start_fight()

            elif self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] - 1] == '.':
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0]] = '.'
                self.map_of_forest[self.start_pos_your_hero[1]][self.start_pos_your_hero[0] - 1] = '@'
                self.start_pos_your_hero[0] -= 1

    def mapping_of_forest(self):
        for i in self.map_of_forest:
            for j in range(len(i)):

                self.map_with_image.append((self.game.image.grass, (j * self.game.settings.fields_size, self.y)))

                if i[j] == '@':
                    self.map_with_image.append((self.game.image.knight_hero, (j * self.game.settings.fields_size, self.y)))

                if i[j] == '!':
                    self.map_with_image.append((self.game.image.goblin, (j * self.game.settings.fields_size, self.y)))

                if i[j] == '#':
                    self.map_with_image.append((self.game.image.tree, (j * self.game.settings.fields_size, self.y)))

                if i[j] == '*':
                    self.map_with_image.append((self.game.image.ent, (j * self.game.settings.fields_size, self.y)))

                if i[j] == '-':
                    self.map_with_image.append((self.game.image.slime, (j * self.game.settings.fields_size, self.y)))



            

                    #self.field.screen.blit(self.game.image.chest, (j * self.game.settings.field_size, self.y))

            self.y += self.game.settings.fields_size
        self.y = 0
        
        return self.map_with_image
    


            #if keys[pygame.K_f]:
                #fight()




#print(t.mapping_of_forest())
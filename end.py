import pygame
import sys


class Screen_for_end:
    def __init__(self, game):
        self.game = game

        self.screen = pygame.display.set_mode(self.game.settings.proportions_game_screen)
        self.sprite = pygame.sprite.Sprite()
        self.all_sprite = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Конечное окно')

    def end_screen(self):
        if "-" not in self.game.map.map_of_forest[5] and "!" not in self.game.map.map_of_forest[1] and "*" not in self.game.map.map_of_forest[3]:
            intro_text = ["Вы победили!!! :D",
                        "Ваше кол-во очков 1000"]

        else:
            intro_text = ["Вы проиграли :(",
                         "Ваше кол-во очков 0"]

        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

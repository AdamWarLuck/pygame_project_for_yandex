import pygame
import sys


class Screen_for_start:
    def __init__(self, game):
        self.game = game

        self.screen = pygame.display.set_mode(self.game.settings.proportions_game_screen)
        self.sprite = pygame.sprite.Sprite()
        self.all_sprite = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Начальное окно')

    def start_screen(self):
        intro_text = ["Правила игры:",
                     "Ходить на: w,a,s,d. В бою: ПКМ(правая кнопка мыши) - атака.",
                     "ЛКМ(левая кнопка мыши) - менять уровень защиты.",
                     "Хочешь начать играть нажми L",
                     "Удачи!"]
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
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

                if keys[pygame.K_l]:
                    self.game.start_game()

            pygame.display.flip()

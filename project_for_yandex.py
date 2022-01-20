import pygame


pygame.init()


def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ["ЗАСТАВКА",
                  "Правила игры"]
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


def fight():
    
    back_ground = pygame.image.load('data/forest_background.png')
    back_ground = pygame.transform.scale(back_ground, (880, 640))

    sword = pygame.image.load('data/sword_with_fire.png')
    sword = pygame.transform.scale(sword, (100, 100))
    sword.set_colorkey(sword.get_at((0, 0)))

    sword2 = pygame.image.load('data/strong_shield.png')
    sword2 = pygame.transform.scale(sword2, (100, 100))
    sword2.set_colorkey(sword2.get_at((0, 0)))

    mar = pygame.image.load('data/knight.png')
    mar = pygame.transform.scale(mar, (350, 300))
    mar.set_colorkey(mar.get_at((0, 0)))

    monstr = pygame.image.load('data/dark_knight.png')
    monstr = pygame.transform.scale(monstr, (350, 300))
    monstr.set_colorkey(monstr.get_at((0, 0)))

    #font = pygame.font.Font(None, 50)
    #text = font.render("Hello, Pygame!", True, (100, 255, 100))
    #text_x = 5
    #text_y = 6
    #text_w = text.get_width()
    #text_h = text.get_height()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return

        screen.blit(back_ground, (0, 0))
        screen.blit(mar, (10, 220))
        screen.blit(monstr, (500, 210))
        screen.blit(sword, (0, 65))
        screen.blit(sword2, (110, 65))

        #screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 300, 60), 1)

        pygame.draw.rect(screen, (0, 0, 0), (0, 65, 100, 100), 1)
        pygame.draw.rect(screen, (0, 0, 0), (110, 65, 100, 100), 1)
        #pygame.draw.rect(screen, (0, 0, 0), (0, 0, 300, 60), 1)
        
        pygame.draw.rect(screen, (255, 0, 0), (1, 1, 300, 60))
        pygame.draw.rect(screen, (255, 0, 0), (580, 0, 300, 60), 1)
        pygame.draw.rect(screen, (255, 0, 0), (580, 1, 300, 60))
        
        pygame.display.flip()




pygame.display.set_caption('Квест Арион')
WIDTH, HEIGHT = 880, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sprite = pygame.sprite.Sprite()
all_sprite = pygame.sprite.Group()
clock = pygame.time.Clock()
running = True

with open('forest.txt', 'r') as f:
    loc = f.read().split('\n')

loc = [list(i) for i in loc]

grass = pygame.image.load('data/grass.png')
grass = pygame.transform.scale(grass, (80, 80))

monstr = pygame.image.load('data/goblin.png')
monstr = pygame.transform.scale(monstr, (50, 80))
monstr.set_colorkey(monstr.get_at((0, 0)))

chest = pygame.image.load('data/chest.png')
chest = pygame.transform.scale(chest, (50, 50))
chest.set_colorkey(chest.get_at((0, 0)))

heal = pygame.image.load('data/heal.png')
heal = pygame.transform.scale(heal, (50, 50))
heal.set_colorkey(heal.get_at((0, 0)))

knight_hero = pygame.image.load('data/knight.png')
knight_hero = pygame.transform.scale(knight_hero, (80, 80))
knight_hero.set_colorkey(knight_hero.get_at((0, 0)))

box = pygame.image.load('data/tree.png')
box = pygame.transform.scale(box, (80, 80))
box.set_colorkey(box.get_at((0, 0)))

all_s = {'#': grass, '.': grass, '@': grass, "!": grass, "+": grass, "$": grass}
y = 0
size = 80
mx, my = 1, 1
start_screen()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_w] and loc[my - 1][mx] == '.':
                loc[my][mx] = '.'
                loc[my - 1][mx] = '@'
                my -= 1

            if keys[pygame.K_s] and loc[my + 1][mx] == '.':
                loc[my][mx] = '.'
                loc[my + 1][mx] = '@'
                my += 1

            if keys[pygame.K_d] and loc[my][mx + 1] == '.':
                loc[my][mx] = '.'
                loc[my][mx + 1] = '@'
                mx += 1

            if keys[pygame.K_a] and loc[my][mx - 1] == '.':
                loc[my][mx] = '.'
                loc[my][mx - 1] = '@'
                mx -= 1

            if keys[pygame.K_f]:
                fight()

    for i in loc:
        for j in range(len(i)):
            screen.blit(all_s[i[j]], (j * size, y))
            if i[j] == '@':
                screen.blit(knight_hero,(j * size, y))

            if i[j] == '!':
                screen.blit(monstr,(j * size, y))

            if i[j] == '#':
                screen.blit(box,(j * size, y))

            if i[j] == '+':
                screen.blit(heal,(j * size, y))

            if i[j] == '$':
                screen.blit(chest,(j * size, y))


        y += 80
    y = 0
    clock.tick(50)
    pygame.display.flip()
pygame.quit()

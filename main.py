import pygame, cc, cp, random
from pygame.locals import *

def draw_board(screen):
    background = pygame.Surface(screen.get_size())
    for y in range(cc.TILES):
        for x in range(cc.TILES):
            if random.randint(1,30) < 10:
                image = cc.DARK_IMAGE
            elif random.randint(1,30) < 20:
                image = cc.LIGHT_IMAGE
            else:
                image = cc.GREEN_IMAGE
            background.blit(image, (x*cc.TILE_SIZE, y*cc.TILE_SIZE))
    return background

def get_resorces():
    resources = pygame.sprite.Group()
    for row in range(cc.TILES):
            for column in range(cc.TILES):
                choice = random.choice(cc.RESOURCES)
                if choice != None:
                    item = cp.Resources(choice, 20, column, row)
                    resources.add(item)
                else:
                    pass
    return resources

def select_player(people):
    mouse_pos =  pygame.mouse.get_pos()
    for person in people:
        if person in people.get_sprites_at(mouse_pos):
            player = person
    return player

def main():
    screen = pygame.display.set_mode((cc.SCREEN_SIZE, cc.SCREEN_SIZE))
    pygame.display.set_caption('World')
    clock = pygame.time.Clock()

    person = cp.Player()
    people = pygame.sprite.Group()
    people.add(person)

    background = draw_board(screen)
    resources = get_resorces()
    ##player = people.get_sprite(0)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                player = select_player(people)
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and player.row < cc.SCREEN_SIZE - 1:
                    player.row += 1
                if event.key == K_LEFT and player.row > 0:
                    player.row -= 1
                if event.key == K_DOWN and player.column < cc.SCREEN_SIZE - 1:
                    player.column += 1
                if event.key == K_UP and player.column > 0:
                    player.column -= 1

        ##selected_resources = pygame.sprite.groupcollide(people, resources, dokill2)
        screen.blit(background, (0, 0))
        resources.draw(screen)
        people.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
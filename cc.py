import pygame, os, cp
#set up some constants

TILE_SIZE = 15
TILES = 45
OFFSET = int(7.5)
SCREEN_SIZE = TILE_SIZE * TILES
LIGHT_IMAGE = pygame.Surface((TILE_SIZE,TILE_SIZE))
LIGHT_IMAGE.fill(pygame.Color('seagreen'))
DARK_IMAGE = pygame.Surface((TILE_SIZE,TILE_SIZE))
DARK_IMAGE.fill(pygame.Color('darkgreen'))
GREEN_IMAGE = pygame.Surface((TILE_SIZE,TILE_SIZE))
GREEN_IMAGE.fill(pygame.Color('green'))

image = pygame.image.load('char.png')
image = pygame.transform.scale(image, (50, 75))

person = cp.Player(image)
people = pygame.sprite.Group()
people.add(person)


FIRE = pygame.image.load('Fire.png')
COAL = pygame.image.load('Coal.png')
FIRE = pygame.transform.scale(FIRE, (TILE_SIZE+10, TILE_SIZE+10))
COAL = pygame.transform.scale(COAL, (int(TILE_SIZE+1.25), int(TILE_SIZE+1.25)))


RESOURCES = [FIRE, COAL, None, None, None]

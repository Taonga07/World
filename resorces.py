import pygame, random

DIRT, GRASS, WATER, COAL, CLOUD, WOOD = 0, 1, 2, 3, 4, 5
FIRE, SAND, GLASS, ROCK, STONE, BRICK, DIAMOND = 6, 7, 8, 9 , 10, 11, 12
resources = [DIRT, GRASS, WATER, COAL, WOOD, FIRE, SAND, GLASS, ROCK, STONE, BRICK, DIAMOND]
WHITE = (255,255,255)
BLACK = (0,0,0)
TILESIZE = 40
MAPWIDTH = 30
MAPHEIGHT = 16

inventory = {
    DIRT: 0,
    GRASS: 0,
    WATER: 0,
    COAL: 0,
    WOOD: 0,
    FIRE: 0,
    SAND: 0,
    GLASS: 0,
    ROCK: 0,
    STONE: 0,
    BRICK: 0,
    DIAMOND: 0
}

# add controls for crafting
# these numbers correspond to
# number keys 1,2,...0, -, =
controls = {
    DIRT: 49, # 1
    GRASS: 50, # 2
    WATER: 51, # 3
    COAL: 52, # 4
    WOOD: 53, # 5
    FIRE: 54, # 6
    SAND: 55, # 7
    GLASS: 56, # 8
    ROCK: 57, # 9 
    STONE: 48, # 0
    BRICK: 45, # -
    DIAMOND: 61 # =
}

# this tells us how many or each resource
# we need to produce a more valuable resource
# so 1 stone takes 1 rock
craft = {
    STONE: {ROCK: 1},
    SAND: {ROCK: 1},
    FIRE: {WOOD: 1},
    GLASS: {FIRE: 1, SAND:1},
    DIAMOND: {WOOD:1, COAL:1},
    BRICK: {ROCK:1, FIRE:1}
}

textures = {
    DIRT: pygame.image.load('dirt.png'),
    GRASS: pygame.image.load('grass.png'),
    WATER: pygame.image.load('water.png'),
    COAL: pygame.image.load('coal.png'),
    CLOUD: pygame.image.load('cloud.png'),
    BRICK: pygame.image.load('brick.png'),
    DIAMOND: pygame.image.load('diamond.png'),
    FIRE: pygame.image.load('fire.png'),
    GLASS: pygame.image.load('glass.png'),
    ROCK: pygame.image.load('rock.png'),
    SAND: pygame.image.load('sand.png'),
    STONE: pygame.image.load('stone.png'),
    WOOD: pygame.image.load('wood.png')
}

player = pygame.image.load('char.png')
playerPos = [0,0]

tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
for row in range(MAPHEIGHT):
    for col in range(MAPWIDTH):
        rn = random.randint(0,15)
        if rn == 0:
            tile = COAL
        elif rn in [1, 2]:
            tile = WATER
        elif rn in [3,4,5,6,7]:
            tile = GRASS
        elif rn in [7,8,9]:
            tile = WOOD
        elif rn in [9,10,11]:
            tile = ROCK
        else:
            tile = DIRT
        tilemap[row][col] = tile
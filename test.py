from pygame.locals import *
import pygame, random, sys
from resorces import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE+50))
INVFONT = pygame.font.Font('freesansbold.ttf', 18)

while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:
                playerPos[0] += 1
            if event.key == K_LEFT and playerPos[0] > 0:
                playerPos[0] -= 1
            if event.key == K_DOWN and playerPos[1] < MAPHEIGHT - 1:
                playerPos[1] += 1
            if event.key == K_UP and playerPos[1] > 0:
                playerPos[1] -= 1
            if event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT
            # we go through all our number keys
            for key in controls:
                # if one was pressed by the player
                if event.key == controls[key]:
                    # if the mouse key was pressed in addition
                    if pygame.mouse.get_pressed()[0]:
                        # if this is a craftable resource
                        if key in craft:
                            # check that we have enough 
                            # ingredients to make the resource
                            canBeMade = True
                            for i in craft[key]:
                                if craft[key][i] > inventory[i]:
                                    canBeMade = False
                                    break
                            # if we can make the resource
                            # craft it and add it to our
                            # inventory
                            if canBeMade == True:
                                for i in craft[key]:
                                    inventory[i] -= craft[key][i]
                                inventory[key] += 1
                    # if no mouse key was pressed
                    # place this resource on the gorund
                    # and grab whatever is currently there
                    # into our inventory
                    else:
                        currentTile = tilemap[playerPos[1]][playerPos[0]]
                        if inventory[key] > 0:
                            inventory[key] -= 1
                            inventory[currentTile] += 1
                            tilemap[playerPos[1]][playerPos[0]] = key

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))

    placePosition = 10
    for item in resources:
        DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT*TILESIZE+20))
        placePosition += 30
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 50

    DISPLAYSURF.blit(player,(playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))
    pygame.display.update()
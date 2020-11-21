import pygame, math, cc

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, column, row):
        pygame.sprite.Sprite.__init__(self) 
        self.image = image
        self.row = row
        self.column = column
        self.rect = self.image.get_rect()

class Player(GameObject):
        def __init__(self, image):
            super().__init__(image, 0, 0)
            self.player = False

class Resources(GameObject):
        def __init__(self, image, amount, column, row):
            super().__init__(image, column, row)
            self.rect.top = cr_to_win(column)
            self.rect.left = cr_to_win(row)
            self.amount = amount

def cr_to_win(num):
    return (num * cc.TILE_SIZE) + cc.OFFSET
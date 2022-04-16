import pygame

class Ship:
    #Ship management class
    def __init__(self, ai_game):
        #Initialize ship and set starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Apply settings
        self.settings = ai_game.settings

        #Load ship image, scale it and get its rectangle
        self.image = pygame.transform.scale(pygame.image.load('images/ship.png'), (self.settings.ship_size, self.settings.ship_size))
        self.rect = self.image.get_rect()

        #Start each ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store decimal value for ship's X position
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        #Center ship on screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        #Update ship position based on movement flag
        #Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        #Draw ship at current location
        self.screen.blit(self.image, self.rect)

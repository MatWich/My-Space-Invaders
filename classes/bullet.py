import config
import pygame

class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def offScreen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return config.collide(self, obj)


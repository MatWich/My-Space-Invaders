import pygame
import config
from classes.ship import Ship

class Player(Ship):
    def __init__(self,x, y, health=100):
        super(Player, self).__init__(x, y, health)  #from Ship class
        self.shipImg = config.OUR_SHIP
        self.bulletImg = config.SHIP_BULLET
        self.mask = pygame.mask.from_surface(self.shipImg)  # mowi gdzie znajduja sie pixele
        self.health = health
        self.maxHealth = health

    def moveBullets(self, vel, objects):
        self.coolDown()
        for b in self.bullets:
            b.move(-vel)
            if b.offScreen(config.HEIGHT):
                self.bullets.remove(b)
            else:
                for obj in objects:
                    if b.collision(obj):
                        objects.remove(obj)
                        self.bullets.remove(b)
                        if b in self.bullets:
                            self.bullets.remove(b)

    def healthBar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.shipImg.get_height() + 10, self.shipImg.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0),(self.x, self.y + self.shipImg.get_height() + 10, self.shipImg.get_width() * (self.health/self.maxHealth), 10))

    def draw(self, window):
        super().draw(window)
        self.healthBar(window)



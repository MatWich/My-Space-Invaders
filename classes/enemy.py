import config
import pygame
from classes.ship import Ship
from classes.bullet import Bullet

class Enemy(Ship):
    COLOR_MAP = {
                "red1": (config.RED_ALIENS[0], config.RED_BULLET),
                "red2": (config.RED_ALIENS[1], config.RED_BULLET),
                "red3": (config.RED_ALIENS[2], config.RED_BULLET),
                "blue1": (config.BLUE_ALIENS[0], config.BLUE_BULLET),
                "blue2": (config.BLUE_ALIENS[1], config.BLUE_BULLET),
                "blue3": (config.BLUE_ALIENS[2], config.BLUE_BULLET),
                "yellow1": (config.YELLOW_ALIENS[0], config.YELLOW_BULLET),
                "yellow2": (config.YELLOW_ALIENS[1], config.YELLOW_BULLET),
                "yellow3": (config.YELLOW_ALIENS[2], config.YELLOW_BULLET),
                "very1": (config.VERY_ALIENS[0], config.GREEN_BULLET),
                "cool": (config.VERY_ALIENS[1], config.GREEN_BULLET),
                "green2": (config.GREEN_ALIENS[0], config.GREEN_BULLET),
                "green3": (config.GREEN_ALIENS[1], config.GREEN_BULLET)

    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.shipImg, self.bulletImg = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.shipImg)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.coolDownCounter == 0:
            bullet = Bullet(self.x, self.y, self.bulletImg)
            self.bullets.append(bullet)
            self.coolDownCounter = 1
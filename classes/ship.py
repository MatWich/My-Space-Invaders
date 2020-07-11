import config
from classes.bullet import Bullet

# Abstract class
class Ship:
    COOLDOWN = config.FPS / 2   #Pol sekundy bo FPS=60 mozna zmienic w configu

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.shipImg = None
        self.bulletImg = None
        self.bullets = []
        self.coolDownCounter = 0

    def draw(self, window):
        window.blit(self.shipImg, (self.x, self.y))
        for b in self.bullets:
            b.draw(window)

    def moveBullets(self, vel, object):
        self.coolDown()

        for b in self.bullets:
            b.move(vel)

            if b.offScreen(config.HEIGHT):
                self.bullets.remove(b)

            elif b.collision(object):
                object.health -= 10
                self.bullets.remove(b)

    def getWidth(self):
        return self.shipImg.get_width()

    def getHeight(self):
        return self.shipImg.get_height()

    def coolDown(self):
        if self.coolDownCounter >= self.COOLDOWN:
            self.coolDownCounter = 0

        elif self.coolDownCounter > 0:
            self.coolDownCounter += 1

    def shoot(self):
        if self.coolDownCounter == 0:
            bullet = Bullet(self.x , self.y, self.bulletImg)
            self.bullets.append(bullet)
            self.coolDownCounter = 1

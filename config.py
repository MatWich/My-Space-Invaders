import pygame
import os
import random

# SCREEN SIZE
WIDTH, HEIGHT = 750, 750
SCREEN_SIZE = (WIDTH, HEIGHT)

# GAME VARIABLES
FPS = 60

# COLORS
BLACK = (0, 0, 0)

# FONTS
pygame.font.init()
mainFont = pygame.font.SysFont("comicsans", 50)
lostFont = pygame.font.SysFont("comicsans", 60)
menuFont = pygame.font.SysFont("comicsans", 70)

# LABELS
menuLabel = menuFont.render("press the mouse to begin... ", 1, (255, 255 ,0))

# ALL KEYS FOR DICT VARIABLE IN Enemy class
enemyColor = ["red1", "red2", "red3", "blue1", "blue2", "blue3", "yellow1", "yellow2", "yellow3", "very1", "cool", "green2", "green3"]

'''LOADING IMAGES'''

# BACKGROUND
BG = pygame.transform.scale(pygame.image.load("images/background.png"), (WIDTH, HEIGHT))        # Rozszerze na cale okno

# ENEMY SHIPS
RED_ALIENS = []
BLUE_ALIENS = []
YELLOW_ALIENS = []

VERY_ALIENS = [pygame.image.load("images/very_alien/Aqua_invader1.png"), pygame.image.load(os.path.join("images/very_alien", "cooler_invader.png"))]
GREEN_ALIENS = [pygame.image.load("images/very_alien/green_invader2.png"), pygame.image.load("images/very_alien/green_invader3.png")]
for x in range(1, 4):
    # LOADING IMAGES
    redImage = pygame.image.load("images/red_alien/red_invader" + str(x) + ".png")
    blueImage = pygame.image.load("images/blue_alien/blue_invader" + str(x) + ".png")
    yellowImage = pygame.image.load("images/yellow_alien/yellow_invader" + str(x) + ".png")

    # APPENDING IMAGES TO THE LISTS
    RED_ALIENS.append(redImage)
    BLUE_ALIENS.append(blueImage)
    YELLOW_ALIENS.append(yellowImage)

# BULLETS
RED_BULLET = pygame.image.load("images/bullets/rocket.png")
YELLOW_BULLET = pygame.image.load("images/bullets/yellow_bullet.png")
GREEN_BULLET = pygame.image.load("images/bullets/green_bullet.png")
BLUE_BULLET = pygame.image.load("images/bullets/blue_bullet.png")
SHIP_BULLET = pygame.image.load("images/bullets/bullet_ship.png")

# MAIN SHIP
shipChoice=random.randrange(0, 3)
SHIP_IMGs = [pygame.image.load("images/ship/ship1.png"), pygame.image.load("images/ship/ship2.png"), pygame.image.load("images/ship/ship3.png")]
OUR_SHIP = SHIP_IMGs[shipChoice]

'''END LOADING IMAGES'''

# FUNCTION TO MAKE OUR pygame.mask WORKS PROPERLY
def collide(object1, object2):
    offsetX = object2.x - object1.x
    offsetY = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offsetX, offsetY)) != None
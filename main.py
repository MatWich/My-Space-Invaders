import pygame
pygame.font.init()

WIDTH, HEIGHT = 750, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Space Invaders")

# COLORS
BLACK = (0, 0, 0)
# BACKGROUND
BG = pygame.transform.scale(pygame.image.load("images/background.png"), (WIDTH, HEIGHT))
# ENEMY SHIPS
RED_ALIENS = []
BLUE_ALIENS = []
YELLOW_ALIENS = []
for x in range(1, 3):
    # LOADING IMAGES
    redImage = pygame.image.load("images/red_alien/red_invader" + str(x) + ".png")
    blueImage = pygame.image.load("images/blue_alien/blue_invader" + str(x) + ".png")
    yellowImage = pygame.image.load("images/yellow_alien/yellow_invader" + str(x) + ".png")

    # APPENDING IMAGES TO THE LISTS
    RED_ALIENS.append(redImage)
    BLUE_ALIENS.append(blueImage)
    YELLOW_ALIENS.append(yellowImage)


# MAIN SHIP
OUR_SHIP = [pygame.image.load("images/ship/ship1.png")]


screen.fill(BLACK)
screen.blit(OUR_SHIP[0], (200, 40))
pygame.display.update()

# MainLoop
run = True
while run:
    screen.blit(BG, (0, 0))
    screen.blit(RED_ALIENS[0], (200, 40))
    pygame.display.update()


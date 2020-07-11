import pygame
import random
import secrets
import config
from classes.player import Player
from classes.enemy import Enemy
from classes.bullet import Bullet

pygame.init()
# SCREEN
screen = pygame.display.set_mode(config.SCREEN_SIZE)
pygame.display.set_caption("My Space Invaders")

def main():
    run = True
    lost = False
    lives = 5
    level = 0
    lostCount = 0

    bulletSpeed = 4

    enemyVel = 1
    enemies = []
    waveLenght = 5

    playerVel = 5

    # SET UP PLAYER COORDS
    player = Player(375, 630)

    clock = pygame.time.Clock()

    def redrawWindow():
        screen.blit(config.BG, (0, 0))
        # TEXTs
        livesLabel = config.mainFont.render(f"Lives: {lives}", 1, (255, 255, 255))
        levelLabel = config.mainFont.render(f"Level: {level}", 1, (255, 255, 255))
        # Draw lives left
        screen.blit(livesLabel, (10, 10))
        # Draw score
        screen.blit(levelLabel, (config.WIDTH - levelLabel.get_width() - 10, 10))

        # draw enemies
        for enemy in enemies:
            enemy.draw(screen)
        # draw player
        player.draw(screen)

        if lost:
            lostLabel = config.lostFont.render("You Lost!!!", 1, (255, 0, 0))
            screen.blit(lostLabel, (config.WIDTH/2, 350))
        # update window
        pygame.display.update()

    # MainLoop
    while run:
        clock.tick(config.FPS)
        redrawWindow()

        if lives <= 0 or player.health <= 0:
            lost = True
            lostCount += 1

        if lost:
            if lostCount > config.FPS * 5:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            waveLenght += 5

            for i in range(waveLenght):
                enemy = Enemy(random.randrange(50, config.WIDTH - 100), random.randrange(-1500, -100), secrets.choice(config.enemyColor))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # it will recognize more than 1 action
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x + playerVel > 0:
            player.x -= playerVel
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + playerVel + player.getWidth() < config.WIDTH:
            player.x += playerVel
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - playerVel > 0:
            player.y -= playerVel
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + playerVel + player.getHeight() + 15 < config.HEIGHT:
            player.y += playerVel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemyVel)
            enemy.moveBullets(bulletSpeed, player)

            # SZANSA ZE STRZELI
            if random.randrange(0, 4 * config.FPS) == 1:
                enemy.shoot()

            # SPRAWDZA CZY TRAFILO GRACZA
            if config.collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            # JESLI INVADER PRZEJDZIE PRZEZ CALA WYSOKOSC OKNA TO GRACZ TRACI ZYCIE
            elif enemy.y + enemy.getHeight() > config.HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.moveBullets(bulletSpeed, enemies)

def menu():

    run = True
    while run:

        screen.blit(config.BG, (0, 0))
        screen.blit(config.menuLabel, (config.WIDTH / 2 - config.menuLabel.get_width()/2, 350))
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

if __name__ == '__main__':
    menu()



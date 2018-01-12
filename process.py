import pygame
from random import randint
from classes import *

def process(player, FPS, totalframes):
    Inputs(player)
    spawn(FPS, totalframes)
    collision()

def Inputs(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_e:
                Projectile.proj_fire = not Projectile.proj_fire

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if player.velX != -5:
            player.velX = -5
            player.going_right = False
            player.image = pygame.image.load("images/player.png")
            player.image = pygame.transform.flip(player.image, True, False)
    elif keys[pygame.K_d]:
        if player.velX != 5:
            player.going_right = True
            player.velX = 5
            player.image = pygame.image.load("images/player.png")
    else:
        player.velX = 0

    if keys[pygame.K_w]:
        player.jumping = True

    if keys[pygame.K_SPACE]:# and player.timer == player.timeTarget:
        #player.timer = 0
        def direction(proj):
            if player.going_right:
                proj.velX = 9
            else:
                proj.velX = -9
                proj.image = pygame.transform.flip(proj.image, True, False)
        if Projectile.proj_fire:
            proj = Projectile(player.rect.x, player.rect.y, 'images/fire.png', True)
        else:
            proj = Projectile(player.rect.x, player.rect.y, 'images/frost.png', False)
        direction(proj)

def spawn(FPS, tf):
    rX = randint(1,2)
    x = 600
    if rX == 1:
        x = 1
    if tf % FPS  == 0:
        Enemy(x, 100, 'images/bat.png')
def collision():
    for enemy in Enemy.List:
        proj = pygame.sprite.spritecollide(enemy, Projectile.List, True)
        for proj in proj:
            enemy.health = 0
            if proj.fire:
                if enemy.velX > 0:
                    enemy.image = pygame.image.load("images/burned_bat.png")
                elif enemy.velX < 0:
                    enemy.image = pygame.image.load("images/burned_bat.png")
                    enemy.image = pygame.transform.flip(enemy.image, True, False)
            else:
                if enemy.velX > 0:
                    enemy.image = pygame.image.load("images/frozen_bat.png")
                elif enemy.velX < 0:
                    enemy.image = pygame.image.load("images/frozen_bat.png")
                    enemy.image = pygame.transform.flip(enemy.image, True, False)

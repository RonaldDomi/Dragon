import pygame, os
from process import process
from classes import *

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

ScreenWidth, ScreenHeight = 640, 480
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

player = Player(100, ScreenHeight - 40, 'images/player.png')
enemy = Enemy(100, 100, 'images/bat.png')
background = pygame.image.load('images/background.png')

clock = pygame.time.Clock()
FPS = 24
total_frames = 0


while True:
    total_frames += 1
    process(player, FPS, total_frames)

    screen.blit(background, (0,0))
    #screen.fill((0,0,0))

    Projectile.List.draw(screen)
    BaseClass.allSpritesList.draw(screen)

    #player.timeProjectile()
    player.motion(ScreenWidth, ScreenHeight)
    enemy.motion(ScreenWidth, ScreenHeight)
    Projectile.motion(ScreenWidth)

    clock.tick(FPS)
    pygame.display.flip()
#end
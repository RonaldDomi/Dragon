import pygame, math
from random import randint

class BaseClass(pygame.sprite.Sprite):
    allSpritesList = pygame.sprite.Group()

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allSpritesList.add(self)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(BaseClass):

    def __init__(self, x, y, image):
        BaseClass.__init__(self, x, y, image)
        self.going_right = True
        self.velY = 40
        self.velX = 0
        self.jumping = False
        self.reset = False
        self.timer = 7
        self.timeTarget = 7

    # def timeProjectile(self):
    #     if self.timer < self.timeTarget:
    #         self.timer+=1

    def motion(self, ScreenWidth, ScreenHeight):
        self.rect.x += self.velX

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x + self.rect.width > ScreenWidth:
            self.rect.x = ScreenWidth - self.rect.width

        if self.jumping:
            if not self.reset:
                self.rect.y -= self.velY
                self.velY -= 2
                if self.rect.y + self.rect.height >= ScreenHeight:
                    self.rect.y = ScreenHeight - self.rect.height
                    self.jumping = False
                    self.reset = True
            else:
                self.velY = 40
                self.reset = False


class Enemy(BaseClass):
    List = pygame.sprite.Group()

    def __init__(self, x, y, image):
        BaseClass.__init__(self, x, y, image)
        Enemy.List.add(self)
        self.velY = 2
        self.velX = 7
        self.health = 1
        self.amplitude, self.period = randint(20, 140), randint(4, 5) / 100.0
    @staticmethod
    def motion(ScreenWidth, ScreenHeight):
        for enemy in Enemy.List:
            if enemy.health == 0:
                enemy.velX = 0
                if enemy.rect.y + enemy.rect.height < ScreenHeight:
                    enemy.rect.y += enemy.velY
            else:
                enemy.rect.x += enemy.velX
                if enemy.rect.x < 0 or enemy.rect.x + enemy.rect.height > ScreenWidth:
                    enemy.velX = -enemy.velX
                    enemy.image = pygame.transform.flip(enemy.image, True, False)
                enemy.rect.y = enemy.amplitude * math.sin(enemy.period * enemy.rect.x) + 140

class Projectile(pygame.sprite.Sprite):
    List = pygame.sprite.Group()
    proj_list = []
    proj_fire = True

    def __init__(self, x, y, image, isFire):
        pygame.sprite.Sprite.__init__(self)
        self.fire = isFire
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if len(Projectile.proj_list) != 0:
            last_element = Projectile.proj_list[-1]
            differenceX =  abs(last_element.rect.x - self.rect.x) - 20
            differenceY =  abs(last_element.rect.y - self.rect.y) - 20
            if differenceX < self.rect.width and differenceY < self.rect.height:
                return

        self.velX = 10
        Projectile.proj_list.append(self)
        Projectile.List.add(self)
    @staticmethod
    def motion(ScreenWidth):
        for proj in Projectile.List:
            proj.rect.x += proj.velX
            if proj.rect.x < 0 or proj.rect.x + proj.rect.width > ScreenWidth:
                Projectile.List.remove(proj)
                del(proj)

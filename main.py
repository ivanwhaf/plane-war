import os
import sys
import random
import pygame as pg

FPS = 30  # FPS
FIRE_RATE = 10  # 开火速率

HERO_SPEED = 10  # 英雄移动速度
ENEMY0_SPEED = 3  # 敌人0移动速度
ENEMY1_SPEED = 2  # 敌人1移动速度
ENEMY2_SPEED = 1  # 敌人2移动速度

ENEMY0_GEN_RATE = 30  # 敌人0生成速率
ENEMY1_GEN_RATE = 10  # 敌人1生成速率
ENEMY2_GEN_RATE = 10  # 敌人2生成速率

ENEMY0_FIRE_RATE = 6  # 敌人0开火速率
ENEMY1_FIRE_RATE = 6  # 敌人1开火速率
ENEMY2_FIRE_RATE = 6  # 敌人2开火速率


class Hero():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = HERO_SPEED
        self.hp = 2


class Bullet0():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 5
        self.damage = 1


class Bullet1():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 5
        self.damage = 2


class Bullet2():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 5
        self.damage = 4


class Enemy0():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = ENEMY0_SPEED
        self.hp = 1


class Enemy1():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = ENEMY1_SPEED
        self.hp = 10


class Enemy2():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = ENEMY2_SPEED
        self.hp = 30


def main():
    pg.init()

    # 加载静态图片
    background = pg.image.load('resources/background.png')
    hero_img = pg.image.load('resources/hero.png')
    bullet0_img = pg.image.load('resources/bullet0.png')
    bullet1_img = pg.image.load('resources/bullet1.png')
    bullet2_img = pg.image.load('resources/bullet2.png')
    enemy0_img = pg.image.load('resources/enemy0.png')
    enemy1_img = pg.image.load('resources/enemy1.png')
    enemy2_img = pg.image.load('resources/enemy2.png')

    size = width, height = 480, 852  # 屏幕大小
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Plane War")  # 设置标题

    clock = pg.time.Clock()
    run = True
    pause = False
    hero = Hero(240, 788, 100, 124)
    # pg.key.set_repeat(10, 15)

    bullets = []
    enemys = []
    accum_fire = 0

    # 主循环
    while run:
        clock.tick(FPS)  # 设置fps
        if pause:
            continue

        key_pressed = pg.key.get_pressed()  # 获取已经按下的按键信息
        # 上方向键按下状态
        if key_pressed[pg.K_UP]:
            hero.y -= hero.speed
            if hero.y < 0+hero.h/2:
                hero.y = int(0+hero.h/2)

        # 下方向键按下状态
        if key_pressed[pg.K_DOWN]:
            hero.y += hero.speed
            if hero.y > 852-hero.h/2:
                hero.y = int(852-hero.h/2)

        # 左方向键按下状态
        if key_pressed[pg.K_LEFT]:
            hero.x -= hero.speed
            if hero.x < 0+hero.w/2:
                hero.x = int(0+hero.w/2)

        # 右方向键按下状态
        if key_pressed[pg.K_RIGHT]:
            hero.x += hero.speed
            if hero.x > 480-hero.w/2:
                hero.x = int(480-hero.w/2)

        # 空格键按下状态
        accum_fire += 1
        if key_pressed[pg.K_SPACE] and accum_fire > FPS/FIRE_RATE:
            accum_fire = 0
            bullet0 = Bullet0(hero.x, int(hero.y-hero.h/2-22/2), 22, 22)
            bullets.append(bullet0)

        # 获取游戏中的事件
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:  # 按 p 键暂停和继续
                    pause = not pause
            elif event.type == pg.QUIT:   # 如果检测到关闭窗口事件
                run = False

        # 按概率生成敌人0
        if random.random() < (1/FPS)*(0.01*ENEMY0_GEN_RATE):
            enemy0 = Enemy0(random.randint(
                int(0+51/2), int(480-51/2)), int(0-39/2), 51, 39)
            enemys.append(enemy0)
        # 按概率生成敌人1
        if random.random() < (1/FPS)*(0.01*ENEMY1_GEN_RATE):
            enemy1 = Enemy1(random.randint(
                int(0+69/2), int(480-69/2)), int(0-89/2), 69, 89)
            enemys.append(enemy1)
        # 按概率生成敌人2
        if random.random() < (1/FPS)*(0.01*ENEMY2_GEN_RATE):
            enemy2 = Enemy2(random.randint(
                int(0+165/2), int(480-165/2)), int(0-246/2), 165, 246)
            enemys.append(enemy2)

        screen.blit(background, (0, 0))  # 绘制背景图

        # 更新玩家信息
        if hero.hp <= 0:
            print('hero dead')
        screen.blit(hero_img, (int(hero.x-hero.w/2),
                               int(hero.y-hero.h/2)))  # 绘制玩家英雄
        # 碰撞检测

        # 更新敌人信息
        for enemy in enemys:
            if enemy.y > 852+enemy.h/2:
                enemys.remove(enemy)
                continue

            if isinstance(enemy, Enemy0):
                if enemy.hp <= 0:
                    enemys.remove(enemy)
                    continue
                # 发射子弹的概率
                if random.random() < (1/FPS)*(0.1*ENEMY0_FIRE_RATE):
                    bullet1 = Bullet1(enemy.x, int(enemy.y+enemy.h/2), 9, 21)
                    bullets.append(bullet1)

                screen.blit(enemy0_img, (int(enemy.x-enemy.w/2),
                                         int(enemy.y-enemy.h/2)))  # 绘制敌人0
                enemy.y += enemy.speed

            if isinstance(enemy, Enemy1):
                if enemy.hp <= 0:
                    enemys.remove(enemy)
                    continue
                # 发射子弹的概率
                if random.random() < (1/FPS)*(0.1*ENEMY1_FIRE_RATE):
                    bullet2 = Bullet2(enemy.x, int(enemy.y+enemy.h/2), 9, 21)
                    bullets.append(bullet2)

                screen.blit(enemy1_img, (int(enemy.x-enemy.w/2),
                                         int(enemy.y-enemy.h/2)))  # 绘制敌人1
                enemy.y += enemy.speed

            if isinstance(enemy, Enemy2):
                if enemy.hp <= 0:
                    enemys.remove(enemy)
                    continue
                # 发射子弹的概率
                if random.random() < (1/FPS)*(0.1*ENEMY2_FIRE_RATE):
                    bullet2 = Bullet2(enemy.x, int(enemy.y+enemy.h/2), 9, 21)
                    bullets.append(bullet2)

                screen.blit(enemy2_img, (int(enemy.x-enemy.w/2),
                                         int(enemy.y-enemy.h/2)))  # 绘制敌人2
                enemy.y += enemy.speed

        # 更新子弹信息
        for bullet in bullets:
            # 检测是子弹否超出边界
            if bullet.y == 0 or bullet.y == 852:
                bullets.remove(bullet)
                continue

            # 玩家发出的子弹
            if isinstance(bullet, Bullet0):
                # 碰撞检测
                for enemy in enemys:
                    if bullet.x >= enemy.x-enemy.w/2 and bullet.x <= enemy.x+enemy.w/2:
                        if bullet.y >= enemy.y-enemy.h/2 and bullet.y <= enemy.y+enemy.h/2:
                            enemy.hp -= bullet.damage
                            bullets.remove(bullet)
                            break

                screen.blit(bullet0_img, (int(bullet.x-bullet.w/2),
                                          int(bullet.y-bullet.h/2)))  # 绘制子弹
                bullet.y -= bullet.speed

            # 敌人发出的类型1子弹
            elif isinstance(bullet, Bullet1):
                # 碰撞检测
                if bullet.x >= hero.x-hero.w/2 and bullet.x <= hero.x+hero.w/2:
                    if bullet.y >= hero.y-hero.h/2 and bullet.y <= hero.y+hero.h/2:
                        hero.hp -= bullet.damage
                        bullets.remove(bullet)
                        break
                screen.blit(bullet1_img, (int(bullet.x-bullet.w/2),
                                          int(bullet.y-bullet.h/2)))  # 绘制子弹
                bullet.y += bullet.speed

            # 敌人发出的类型2子弹
            elif isinstance(bullet, Bullet2):
                # 碰撞检测
                if bullet.x >= hero.x-hero.w/2 and bullet.x <= hero.x+hero.w/2:
                    if bullet.y >= hero.y-hero.h/2 and bullet.y <= hero.y+hero.h/2:
                        hero.hp -= bullet.damage
                        bullets.remove(bullet)
                        break
                screen.blit(bullet2_img, (int(bullet.x-bullet.w/2),
                                          int(bullet.y-bullet.h/2)))  # 绘制子弹
                bullet.y += bullet.speed

        pg.display.update()  # 更新屏幕

    pg.quit()


if __name__ == "__main__":
    main()

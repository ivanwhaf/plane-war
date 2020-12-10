import os
import sys
import random
import pygame as pg
import pygame.freetype

FPS = 30  # FPS
FIRE_RATE = 8  # 开火速率

HERO_HP = 100  # 玩家初始生命值
ENEMY0_HP = 1  # 敌人0初始生命值
ENEMY1_HP = 10  # 敌人1初始生命值
ENEMY2_HP = 30  # 敌人2初始生命值

HERO_SPEED = 10  # 玩家移动速度
ENEMY0_SPEED = 3  # 敌人0移动速度
ENEMY1_SPEED = 2  # 敌人1移动速度
ENEMY2_SPEED = 1  # 敌人2移动速度

ENEMY0_GEN_RATE = 25  # 敌人0生成速率
ENEMY1_GEN_RATE = 8  # 敌人1生成速率
ENEMY2_GEN_RATE = 2  # 敌人2生成速率

ENEMY0_FIRE_RATE = 5  # 敌人0开火速率
ENEMY1_FIRE_RATE = 2  # 敌人1开火速率
ENEMY2_FIRE_RATE = 2  # 敌人2开火速率-

BULLET0_DAMAGE = 1  # 子弹0伤害
BULLET1_DAMAGE = 1  # 子弹1伤害
BULLET2_DAMAGE = 2  # 子弹2伤害

BULLET0_SPEED = 4  # 子弹0飞行速度
BULLET1_SPEED = 4  # 子弹1飞行速度
BULLET2_SPEED = 4  # 子弹2飞行速度

BOMB0_GEN_RATE = 5  # 炸药0生成速率
BOMB1_GEN_RATE = 1  # 炸药1生成速率
BOMB2_GEN_RATE = 1  # 炸药2生成速率


class Hero():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = HERO_SPEED
        self.hp = HERO_HP
        self.bomb0_count = 0
        self.bomb1_count = 0
        self.bomb2_count = 0
        self.dead = False
        self.dead_fram_count = 0


class Bullet0():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = BULLET0_SPEED
        self.damage = BULLET0_DAMAGE


class Bullet1():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = BULLET1_SPEED
        self.damage = BULLET1_DAMAGE


class Bullet2():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = BULLET2_SPEED
        self.damage = BULLET2_DAMAGE


class Enemy0():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = ENEMY0_SPEED
        self.hp = ENEMY0_HP
        self.dead_fram_count = 0


class Enemy1():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = ENEMY1_SPEED
        self.hp = ENEMY1_HP
        self.dead_fram_count = 0


class Enemy2():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = ENEMY2_SPEED
        self.hp = ENEMY2_HP
        self.dead_fram_count = 0


class Bomb0():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 4


class Bomb1():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 4


def main():
    pg.init()

    # 加载静态图片
    background = pg.image.load('resources/background.png')
    hero_img = pg.image.load('resources/hero.png')
    hero_destroy1_img = pg.image.load('resources/hero_destroy1.png')
    hero_destroy2_img = pg.image.load('resources/hero_destroy2.png')
    hero_destroy3_img = pg.image.load('resources/hero_destroy3.png')
    hero_destroy4_img = pg.image.load('resources/hero_destroy4.png')

    bullet0_img = pg.image.load('resources/bullet0.png')
    bullet1_img = pg.image.load('resources/bullet1.png')
    bullet2_img = pg.image.load('resources/bullet2.png')
    enemy0_img = pg.image.load('resources/enemy0.png')

    enemy0_destroy1_img = pg.image.load('resources/enemy0_destroy1.png')
    enemy0_destroy2_img = pg.image.load('resources/enemy0_destroy2.png')
    enemy0_destroy3_img = pg.image.load('resources/enemy0_destroy3.png')
    enemy0_destroy4_img = pg.image.load('resources/enemy0_destroy4.png')

    enemy1_img = pg.image.load('resources/enemy1.png')
    enemy1_hit_img = pg.image.load('resources/enemy1_hit.png')
    enemy1_destroy1_img = pg.image.load('resources/enemy1_destroy1.png')
    enemy1_destroy2_img = pg.image.load('resources/enemy1_destroy2.png')
    enemy1_destroy3_img = pg.image.load('resources/enemy1_destroy3.png')
    enemy1_destroy4_img = pg.image.load('resources/enemy1_destroy4.png')

    enemy2_img = pg.image.load('resources/enemy2.png')
    enemy2__hit_img = pg.image.load('resources/enemy2_hit.png')
    enemy2_destroy1_img = pg.image.load('resources/enemy2_destroy1.png')
    enemy2_destroy2_img = pg.image.load('resources/enemy2_destroy2.png')
    enemy2_destroy3_img = pg.image.load('resources/enemy2_destroy3.png')
    enemy2_destroy4_img = pg.image.load('resources/enemy2_destroy4.png')
    enemy2_destroy5_img = pg.image.load('resources/enemy2_destroy5.png')
    enemy2_destroy6_img = pg.image.load('resources/enemy2_destroy6.png')

    bomb0_img = pg.image.load('resources/bomb0.png')
    bomb1_img = pg.image.load('resources/bomb1.png')

    game_pause_np_img = pg.image.load('resources/game_pause_nopressed.png')
    game_pause_p_img = pg.image.load('resources/game_pause_pressed.png')
    game_resume_np_img = pg.image.load('resources/game_resume_nopressed.png')
    game_resume_p_img = pg.image.load('resources/game_resume_pressed.png')

    size = width, height = 480, 852  # 屏幕大小
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Plane War")  # 设置标题

    clock = pg.time.Clock()
    run = True
    pause = False
    hero = Hero(240, 788, 100, 124)
    # pg.key.set_repeat(10, 15)

    score = 0
    bullets = []
    enemys = []
    bombs = []
    accum_fire = 0

    # 主循环
    while run:
        clock.tick(FPS)  # 设置fps

        # 获取游戏中的事件
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:  # 按 P 键暂停和继续
                    pause = not pause
            elif event.type == pg.QUIT:   # 检测到关闭窗口事件
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pg.mouse.get_pos()  # 按钮检测
                if 430 < x < 430+42 and 800 < y < 800+45:
                    pause = not pause

        # 判断pause值并绘制背景图必须在按钮检测之后
        if not pause:
            screen.blit(background, (0, 0))  # 绘制背景图

        # 绘制按钮
        pg.draw.rect(screen, (190, 190, 190), (430, 800, 45, 45), 0)
        # if not pause:
        #     screen.blit(game_pause_np_img, (430, 800))  # 绘制暂停按下按钮
        # else:
        #     screen.blit(game_resume_np_img, (430, 800))  # 绘制暂停按下按钮
        x, y = pg.mouse.get_pos()
        if 430 < x < 430+42 and 800 < y < 800+45:
            if pause == False:
                screen.blit(game_pause_p_img, (430, 800))  # 绘制暂停按下按钮
            else:
                screen.blit(game_resume_p_img, (430, 800))  # 绘制开始按下按钮
        else:
            if pause == False:
                screen.blit(game_pause_np_img, (430, 800))  # 绘制暂停没按下按钮
            else:
                screen.blit(game_resume_np_img, (430, 800))  # 绘制开始没按下按钮

        # 暂停状态则不更新游戏信息
        if pause:
            pg.display.update()  # 还是要刷新一下屏幕更新按钮变化
            continue

        if hero.hp > 0:
            key_pressed = pg.key.get_pressed()  # 获取已经按下的按键信息
            # 上方向键为按下状态
            if key_pressed[pg.K_UP]:
                hero.y -= hero.speed
                if hero.y < 0+hero.h/2:
                    hero.y = int(0+hero.h/2)

            # 下方向键为按下状态
            if key_pressed[pg.K_DOWN]:
                hero.y += hero.speed
                if hero.y > 852-hero.h/2:
                    hero.y = int(852-hero.h/2)

            # 左方向键为按下状态
            if key_pressed[pg.K_LEFT]:
                hero.x -= hero.speed
                if hero.x < 0+hero.w/2:
                    hero.x = int(0+hero.w/2)

            # 右方向键为按下状态
            if key_pressed[pg.K_RIGHT]:
                hero.x += hero.speed
                if hero.x > 480-hero.w/2:
                    hero.x = int(480-hero.w/2)

            # 空格键为按下状态
            accum_fire += 1
            if key_pressed[pg.K_SPACE] and accum_fire > FPS/FIRE_RATE:
                accum_fire = 0
                # 发射子弹0
                if hero.bomb2_count > 0:
                    hero.bomb2_count -= 1

                elif hero.bomb1_count > 0:
                    hero.bomb1_count -= 1

                elif hero.bomb0_count > 0:
                    hero.bomb0_count -= 1
                    bullet0_0 = Bullet0(hero.x-22, int(
                        hero.y-hero.h/2-22/2), 22, 22)
                    bullets.append(bullet0_0)

                    bullet0_1 = Bullet0(hero.x, int(
                        hero.y-hero.h/2-22/2), 22, 22)
                    bullets.append(bullet0_1)

                    bullet0_2 = Bullet0(hero.x+22, int(
                        hero.y-hero.h/2-22/2), 22, 22)
                    bullets.append(bullet0_2)
                else:
                    bullet0 = Bullet0(hero.x, int(
                        hero.y-hero.h/2-22/2), 22, 22)
                    bullets.append(bullet0)

            screen.blit(hero_img, (int(hero.x-hero.w/2),
                                   int(hero.y-hero.h/2)))  # 绘制玩家英雄
        else:
            hero.dead_fram_count += 1
            if hero.dead_fram_count < 20:
                screen.blit(hero_destroy1_img, (int(hero.x-hero.w/2),
                                                int(hero.y-hero.h/2)))  # 绘制玩家英雄摧毁状态1
            elif 20 <= hero.dead_fram_count < 40:
                screen.blit(hero_destroy2_img, (int(hero.x-hero.w/2),
                                                int(hero.y-hero.h/2)))  # 绘制玩家英雄摧毁状态2
            elif 40 <= hero.dead_fram_count < 60:
                screen.blit(hero_destroy3_img, (int(hero.x-hero.w/2),
                                                int(hero.y-hero.h/2)))  # 绘制玩家英雄摧毁状态3
            elif 60 <= hero.dead_fram_count < 80:
                screen.blit(hero_destroy4_img, (int(hero.x-hero.w/2),
                                                int(hero.y-hero.h/2)))  # 绘制玩家英雄摧毁状态4
            else:
                hero.dead_fram_count = 10000

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
        # 按概率生成炸弹0
        if random.random() < (1/FPS)*(0.01*BOMB0_GEN_RATE):
            bomb0 = Bomb0(random.randint(
                int(0+63/2), int(480-63/2)), int(0-53/2), 63, 53)
            bombs.append(bomb0)

        # 更新敌人信息
        for enemy in enemys:
            if enemy.y > 852+enemy.h/2:
                enemys.remove(enemy)
                continue
            # 敌人0
            if isinstance(enemy, Enemy0):
                if enemy.hp <= 0:
                    enemy.dead_fram_count += 1
                    if enemy.dead_fram_count < 20:
                        screen.blit(enemy0_destroy1_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人0摧毁状态1
                    elif 20 <= enemy.dead_fram_count < 40:
                        screen.blit(enemy0_destroy2_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人0摧毁状态2
                    elif 40 <= enemy.dead_fram_count < 60:
                        screen.blit(enemy0_destroy3_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人0摧毁状态3
                    elif 60 <= enemy.dead_fram_count < 80:
                        screen.blit(enemy0_destroy4_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人0摧毁状态4
                    else:
                        enemys.remove(enemy)
                else:
                    # 按概率发射子弹1
                    if random.random() < (1/FPS)*(0.1*ENEMY0_FIRE_RATE):
                        bullet1 = Bullet1(enemy.x, int(
                            enemy.y+enemy.h/2), 9, 21)
                        bullets.append(bullet1)

                    screen.blit(enemy0_img, (int(enemy.x-enemy.w/2),
                                             int(enemy.y-enemy.h/2)))  # 绘制敌人0
                    enemy.y += enemy.speed
            # 敌人1
            if isinstance(enemy, Enemy1):
                if enemy.hp <= 0:
                    enemy.dead_fram_count += 1
                    if enemy.dead_fram_count < 20:
                        screen.blit(enemy1_destroy1_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人1摧毁状态1
                    elif 20 <= enemy.dead_fram_count < 40:
                        screen.blit(enemy1_destroy2_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人1摧毁状态2
                    elif 40 <= enemy.dead_fram_count < 60:
                        screen.blit(enemy1_destroy3_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人1摧毁状态3
                    elif 60 <= enemy.dead_fram_count < 80:
                        screen.blit(enemy1_destroy4_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人1摧毁状态4
                    else:
                        enemys.remove(enemy)
                else:
                    # 按概率发射子弹2
                    if random.random() < (1/FPS)*(0.1*ENEMY1_FIRE_RATE):
                        bullet2 = Bullet2(enemy.x, int(
                            enemy.y+enemy.h/2), 9, 21)
                        bullets.append(bullet2)

                    screen.blit(enemy1_img, (int(enemy.x-enemy.w/2),
                                             int(enemy.y-enemy.h/2)))  # 绘制敌人1
                    enemy.y += enemy.speed
            # 敌人2
            if isinstance(enemy, Enemy2):
                if enemy.hp <= 0:
                    enemy.dead_fram_count += 1
                    if enemy.dead_fram_count < 25:
                        screen.blit(enemy2_destroy1_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人2摧毁状态1
                    elif 25 <= enemy.dead_fram_count < 50:
                        screen.blit(enemy2_destroy2_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人2摧毁状态2
                    elif 50 <= enemy.dead_fram_count < 75:
                        screen.blit(enemy2_destroy3_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人2摧毁状态3
                    elif 75 <= enemy.dead_fram_count < 100:
                        screen.blit(enemy2_destroy4_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人2摧毁状态4
                    elif 100 <= enemy.dead_fram_count < 125:
                        screen.blit(enemy2_destroy5_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人2摧毁状态5
                    elif 125 <= enemy.dead_fram_count < 150:
                        screen.blit(enemy2_destroy6_img, (int(enemy.x-enemy.w/2),
                                                          int(enemy.y-enemy.h/2)))  # 绘制敌人2摧毁状态6
                    else:
                        enemys.remove(enemy)
                else:
                    # 按概率发射子弹2
                    if random.random() < (1/FPS)*(0.1*ENEMY2_FIRE_RATE):
                        bullet2 = Bullet2(enemy.x, int(
                            enemy.y+enemy.h/2), 9, 21)
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

            # 玩家发出的类型0子弹
            if isinstance(bullet, Bullet0):
                # 碰撞检测
                if hero.hp > 0:
                    for enemy in enemys:
                        if bullet.x >= enemy.x-enemy.w/2 and bullet.x <= enemy.x+enemy.w/2:
                            if bullet.y >= enemy.y-enemy.h/2 and bullet.y <= enemy.y+enemy.h/2:
                                if enemy.hp > 0:
                                    enemy.hp -= bullet.damage
                                    if enemy.hp <= 0:
                                        # add score when destroy an enemys
                                        if isinstance(enemy, Enemy0):
                                            score += 1
                                        elif isinstance(enemy, Enemy1):
                                            score += 2
                                        elif isinstance(enemy, Enemy2):
                                            score += 4
                                    bullets.remove(bullet)
                                    break

                screen.blit(bullet0_img, (int(bullet.x-bullet.w/2),
                                          int(bullet.y-bullet.h/2)))  # 绘制子弹
                bullet.y -= bullet.speed

            # 敌人发出的类型1子弹
            elif isinstance(bullet, Bullet1):
                # 碰撞检测
                if hero.hp > 0:
                    if bullet.x >= hero.x-hero.w/2 and bullet.x <= hero.x+hero.w/2:
                        if bullet.y >= hero.y-hero.h/2 and bullet.y <= hero.y+hero.h/2:
                            hero.hp -= bullet.damage
                            if hero.hp <= 0:
                                hero.hp = 0
                                print('hero dead!')
                            bullets.remove(bullet)
                            continue
                screen.blit(bullet1_img, (int(bullet.x-bullet.w/2),
                                          int(bullet.y-bullet.h/2)))  # 绘制子弹
                bullet.y += bullet.speed

            # 敌人发出的类型2子弹
            elif isinstance(bullet, Bullet2):
                # 碰撞检测
                if hero.hp > 0:
                    if bullet.x >= hero.x-hero.w/2 and bullet.x <= hero.x+hero.w/2:
                        if bullet.y >= hero.y-hero.h/2 and bullet.y <= hero.y+hero.h/2:
                            hero.hp -= bullet.damage
                            if hero.hp <= 0:
                                hero.hp = 0
                                print('hero dead!')
                            bullets.remove(bullet)
                            continue
                screen.blit(bullet2_img, (int(bullet.x-bullet.w/2),
                                          int(bullet.y-bullet.h/2)))  # 绘制子弹
                bullet.y += bullet.speed

        # 更新炸弹信息
        for bomb in bombs:
            # 检测是炸弹否超出边界
            if bomb.y == 0 or bomb.y == 852:
                bombs.remove(bomb)
                continue

            # 类型0炸弹
            if isinstance(bomb, Bomb0):
                # 碰撞检测
                if hero.hp > 0:
                    if bomb.x >= hero.x-hero.w/2 and bomb.x <= hero.x+hero.w/2:
                        if bomb.y >= hero.y-hero.h/2 and bomb.y <= hero.y+hero.h/2:
                            bombs.remove(bomb)
                            print('get bomb0!')
                            hero.bomb0_count += 30
                            continue

                screen.blit(bomb0_img, (int(bomb.x-bomb.w/2),
                                        int(bomb.y-bomb.h/2)))  # 绘制炸弹0
                bomb.y += bomb.speed

        # 绘制文字
        f1 = pg.freetype.Font("resources/monaco.ttf", 24)
        f1rect = f1.render_to(screen, (0, 832), "Score: "+str(score),
                              fgcolor=(0, 0, 0), bgcolor=(190, 190, 190))
        f1 = pg.freetype.Font("resources/segoeprb.ttf", 24)
        f1rect = f1.render_to(screen, (0, 810), "HP: "+str(hero.hp),
                              fgcolor=(0, 0, 0), bgcolor=(190, 190, 190))
        if hero.bomb0_count > 0:
            f1 = pg.freetype.Font("resources/segoeprb.ttf", 24)
            f1rect = f1.render_to(screen, (0, 780), "Bomb0: "+str(hero.bomb0_count),
                                  fgcolor=(0, 0, 0), bgcolor=(190, 190, 190))

        pg.display.update()  # 更新屏幕

    pg.quit()


if __name__ == "__main__":
    main()

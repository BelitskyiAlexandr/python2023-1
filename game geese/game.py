import pygame
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()
FPS = pygame.time.Clock()

# Вікно
HEIGHT = 500
WIDTH = 1500
main_display = pygame.display.set_mode((WIDTH, HEIGHT))


# Гравець
player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill((153, 255, 204))
player_rect = player.get_rect()
player_speed = [1, 1]

# Enemy
def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size)
    enemy.fill((204, 0, 204))
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]

    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (30, 30)
    bonus = pygame.Surface(bonus_size)
    bonus.fill((255, 255, 102))
    bonus_rect = pygame.Rect(random.randint(0, WIDTH), 0, *bonus_size)
    bonus_move = [0, random.randint(1, 3)]

    return [bonus, bonus_rect, bonus_move]


CREATE_ENEMY = pygame.USEREVENT + 1
CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_ENEMY, 1500)
pygame.time.set_timer(CREATE_BONUS, 3000)

# Основний цикл
playing = True
enemies = []
bonuses = []
while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    main_display.fill((0, 0, 0))
    
    #enemy-process
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            playing = False

    #Bonus-process
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
        main_display.blit(bonus[0], bonus[1])
        if player_rect.colliderect(bonus[1]):
            pass
        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))

    main_display.blit(player, player_rect)



    #Перевірки
    keys = pygame.key.get_pressed()
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move([0, 5])
    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move([0, -5])
    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move([-5, 0])
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move([5, 0])        





    pygame.display.flip()
        



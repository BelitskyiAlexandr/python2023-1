import pygame
import random
import os
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()
FPS = pygame.time.Clock()

# Вікно
HEIGHT = 500
WIDTH = 1500
main_display = pygame.display.set_mode((WIDTH, HEIGHT))


# Гравець
player_size = (100,60)
player = pygame.transform.scale(pygame.image.load('player.png').convert_alpha(), player_size)
player_rect = pygame.Rect(WIDTH//4, HEIGHT//2, *player_size)
player_speed = [1, 1]
PLAYER_IMAGES = os.listdir("goose")

# Enemy
def create_enemy():
    enemy_size = (180, 80)
    enemy = pygame.transform.scale(pygame.image.load('enemy.png').convert_alpha(),  enemy_size)
    enemy_rect = pygame.Rect(WIDTH, random.randint(40, HEIGHT-40), *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]

    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (80, 120)
    bonus = pygame.transform.scale(pygame.image.load('bonus.png').convert_alpha(), bonus_size)
    bonus_rect = pygame.Rect(random.randint(40, WIDTH-40), -120, *bonus_size)
    bonus_move = [0, random.randint(2, 4)]

    return [bonus, bonus_rect, bonus_move]


CREATE_ENEMY = pygame.USEREVENT + 1
CREATE_BONUS = pygame.USEREVENT + 2
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CREATE_ENEMY, 1500)
pygame.time.set_timer(CREATE_BONUS, 3000)
pygame.time.set_timer(CHANGE_IMAGE, 250)

#Interface
font = pygame.font.Font('Mauryssel_Bold.ttf', 36)
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bg1 = 0
bg2 = bg.get_width()
bg_move = 2




# Основний цикл
playing = True
enemies = []
bonuses = []
score = 0
image_index = 0
while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join("goose", PLAYER_IMAGES[image_index]))
            player = pygame.transform.scale(player, (100,60))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):         
                image_index = 0


    bg1 -= bg_move
    bg2 -= bg_move
    if bg1 < -bg.get_width():
        bg1 = bg.get_width()
    if bg2 < -bg.get_width():
        bg2 = bg.get_width()
    main_display.blit(bg, (bg1, 0))
    main_display.blit(bg, (bg2, 0))
    main_display.blit(font.render(str(score), True, (255,255,255)), (WIDTH-60, 20))
    
    #enemy-process
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            #main_display.blit(font.render(f"You lost. Your score: {score}", True, (255,255,255)), (WIDTH//2, HEIGHT//2))
            playing = False

    #Bonus-process
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
        main_display.blit(bonus[0], bonus[1])
        if player_rect.colliderect(bonus[1]):
            score += 1
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
 

        



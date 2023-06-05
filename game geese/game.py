import pygame

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

        
# Основний цикл
playing = True
while playing:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    main_display.fill((0, 0, 0))
    
    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)

    #Перевірки
    if player_rect.bottom >= HEIGHT:
        player_speed[1] = -1            
    if player_rect.top <= 0:
        player_speed[1] = 1   
    if player_rect.right >= WIDTH:
        player_speed[0] = -1          
    if player_rect.left <= 0:
        player_speed[0] = 1  

    pygame.display.flip()
        



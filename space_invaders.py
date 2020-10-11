import pygame
import random
pygame.init()
pygame.mixer.init()
# scree size initialize
screen_width = 800
screen_height = 600
# Display window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("people.png")
pygame.display.set_icon(icon)
# background
background = pygame.image.load("background.jpg")
# display image
enemy_ship_image = pygame.image.load("ufo.png")
bullet_image = pygame.image.load("bullet.png")
space_ship_image = pygame.image.load("space_ship.png")
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])
def end(exit_type):
    exit_game = False
    back = pygame.image.load("over.jpg")
    pygame.mixer.music.load("mario.mp3")
    pygame.mixer.music.play()
    while not exit_game:
        if exit_type == 1:
            screen.fill((225,225,225))
            screen.blit(back, (0,0))
            text_screen("You crashed!!", (0,0,0), 250, 180)
            text_screen("Press 'Enter' to play again", (0,0,0), 170, 250)
            text_screen("Press 'q' to exit", (0,0,0), 260, 320)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # exit_game = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
        if exit_type == 2:
            screen.fill((225,225,225))
            screen.blit(back, (0,0))
            text_screen("Aliens ate your planet!!", (0,0,0), 200, 180)
            text_screen("Press 'Enter' to play again", (0,0,0), 170, 250)
            text_screen("Press 'q' to exit", (0,0,0), 260, 320)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
        pygame.display.update()
def welcome():
    exit_game = False
    bcing = pygame.image.load("welcome.jpg")
    pygame.mixer.music.load("start.mp3")
    pygame.mixer.music.play()
    while not exit_game:
        screen.fill((225,225,225))
        screen.blit(bcing, (0, 0))
        text_screen("Welcome to space invaders", (225,0,0), 170,200)
        text_screen("Press spacebar to play", (225,0,0), 200,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    game()
        pygame.display.update()
def game():
    running = True
    space_ship_image_x = 368
    space_ship_image_y = 500
    space_ship_image_x_vel = 0
    space_ship_image_y_vel = 0
    # display enemy
    enemy_ship_image_x = random.randint(30, 706)
    enemy_ship_image_y = random.randint(50, 150)
    enemy_ship_image_x_vel = 4
    enemy_ship_image_y_vel = 0
    enemy_vel = 4
    enemy_running = True
    # bullet
    bullet_x = 0
    bullet_y = 468
    bullet_y_vel = 0
    a = False
    b = False
    score = 0
    score1 = 0
    level = 1
    pygame.mixer.music.load("main.mp3")
    pygame.mixer.music.play(-1)
    def player():
        screen.blit(space_ship_image, (space_ship_image_x, space_ship_image_y))
    def enemy(enemy_x, enemy_y):
        screen.blit(enemy_ship_image, (enemy_x, enemy_y))
    def bullet():
        screen.blit(bullet_image, (bullet_x, bullet_y))
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if space_ship_image_x_vel == -4:
                        space_ship_image_x_vel = 4
                    elif space_ship_image_x_vel == 4:
                        space_ship_image_x_vel = 4
                    else:
                        space_ship_image_x_vel += 4
                if event.key == pygame.K_LEFT:
                    if space_ship_image_x_vel == 4:
                        space_ship_image_x_vel = -4
                    elif space_ship_image_x_vel == -4:
                        space_ship_image_x_vel = -4
                    else:
                        space_ship_image_x_vel += -4
                if event.key == pygame.K_UP:
                    space_ship_image_y_vel -= 1
                if event.key == pygame.K_DOWN:
                    space_ship_image_y_vel += 1
                if event.key == pygame.K_SPACE:
                    if not b:
                        bullet_x = space_ship_image_x + 26
                        bullet_y = space_ship_image_y - 32
                        bullet_y_vel = 4
                        b = True
                    a = True
        enemy_ship_image_x += enemy_ship_image_x_vel
        if a:
            bullet_y -= bullet_y_vel
            ###############ship movements######################
        if enemy_ship_image_x <= 0:
            enemy_ship_image_x = 0
            enemy_ship_image_y += 64
        if enemy_ship_image_x >= 736:
            enemy_ship_image_x = 736
            enemy_ship_image_y += 64
        if space_ship_image_x < 0:
            space_ship_image_x = 0
        if space_ship_image_x > 736:
            space_ship_image_x = 736
        if space_ship_image_y > 536:
            space_ship_image_y = 536
        if space_ship_image_y < 0:
            space_ship_image_y = 0
        if enemy_ship_image_x <= 0:
            enemy_ship_image_x_vel = enemy_vel
        if enemy_ship_image_x >= 736:
            enemy_ship_image_x_vel = -enemy_vel
        #############################ship movements#############################33
        ########################  bullet alien hit##########################################################3
        if bullet_x >= enemy_ship_image_x and ((bullet_y - enemy_ship_image_y) <= 64):
            if (abs(enemy_ship_image_x - bullet_x) <= 52) and (32 <= (bullet_y - enemy_ship_image_y) <= 64):
                score += 1
                score1 = score
                enemy_ship_image_x = random.randint(30, 706)
                enemy_ship_image_y = random.randint(50, 150)
                bullet_x = 800
                bullet_y = 600
                a = False
                b = False
                explode = pygame.mixer.Sound("Explosion.wav")
                explode.play()
         ############################## ended ###################################################3
        space_ship_image_x += space_ship_image_x_vel
        space_ship_image_y += space_ship_image_y_vel
        if enemy_running:
            enemy(enemy_ship_image_x, enemy_ship_image_y)
        if score1 % 5 == 0 and score1 != 0:
            score1 = 0
            enemy_vel += 1
            level += 1
        player()
        if a:
            bullet()
        text_screen("Score: " + str(score), (225,225,225), 5, 5)
        text_screen("Level: " + str(level), (225,225,225), 5, 56)
        pygame.display.update()
        if bullet_y < 0:
            bullet_y = space_ship_image_y - 32
            a = False
            b = False
        if (abs(space_ship_image_x - enemy_ship_image_x) < 64) and (abs(space_ship_image_y - enemy_ship_image_y) < 64):
            running = False
            pygame.mixer.music.stop()
            end(1)
        if enemy_ship_image_y >= 536:
            running = False
            pygame.mixer.music.stop()
            end(2)

welcome()
# end(1)
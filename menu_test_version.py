import pygame
import button_class
# Define constants
def Menu(wdth,hgth,okno):
    WIDTH = wdth
    HEIGHT = hgth
    CELL_SIZE = 100
    ROWS = HEIGHT // CELL_SIZE
    COLS = WIDTH // CELL_SIZE
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Initialize pygame
    pygame.init()
    screen = okno
    clock = pygame.time.Clock()
    # Define player class
    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y, color):
            super().__init__()
            self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
            self.image.fill(color)
            self.image.set_alpha(200)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.select_lock=False

        def move(self, dx, dy):
            self.rect.x += dx * CELL_SIZE
            self.rect.y += dy * CELL_SIZE

            # Wrap around screen if player goes out of bounds
            if self.rect.left < 0:
                self.rect.right = WIDTH
            elif self.rect.right > WIDTH:
                self.rect.left = 0
#            elif self.rect.top < 0:
 #               self.rect.bottom = HEIGHT
 #           elif self.rect.bottom > HEIGHT:
 #               self.rect.top = 0

    # Create group of all sprites
    all_sprites = pygame.sprite.Group()
    def rysuj_tlo():
        tlo_przeskalowane=pygame.transform.scale(wybrane_tlo,(WIDTH,HEIGHT))
        okno.blit(tlo_przeskalowane,(0,0))
    #def rysuj_gracza():
    #    if player2.rect.collidelist(buttons):
    #        okno.blit(tlo_przeskalowane,(0,0))
    # Load button images
    tlo=pygame.image.load("assets/images/background/Battleground2/Pale/Battleground2.png").convert_alpha()
    tlo2=pygame.image.load("assets/images/background/Battleground3/Pale/Battleground3.png").convert_alpha()
    wybrane_tlo=tlo
    Nomad_Mage_img=pygame.image.load('assets/images/buttons/Nomad_Mage2.png').convert_alpha()
    Samurai_Commander_img=pygame.image.load('assets/images/buttons/Samurai_Commander2.png').convert_alpha()
    Samurai_Warrior_img=pygame.image.load('assets/images/buttons/Samurai_Warrior2.png').convert_alpha()
    Skeleton_Warrior_img=pygame.image.load('assets/images/buttons/Skeleton_Warrior2.png').convert_alpha()
    cell_img = pygame.image.load("assets/images/buttons/Cell.png").convert_alpha()
    cell_scaled=pygame.transform.scale(cell_img,(100,100))
    # Create buttons from button class
    Samurai_Commander_button=button_class.button(300,700,Samurai_Commander_img,2,0)
    Samurai_Warrior_button=button_class.button(200,700,Samurai_Warrior_img,2,1)
    Nomad_Mage_button=button_class.button(100,700,Nomad_Mage_img,2,2)
    Skeleton_Warrior_button=button_class.button(0,700,Skeleton_Warrior_img,2,3)
    buttons=[Samurai_Commander_button,Samurai_Warrior_button,Nomad_Mage_button,Skeleton_Warrior_button]
    #buttons_colliders=[Samurai_Commander_button.rect,Samurai_Warrior_button.rect,Nomad_Mage_button.rect,Skeleton_Warrior_button.rect]
    # Create grid of cells
    grid = []
    for col in range(COLS):
        rect = pygame.Rect(col*CELL_SIZE, 700, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

    # Create player sprites
    player1 = Player(0, 700, BLACK)
    player2 = Player(300, 700, RED)
    all_sprites.add(player1, player2)
    #Load sound
    click_sfx=pygame.mixer.Sound("assets/sound/click.mp3")
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if player2.select_lock==False:
                    if event.key == pygame.K_LEFT:
                        player2.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        player2.move(1, 0)
                    #elif event.key == pygame.K_UP:
                    #    player2.move(0, -1)
                    #elif event.key == pygame.K_DOWN:
                    #    player2.move(0, 1)
                    elif event.key==pygame.K_KP1:
                        index=player2.rect.collidelist(buttons)
                        click_sfx.play()
                        if index>=0:
                            player2.select_lock=True
                            player_2_hero=buttons[index].hero_number
                            print(player_2_hero)
                        else:
                            print("nothing there")
                if player1.select_lock==False:
                    if event.key == pygame.K_a:
                        player1.move(-1, 0)
                    elif event.key == pygame.K_d:
                        player1.move(1, 0)
                    #elif event.key == pygame.K_w:
                    #    player1.move(0, -1)
                    #elif event.key == pygame.K_s:
                    #    player1.move(0, 1)
                    # Player selected hero
                    elif event.key==pygame.K_r:
                        index=player1.rect.collidelist(buttons)
                        click_sfx.play()
                        if index>=0:
                            player1.select_lock=True
                            player_1_hero=buttons[index].hero_number
                            print(player_1_hero)
                        else:
                            print("nothing there")
                if event.key == pygame.K_SPACE:
                    if wybrane_tlo==tlo:
                        wybrane_tlo=tlo2
                    else:
                        wybrane_tlo=tlo
                elif player1.select_lock==True and player2.select_lock==True:
                    data=[True,[player_1_hero,player_2_hero],wybrane_tlo]
                    return data

        # Draw screen
        rysuj_tlo()
        for col in range(COLS):
            screen.blit(cell_scaled,(col*CELL_SIZE,700))
            pygame.draw.rect(screen, WHITE, grid[col], 1)
        all_sprites.draw(screen)
        for button in buttons:
            button.draw(screen)
        # Update display
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)
    # Quit pygame
    data=[False,[1,1],wybrane_tlo]
    return data
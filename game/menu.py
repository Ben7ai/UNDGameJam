import pygame, sys
from button import Button

# Initialize Pygame
pygame.init()

# Load and play background music
pygame.mixer.music.load("Assets/background/audio/menu_background.mp3")
pygame.mixer.music.play(-1, 0, 300)

# Define a function to set the music volume
def set_music_volume(volume):
    pygame.mixer.music.set_volume(volume)

# Define a function to get a font object
def get_font(size):
    return pygame.font.SysFont("Arial", size)

# Set the initial volume of the background music
set_music_volume(0.5)

# Set up the display
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# Define a function to set the music volume
def set_music_volume(volume):
    pygame.mixer.music.set_volume(volume)

# Define a function to get a font object
def get_font(size):
    return pygame.font.SysFont("Arial", size)

# Define the play function
def play():
    # Set the initial volume of the background music
    set_music_volume(0.3)

    # Load the background image
    background = pygame.image.load("Assets/background/play_background.png")
    background_rect = background.get_rect(topleft=(0, 0))

    # Load the title and description text
    title_font = get_font(60)
    title_text = title_font.render("Welcome to the Game!", True, "White")
    title_rect = title_text.get_rect(center=(640, 150))

    description_font = get_font(25)
    description_text = description_font.render("This is the play screen. You can start playing the game by clicking on the 'Start Game' button below.", True, "White")
    description_rect = description_text.get_rect(center=(640, 400))

    # Create volume up and down buttons
    volume_up_button = Button(image=volume_up_image, pos=(100, 50), image_size=(50, 50), base_color="White")
    volume_down_button = Button(image=volume_down_image, pos=(100, 100), image_size=(50, 50), base_color="White")

    # Set the initial volume of the background music
    volume = 0.3

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle volume up button input
                if volume_up_button.checkForInput(pygame.mouse.get_pos()):
                    volume += 0.1
                    if volume > 1.0:
                        volume = 1.0
                    set_music_volume(volume)

                # Handle volume down button input
                if volume_down_button.checkForInput(pygame.mouse.get_pos()):
                    volume -= 0.1
                    if volume < 0.0:
                        volume = 0.0
                    set_music_volume(volume)

                # Handle back button input
                if PLAY_BACK.checkForInput(pygame.mouse.get_pos()):
                    main_menu()

                # Handle start game button input
                if PLAY_START_GAME.checkForInput(pygame.mouse.get_pos()):
                    # Start the game here
                    pass

            elif event.type == pygame.KEYDOWN:
                # Handle volume up and down keys
                if event.key == pygame.K_UP:
                    volume += 0.1
                    if volume > 1.0:
                        volume = 1.0
                    set_music_volume(volume)
                elif event.key == pygame.K_DOWN:
                    volume -= 0.1
                    if volume < 0.0:
                        volume = 0.0
                    set_music_volume(volume)

        # Draw the screen
        SCREEN.fill("black")

        volume_percent = int(volume * 100)  # Calculate the volume percentage
        volume_text = get_font(20).render("Volume: {}%".format(volume_percent), True, "White")
        volume_rect = volume_text.get_rect(center=(640, 50))
        SCREEN.blit(volume_text, volume_rect)

        PLAY_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_START_GAME = Button(image=None, pos=(640, 350), 
                            text_input="START GAME", font=get_font(50), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(pygame.mouse.get_pos())
        PLAY_START_GAME.changeColor(pygame.mouse.get_pos())

        PLAY_BACK.update(SCREEN)
        PLAY_START_GAME.update(SCREEN)

        SCREEN.blit(background, background_rect)
        SCREEN.blit(title_text, title_rect)
        SCREEN.blit(description_text, description_rect)

        # Draw the volume buttons
        volume_up_button.update(SCREEN)
        volume_down_button.update(SCREEN)

        pygame.display.update()

# Define the main menu function
def main_menu():
    # Set the initial volume of the background music
    volume = 0.5
    set_music_volume(volume)

    # Load the title image
    MENU_IMAGE = pygame.image.load("Assets/background/title.png")
    MENU_IMAGE = pygame.transform.scale(MENU_IMAGE, (400, 100)) 
    MENU_RECT = MENU_IMAGE.get_rect(center=(640, 150))





    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:


                # Handle play button input
                if PLAY_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    play()

                # Handle quitbutton input
                if QUIT_BUTTON.checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Handle volume up and down keys
                if event.key == pygame.K_UP:
                    volume += 0.1
                    if volume > 1.0:
                        volume = 1.0
                    set_music_volume(volume)
                elif event.key == pygame.K_DOWN:
                    volume -= 0.1
                    if volume < 0.0:
                        volume = 0.0
                    set_music_volume(volume)

        # Draw the screen
        SCREEN.fill("gray")

        volume_percent = int(volume * 100)  # Calculate the volume percentage
        volume_text = get_font(20).render("Volume (Arrow UP and Down): {}%".format(volume_percent), True, "Black")
        volume_rect = volume_text.get_rect(center=(640, 50))
        SCREEN.blit(volume_text, volume_rect)

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/background/Start-Game.png"), pos=(640 - 100, 350), image_size=(500, 100), 
                                    text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/background/Quit.png"), pos=(640 - 30, 400), image_size=(3000, 500), 
                                    text_input="", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_IMAGE, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(SCREEN)


        pygame.display.update()

# Run the main menu function
main_menu()
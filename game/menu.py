import pygame, sys
from button import Button

pygame.init()


# Load and play background music
pygame.mixer.music.load("Assets/background/audio/menu_background.mp3")
pygame.mixer.music.play(-1, 0, 300)


SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# Use a solid color background
SCREEN.fill("gray")

# Use a default font
def get_font(size):
    return pygame.font.SysFont("Arial", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    font = get_font(100) # create a font object
    while True:
        SCREEN.blit(SCREEN, (0, 0)) # draw the solid color background

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Calculate the center position of the screen
        center_x, center_y = SCREEN.get_width() // 2, SCREEN.get_height() // 2

        MENU_IMAGE = pygame.image.load("Assets/background/title.png")
        MENU_IMAGE = pygame.transform.scale(MENU_IMAGE, (400, 100)) 
        MENU_RECT = MENU_IMAGE.get_rect(center=(center_x, center_y - 150))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/background/Start-Game.png"), pos=(center_x - 100, center_y), image_size=(500, 100), 
                                    text_input="", font=font, base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Assets/background/Options Rect.png"), pos=(center_x - 100, center_y + 300), image_size=(500, 100), 
                                    text_input="", font=font, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/background/Quit.png"), pos=(center_x - 30, center_y + 150), image_size=(3000, 500), 
                                    text_input="", font=font, base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(MENU_IMAGE, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    

                        
main_menu()
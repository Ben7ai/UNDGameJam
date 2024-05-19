import pygame

class Button():
    def __init__(self, image, pos, image_size, text_input, font, base_color, hovering_color):
        self.image = image
        self.pos = pos
        self.image_size = image_size
        self.text_input = text_input
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.rect = self.image.get_rect(topleft = self.pos) if self.image else pygame.Rect(self.pos[0], self.pos[1], self.image_size[0], self.image_size[1])

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.color = self.hovering_color
        else:
            self.color = self.base_color

    def checkForInput(self, position):
        mouse_pressed = pygame.mouse.get_pressed()
        if self.rect.collidepoint(position) and mouse_pressed[0] == 1:
            return True
        return False

    def update(self, screen):
        screen.blit(self.image, self.rect) if self.image else screen.blit(self.font.render(self.text_input, True, self.color), self.rect)
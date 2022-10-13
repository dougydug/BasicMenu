import sys
import pygame
pygame.font.init()


class UI:
    def __init__(self, screen):
        self.background = screen
        self.button_gap = 10
        self.active_surface = screen
        self.active_buttons = []
        self.active_text = []

    def draw(self, screen):
        screen.blit(self.active_surface, self.background.get_rect())
        for x in self.active_buttons:
            screen.blit(x[1], x[0])
        for y in self.active_text:
            screen.blit(y[1], y[0])


class PauseMenu(UI):
    def __init__(self, screen):
        UI.__init__(self, screen)
        self.menu_button_size = (100, 50)
        self.button_surface = pygame.Surface(self.menu_button_size)

            #Button location in middle of screen
        self.button_location = ((self.background.get_width() - self.menu_button_size[0]) / 2,
                                (self.background.get_height() - self.menu_button_size[1]) / 2)

        self.button_text_font = pygame.font.SysFont('Comic Sans MS', 32)
        self.exit_button_text = self.button_text_font.render('EXIT', False, (200, 200, 200))

            #Creating button object
        self.exit_button_rect = pygame.Rect(self.button_location[0], self.button_location[1], self.menu_button_size[0],
                                            self.menu_button_size[1])

        self.button_surface.fill((0, 0, 0))
        self.QUIT_EVENT = pygame.event.Event(pygame.QUIT)
        self.pause_menu_surface = pygame.Surface((self.background.get_width(), self.background.get_height()),
                                                 pygame.SRCALPHA, 32)
        self.pause_menu_surface.fill((200, 200, 200))
        self.pause_menu_surface.convert_alpha()

    def set_active_screen(self):
        self.active_surface = self.pause_menu_surface
        self.active_buttons.clear()
        self.active_buttons.append([self.exit_button_rect, self.button_surface])
        self.active_text.append([ self.exit_button_rect, self.exit_button_text])

    def resolve_click(self, mouse_pos):
        if self.exit_button_rect.collidepoint(mouse_pos):
            pygame.event.post(self.QUIT_EVENT)

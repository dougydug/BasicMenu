import sys
import pygame

from User_Interface import PauseMenu


from pygame.locals import *

clock = pygame.time.Clock()

WINDOW_SIZE = [1920,1080]

screen = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN, 32)

paused = False

interface = PauseMenu(screen)

help_text_font = pygame.font.SysFont('Comic Sans MS', 50)
help_button_text = help_text_font.render('P to Pause, ESC to EXIT', False, (0, 0, 0))


while True:
    screen.fill((250, 250, 250))

    events = []

    for event in pygame.event.get():
        events.append(event)
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == K_p:
                paused = not paused

        if paused and event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            interface.resolve_click(pos)

    if paused:
        interface.draw(screen)
        interface.set_active_screen()
    else:
        screen.blit(help_button_text, (screen.get_width() / 4, screen.get_height() / 4))

    pygame.display.flip()
    clock.tick(60)

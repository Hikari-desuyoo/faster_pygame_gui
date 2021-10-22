import pygame, pygame_gui, sys
from interface import Interface, InterfaceElement
from rect_helpers import below_rect, right_rect

window_size = (900,600)
pygame.init()
display_surf = pygame.display.set_mode(window_size, 0, 32)

manager = pygame_gui.UIManager(display_surf.get_size())
clock = pygame.time.Clock()

interface = Interface()

#FIRST BUTTON
def first_button_click():
    print('aaaaaaaa')

first_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(5, 5, 100, 50),
    text='first_button',
    manager=manager
)

interface['first_button'] = first_button, first_button_click

#SECOND BUTTON
def second_button_click():
    print('bbbbbb')

second_button = pygame_gui.elements.UIButton(
    relative_rect=right_rect(first_button.relative_rect, (100, 50), margin=5),
    text='second_button',
    manager=manager
)

interface['second_button'] = second_button, second_button_click

while True:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == None:
                    pass

        manager.process_events(event)
        interface.process_events(event)

    manager.update(time_delta)

    display_surf.fill('black')
    #your code here

    manager.draw_ui(display_surf)
    pygame.display.update()
    clock.tick(60)
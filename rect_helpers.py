import pygame 
import pygame_gui

def below_rect(anchor_rect, size, margin=10):
    new_rect = pygame.Rect((0,0), size)
    new_rect.topleft = anchor_rect.topleft 
    new_rect.y += margin + anchor_rect.h
    return new_rect

def right_rect(anchor_rect, size, margin=10):
    new_rect = pygame.Rect((0,0), size)
    new_rect.topleft = anchor_rect.topleft 
    new_rect.x += margin + anchor_rect.w
    return new_rect

rect_function_dict = {
    'below_rect': below_rect,
    'right_rect': right_rect
}

def create_field(manager, text, label_rect, entry_size, inside_margin=0, entry_is='below_rect'):
    label = pygame_gui.elements.ui_label.UILabel(
        relative_rect=label_rect,
        manager=manager,
        text=text
    )

    rect_function = rect_function_dict[entry_is]

    entry_line_rect = rect_function(label_rect, entry_size, margin=inside_margin)

    entry_line = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=entry_line_rect,
        manager=manager
    )

    return label, entry_line

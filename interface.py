import pygame
import pygame_gui 

class InterfaceElement:
    def __init__(self, gui_element, on_click):
        self.gui_element = gui_element
        self.on_click = on_click
    
    def on(self):
        self.on_click()

class Interface:
    def __init__(self):
        self.elements = {}

    def __setitem__(self, key, element_parameters):
        interface_element = InterfaceElement(*element_parameters)
        self.elements[key] = interface_element
        
    def __getitem__(self, key):
        return self.elements[key]

    def get_gui_element(self, key):
        return self.elements[key].gui_element

    def process(self):
        for element in self.elements.values():
            element.partial.process()

    def disable_all_partials(self):
        for element in self.elements.values():
            element.off()

    def process_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                for element in self.elements.values():
                    if event.ui_element == element.gui_element:
                        element.on()
                        return



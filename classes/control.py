import pygame
from classes.enums import ControlType

class Control():
    def __init__(self, control_type = ControlType.KEYBOARD) -> None:
        
        self.set_keys(control_type)


    def set_keys(self, control_type: ControlType):
        if control_type == ControlType.KEYBOARD:
            self.set_key_up(pygame.K_w)
            self.set_key_down(pygame.K_s)
        elif control_type == ControlType.MOUSE:
            self.set_key_up(1)
            self.set_key_down(-1)


    def set_key_up(self, key):
        self.key_up = key


    def set_key_down(self, key):
        self.key_down = key


    def up(self):
        print('up')

    
    def down(self):
        print('down')
    

    def __str__(self) -> str:
        return f'Control: {self.key_up} / {self.key_down}'
    

    def __repr__(self) -> str:
        return f'Control: {self.key_up} / {self.key_down}'
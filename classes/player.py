from classes.control import Control
from classes.enums import ControlType
from classes.enums import Side

class Player():
    def __init__(self, side : Side = Side.LEFT, controls : Control = Control(), position : list[int, int] = [0, 0], name = 'default', size = 10, color = 'white') -> None:
        self.name = name
        self.color = color

        self.width = size
        self.height = size * 8 

        self.controls = controls
        self.side = side
        self.position = position


    def get_player_center(self):
        return [self.position[0] + self.width / 2, self.position[1] + self.height / 2]


    def set_controls(self, control_type : ControlType):
        self.controls.set_keys(control_type)
    

    def set_side(self, side_type : Side):
        self.side = side_type


    def handle_control_strokes(self, key_event):
        if key_event == self.controls.key_up:
            self.controls.up()
            self.move_player_up()
        elif key_event == self.controls.key_down:
            self.controls.down()
            self.move_player_down()

    
    def move_player_up(self):
        self.position[1] -= 10


    def move_player_down(self):
        self.position[1] += 10


    def class_info_string(self):
        return f'Player: {self.name} / Side: {self.side} / Controls: {self.controls} / Position: {self.position}'


    def __str__(self) -> str:
        return self.class_info_string()

    def __repr__(self) -> str:
        return self.class_info_string()
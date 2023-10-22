from classes.player import Player
from classes.control import Control
from classes.gui import GUI
from classes.enums import ControlType
from classes.enums import Side

def main():
    player_one = Player(
        name='Player One', 
        color='red', 
        side=Side.LEFT, 
        controls=Control(ControlType.KEYBOARD),
        position=[100, 300]
    )

    player_two = Player(
        name='Player Two', 
        color='blue', 
        side=Side.RIGHT, 
        controls=Control(ControlType.MOUSE),
        position=[700, 300]
    )

    gui = GUI(players=[player_one, player_two])
    gui.run_game()


if __name__ == '__main__':
    main()
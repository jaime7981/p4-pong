from classes.player import Player
from classes.control import Control
from classes.gui import GUI
from classes.enums import ControlType
from classes.enums import Side
from classes.enums import Difficulty


def difficulty_selection():
    x = input('Select difficulty: 1. Easy 2. Medium 3. Hard\n')

    if x == '1':
        return Difficulty.EASY
    elif x == '2':
        return Difficulty.MEDIUM
    elif x == '3':
        return Difficulty.HARD
    else:
        print('Invalid option, try again')
        return difficulty_selection()


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

    difficulty = difficulty_selection()

    gui = GUI(players=[player_one, player_two], difficulty=difficulty)
    gui.run_game()


if __name__ == '__main__':
    main()
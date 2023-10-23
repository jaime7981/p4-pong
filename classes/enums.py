import enum


class ControlType(enum.Enum):
    KEYBOARD = 1
    MOUSE = 2


class Side(enum.Enum):
    LEFT = 1
    RIGHT = 2


class Difficulty(enum.Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

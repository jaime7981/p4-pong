import pygame
from classes.enums import Side

class Ball():
    def __init__(self, width: int, height: int):
        self.radius = 10
        self.x_coordinate = width/2 - self.radius
        self.y_coordinate = height/2 - self.radius
        self.x_velocity = 2
        self.y_velocity = 2

    def check_wall_collision(self):
        if self.y_coordinate <= 0 + self.radius or self.y_coordinate >= 600 - self.radius:
            self.y_velocity *= -1 #si toca el borde superor o inferior de la pantalla cambiar sentido
        if self.x_coordinate <= 0 + self.radius or self.x_coordinate >= 800 - self.radius:
            self.x_velocity *= -1 #si toca el borde izquierdo o derecho de la pantalla cambiar sentido
    
    def move(self):
        self.x_coordinate += self.x_velocity
        self.y_coordinate += self.y_velocity
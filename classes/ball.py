import pygame
from classes.enums import Side

class Ball():
    def __init__(self, width: int, height: int):
        self.radius = 10
        self.x_coordinate = width/2 - self.radius
        self.y_coordinate = height/2 - self.radius
        self.x_velocity = 1.0
        self.y_velocity = 1.0
        self.left_side_collision = pygame.event.custom_type()
        self.right_side_collision = pygame.event.custom_type()


    def set_speed(self, speed: int):
        self.x_velocity = speed
        self.y_velocity = speed

    def check_collision(self, players_positions: list[list[int]], players_proportions: list[int]):
        has_player_collided = self.check_player_collision(players_positions, players_proportions)
        if not has_player_collided:
            has_ball_collided = self.check_wall_collision()

    def check_player_collision(self, players_positions: list[list[int]], players_proportions: list[int]):
        players_width = players_proportions[0]
        players_height = players_proportions[1]
        left_player_position = players_positions[0]
        right_player_position = players_positions[1]
        has_left_player_vertically_collided = left_player_position[1] <= self.y_coordinate <= left_player_position[1] + players_height
        has_left_player_horizontally_collided = left_player_position[0] <= self.x_coordinate <= left_player_position[0] + players_width
        has_right_player_vertically_collided = right_player_position[1] <= self.y_coordinate <= right_player_position[1] + players_height
        has_right_player_horizontally_collided = right_player_position[0] <= self.x_coordinate <= right_player_position[0] + players_width
        has_left_player_collided = has_left_player_vertically_collided and has_left_player_horizontally_collided
        has_right_player_collided = has_right_player_vertically_collided and has_right_player_horizontally_collided
        has_colided = has_left_player_collided or has_right_player_collided
        if has_left_player_collided:
            self.x_coordinate = left_player_position[0] + players_width
            self.x_velocity *= -1
            self.increase_speed()

        if has_right_player_collided:
            self.x_coordinate = right_player_position[0]
            self.x_velocity *= -1
            self.increase_speed()
        return has_colided

    def check_wall_collision(self):
        has_colided = False
        if self.y_coordinate <= 0 + self.radius or self.y_coordinate >= 600 - self.radius:
            self.y_velocity *= -1.0 #si toca el borde superor o inferior de la pantalla cambiar sentido
            has_colided = True
            self.increase_speed()
        if self.x_coordinate >= 800 - self.radius: #right side collision
            self.x_coordinate = 800/2 - self.radius
            self.y_coordinate = 600/2 - self.radius
            self.x_velocity = -1.0
            self.y_velocity = 1.0
            has_colided = True
            pygame.event.post(pygame.event.Event(self.right_side_collision))
        if self.x_coordinate <= 0 + self.radius: #left side collision
            self.x_coordinate = 800/2 - self.radius
            self.y_coordinate = 600/2 - self.radius
            self.x_velocity = 1.0
            self.y_velocity = 1.0
            has_colided = True
            pygame.event.post(pygame.event.Event(self.left_side_collision))
        return has_colided

    def increase_speed(self,):
        if self.x_velocity > 0:
            self.x_velocity += 0.2
        else:
            self.x_velocity += -0.2
        if self.y_velocity > 0:
            self.y_velocity += 0.2
        else:
            self.y_velocity += -0.2

    def move(self):
        self.x_coordinate += self.x_velocity
        self.y_coordinate += self.y_velocity
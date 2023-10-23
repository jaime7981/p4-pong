import pygame
from classes.player import Player
from classes.control import Control
from classes.enums import ControlType
from classes.enums import Side
from classes.enums import Difficulty
from classes.ball import Ball

class GUI():
    def __init__(self, players : list[Player] = [Player(), Player()], difficulty: Difficulty = Difficulty.EASY) -> None:
        self.players : list[Player] = players
        self.ball = Ball(800, 600)

        self.screen = pygame.display.set_mode((800, 600)) # (width,height)
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.background_color = (0, 0, 0)
        
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 10)

        self.setup_players()
        self.setup_difficulty(difficulty)


    def setup_difficulty(self, difficulty: Difficulty):
        if difficulty == Difficulty.EASY:
            self.ball.set_speed(1.0)
        elif difficulty == Difficulty.MEDIUM:
            self.ball.set_speed(2.0)
        elif difficulty == Difficulty.HARD:
            self.ball.set_speed(3.0)

        for player in self.players:
            if difficulty == Difficulty.EASY:
                player.set_size(10)
            elif difficulty == Difficulty.MEDIUM:
                player.set_size(20)
            elif difficulty == Difficulty.HARD:
                player.set_size(30)
        

    def setup_players(self):
        for counter, player in enumerate(self.players):
            if counter == 0:
                player.set_controls(ControlType.KEYBOARD)
                player.set_side(Side.LEFT)
                player.position[0] = self.screen.get_width() / 10 + player.width + 10
            elif counter == 1:
                player.set_controls(ControlType.MOUSE)
                player.set_side(Side.RIGHT)
                player.position[0] = 9 * self.screen.get_width() / 10 - player.width - 10


    def handle_events(self):
        left_side_player = self.players[0]
        right_side_player = self.players[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                self.handle_player_controls(event.key)

            if event.type == self.ball.left_side_collision:
                right_side_player.score += 1

            if event.type == self.ball.right_side_collision:
                left_side_player.score += 1

    def handle_player_controls(self, event):
        for player in self.players:
            player.handle_control_strokes(event)


    def draw_players(self):
        for player in self.players:
            player_position_x = player.position[0]
            player_position_y = player.position[1]

            if player.side == Side.LEFT:
                player_position_x = player.position[0] - player.width

            pygame.draw.rect(
                self.screen, 
                player.color, 
                pygame.Rect(
                    player_position_x, 
                    player_position_y, 
                    player.width, 
                    player.height
                )
            )

            pygame.draw.circle(self.screen,'white', (self.ball.x_coordinate, self.ball.y_coordinate), self.ball.radius)
            
            # For debuging purposes draws the player saved postition
            pygame.draw.circle(
                self.screen, 
                'white', 
                player.position, 
                player.width / 4
            )
            
            # For debuging purposes draws the player center
            pygame.draw.circle(
                self.screen, 
                'grey',
                player.get_player_center(), 
                player.width / 4
            )

            self.draw_players_score(player)


    def draw_players_score(self, player : Player):
        score_offset = 100
        score_size = 80

        score_x = player.position[0] - score_offset - score_size / 2 - player.width
        score_y = 30

        if player.side == Side.LEFT:
            score_x = player.position[0] + score_offset

        score = pygame.font.SysFont('Arial', score_size).render(str(player.score), True, player.color)
        self.screen.blit(score, (score_x, score_y))
        

    def run_game(self):
        print(self.players)
        
        while self.running:
            self.clock.tick(self.fps)
            self.handle_events()

            self.screen.fill(self.background_color)
            self.draw_players()
            self.ball.check_collision(
                [
                    self.players[0].position, # asuming the left player will always be the first on the list
                    self.players[1].position
                ],
                [self.players[0].width,self.players[0].height]
                )
            self.ball.move()
            # pygame.display.flip()
            pygame.display.update()
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
        
        pygame.key.set_repeat(40)
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
                player.set_size(30)
            elif difficulty == Difficulty.MEDIUM:
                player.set_size(20)
            elif difficulty == Difficulty.HARD:
                player.set_size(10)
        

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

            if event.type == pygame.MOUSEWHEEL:
                self.handle_player_controls(event.y)

            if event.type == self.ball.left_side_collision:
                right_side_player.score += 1
                self.handle_end_game(right_side_player)

            if event.type == self.ball.right_side_collision:
                left_side_player.score += 1
                self.handle_end_game(left_side_player)

    def handle_player_controls(self, event):
        for player in self.players:
            player.handle_control_strokes(event)

    def handle_end_game(self, player):
        if player.score >= 5:
            self.running = False

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

    
    def draw_keys(self):
        for player in self.players:
            key_up = None
            key_down = None

            if player.side == Side.LEFT:
                key_up = self.font.render('w', True, player.color)
                key_down = self.font.render('s', True, player.color)
            elif player.side == Side.RIGHT:
                key_up = self.font.render('Scroll Up ↑', True, player.color)
                key_down = self.font.render('Scroll Down ↓', True, player.color)
            
            # draw key up
            key_up_x = player.position[0] - 20
            key_up_y = player.position[1] - 20

            self.screen.blit(key_up, (key_up_x, key_up_y))

            # draw key down
            key_down_x = player.position[0] - 20
            key_down_y = player.position[1] + player.height

            self.screen.blit(key_down, (key_down_x, key_down_y))
    
    def get_player_with_highest_score(self):
        highest_score = 0
        player_with_highest_score = None

        if self.is_player_score_draw():
            return "Tie"

        for player in self.players:
            if player.score > highest_score:
                highest_score = player.score
                player_with_highest_score = player

        return player_with_highest_score.name
    
    def is_player_score_draw(self):
        if self.players[0].score == self.players[1].score:
            return True
        else:
            return False

    def draw_game_over(self):
        # Draw Game over text
        winner_player = self.get_player_with_highest_score()
        game_over_message = f'Game Over: {winner_player} wins'

        if winner_player == "Tie":
            game_over_message = "Game Over: Tie"

        game_over_text = pygame.font.SysFont('Arial', 50).render(game_over_message, True, (255, 255, 255))
        game_over_text_x = self.screen.get_width() / 2 - game_over_text.get_width() / 2
        game_over_text_y = self.screen.get_height() / 2 - game_over_text.get_height() / 2
        self.screen.blit(game_over_text, (game_over_text_x, game_over_text_y))



    def run_game(self):
        print(self.players)
        
        while self.running:
            self.clock.tick(self.fps)
            self.handle_events()

            self.screen.fill(self.background_color)
            self.draw_players()
            self.draw_keys()
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

        self.draw_game_over()
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        """ input('Press any key to exit')
        pygame.quit() """
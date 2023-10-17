import pygame
from classes.player import Player
from classes.control import Control
from classes.enums import ControlType
from classes.enums import Side

class GUI():
    def __init__(self, players : list[Player] = [Player(), Player()]) -> None:
        self.players : list[Player] = players

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.background_color = (0, 0, 0)

        #self.setup_players()


    def setup_players(self):
        for counter, player in enumerate(self.players):
            if counter == 0:
                player.set_controls(ControlType.KEYBOARD)
                player.set_side(Side.LEFT)
                player.position[0] = 100
            elif counter == 1:
                player.set_controls(ControlType.MOUSE)
                player.set_side(Side.RIGHT)
                player.position[0] = self.screen.get_width() - player.width


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                self.handle_player_controls(event.key)


    def handle_player_controls(self, event):
        for player in self.players:
            player.handle_control_strokes(event)


    def draw_players(self):
        for player in self.players:
            player_position_x = player.position[0]
            player_position_y = player.position[1]

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



    def run_game(self):
        print(self.players)
        
        while self.running:
            self.clock.tick(self.fps)
            self.handle_events()

            self.screen.fill(self.background_color)
            self.draw_players()

            # pygame.display.flip()
            pygame.display.update()
import pygame
from pygame.locals import QUIT
from engine.constants import WIDTH, HEIGHT, FPS, COLORS
from engine.objects import Player, Bol

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont("arial", 20, True)
        self.clock = pygame.time.Clock()
        self.players = {
            "player1": {
                "object": None,
                "score": 0
            },
            "player2": {
                "object": None,
                "score": 0
            }
        }
    
    def render_scoreboard(self, text):
        label = self.font.render(text, True, COLORS["black"], COLORS["gray"])
        ret_label = label.get_rect()
        ret_label.center = (WIDTH/2, HEIGHT*0.05)

        self.screen.blit(label, ret_label)

    def reset_game(self, scoreboard: bool = False):
        self.players["player1"]["object"] = Player(self.screen, "left")
        self.players["player2"]["object"] = Player(self.screen, "right")
        self.bol = Bol(self.screen)

        if scoreboard:
            self.players["player1"]["score"] = 0
            self.players["player2"]["score"] = 0

    def start(self):
        self.reset_game()
        while True:
            self.clock.tick(FPS)
            self.screen.fill(COLORS["red"], rect=(0,0, WIDTH/2, HEIGHT))
            self.screen.fill(COLORS["blue"], rect=(WIDTH/2,0, WIDTH/2, HEIGHT))

            self.render_scoreboard(f"{self.players['player1']['score']}  X   {self.players['player2']['score']}")

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            
            self.players["player1"]["object"].update()
            self.players["player2"]["object"].update()
            self.bol.update()

            if self.bol.bol.colliderect(self.players["player1"]["object"].bar) or self.bol.bol.colliderect(self.players["player2"]["object"].bar):
                self.bol.dir_bx *= -1
                self.bol.dir_by *= self.bol.random_dir()
            
            if self.bol.bx < WIDTH*0.05 or self.bol.bx > WIDTH - WIDTH*0.05:
                if self.bol.bx < WIDTH*0.05:
                    self.players["player2"]["score"] += 1
                else:
                    self.players["player1"]["score"] += 1
                self.reset_game()

            pygame.display.update()
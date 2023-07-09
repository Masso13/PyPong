from engine import pygame
from engine.constants import VELOCITY_BAR, VELOCITY_BOL, COLORS, WIDTH, HEIGHT
from pygame.locals import K_UP, K_DOWN, K_w, K_s
from random import randint

class Player:
    def __init__(self, screen, side: str):
        self.w, self.h = WIDTH*0.005,  HEIGHT/5
        self.screen = screen
        self.side = side
        self.px = WIDTH*0.05 if side == "left" else WIDTH - WIDTH*0.05
        self.py = (HEIGHT - self.h)/2
    
    def update(self):
        dir_py = 0
        keys = pygame.key.get_pressed()
        if self.side == "left":
            if keys[K_w]:
                dir_py = -1
            elif keys[K_s]:
                dir_py = 1
        elif self.side == "right":
            if keys[K_UP]:
                dir_py = -1
            elif keys[K_DOWN]:
                dir_py = 1
        
        self.py += VELOCITY_BAR*dir_py
        self.py = max(0, min(self.py, HEIGHT - self.h))

        self.bar = pygame.draw.rect(self.screen, COLORS["gray"], (self.px, self.py, self.w, self.h), 0, 4)

class Bol:
    def __init__(self, screen):
        self.r = WIDTH*0.01
        self.screen = screen
        self.bx, self.by = WIDTH/2, HEIGHT/2
        self.dir_bx, self.dir_by = self.random_dir(), self.random_dir()
    
    def update(self):
        if self.by <= 0 or self.by >= HEIGHT:
            self.dir_by *= -1
        
        self.bx += VELOCITY_BOL*self.dir_bx
        self.by += VELOCITY_BOL*self.dir_by

        self.bol = pygame.draw.circle(self.screen, COLORS["gray"], (self.bx, self.by), self.r)
    
    def random_dir(self):
        return [-1, 1][randint(0, 1)]
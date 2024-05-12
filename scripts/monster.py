from scripts.constants import *
from scripts.utils import *
import pygame


class Monster:
    def __init__(self, world, position) -> None:
        self.world = world
        self.position = position
        self.rect = FRect((0, 0), MONSTER_SIZE)
        self.ate = False

    def eat(self):
        self.ate = True

    def update(self, input, dt):
        if circle_on_rectangle(
            self.world.candy.position, CANDY_RADIUS, self.position, MONSTER_SIZE
        ):
            self.eat()

        self.rect.center = self.position

    def render(self, screen):
        pygame.draw.rect(screen, MONSTER_COLOR, self.rect)

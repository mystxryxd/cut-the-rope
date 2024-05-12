from scripts.constants import *
from scripts.utils import *

import pygame


class Star:
    def __init__(self, world, position) -> None:
        self.world = world
        self.position = position
        self.rect = FRect((0, 0), STAR_SIZE)
        self.collected = False

    def collect(self):
        self.collected = True

    def update(self, input, dt):
        if not self.collected and circle_on_rectangle(
            self.world.candy.position, CANDY_RADIUS, self.position, STAR_SIZE
        ):
            self.collect()

        self.rect.center = self.position

    def render(self, screen):
        pygame.draw.rect(screen, STAR_COLOR, self.rect)

from scripts.constants import *
from scripts.utils import *

import pygame


class Hook:
    def __init__(self, world, position) -> None:
        self.world = world
        self.position = position

    def render(self, screen):
        pygame.draw.circle(screen, HOOK_COLOR, self.position, HOOK_RADIUS)

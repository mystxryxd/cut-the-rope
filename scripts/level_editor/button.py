from ..input import Input, MouseButton
from ..constants import *
from ..utils import *
import pygame


class Button:
    def __init__(self, position, size, color=Color("WHITE")) -> None:
        self.position = position
        self.size = size
        self.color = color
        self.rect = FRect((0, 0), size)
        self.clicked = False

    def update(self, input: Input, dt):
        self.clicked = False

        if input.just_pressed(MouseButton.LEFT) and point_in_rectangle(
            input.mouse_position(), self.position, self.size
        ):
            self.clicked = True

        self.rect.center = self.position

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

from scripts.constants import *

import pygame


class Point:
    def __init__(
        self,
        position: Vector2,
        prev_position: Vector2,
        radius=POINT_RADIUS,
        color=POINT_COLOR,
    ) -> None:
        self.position = position
        self.prev_position = prev_position
        self.radius = radius
        self.color = color

    def get_velocity(self) -> Vector2:
        return self.position - self.prev_position

    def update(self, dt):
        velocity = self.get_velocity()

        velocity *= 1 - FRICTION

        self.prev_position = self.position.copy()
        self.position += velocity + GRAVITY * dt

from scripts.point import Point
from scripts.input import Input
from scripts.constants import *
from scripts.utils import *
import pygame, math


class Rope:
    def __init__(
        self, world, anchor_position: Vector2, point_count: int, length=None
    ) -> None:
        self.world = world
        self.is_candy_owner = False

        self.point_count = point_count
        self.anchor_position = anchor_position
        self.length = length
        self.connection_length = self.length / self.point_count

        self.cut = False

        self.create_points()

    def set_candy_owner(self):
        self.is_candy_owner = True

        if self.points[-1] in self.stationary_points:
            self.stationary_points.remove(self.points[-1])

    def remove_candy_owner(self):
        self.is_candy_owner = False

    def collides_with_line(
        self, line_start_position: Vector2, line_end_position: Vector2
    ):
        for head, tail in zip(self.points, self.points[1:]):
            if line_on_line(
                line_start_position.x,
                line_start_position.y,
                line_end_position.x,
                line_end_position.y,
                head.position.x,
                head.position.y,
                tail.position.x,
                tail.position.y,
            ):
                return True

        return False

    def create_points(self):
        self.points = [
            Point(
                Vector2(
                    self.anchor_position.x,
                    self.anchor_position.y + i * self.connection_length,
                ),
                Vector2(
                    self.anchor_position.x,
                    self.anchor_position.y + i * self.connection_length,
                ),
            )
            for i in range(self.point_count)
        ]

        self.stationary_points = [self.points[0], self.points[-1]]

    def update_points(self, dt):
        for point in self.points:
            if not point in self.stationary_points:
                point.update(dt)

    def update_constraints(self, dt):
        for head, tail in zip(self.points, self.points[1:]):
            distance = (tail.position - head.position).magnitude()
            distance_diff = abs(distance - self.connection_length)
            mv_ratio = distance_diff

            velocity = Vector2(0, 0)

            if distance > self.connection_length:
                velocity = (head.position - tail.position).normalize()
            elif distance < self.connection_length:
                velocity = (tail.position - head.position).normalize()

            if not head in self.stationary_points:
                head.position -= velocity * mv_ratio * 0.85

            if not tail in self.stationary_points:
                tail.position += velocity * mv_ratio * 0.85

    def update(self, input: Input, dt: float):
        if not self.is_candy_owner:
            self.points[-1].position = self.world.candy.position
            self.points[-1].prev_position = self.world.candy.position

        self.update_points(dt)

        for _ in range(CONSTRAINT_UPDATE_FREQUENCY):
            self.update_constraints(dt)

    def render(self, screen):
        for head, tail in zip(self.points, self.points[1:]):
            pygame.draw.line(screen, Color("WHITE"), head.position, tail.position, 2)

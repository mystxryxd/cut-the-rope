from scripts.input import Input, MouseButton
from scripts.rope import Rope
from scripts.constants import *
from scripts.utils import *
from typing import List

import pygame


class Candy:
    def __init__(self, world, ropes: List[Rope]) -> None:
        self.world = world
        self.ropes = ropes

        self.owner = None
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.swipe_start = None

        self.lost = False

    def swipe(self, mouse_position: Vector2):
        if self.swipe_start == mouse_position:
            return

        for rope in self.ropes:
            if rope.collides_with_line(self.swipe_start, mouse_position):
                rope.cut = True

    def update_position(self, dt):
        if self.owner:
            self.position = self.owner.points[-1].position
            self.velocity = self.owner.points[-1].get_velocity()
        else:
            self.velocity += GRAVITY * dt
            self.position += self.velocity

        if self.position.y > SCREEN_SIZE.y:
            self.lost = True

    def set_owner(self, rope: Rope):
        if self.owner and self.owner != rope:
            self.owner.remove_candy_owner()

        self.owner = rope
        rope.set_candy_owner()

    def compute_owner(self):
        if len(self.ropes) > 0:
            shortest_rope = self.ropes[0]

            for rope in self.ropes[1:]:
                if rope.length < shortest_rope.length:
                    shortest_rope = rope

            self.set_owner(shortest_rope)
        else:
            self.owner = None

    def remove_cut_ropes(self):
        for rope in self.ropes:
            if rope.cut:
                self.ropes.remove(rope)

    def update_ropes(self, input: Input, dt: float):
        for rope in self.ropes:
            rope.update(input, dt)

    def update(self, input: Input, dt: float):
        if input.just_pressed(MouseButton.LEFT):
            self.swipe_start = input.mouse_position()

        if input.just_released(MouseButton.LEFT) and self.swipe_start:
            self.swipe(input.mouse_position())

        self.remove_cut_ropes()
        self.compute_owner()
        self.update_position(dt)
        self.update_ropes(input, dt)

    def render_ropes(self, screen):
        for rope in self.ropes:
            rope.render(screen)

    def render(self, screen):
        self.render_ropes(screen)

        pygame.draw.circle(screen, CANDY_COLOR, self.position, CANDY_RADIUS)

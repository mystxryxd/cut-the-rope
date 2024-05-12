from scripts.constants import *
import pygame


class MouseButton:
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3


class Input:
    def __init__(self, game) -> None:
        self.game = game

        self._pressed = {}
        self._just_pressed = {}
        self._just_released = {}

    def mouse_position(self) -> Vector2:
        return Vector2(pygame.mouse.get_pos())

    def pressed(self, key):
        return self._pressed.get(key)

    def just_pressed(self, key):
        return self._just_pressed.get(key)

    def just_released(self, key):
        return self._just_released.get(key)

    def process(self):
        for event in pygame.event.get():
            if event.type in (KEYDOWN, MOUSEBUTTONDOWN):
                key = event.key if event.type == KEYDOWN else event.button

                self._pressed[key] = True
                self._just_pressed[key] = True

            if event.type in (KEYUP, MOUSEBUTTONUP):
                key = event.key if event.type == KEYUP else event.button

                self._pressed[key] = False
                self._just_released[key] = True

            if event.type == QUIT:
                self.game.quit()

    def flush(self):
        self._just_pressed.clear()
        self._just_released.clear()

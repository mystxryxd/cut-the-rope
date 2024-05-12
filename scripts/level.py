from scripts.constants import *
from scripts.candy import Candy
from scripts.monster import Monster
from scripts.rope import Rope
from scripts.star import Star
from scripts.hook import Hook
from typing import List, Dict
from copy import deepcopy
from pprint import pprint
import pygame


class Level:
    def __init__(self, game) -> None:
        self.game = game
        self.current_level = 2

        self.candy: Candy = None
        self.monster: Monster = None
        self.stars: List[Star] = []
        self.hooks: List[Hook] = []

        self.level_data = self.get_converted_level_data()

        self.load_next_level()

    def get_converted_level_data(
        self,
    ):
        new_level_data: Dict = deepcopy(LEVEL_DATA)

        for level, level_data in new_level_data.items():
            for entity_type, entities in level_data.items():
                for entity in entities:
                    if "position" in entity:
                        entity["position"] = Vector2(
                            SCREEN_SIZE.x * entity["position"][0],
                            SCREEN_SIZE.y * entity["position"][1],
                        )

                    if "length" in entity:
                        entity["length"] = SCREEN_SIZE.y * entity["length"]

        return new_level_data

    def load_next_level(self):
        self.current_level += 1
        self.load_level(self.current_level)

    def restart_level(self):
        self.load_level(self.current_level)

    def load_level(self, level: int):
        level = str(level)

        if not level in self.level_data:
            raise IndexError(f"No level {level}")

        level_data = self.level_data[level]

        self.hooks = [Hook(self, rope["position"]) for rope in level_data["ropes"]]
        self.stars = [Star(self, star["position"]) for star in level_data["stars"]]
        self.monster = Monster(self, level_data["monster"][0]["position"])
        self.candy = Candy(
            self,
            [
                Rope(self, rope["position"], POINT_COUNT, rope["length"])
                for rope in level_data["ropes"]
            ],
        )

    def update(self, input, dt):
        for star in self.stars:
            star.update(input, dt)

            if star.collected:
                self.stars.remove(star)

        self.candy.update(input, dt)
        self.monster.update(input, dt)

        if self.candy.lost:
            self.restart_level()

        if self.monster.ate:
            self.load_next_level()

    def render(self, screen):
        for hook in self.hooks:
            hook.render(screen)

        for star in self.stars:
            star.render(screen)

        self.monster.render(screen)
        self.candy.render(screen)

from pygame import Vector2, Color, Surface, Rect, FRect
from pygame.constants import *
import pygame, json, os, regex

pygame.init()
pygame.font.init()

GAME_TITLE = "Cut the rope"
FPS = 60

SCREEN_SIZE = Vector2(400, 700)

BACKGROUND_COLOR = Color(44, 44, 44)

GRAVITY = Vector2(0, 20)
FRICTION = 0.0005
CONSTRAINT_UPDATE_FREQUENCY = 80

POINT_RADIUS = 1
POINT_COUNT = 35
POINT_COLOR = Color(240, 240, 240)

CANDY_RADIUS = 12
CANDY_COLOR = Color("Red")

MONSTER_SIZE = Vector2(50, 50)
MONSTER_COLOR = Color("Green")

STAR_SIZE = Vector2(20, 20)
STAR_COLOR = Color("Yellow")

HOOK_RADIUS = 10
HOOK_COLOR = Color("Blue")

JETBRAINS_MONO = pygame.font.SysFont("JetBrainsMono", 15)

LEVEL_DATA = {}

for level_data_file_name in os.listdir("assets/level_data"):
    with open(f"assets/level_data/{level_data_file_name}") as l:
        LEVEL_DATA[regex.search(r"\d+", level_data_file_name).group(0)] = json.load(l)

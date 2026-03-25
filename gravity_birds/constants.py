from __future__ import annotations

WIDTH = 1920
HEIGHT = 1080
FPS = 60
PHYSICS_STEP = 1 / 120

SKY_TOP = (12, 24, 53)
SKY_BOTTOM = (94, 162, 213)
GROUND = (104, 78, 57)
TEXT = (244, 240, 227)
SUBTLE = (180, 198, 212)
PANEL = (10, 18, 36, 210)
ACCENT = (245, 186, 75)
SUCCESS = (143, 217, 104)
DANGER = (250, 115, 97)

SLING_ANCHOR = (250, 770)
MAX_PULL = 155
BASE_LAUNCH_SPEED = 7.4

BIRD_DATA = {
    "red": {
        "color": (220, 73, 65),
        "outline": (122, 24, 21),
        "radius": 22,
        "label": "Red",
        "description": "Базовая птица без спецспособностей.",
        "launch_scale": 1.0,
    },
    "black": {
        "color": (36, 36, 46),
        "outline": (214, 172, 92),
        "radius": 25,
        "label": "Black Bomb",
        "description": "Взрывается при первом сильном касании.",
        "launch_scale": 0.95,
    },
    "blue": {
        "color": (91, 175, 236),
        "outline": (24, 74, 126),
        "radius": 18,
        "label": "Blue Triplet",
        "description": "После запуска делится на три птицы.",
        "launch_scale": 1.05,
    },
    "yellow": {
        "color": (247, 204, 65),
        "outline": (125, 80, 0),
        "radius": 20,
        "label": "Yellow Boost",
        "description": "Летит быстрее и может ускориться в полете.",
        "launch_scale": 1.22,
    },
}

MATERIALS = {
    "wood": {"color": (165, 114, 70), "outline": (92, 58, 29), "density": 0.7, "hp": 240},
    "stone": {"color": (121, 130, 150), "outline": (67, 74, 86), "density": 1.25, "hp": 460},
    "glass": {"color": (152, 228, 235), "outline": (75, 146, 155), "density": 0.5, "hp": 125},
}

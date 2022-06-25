"""Config module for baby screen lock game"""
import os
import pygame as pg

pg.init()

# Colors
BLACK = pg.Color(0, 0, 0)
COL_1 = pg.Color(255, 0, 0)
COL_2 = pg.Color(255, 127, 0)
COL_3 = pg.Color(255, 255, 0)
COL_4 = pg.Color(0, 255, 0)
COL_5 = pg.Color(0, 255, 127)
COL_6 = pg.Color(0, 255, 255)
COL_7 = pg.Color(0, 0, 255)
COL_8 = pg.Color(127, 0, 255)
COL_9 = pg.Color(255, 0, 255)

# Globals
INFO_OBJ = pg.display.Info()
SCREEN_RECT = pg.Rect(0, 0, INFO_OBJ.current_w, INFO_OBJ.current_h)
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)
SCREEN_NINTH = int(SCREEN_RECT.w/9)

# Text rendering
def print_text(text, color, text_font, surface, pos):
    text = text_font.render(text, 1, color)
    text_pos = text.get_rect(center=pos)
    surface.blit(text, text_pos)

NORMAL_FONT = pg.font.Font(None, 50)

# Images
def load_image(name):
    """Function for loading images from the 'resources' folder"""
    fullname = os.path.join("assets", name)
    try:
        image = pg.image.load(fullname)
    except pg.error as message:
        print("Cannot load image:", name)
        raise SystemExit(message)
    image = image.convert_alpha()

    return image

CLOSE_BTN = "close.png"

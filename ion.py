# ion.py (PC mock)
# No need to port on Numworks as
# the `ion` lib already exists there
# this script just emulates it
# Credits: ZetaMap

import keyboard


# Useless
KEY_BACK = "backspace"
KEY_HOME = "escape"
KEY_ONOFF = "end" #??

# Upper keys
KEY_OK = "space"

KEY_UP = "up"
KEY_DOWN = "down"
KEY_LEFT = "left"
KEY_RIGHT = "right"

# Keys per row:

KEY_SHIFT = "shift"
KEY_ALPHA = "ctrl"
KEY_XNT = "x"
KEY_VAR = "v"
KEY_TOOLBOX = "\""
KEY_BACKSPACE = "del"

KEY_EXP = "e"
KEY_LN = "n"
KEY_LOG = "l"
KEY_IMAGINARY = "i"
KEY_COMMA = ","
KEY_POWER = "^"

KEY_SINE = "s"
KEY_COSINE = "c"
KEY_TANGENT = "t"
KEY_PI = "p"
KEY_SQRT = "r"
KEY_SQUARE = ">"

KEY_SEVEN = "7"
KEY_EIGHT = "8"
KEY_NINE = "9"
KEY_LEFTPARENTHESIS = "("
KEY_RIGHTPARENTHESIS = ")"

KEY_FOUR = "4"
KEY_FIVE = "5"
KEY_SIX = "6"
KEY_MULTIPLICATION = "*"
KEY_DIVISION = "/"

KEY_ONE = "1"
KEY_TWO = "2"
KEY_THREE = "3"
KEY_PLUS = "+"
KEY_MINUS = "-"

KEY_ZERO = "0"
KEY_DOT = "."
KEY_EE = "!"
KEY_ANS = "a"
KEY_EXE = "enter"

ALL_KEYS: list[str] = [
    KEY_BACK, KEY_HOME, KEY_ONOFF, KEY_OK,
    KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT,
    KEY_SHIFT, KEY_ALPHA, KEY_XNT, KEY_VAR, KEY_TOOLBOX, KEY_BACKSPACE,
    KEY_EXP, KEY_LN, KEY_LOG, KEY_IMAGINARY, KEY_COMMA, KEY_POWER,
    KEY_SINE, KEY_COSINE, KEY_TANGENT, KEY_PI, KEY_SQRT, KEY_SQUARE,
    KEY_SEVEN, KEY_EIGHT, KEY_NINE, KEY_LEFTPARENTHESIS, KEY_RIGHTPARENTHESIS,
    KEY_FOUR, KEY_FIVE, KEY_SIX, KEY_MULTIPLICATION, KEY_DIVISION,
    KEY_ONE, KEY_TWO, KEY_THREE, KEY_PLUS, KEY_MINUS,
    KEY_ZERO, KEY_DOT, KEY_EE, KEY_ANS, KEY_EXE
]

def keydown(key: str):
    """Returns True if the key is pressed"""
    if not key in ALL_KEYS:
       print(f"Key {key} doesn't exist!")
       return
    return keyboard.is_pressed(key)


def get_keys():
    """Get names of currently pressed keys"""
    pressed_keys: list[str] = []
    for key in ALL_KEYS:
        if keyboard.is_pressed(key):
            pressed_keys.append(key)
    return pressed_keys

# All the following functions only give a fake result to give a real look of library
def battery():
    """Return battery voltage"""
    voltage = 4.2
    return voltage

def battery_level() -> int:
    """Return battery level"""
    level = 3
    return level

def battery_ischarging() -> bool:
    """Return True if the battery is charging"""
    charging = True
    return charging

def set_brightness(level: int, /):
    """Set brightness level of screen"""
    pass

def get_brightness() -> int:
    """Get brightness level of screen"""
    brightness = 240
    return brightness

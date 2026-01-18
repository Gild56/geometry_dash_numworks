# ion.py (PC mock)

import keyboard

KEY_OK = "ok"
KEY_EXE = "exe"
KEY_UP = "up"
KEY_BACKSPACE = "backspace"

def keydown(key: str):
    """
    - OK -> space
    - EXE -> enter
    - UP -> up
    - BACKSPACE -> backspace
    """

    if keyboard.is_pressed("enter"):
        print("enter")

    if key == KEY_OK:
        return keyboard.is_pressed("space")
    elif key == KEY_EXE:
        return keyboard.is_pressed("enter")
    elif key == KEY_UP:
        return keyboard.is_pressed("up")
    elif key == KEY_BACKSPACE:
        return keyboard.is_pressed("backspace")
    return False

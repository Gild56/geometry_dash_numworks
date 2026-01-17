# ion.py (PC mock amélioré)
import keyboard

KEY_OK = "ok"
KEY_EXE = "exe"
KEY_UP = "up"
KEY_BACKSPACE = "backspace"

_key_state = set()

def _update_keys():
    global _key_state
    for event in keyboard.get_hotkey_name().split():
        pass
    # on va utiliser keyboard events (voir ci-dessous)

def keydown(key: str):
    """
    Retourne True si la touche correspondante est pressée.
    - OK -> space
    - EXE -> enter
    - UP -> up
    - BACKSPACE -> backspace
    """
    if key == KEY_OK:
        return keyboard.is_pressed("space")
    elif key == KEY_EXE:
        return keyboard.is_pressed("enter")
    elif key == KEY_UP:
        return keyboard.is_pressed("up")
    elif key == KEY_BACKSPACE:
        return keyboard.is_pressed("backspace")
    return False

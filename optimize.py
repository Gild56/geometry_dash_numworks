import re

INPUT_FILE = "gd.py"
OUTPUT_FILE = "optimized.py"

INDENT_SIZE = 1

REPLACE_DICT = {
    "BLOCKS": "0",
    "SPIKES": "1",
    "END": "2",
    "BG_COLOR": "3",
    "BLOCKS_COLOR": "4",
    "NAME": "5",
    "RECORD": "6",
    "ATTEMPTS": "7",
    "AUTHOR": "8",
    "JUMP_PADS": "9",
    "JUMPS": "10",
    "COINS": "11",
    "TICK": "1/30",
    "speed": "6",
    "RESPAWN_TIME": "1",
    "SCREEN_WIDTH": "320",
    "SCREEN_HEIGHT": "222",
    "TILE_SIZE_X": "10",
    "CHARACTER_WIDTH": "10",
    "CHARACTER_HEIGHT": "18",
    "CHARACTERS_LIMIT": "32",
    "PLAYER_WIDTH": "20",
    "PLAYER_HEIGHT": "20",
    "DARK_GREEN": "(0,150,0)",
    "DARK_BLUE": "(0,0,150)",
    "RED": "(255,0,0)",
    "GREEN": "(0,255,0)",
    "BLACK": "(0,0,0)",
    "WHITE": "(255,255,255)",
    "YELLOW": "(255,255,0)",
    "PINK": "(255,150,150)",
    "PURPLE": "(255,0,255)",
    "BLUE": "(0,0,255)",
    "GREY": "(170,170,170)",
    "BROWN": "(117,39,0)",
    "COIN_SIDE": "20",
    "MAIN_MENU_COLOR": "(0,60,255)",
    "GARAGE_MENU_COLOR": "(131,63,0)",
    "VERSION": '"v1.2.0"',
    "current_level": "cl",
    "map_offset_x": "mx",
    "player_x": "px",
    "player_y": "py",
    "True": "1",
    "False": "0",
    "levels": "l",
    "draw_centered_string": "dc",
    "": "",
    "": "",
    "": "",
    #"": "",
}

OP_REPLACEMENTS = [
    (" = ","="),
    (" + ","+"),
    (" - ","-"),
    (" * ","*"),
    (" / ","/"),
    (" == ","=="),
    (" != ","!="),
    (" >= ",">="),
    (" <= ","<="),
    (", ",","),
    (": ",":"),
]

def strip_comment(line: str):
    return line.split("#",1)[0]

def reduce_indentation(line: str):
    line = line.replace("\t"," "*INDENT_SIZE)
    m = re.match(r"^( +)",line)
    if not m:
        return line
    spaces = len(m.group(1))
    levels = spaces//4
    return " "*(levels*INDENT_SIZE) + line[m.end():]

def optimize_line(line: str):
    line = strip_comment(line).rstrip()
    line = reduce_indentation(line)

    if re.match(r"\s*print\s*\(", line):
        return ""

    for o,n in OP_REPLACEMENTS:
        line = line.replace(o, n)

    for k,v in REPLACE_DICT.items():
        line = re.sub(rf"\b{k}\b", v, line)


    return line

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        src = f.read()
    lines = src.splitlines()

    out=[]
    for l in lines:
        l=optimize_line(l)
        if l.strip():
            out.append(l)

    result="\n".join(out)

    with open(OUTPUT_FILE,"w",encoding="utf-8") as f:
        f.write(result)

    print("optimized.py generated")
    print("Lines:", len(lines), "→", len(out))
    print("Chars:", len(src), "→", len(result))
    print("Gain:", round(100 - (len(result) / len(src)) * 100, 2), "%")

if __name__=="__main__":
    main()
# Ce fichier n'a pas besoin d'être optimisé, mais lisible!!!
# Code pour supprimer les print() et les annotations de types, remplacer True / False par 1 / 0
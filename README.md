# Geometry Works

A recreation of Geometry Dash on Numworks calculators (MicroPython 1.17 compatible with Python 3.4).

Four levels available for now :D

Donwnload the libs: `pip install -m requirements.py` and execute `gd.py` to play the game!


## PC Emulator Controls

| Numworks  | Keyboard    |
|-----------|-------------|
| OK        | Space       |
| EXE       | Enter       |
| Backspace | Del         |
| Up        | Up Arrow    |
| Left      | Left Arrow  |
| Right     | Right Arrow |


## Levels

To build your own levels you will need to modify `levels: list[list[Any]]`

| Type                      | Index | Meaning
|---------------------------|-------|--------------------------------------------------------------------|
| list[int, int, int, int], | [0]   | blocks[x_tile, y_tile, width_tiles, height_tiles]                  |
| list[int, int, int],      | [1]   | spikes[x_tile, y_tile, orientation (0=normal / 1=upside down)]     |
| int,                      | [2]   | level end (mesured in tiles)                                       |
| tuple[int, int, int],     | [3]   | background color (red, green, blue)                                |
| tuple[int, int, int],     | [4]   | blocks color (red, green, blue)                                    |
| str,                      | [5]   | level name                                                         |
| float,                    | [6]   | record (initially 0)                                               |
| int,                      | [7]   | attempts (initially 0)                                             |
| str                       | [8]   | author of the level                                                |
| list[int, int]            | [9]   | jump pads[x, y]                                                    |

Example of use:

`levels[current_level][5]`

Gets the name of the current level

`current_level` should go from `0` to `len(levels) - 1`


## Credits

- [Calm_Repeat_7267](https://www.reddit.com/r/numworks/comments/s60imu/i_made_geometry_dash_on_my_calculator/?tl=fr)
- [wperez274](https://my.numworks.com/python/wperez274/geometry_dash_x)
- [ZetaMap](https://github.com/ZetaMap/Ion-numworks/tree/main/src/ion)
- [NumWorks Team](https://github.com/numworks/epsilon)
- [PyGame Team](https://www.pygame.org/news)


## Thanks to:

Minh, Roxy, Malo, Lowan, Matthieu for playtesting, suggesting ideas, etc...

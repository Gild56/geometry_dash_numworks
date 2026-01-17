from time import sleep
from random import randint
from kandinsky import fill_rect as FILL
from kandinsky import draw_string as STR
from ion import KEY_BACKSPACE, KEY_OK, KEY_EXE, KEY_UP, keydown as KEY

bg_color=(0, 0, 0)

FILL(0, 0, 322, 222, bg_color)
while not KEY(KEY_EXE):
    FILL(0, 10, 322, 5, "red")
    FILL(0, 50, 322, 5, "red")

    FILL(0, 180, 322, 2, "red")

    STR("Geometry Dash", 90, 25, "white", bg_color)
    STR("Key [Up]/[OK] = Jump", 40, 80, "white", bg_color)
    STR("Key [Backspace] = Pause/Resume", 10, 120, "cyan", bg_color)

lives = 6
score = 0
energy= 40
game = True

bg_color = (randint(210, 255), randint(210, 255), randint(210, 255))
player_color = (randint(0, 155), randint(0, 155), randint(0, 155))
ground_color = (randint(0, 55), randint(0, 55), randint(0, 55))

Level = tuple[
    list[list[int]],    # blocks
    list[list[int]],    # spikes
    int,                # level end
    tuple[int,int,int], # bg color
    tuple[int,int,int]  # ground
]

levels: list[Level] = [
    (
        [
            [0, 6, 32, 1], [32, 5, 58, 2], [90, 4, 30, 3], [108, 3, 12, 1], [120, 6, 74, 1], [128, 3, 8, 1], [132, 2, 22, 1], [150, 1, 26, 1], [162, 5, 32, 1], [172, 2, 20, 1], [202, 5, 42, 2], [248, 4, 4, 3], [254, 5, 4, 2], [260, 6, 16, 1]
        ],
        [
            [218, 5, 0], [133, 4, 1], [42, 5, 0], [52, 5, 0], [62, 5, 0], [73, 5, 0], [82, 5, 0], [144, 6, 0], [146, 6, 0], [142, 2, 0], [151, 1, 0], [164, 1, 0], [160, 6, 0], [166, 5, 0], [153, 3, 1], [158, 2, 1], [176, 3, 1], [220, 5, 0], [230, 5, 0], [240, 5, 0], [268, 6, 0]
        ],
        276, (0, 130, 240), (0, 0, 70)
    ),
    (
        [
            [0, 6, 32,1], [28, 5, 26, 1], [42, 4, 12, 1], [62, 5, 24, 1], [82, 4, 4, 1], [94, 6, 108, 1], [94, 5, 42, 1], [94, 4, 38, 1], [118, 3, 14, 1], [138, 3, 8, 1], [142, 2, 24, 1], [162, 3, 8, 1], [174, 5, 14, 1], [206, 6, 4, 1], [216, 6, 20, 1], [240, 5, 10, 1], [254, 4, 8, 1], [266, 3, 6, 1], [32, 6, 54, 1]
        ],
        [
            [158, 6, 0], [159, 2, 0], [126, 3, 0], [106, 4, 0], [104, 4, 0], [73, 5, 0], [63, 5, 0], [50, 4, 0], [35, 5, 0], [124, 3, 0], [149, 2, 0], [151, 2, 0], [157, 2, 0], [150, 6, 0], [156, 6, 0], [195, 6, 0], [224, 6, 0], [226, 6, 0], [181, 5, 0],[244,5,0]
        ],
        272, (0, 250, 80), (0, 70, 70)
    ),
    (
        [
            [0, 6, 32, 1], [172, 6, 42, 1], [110, 6, 24, 1], [66, 4, 32, 1], [56, 5, 46, 2], [52, 5, 2, 2], [32, 5, 18, 2], [120, 5, 4, 1], [120, 3, 4, 1], [140, 5, 4, 2], [148, 4, 4, 3], [154, 3, 4, 4], [160, 4, 4, 3], [166, 5, 4, 2], [220, 6, 52, 1], [248, 5, 24, 1], [258, 4, 14, 1]
        ],
        [
            [184, 6, 0], [169, 5, 0], [167, 5, 0], [121, 3, 0], [123, 3, 0], [92, 4, 0], [53, 5, 0], [41, 5, 0], [83, 4, 0], [74, 4, 0], [186, 6, 0], [194, 6, 0], [202, 6, 0], [204, 6, 0], [217, 6, 1], [217, 6, 0], [249, 5, 0], [230, 6, 0], [239, 6, 0], [259, 4, 0]
        ],
        272, (200, 0, 0), (50, 0, 0)
    ),
    (
        [
            [0, 6, 32, 1], [48, 4, 23, 1], [35, 5, 36, 1], [32, 6, 77, 1], [104, 5, 5, 1], [79, 5, 14, 1]
        ],
        [
            [92, 5, 0], [80, 5, 0], [59, 4, 0], [61, 4, 0], [36, 5, 0], [20, 6, 0], [103, 6, 0]
        ],
        109, (0, 190, 190), (0, 30, 30)
    )
]

sleep(0.5)

game_started = False
start_prompt_timer = False

current_level = False

is_falling = False

player_x = 50
player_y = 50
can_jump = True

map_offset_x = 0

level_completed = False
is_jumping = False

jump_velocity = 38
air_ticks = 0

FILL(0, 0, 320, 222, bg_color)

player_width = 20
player_height = 20

def draw_player(color: tuple[int, int, int]):
    global player_width, player_height
    FILL(player_x, player_y, player_width, player_height, color)

def draw_spike(x_tile: int, y_tile: int, orientation: int):
    for i in range(5):
        FILL(
            map_offset_x + x_tile * 10 - 10 + i * 2,
            y_tile * 32 - i * 4 + (2 * i * 4 * orientation) - 4 * (1 - orientation), 20 - i * 4, 4, ground_color
        )
        FILL(
            map_offset_x + x_tile * 10 + 10 - i * 2,
            y_tile * 32 - i * 4 + (2 * i * 4 * orientation) - 4 * (1 - orientation), 6, 4, bg_color
        )

def draw_platform(x_tile: int, y_tile: int, width_tiles: int, height_tiles: int):
    FILL(
        map_offset_x + x_tile * 10, y_tile * 32,
        10 * width_tiles, height_tiles * 32, ground_color
    )

    if width_tiles < 0:
        FILL(map_offset_x + x_tile * 10, y_tile * 32, 6, height_tiles * 32, bg_color)
    else:
        FILL(map_offset_x + x_tile * 10 + width_tiles * 10, y_tile * 32, 6, height_tiles*32, bg_color)

def height_tiles(tile_x: int):
    FILL(map_offset_x + tile_x * 10, 0, 10, 222, (0, 255, 0))
    FILL(map_offset_x + tile_x * 10 + 10, 0, 6, 222, bg_color)

def draw_level():
    for i in range(len(levels[current_level][0])):
        if (
            map_offset_x+levels[current_level][0][i][0] * 10 < 320
            and map_offset_x+levels[current_level][0][i][0] * 10 + levels[current_level][0][i][2] * 10 > -10
        ):
            draw_platform(
                levels[current_level][0][i][0],
                levels[current_level][0][i][1],
                levels[current_level][0][i][2],
                levels[current_level][0][i][3]
            )

    for j in range(len(levels[current_level][1])):
        if -10 < map_offset_x+levels[current_level][1][j][0] * 10 + 20 < 340:
            draw_spike(
                levels[current_level][1][j][0],
                levels[current_level][1][j][1],
                levels[current_level][1][j][2]
            )

    height_tiles(levels[current_level][2])

draw_level()
draw_player(player_color)


def check_collision():
    collision_detected = False
    for i in range(len(levels[current_level][0])):
        if (
            player_x + 20 < levels[current_level][0][i][0] * 10 + map_offset_x
            or player_x > levels[current_level][0][i][0] * 10 + levels[current_level][0][i][2] * 10 + map_offset_x
            or player_y < levels[current_level][0][i][1] * 32
            or player_y > levels[current_level][0][i][1] * 32 + levels[current_level][0][i][3] * 32
        ):
            collision_detected = False
        else:
            collision_detected = True
            break
    if collision_detected == False:
        for i in range(len(levels[current_level][1])):
            if (
                player_x + 20 < levels[current_level][1][i][0] * 10 + map_offset_x
                or player_x > levels[current_level][1][i][0] * 10 + 15 + map_offset_x
                or player_y > levels[current_level][1][i][1] * 32 + levels[current_level][1][i][2] * 32
                or player_y < levels[current_level][1][i][1] * 32 - (1 - levels[current_level][1][i][2]) * 32
            ):
                collision_detected = False
            else:
                collision_detected = True
                break
    return collision_detected


while game:
    STR("Score:" + str(score), 0, 0, "cyan", "black")
    STR("Lives:" + str(lives), 240, 0, "green", "black")

    if game_started==0:

        STR("Press [EXE] to Randomize", 20, 110)
        STR("the Theme!", 20, 130)

        if KEY(KEY_EXE):
            sleep(0.2)
            bg_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            ground_color = (randint(0, 255),randint(0, 255),randint(0, 255))
            FILL(0, 0, 320, 222, bg_color)
            draw_level()
            draw_player(player_color)

        if KEY(KEY_OK) or KEY(KEY_EXE):
            FILL(0, 0, 322, 222, bg_color)
            game_started = True
            start_prompt_timer = 80

        if start_prompt_timer < 50:
            STR("Press [OK] to Start", 40, 50, ground_color, bg_color)
            start_prompt_timer += 1

        if start_prompt_timer > 49:
            STR("Press [OK] to Start", 40, 50, bg_color, bg_color)
            start_prompt_timer += 1

        if start_prompt_timer > 79:
            start_prompt_timer = 0

    if game_started==True:
        if is_jumping == False and level_completed == False:
            for i in range(len(levels[current_level][0])):
                if (
                    player_y + 20 == levels[current_level][0][i][1] * 32 and levels[current_level][0][i][0] * 10 + map_offset_x -19 <= 50 <= levels[current_level][0][i][2] * 10 + levels[current_level][0][i][0] * 10 + map_offset_x
                ):
                    can_jump = True
                    is_falling=False
                    break
                else:
                    can_jump = False
                    is_falling = True

            if is_falling == True:
                draw_player(bg_color)
                player_y += 16
                draw_player(player_color)

            if (
                KEY(KEY_OK) and can_jump == True
                or KEY(KEY_UP) and can_jump == True
            ):
                draw_player(bg_color)
                jump = True
                player_y -= int(jump_velocity)
                jump_velocity = jump_velocity / 2
                draw_player(player_color)

    if is_jumping == True and level_completed==False and can_jump==True:
        draw_player(bg_color)

        for k in range(len(levels[current_level][0])):
            if player_y + 20 != levels[current_level][0][k][1] * 32:
                is_jumping = True
            elif (
                levels[current_level][0][k][0] * 10 + map_offset_x-19 < 50 < levels[current_level][0][k][0] * 10 + map_offset_x + levels[current_level][0][k][2] * 10 + 20
            ):
                is_jumping = False
            break

        if is_jumping == True:
            player_y -= int(jump_velocity)
            if jump_velocity > 2:
                jump_velocity = jump_velocity / 2
            elif jump_velocity == 2:
                jump_velocity = 0
            elif jump_velocity == 0:
                air_ticks += 1

            if air_ticks == 4:
                air_ticks = 0
                jump_velocity =- 2
            elif jump_velocity <= (-2) and jump_velocity > (-32):
                jump_velocity=jump_velocity*2
            else:
                jump = False
                jump_velocity = 32
                can_jump = True
        else:
            jump = False
            jump_velocity = 32
            can_jump = True

    draw_player(player_color)

    if level_completed==False:
        map_offset_x-=6
        draw_level()

    else:  # level completed
        STR("MISSION COMPLETE!!", 100, 50, ground_color, bg_color)
        STR("Press [OK] key", 110, 150, ground_color, bg_color)
        game = False

    if player_y + player_height > 222 or check_collision():  # player crashes
        lives -= 1

        #randomize colors
        bg_color = (randint(210, 255), randint(210, 255), randint(210, 255))
        ground_color = (randint(0, 55), randint(0, 55), randint(0, 55))
        player_color = (randint(0, 155), randint(0, 155), randint(0, 155))

        FILL(0, 0, 320, 222, bg_color)
        map_offset_x = 0
        player_y = 172

    if lives < 1:
        game = False
    sleep(0.03)

    if player_x + player_width > levels[current_level][2] * 10 + map_offset_x:
        level_completed = True

    if level_completed == True and KEY(KEY_OK):
        sleep(0.5)
        if not KEY(KEY_OK):
            game_started=False
            FILL(0, 0, 320, 222, bg_color)
            map_offset_x = 0
            player_y = 172
            level_completed = False
            draw_level()
            draw_player(player_color)

    if KEY(KEY_OK) or KEY(KEY_UP):
        score+=randint(5,20)
        energy+=0.2

    if energy > 10:
        energy = 0
        lives += 1
        FILL(player_x, player_y, player_width, player_height, "green")

    if KEY(KEY_BACKSPACE):
        STR("(PAUSED)", 110, 60, "black", bg_color)
        STR("Press [Backspack] to Resume", 15, 100, "blue", bg_color)
        while KEY(KEY_BACKSPACE):
            pass
        while not KEY(KEY_BACKSPACE):
            pass
        while KEY(KEY_BACKSPACE):
            STR("        ", 110, 60, bg_color, bg_color)
            STR("                            ", 15, 100, bg_color, bg_color)
        pass

FILL(0, 0, 322, 222, "black")
STR("GAME OVER", 100, 100, "green", "black")
STR("SCORE:" + str(score), 100, 140, "white", "black")

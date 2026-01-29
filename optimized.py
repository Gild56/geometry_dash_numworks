from random import choice
from time import monotonic
from kandinsky import fill_rect,draw_string
from time import sleep
from ion import (
 KEY_OK,KEY_EXE,KEY_UP,
 KEY_LEFT,KEY_RIGHT,KEY_BACKSPACE,
 KEY_SHIFT,KEY_SEVEN,keydown
)
l=[
 [
  [
   [0,6,32,1],[48,4,23,1],[35,5,36,1],[32,6,77,1],[104,5,5,1],[79,5,14,1]
  ],
  [
   [20,6,0],[36,5,0],[59,4,0],[61,4,0],[80,5,0],[92,5,0],[103,6,0]
  ],
  109,(0,190,190),(0,30,30),"Gild Madness",0,0,"wperez274",[[13,5]],0,[[13,3,0],[17,3,0]]
 ],
 [
  [
   [0,6,32,1],[28,5,26,1],[42,4,12,1],[62,5,24,1],[82,4,4,1],[94,6,108,1],[94,5,42,1],[94,4,38,1],[118,3,14,1],[138,3,8,1],[142,2,24,1],[174,5,14,1],[206,6,4,1],[216,6,20,1],[240,5,10,1],[254,4,8,1],[266,3,6,1],[32,6,54,1]
  ],
  [
   [35,5,0],[50,4,0],[63,5,0],[73,5,0],[104,4,0],[106,4,0],[124,3,0],[126,3,0],[149,2,0],[150,6,0],[151,2,0],[156,6,0],[157,2,0],[158,6,0],[159,2,0],[181,5,0],[195,6,0],[224,6,0],[226,6,0],[244,5,0]
  ],
  272,(0,250,80),(0,70,70),"Back in Green",0,0,"wperez274",[],0,[]
 ],
 [
  [
   [0,6,32,1],[32,5,58,2],[90,4,30,3],[108,3,12,1],[120,6,74,1],[128,3,8,1],[132,2,22,1],[150,1,26,1],[162,5,32,1],[172,2,20,1],[202,5,42,2],[248,4,4,3],[254,5,4,2],[260,6,16,1]
  ],
  [
   [42,5,0],[52,5,0],[62,5,0],[73,5,0],[82,5,0],[133,4,1],[142,2,0],[144,6,0],[146,6,0],[151,1,0],[153,3,1],[158,2,1],[160,6,0],[164,1,0],[166,5,0],[176,3,1],[218,5,0],[220,5,0],[230,5,0],[240,5,0],[268,6,0]
  ],
  276,(0,130,240),(0,0,70),"Polablue",0,0,"Calm_Repeat_7267",[],0,[]
 ],
 [
  [
   [0,6,32,1],[172,6,42,1],[110,6,24,1],[66,4,32,1],[56,5,46,2],[52,5,2,2],[32,5,18,2],[120,5,4,1],[120,3,4,1],[140,5,4,2],[148,4,4,3],[154,3,4,4],[160,4,4,3],[166,5,4,2],[220,6,52,1],[248,5,24,1],[258,4,14,1]
  ],
  [
   [41,5,0],[53,5,0],[74,4,0],[83,4,0],[92,4,0],[121,3,0],[123,3,0],[167,5,0],[169,5,0],[184,6,0],[186,6,0],[194,6,0],[202,6,0],[204,6,0],[217,6,1],[217,6,0],[230,6,0],[239,6,0],[249,5,0],[259,4,0]
  ],
  272,(180,0,0),(50,0,0),"Dry Red",0,0,"wperez274",[],0,[]
 ]
]
endscreen_sentences=[
 "This is a serious question","Don't hack like uranium",
 "Ty Roxy for playtesting","Ty Minh for playtesting",
 "Ty Ihv2010 for support","Subscribe to Gild56 on YT",
 "Eat,sleep,dash,repeat","C'est très fort"
]
new_best_sentences=[
 "brih","yea","wiw","loll","wot","wha","xd",
 "Nope","Pauvre jeune homme...","RIP"
]
if __name__=="__main__":
 game=1
else:
 game=0
hitboxes=0
percentage=0
menu_button=2
max_menu_buttons=3
menu="main"
percentage_label=""
cl=0
start_wait=None
clicked=0
attempts=0
current_coins_taken=[]
coins_just_taken=[]
total_attempts=0
total_jumps=0
total_coins=0
max_coins=0
for level in l:
 max_coins += len(level[11])
px=50
py=172
mx=0
can_jump=1
is_jumping=0
is_falling=0
jump_velocity=32
air_ticks=0
took_pad=0
bg_color=(0,0,0)
player_color=(255,255,0)
blocks_color=(0,0,0)
color_chosen=1
colors=[
 ["yellow",1,(255,255,0),"Default color"],
 ["blue",0,(0,0,255),"Complete \""+l[0][5]+"\""],
 ["green",0,(0,255,0),"Complete \""+l[1][5]+"\""],
 ["purple",0,(255,0,255),"Complete \""+l[2][5]+"\""],
 ["pink",0,(255,150,150),"Complete \""+l[3][5]+"\""],
 ["brown",0,(117,39,0),"Do 100 jumps"],
 ["black",0,(0,0,0),"Die 100 times"],
 ["white",0,(255,255,255),"Complete every level with coins"]
]
def get_visible_tile_range():
 first_tile=(-mx) // 10-2
 last_tile=first_tile+(320 // 10)+4
 return first_tile,last_tile
def draw_player(color:tuple[int,int,int] | None=None):
 if color:
  fill_rect(px,py,20,20,color)
 else:
  fill_rect(px,py,20,20,player_color)
def draw_spike(x_tile:int,y_tile:int,orientation:int):
 for i in range(5):
  fill_rect(
   mx+x_tile*10-10+i*2,
   y_tile*32-i*4+(2*i*4*orientation)-4*(1-orientation),
   20-i*4,4,blocks_color
  )
  fill_rect(
   mx+x_tile*10+10-i*2,
   y_tile*32-i*4+(2*i*4*orientation)-4*(1-orientation),
   6,4,bg_color
  )
def draw_platform(x_tile:int,y_tile:int,width_tiles:int,height_tiles:int):
 fill_rect(
  mx+x_tile*10,y_tile*32,
  10*width_tiles,height_tiles*32,blocks_color
 )
 if width_tiles < 0:
  fill_rect(mx+x_tile*10,y_tile*32,6,height_tiles*32,bg_color)
 else:
  fill_rect(
   mx+x_tile*10+width_tiles*10,y_tile*32,
   6,height_tiles*32,bg_color
  )
def draw_pad(x_tile:int,y_tile:int):
 fill_rect(
  round(mx+(x_tile+0.2)*10),round((y_tile+0.7)*32),
  20,20 // 2,(255,255,0)
 )
 fill_rect(
  round(mx+(x_tile+0.2)*10+20),round((y_tile+0.7)*32),
  6,20 // 2,bg_color
 )
def draw_coin(x_tile:int,y_tile:int,taken:bool):
 fill_rect(
  round(mx+(x_tile+0.2)*10),round((y_tile+0.7)*32),
  20,20,(170,170,170) if taken else (255,255,255)
 )
 fill_rect(
  round(mx+(x_tile+0.2)*10+20),round((y_tile+0.7)*32),
  6,20,bg_color
 )
def erase_coin(x_tile:int,y_tile:int):
 fill_rect(
  round(mx+(x_tile+0.2)*10),round((y_tile+0.7)*32),
  20+6,20,bg_color
 )
def draw_level():
 global attempts,percentage_label,percentage
 first_tile,last_tile=get_visible_tile_range()
 for x,y,orientation in l[cl][1]:
  if first_tile<=x<=last_tile:
   draw_spike(x,y,orientation)
 for x,y,w,h in l[cl][0]:
  if x+w>=first_tile and x<=last_tile:
   draw_platform(x,y,w,h)
 for x,y in l[cl][9]:
  if x+10>=first_tile and x<=last_tile:
   draw_pad(x,y)
 for i,(x,y,taken) in enumerate(l[cl][11]):
  if i in current_coins_taken:
   if i in coins_just_taken:
    erase_coin(x,y)
   continue
  if x+10>=first_tile and x<=last_tile:
   draw_coin(x,y,taken)
 end_x=l[cl][2]
 if first_tile<=end_x<=last_tile:
  fill_rect(mx+end_x*10,0,10,222,(0,255,0))
  fill_rect(mx+end_x*10+10,0,6,222,bg_color)
 attempts=l[cl][7]
 attempts_label=str(attempts)
 if attempts < 100:
  attempts_label="0"+attempts_label
  if attempts < 10:
   attempts_label="0"+attempts_label
 percentage=round(
  (
   ((l[cl][2]*10)-(l[cl][2]*10+mx))
  /(l[cl][2]*10-(px+20))
  *100
  ),2
 )
 if percentage > 100:
  percentage=100.0
 percentage_label="{:.2f}".format(percentage)
 if percentage < 10:
  percentage_label="0"+percentage_label
 if len(percentage_label) < 5:
  percentage_label += "0"
 dc(" "+l[cl][5]+" ",0,bg_color,(0,0,0),"left")
 dc(" Attempts:"+attempts_label+" ",0,(255,0,0),(0,0,0),"right")
 dc(percentage_label+"%",20,(0,0,0),bg_color)
def draw_hitbox(
  left:float,
  top:float,
  right:float,
  bottom:float,
  color:tuple[int,int,int]
 ):
 if not hitboxes:
  return
 if right+(right-left) < 0 or left > 320:
  return
 fill_rect(
  int(left)+6,
  int(top),
  int(right-left),
  int(bottom-top),
  bg_color
 )
 fill_rect(
  int(left),
  int(top),
  int(right-left),
  int(bottom-top),
  color
 )
def check_collision():
 player_tile=(-mx+px) // 10
 first_tile=player_tile-2
 last_tile=player_tile+2
 player_left  =px
 player_right =px+20
 player_top   =py
 player_bottom=py+20
 for x,y,w,h in l[cl][0]:
  if x > last_tile or x+w < first_tile:
   continue
  plat_left  =x*10+mx
  plat_top   =y*32
  plat_right =plat_left+w*10
  plat_bottom=plat_top+h*32
  if (
   player_right  > plat_left and
   player_left   < plat_right and
   player_bottom > plat_top and
   player_top    < plat_bottom
  ):
   return 1
 for x,y,orientation in l[cl][1]:
  if (x < first_tile or x > last_tile) and not hitboxes:
   continue
  spike_left =x*10+mx
  spike_right=spike_left+10
  spike_y    =y*32
  if orientation==0:
   spike_top   =spike_y-16
   spike_bottom=spike_y
  else:
   spike_top   =spike_y
   spike_bottom=spike_y+16
  draw_hitbox(
   spike_left,spike_top,
   spike_right,spike_bottom,
   (255,0,0)
  )
  if (
   player_right  > spike_left and
   player_left   < spike_right and
   player_bottom > spike_top and
   player_top    < spike_bottom
  ):
   return 1
 if not hitboxes:
  return 0
 for x,y in l[cl][9]:
  if (x < first_tile or x > last_tile) and not hitboxes:
   continue
  pad_left  =mx+(x+0.2)*10
  pad_top   =(y+0.7)*32
  pad_right =pad_left+20
  pad_bottom=pad_top+20 // 2
  player_left  =px
  player_right =px+20
  player_top   =py
  player_bottom=py+20
  draw_hitbox(
   pad_left,pad_top,
   pad_right,pad_bottom,
   (0,255,0)
  )
 for x,y,_ in l[cl][11]:
  if (x < first_tile or x > last_tile) and not hitboxes:
   continue
  coin_left  =mx+(x+0.2)*10
  coin_top   =(y+0.7)*32
  coin_right =coin_left+20
  coin_bottom=coin_top+20
  player_left  =px
  player_right =px+20
  player_top   =py
  player_bottom=py+20
  draw_hitbox(
   coin_left,coin_top,
   coin_right,coin_bottom,
   (0,255,0)
  )
 return 0
def check_pad_collision():
 player_tile=(-mx+px) // 10
 first_tile=player_tile-2
 last_tile=player_tile+2
 for x,y in l[cl][9]:
  if (x < first_tile or x > last_tile) and not hitboxes:
   continue
  pad_left  =mx+(x+0.2)*10
  pad_top   =(y+0.7)*32
  pad_right =pad_left+20
  pad_bottom=pad_top+20 // 2
  player_left  =px
  player_right =px+20
  player_top   =py
  player_bottom=py+20
  if (
   player_right  > pad_left
   and player_left < pad_right
   and player_bottom > pad_top
   and player_top < pad_bottom
  ):
   return 1
 return 0
def check_coin_collision() -> list[int | None]:
 player_tile=(-mx+px) // 10
 first_tile=player_tile-2
 last_tile=player_tile+2
 i=0
 coins_taken=[]
 for i,(x,y,_) in enumerate(l[cl][11]):
  if (x < first_tile or x > last_tile) and not hitboxes:
   continue
  coin_left  =mx+(x+0.2)*10
  coin_top   =(y+0.7)*32
  coin_right =coin_left+20
  coin_bottom=coin_top+20
  player_left  =px
  player_right =px+20
  player_top   =py
  player_bottom=py+20
  if (
   player_right  > coin_left
   and player_left < coin_right
   and player_bottom > coin_top
   and player_top < coin_bottom
  ):
   coins_taken.append(i)
 return coins_taken
def is_player_on_block():
 for x,y,w,_ in l[cl][0]:
  if (
   py+20==y*32
   and x*10+mx-19
  <=px <=
   x*10+w*10+mx
  ):
   return 1
 return 0
def is_level_finished() -> bool:
 return px+20 > l[cl][2]*10+mx
def respawn():
 global mx,py,bg_color
 global menu,bg_color,blocks_color
 global start_wait,current_coins_taken,total_attempts
 l[cl][7] += 1
 total_attempts += 1
 current_coins_taken=[]
 menu="level"
 start_wait=None
 bg_color=l[cl][3]
 blocks_color=l[cl][4]
 fill_screen(bg_color)
 mx=0
 py=172
 draw_level()
 draw_player()
def fill_screen(color:tuple[int,int,int]):
 fill_rect(0,0,320,222,color)
def dc(
  text:str,
  y:int,
  color:tuple[int,int,int],
  background:tuple[int,int,int],
  side:str | None=None
 ):
 formatted_text=text
 if len(text) > 32:
  formatted_text=text[:32]
 if not side:
  x=round((320-(len(formatted_text)*10))/2)
 elif side=="left":
  x=0
 elif side=="right":
  x=320-(len(formatted_text)*10)
  pass
 else:
  x=round((320-(len(formatted_text)*10))/2)
 draw_string(formatted_text,x,y,color,background)
def if_clicked():
 if (
  keydown(KEY_EXE) or
  keydown(KEY_OK) or
  keydown(KEY_SHIFT) or
  keydown(KEY_BACKSPACE) or
  keydown(KEY_LEFT) or
  keydown(KEY_RIGHT)
 ):
  return 1
 return 0
def enter_endscreen():
 global menu
 menu="endscreen"
 coins=l[menu_button-1][11]
 amount_of_coins=str(len(coins))
 coins_taken=0
 for coin in coins:
  if coin[2]:
   coins_taken += 1
 coins_taken=str(coins_taken)
 fill_screen(blocks_color)
 MARGIN=30
 fill_rect(MARGIN,MARGIN,320-MARGIN*2,222-MARGIN*2,bg_color)
 dc("LEVEL COMPLETED",60,(0,150,0),bg_color)
 dc("Attempts:"+str(attempts),100,(0,0,0),bg_color)
 dc(choice(endscreen_sentences[:26]),130,(0,0,0),bg_color)
 if coins:
  dc("Coins:"+coins_taken+"/"+amount_of_coins,160,(0,0,0),bg_color)
def enter_main_menu():
 global menu,menu_button,max_menu_buttons
 menu="main"
 max_menu_buttons=3
 menu_button=2
 fill_screen((0,60,255))
 draw_main_menu()
def draw_main_menu():
 if menu_button==2:
  chosen_color=(255,255,255)
 else:
  chosen_color=(0,60,255)
 CHOSEN_BIG_BUTTON_SIDE=90
 fill_rect(
  round((320-CHOSEN_BIG_BUTTON_SIDE)/2),
  round((222-CHOSEN_BIG_BUTTON_SIDE)/2),
  CHOSEN_BIG_BUTTON_SIDE,
  CHOSEN_BIG_BUTTON_SIDE,
  chosen_color
 )
 BIG_BUTTON_SIDE=70
 BIG_BUTTON_X_MARGIN=(320-BIG_BUTTON_SIDE)/2
 BIG_BUTTON_Y_MARGIN=(222-BIG_BUTTON_SIDE)/2
 fill_rect(
  round(BIG_BUTTON_X_MARGIN),
  round(BIG_BUTTON_Y_MARGIN),
  BIG_BUTTON_SIDE,
  BIG_BUTTON_SIDE,
  (0,255,0)
 )
 PIXELS_X=5
 PIXEL_WIDTH=BIG_BUTTON_SIDE/(PIXELS_X+2)
 MAX_HEIGHT=PIXELS_X*PIXEL_WIDTH
 TOTAL_MINI_PIXELS=(PIXELS_X*2-1)
 MINI_PIXEL=MAX_HEIGHT/TOTAL_MINI_PIXELS
 current_pixels=TOTAL_MINI_PIXELS
 for i in range(PIXELS_X):
  fill_rect(
   round(BIG_BUTTON_X_MARGIN+PIXEL_WIDTH*(i+1)),
   round(BIG_BUTTON_Y_MARGIN+PIXEL_WIDTH+MINI_PIXEL*i),
   round(PIXEL_WIDTH),
   round(current_pixels*MINI_PIXEL),
   (255,255,0)
  )
  current_pixels -= 2
 if menu_button==1:
  chosen_color=(255,255,255)
 else:
  chosen_color=(0,60,255)
 CHOSEN_SMALL_BUTTON_SIDE=70
 CHOSEN_SMALL_BUTTON_Y_MARGIN=round(
  (222-CHOSEN_SMALL_BUTTON_SIDE)/2
 )
 fill_rect(
  round((BIG_BUTTON_X_MARGIN-CHOSEN_SMALL_BUTTON_SIDE)/2),
  CHOSEN_SMALL_BUTTON_Y_MARGIN,
  CHOSEN_SMALL_BUTTON_SIDE,
  CHOSEN_SMALL_BUTTON_SIDE,
  chosen_color
 )
 SMALL_BUTTON_SIDE=50
 SMALL_BUTTON_Y_MARGIN=round(
  (222-SMALL_BUTTON_SIDE)/2
 )
 fill_rect(
  round((BIG_BUTTON_X_MARGIN-SMALL_BUTTON_SIDE)/2),
  SMALL_BUTTON_Y_MARGIN,
  SMALL_BUTTON_SIDE,
  SMALL_BUTTON_SIDE,
  (0,255,0)
 )
 CUBE_ICON_SIDE=30
 CUBE_ICON_X_MARGIN=round(
  (BIG_BUTTON_X_MARGIN-CUBE_ICON_SIDE)/2
 )
 CUBE_ICON_Y_MARGIN=round(
  (222-CUBE_ICON_SIDE)/2
 )
 fill_rect(
  CUBE_ICON_X_MARGIN,
  CUBE_ICON_Y_MARGIN,
  CUBE_ICON_SIDE,
  CUBE_ICON_SIDE,
  (255,255,0)
 )
 if menu_button==3:
  chosen_color=(255,255,255)
 else:
  chosen_color=(0,60,255)
 CHOSEN_RIGHT_SMALL_BUTTON_X_MARGIN=round(
  (BIG_BUTTON_X_MARGIN-CHOSEN_SMALL_BUTTON_SIDE)/2
 +BIG_BUTTON_SIDE+BIG_BUTTON_X_MARGIN
 )
 fill_rect(
  CHOSEN_RIGHT_SMALL_BUTTON_X_MARGIN,
  CHOSEN_SMALL_BUTTON_Y_MARGIN,
  CHOSEN_SMALL_BUTTON_SIDE,
  CHOSEN_SMALL_BUTTON_SIDE,
  chosen_color
 )
 RIGHT_SMALL_BUTTON_X_MARGIN=round(
  (BIG_BUTTON_X_MARGIN-SMALL_BUTTON_SIDE)/2
 +BIG_BUTTON_SIDE+BIG_BUTTON_X_MARGIN
 )
 fill_rect(
  RIGHT_SMALL_BUTTON_X_MARGIN,
  SMALL_BUTTON_Y_MARGIN,
  SMALL_BUTTON_SIDE,
  SMALL_BUTTON_SIDE,
  (0,255,0)
 )
 CONTROLS_MARGIN=5
 CONTROLS_X=RIGHT_SMALL_BUTTON_X_MARGIN+CONTROLS_MARGIN
 CONTROLS_Y=SMALL_BUTTON_Y_MARGIN+CONTROLS_MARGIN
 CONTROLS_SIDE=SMALL_BUTTON_SIDE-(CONTROLS_MARGIN*2)
 CONTROLS_MAP_Y=[1,2,3,0,3,2,1]
 CONTROLS_PIXELS_X=len(CONTROLS_MAP_Y)
 CONTROLS_MAX_PIXELS_Y=max(CONTROLS_MAP_Y)
 CONTROLS_PIXEL_SIZE_Y=CONTROLS_SIDE/CONTROLS_MAX_PIXELS_Y
 CONTROLS_PIXEL_SIZE_X=CONTROLS_SIDE/CONTROLS_PIXELS_X
 for i in range(CONTROLS_PIXELS_X):
  current_height=CONTROLS_PIXEL_SIZE_Y*CONTROLS_MAP_Y[i]
  fill_rect(
   round(CONTROLS_X+CONTROLS_PIXEL_SIZE_X*i),
   round(CONTROLS_Y+((CONTROLS_SIDE-current_height)/2)),
   round(CONTROLS_PIXEL_SIZE_X),
   round(current_height),
   (255,255,0)
  )
 dc("GEOMETRY WORKS",20,(255,255,255),(0,60,255))
 dc("Up/OK=Jump | Shift=Restart",222-18*3-5,(255,255,255),(0,60,255))
 dc("OK/EXE=Choose | Backspace=Exit",222-18*2-5,(255,255,255),(0,60,255))
 dc(" Game By Gild56 (on YT)",222-18-5,(255,255,255),(0,60,255),"left")
 dc("v1.2.0"+" ",222-18-5,(255,255,255),(0,60,255),"right")
def enter_browse_levels_menu():
 global menu,menu_button,max_menu_buttons
 menu_button=cl+1
 max_menu_buttons=len(l)
 menu="browse_levels"
 draw_level_menu()
def draw_level_menu():
 completed_color=(0,150,0)
 bg_color=l[menu_button-1][3]
 blocks_color=l[menu_button-1][4]
 best=l[menu_button-1][6]
 coins=l[menu_button-1][11]
 amount_of_coins=str(len(coins))
 coins_taken=0
 for coin in coins:
  if coin[2]:
   coins_taken += 1
 coins_taken=str(coins_taken)
 fill_screen(blocks_color)
 dc(l[menu_button-1][5],40,(255,255,255),blocks_color)
 dc("by "+str(l[menu_button-1][8]),70,bg_color,blocks_color)
 dc("Attempts:"+str(l[menu_button-1][7]),150,bg_color,blocks_color)
 dc("Jumps:"+str(l[menu_button-1][10]),170,bg_color,blocks_color)
 if coins:
  dc("Coins:"+coins_taken+"/"+amount_of_coins,190,bg_color,blocks_color)
 MARGIN=30
 Y_POSITION=110
 LENGTH=320-(MARGIN*2)
 fill_rect(MARGIN,Y_POSITION,LENGTH,18+2,bg_color)
 COMPLETED_LENGTH=round(LENGTH/100*best)
 fill_rect(MARGIN,Y_POSITION,COMPLETED_LENGTH,18+2,completed_color)
 if best > 50:
  bg_text_color=completed_color
  letters_color=(255,255,255)
 else:
  bg_text_color=bg_color
  letters_color=blocks_color
 dc(str(round(best))+"%",Y_POSITION,letters_color,bg_text_color)
 LITTLE_MARGIN=10
 draw_string("<",LITTLE_MARGIN,Y_POSITION,(255,255,255),blocks_color)
 draw_string(">",320-LITTLE_MARGIN-10,Y_POSITION,(255,255,255),blocks_color)
def enter_garage_menu():
 global menu,menu_button,max_menu_buttons
 menu_button=1
 max_menu_buttons=len(colors)
 menu="garage"
 if not colors[5][1] and total_jumps>=100:
  colors[5][1]=1
 if not colors[6][1] and total_attempts>=100:
  colors[6][1]=1
 if not colors[7][1] and total_coins==max_coins:
  colors[7][1]=1
 draw_garage_menu()
def draw_garage_menu():
 fill_screen((131,63,0))
 dc("You:",20,(255,255,255),(131,63,0))
 dc("Choose your color:",110,(255,255,255),(131,63,0))
 if not colors[menu_button-1][1]:
  dc(colors[menu_button-1][3],180,(255,255,255),(131,63,0))
  dc("to get this color",200,(255,255,255),(131,63,0))
 CUBE_SIDE=40
 CUBE_X_MARGIN=round((320-CUBE_SIDE)/2)
 fill_rect(CUBE_X_MARGIN,50,CUBE_SIDE,CUBE_SIDE,player_color)
 COLORS_COUNT=len(colors)
 COLOR_SIDE=25
 X_MARGIN=20
 X_SPACE=320-(X_MARGIN*2)-COLOR_SIDE
 Y_MARGIN=50
 CHOSEN_MARGIN=3
 for i in range(COLORS_COUNT):
  if i+1==menu_button:
   fill_rect(
    round(X_MARGIN+(X_SPACE/(COLORS_COUNT-1)*i))-CHOSEN_MARGIN,
    222-Y_MARGIN-COLOR_SIDE-CHOSEN_MARGIN,
    COLOR_SIDE+CHOSEN_MARGIN*2,
    COLOR_SIDE+CHOSEN_MARGIN*2,
    (255,255,255) if colors[menu_button-1][1] else (170,170,170)
   )
 for i in range(COLORS_COUNT):
  fill_rect(
   round(X_MARGIN+(X_SPACE/(COLORS_COUNT-1)*i)),
   222-Y_MARGIN-COLOR_SIDE,
   COLOR_SIDE,COLOR_SIDE,colors[i][2]
  )
enter_main_menu()
while game:
 start_frame=monotonic()
 if menu=="level" and not start_wait:
  if keydown(KEY_SEVEN):
   hitboxes=1
  else:
   hitboxes=0
  coins_just_taken=[]
  coins_touched=check_coin_collision()
  if len(coins_touched) > 0:
   for coin in coins_touched:
    if coin not in current_coins_taken:
     current_coins_taken.append(coin)
     coins_just_taken.append(coin)
  if not is_jumping:
   on_block=is_player_on_block()
   can_jump=on_block
   is_falling=not on_block
   jumped=keydown(KEY_OK) or keydown(KEY_UP)
   if is_falling:
    draw_player(bg_color)
    py += 16
   if check_pad_collision():
    took_pad=1
    jump_velocity *= 2
    draw_player(bg_color)
    is_jumping=1
    py -= int(jump_velocity)
    jump_velocity=jump_velocity/2
   elif jumped and not clicked and can_jump:
    draw_player(bg_color)
    is_jumping=1
    py -= int(jump_velocity)
    jump_velocity=jump_velocity/2
    total_jumps += 1
    l[cl][10] += 1
  elif can_jump:
   draw_player(bg_color)
   for i in range(len(l[cl][0])):
    if py+20!=l[cl][0][i][1]*32:
     is_jumping=1
    elif (
     l[cl][0][i][0]*10+mx-19
     < 50 <
     (
      l[cl][0][i][0]*10+mx +
      l[cl][0][i][2]*10+20
     )
    ):
     is_jumping=0
     jump_velocity=32
     break
   if is_jumping:
    py -= int(jump_velocity)
    if jump_velocity > 2:
     jump_velocity=jump_velocity/2
    elif jump_velocity==2:
     jump_velocity=0
    elif jump_velocity==0:
     air_ticks += 1
     if air_ticks==4:
      air_ticks=0
      jump_velocity=-2
    elif jump_velocity<=(-2) and jump_velocity > (-32):
     jump_velocity=jump_velocity*2
    else:
     is_jumping=0
     jump_velocity=32
     can_jump=1
   else:
    is_jumping=0
    jump_velocity=32
  draw_player(player_color)
  mx -= 6
  draw_level()
  if keydown(KEY_SHIFT) and not clicked:
   respawn()
   clicked=1
  elif not if_clicked() and clicked:
   clicked=0
  if keydown(KEY_BACKSPACE):
   enter_browse_levels_menu()
   clicked=1
  elif py+20 > 222 or check_collision():
   draw_player((255,0,0))
   if l[cl][6] < percentage:
    l[cl][6]=percentage
    dc(percentage_label+"%",70,(255,255,255),bg_color)
    dc("NEW BEST!",90,(255,255,255),bg_color)
    dc(choice(new_best_sentences[:32]),120,(255,255,255),bg_color)
   start_wait=monotonic()
  elif is_level_finished():
   draw_player(bg_color)
   draw_level()
   dc("LEVEL COMPLETED!",100,(0,150,0),bg_color)
   l[cl][6]=100.0
   colors[cl+1][1]=1
   for coin in current_coins_taken:
    l[cl][11][coin][2]=1
   total_coins=0
   for level in l:
    for coin in level[11]:
     if coin[2]:
      total_coins += 1
   start_wait=monotonic()
 elif menu=="level":
  if keydown(KEY_SHIFT):
   respawn()
   clicked=1
   continue
  current_wait=monotonic()
  if current_wait-start_wait < 1:
   continue
  if is_level_finished():
   enter_endscreen()
  else:
   respawn()
 elif menu=="endscreen":
  start_wait=None
  if (
   keydown(KEY_EXE) or
   keydown(KEY_BACKSPACE) or
   keydown(KEY_OK) or
   keydown(KEY_SHIFT)
  ):
   clicked=1
   if keydown(KEY_SHIFT):
    respawn()
   else:
    enter_browse_levels_menu()
 elif menu=="garage":
  if keydown(KEY_RIGHT) and not clicked:
   menu_button += 1
   if menu_button > max_menu_buttons or menu_button < 1:
    menu_button=1
   clicked=1
   draw_garage_menu()
  elif keydown(KEY_LEFT) and not clicked:
   menu_button -= 1
   if menu_button > max_menu_buttons or menu_button < 1:
    menu_button=max_menu_buttons
   clicked=1
   draw_garage_menu()
  if (keydown(KEY_EXE) or keydown(KEY_OK)) and not clicked:
   if colors[menu_button-1][1]:
    clicked=1
    player_color=colors[menu_button-1][2]
    draw_garage_menu()
  if keydown(KEY_BACKSPACE) and not clicked:
   enter_main_menu()
  if not if_clicked() and clicked:
   clicked=0
 elif menu=="browse_levels":
  if keydown(KEY_RIGHT) and not clicked:
   menu_button += 1
   if menu_button > max_menu_buttons or menu_button < 1:
    menu_button=1
   clicked=1
   draw_level_menu()
  if keydown(KEY_LEFT) and not clicked:
   menu_button -= 1
   if menu_button > max_menu_buttons or menu_button < 1:
    menu_button=max_menu_buttons
   clicked=1
   draw_level_menu()
  if (keydown(KEY_EXE) or keydown(KEY_OK)) and not clicked:
   cl=menu_button-1
   clicked=1
   respawn()
  if keydown(KEY_BACKSPACE) and not clicked:
   clicked=1
   enter_main_menu()
  if not if_clicked() and clicked:
   clicked=0
 elif menu=="main":
  if keydown(KEY_RIGHT) and not clicked:
   menu_button += 1
   if menu_button > max_menu_buttons or menu_button < 1:
    menu_button=1
   clicked=1
   draw_main_menu()
  elif keydown(KEY_LEFT) and not clicked :
   menu_button -= 1
   if menu_button > max_menu_buttons or menu_button < 1:
    menu_button=max_menu_buttons
   clicked=1
   draw_main_menu()
  elif (not keydown(KEY_RIGHT)) and (not keydown(KEY_LEFT)) and clicked:
   clicked=0
  if keydown(KEY_EXE) or keydown(KEY_OK):
   if menu_button==1:
    enter_garage_menu()
    clicked=1
   elif menu_button==2:
    enter_browse_levels_menu()
    clicked=1
 wait=1/30-(monotonic()-start_frame)
 if wait > 0:
  sleep(wait)
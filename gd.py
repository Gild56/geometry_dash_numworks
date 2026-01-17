from kandinsky import *
from ion import *
from time import *
from random import *
from kandinsky import fill_rect as FILL
from kandinsky import draw_string as STR
from ion import keydown as KEY

backcolor=(0,)*3

FILL(0,0,322,222,backcolor)
while not KEY(KEY_EXE):
  FILL(0,10,322,5,"red")
  FILL(0,50,322,5,"red")
  
  FILL(0,180,322,2,"red")
    
  STR("Geometry Dash",90,25,"white",backcolor)
  STR("Key [Up]/[OK] = Jump",40,80,"white",backcolor)
  STR("Key [Backspace] = Pause/Resume",10,120,"cyan",backcolor)

plives=6
pscore=0
penergy=40
game=True

#background
backcolor=(randint(210,255),randint(210,255),randint(210,255))
#player
playercolor=(randint(0,155),randint(0,155),randint(0,155))
#ground/platform
colorSol=(randint(0,55),randint(0,55),randint(0,55))

Map=[
    [[[0, 6, 32,1], [32, 5, 58, 2], [90, 4, 30, 3], [108, 3, 12, 1], [120, 6, 74, 1], [128, 3, 8, 1], [132, 2, 22, 1], [150, 1, 26, 1], [162, 5, 32, 1], [172, 2, 20, 1], [202, 5, 42, 2], [248, 4, 4, 3], [254, 5, 4, 2], [260, 6, 16, 1]], [[218, 5, 0], [133, 4, 1], [42, 5, 0], [52, 5, 0], [62, 5, 0], [73, 5, 0], [82, 5, 0], [144, 6, 0], [146, 6, 0], [142, 2, 0], [151, 1, 0], [164, 1, 0], [160, 6, 0], [166, 5, 0], [153, 3, 1], [158, 2, 1], [176, 3, 1], [220, 5, 0], [230, 5, 0], [240, 5, 0], [268, 6, 0]], 276,(0,130,240),(0,0,70)],
    [[[0, 6, 32,1], [28, 5, 26, 1], [42, 4, 12, 1], [62, 5, 24, 1], [82, 4, 4, 1], [94, 6, 108, 1], [94, 5, 42, 1], [94, 4, 38, 1], [118, 3, 14, 1], [138, 3, 8, 1], [142, 2, 24, 1], [162, 3, 8, 1], [174, 5, 14, 1], [206, 6, 4, 1], [216, 6, 20, 1], [240, 5, 10, 1], [254, 4, 8, 1], [266, 3, 6, 1], [32, 6, 54, 1]], [[158, 6, 0], [159, 2, 0], [126, 3, 0], [106, 4, 0], [104, 4, 0], [73, 5, 0], [63, 5, 0], [50, 4, 0], [35, 5, 0], [124, 3, 0], [149, 2, 0], [151, 2, 0], [157, 2, 0], [150, 6, 0], [156, 6, 0], [195, 6, 0], [224, 6, 0], [226, 6, 0], [181, 5, 0],[244,5,0]], 272,(0,250,80),(0,70,70)],
    [[[0, 6, 32, 1], [172, 6, 42, 1], [110, 6, 24, 1], [66, 4, 32, 1], [56, 5, 46, 2], [52, 5, 2, 2], [32, 5, 18, 2], [120, 5, 4, 1], [120, 3, 4, 1], [140, 5, 4, 2], [148, 4, 4, 3], [154, 3, 4, 4], [160, 4, 4, 3], [166, 5, 4, 2], [220, 6, 52, 1], [248, 5, 24, 1], [258, 4, 14, 1]], [[184, 6, 0], [169, 5, 0], [167, 5, 0], [121, 3, 0], [123, 3, 0], [92, 4, 0], [53, 5, 0], [41, 5, 0], [83, 4, 0], [74, 4, 0], [186, 6, 0], [194, 6, 0], [202, 6, 0], [204, 6, 0], [217, 6, 1], [217, 6, 0], [249, 5, 0], [230, 6, 0], [239, 6, 0], [259, 4, 0]], 272,(200,0,0),(50,0,0)],
    [[[0, 6, 32, 1], [48, 4, 23, 1], [35, 5, 36, 1], [32, 6, 77, 1], [104, 5, 5, 1], [79, 5, 14, 1]], [[92, 5, 0], [80, 5, 0], [59, 4, 0], [61, 4, 0], [36, 5, 0], [20, 6, 0], [103, 6, 0]], 109,(0,190,190),(0,30,30)]
    ]

sleep(0.5)

cEstParti=False
okPourJouer=False
b=False

quelNiveau=False

gravity=False

xPlayer=50
yPlayer=50
SautAutorise=True

xMap=0

fini=False
jump=False

Vjump=38
enLAir=0

FILL(0,0,320,222,backcolor)

wPlayer=20
hPlayer=20
 
def player(e):
  global wPlayer,hPlayer
  FILL(xPlayer,yPlayer,wPlayer,hPlayer,e)
  

def pic(a,b,c):
  for i in range(5):
    FILL(xMap+a*10-10+i*2,b*32-i*4+(2*i*4*c)-4*(1-c),20-i*4,4,colorSol)
    FILL(xMap+a*10+10-i*2,b*32-i*4+(2*i*4*c)-4*(1-c),6,4,backcolor)
    
def sol(x,y,longueur,hauteur):
  FILL(xMap+x*10,y*32,10*longueur,hauteur*32,colorSol)
  if longueur<0:
    FILL(xMap+x*10,y*32,6,hauteur*32,backcolor)
  else:
    FILL(xMap+x*10+longueur*10,y*32,6,hauteur*32,backcolor)

def arrivee(k):
  FILL(xMap+k*10,0,10,222,(0,255,0))
  FILL(xMap+k*10+10,0,6,222,backcolor)

def mapp():
  for i in range(len(Map[quelNiveau][0])):
    if xMap+Map[quelNiveau][0][i][0]*10<320 and xMap+Map[quelNiveau][0][i][0]*10+Map[quelNiveau][0][i][2]*10>-10:
      sol(Map[quelNiveau][0][i][0],Map[quelNiveau][0][i][1],Map[quelNiveau][0][i][2],Map[quelNiveau][0][i][3])
  for j in range(len(Map[quelNiveau][1])):
    if -10<xMap+Map[quelNiveau][1][j][0]*10+20<340:
      pic(Map[quelNiveau][1][j][0],Map[quelNiveau][1][j][1],Map[quelNiveau][1][j][2])
  arrivee(Map[quelNiveau][2])
  
mapp()
player(playercolor)


def hitBox():
  
  for i in range(len(Map[quelNiveau][0])):
    if xPlayer+20<Map[quelNiveau][0][i][0]*10+xMap or xPlayer>Map[quelNiveau][0][i][0]*10+Map[quelNiveau][0][i][2]*10+xMap or yPlayer<Map[quelNiveau][0][i][1]*32 or yPlayer>Map[quelNiveau][0][i][1]*32+Map[quelNiveau][0][i][3]*32:
      b=False
    else:
      b=True
      break
  if b==False:
    for i in range(len(Map[quelNiveau][1])):
      if xPlayer+20<Map[quelNiveau][1][i][0]*10+xMap or xPlayer>Map[quelNiveau][1][i][0]*10+15+xMap or yPlayer>Map[quelNiveau][1][i][1]*32+Map[quelNiveau][1][i][2]*32 or yPlayer<Map[quelNiveau][1][i][1]*32-(1-Map[quelNiveau][1][i][2])*32:
        b=False
      else:
        b=True
        break
  return b

#main loop
while game:
  
  STR("Score:"+str(pscore),0,0,"cyan","black")
  STR("Lives:"+str(plives),240,0,"green","black")
  
  
  if cEstParti==0:

    STR("Press [EXE] to Randomize",20,110)
    STR("the Theme!",20,130)
    
    if KEY(KEY_EXE):
      sleep(0.2)
      backcolor=(randint(0,255),randint(0,255),randint(0,255))
      colorSol=(randint(0,255),randint(0,255),randint(0,255))
      FILL(0,0,320,222,backcolor)
      mapp()
      player(playercolor)
    if KEY(KEY_OK) or KEY(KEY_EXE):
      FILL(0,0,322,222,backcolor)
      cEstParti=True
      okPourJouer=80
    if okPourJouer<50:
      STR("Press [OK] to Start",40,50,colorSol,backcolor)
      okPourJouer+=1
    if okPourJouer>49:
      STR("Press [OK] to Start",40,50,backcolor,backcolor)
      okPourJouer+=1
      if okPourJouer>79:
        okPourJouer=0

  if cEstParti==True:

    if jump==False and fini==False:
      for i in range(len(Map[quelNiveau][0])):
        if yPlayer+20==Map[quelNiveau][0][i][1]*32 and Map[quelNiveau][0][i][0]*10+xMap-19<=50<=Map[quelNiveau][0][i][2]*10+Map[quelNiveau][0][i][0]*10+xMap:
          SautAutorise=True
          gravity=False
          break
        else:
          SautAutorise=False
          gravity=True
      if gravity==True:
        player(backcolor)
        yPlayer+=16
        player(playercolor)  

      if KEY(KEY_OK) and SautAutorise==True or KEY(KEY_UP) and SautAutorise==True:
        player(backcolor)
        jump=True
        yPlayer-=int(Vjump)
        Vjump=Vjump/2
        player(playercolor)
    
    if jump==True and fini==False and SautAutorise==True:
      player(backcolor)
      
      for k in range(len(Map[quelNiveau][0])):
        if yPlayer+20!=Map[quelNiveau][0][k][1]*32:
          jump=True
        elif Map[quelNiveau][0][k][0]*10+xMap-19<50<Map[quelNiveau][0][k][0]*10+xMap+Map[quelNiveau][0][k][2]*10+20:
          jump=False
          break
      if jump==True:
        yPlayer-=int(Vjump)
        if Vjump>2:
          Vjump=Vjump/2
        elif Vjump==2:
          Vjump=0
        elif Vjump==0:
          enLAir+=1
          if enLAir==4:
            enLAir=0
            Vjump=-2
        elif Vjump<=(-2) and Vjump>(-32):
          Vjump=Vjump*2
        else:
          jump=False
          Vjump=32
          SautAutorise=True
      else:
        jump=False
        Vjump=32
        SautAutorise=True
    player(playercolor)    
    
    if fini==False:
      xMap-=6
      mapp()
    # level completed
    else:
      STR("MISSION COMPLETE!!",100,50,colorSol,backcolor)

      STR("Press [OK] key",110,150,colorSol,backcolor)
      game=False
      
   # player crashes 
    if yPlayer+hPlayer>222 or hitBox():
      
      plives-=1
      #randomize colors
         
      backcolor=(randint(210,255),randint(210,255),randint(210,255))
      colorSol=(randint(0,55),randint(0,55),randint(0,55))
      playercolor=(randint(0,155),randint(0,155),randint(0,155))

      FILL(0,0,320,222,backcolor)
      xMap=0
      yPlayer=172
   
 
    if plives<1:
      game=False
    sleep(0.03)
    
    if xPlayer+wPlayer>Map[quelNiveau][2]*10+xMap:
      fini=True
      
                  
    if fini==True and KEY(KEY_OK):
      
      sleep(0.5)
      if not KEY(KEY_OK):
        cEstParti=False
        FILL(0,0,320,222,backcolor)
        xMap=0
        yPlayer=172
        fini=False
        mapp()
        player(playercolor)
        
  
  
  if KEY(KEY_OK) or KEY(KEY_UP):
    pscore+=randint(5,20)
    penergy+=0.2
  
  if penergy>10:
    penergy=0
    plives+=1
    FILL(xPlayer,yPlayer,wPlayer,hPlayer,"green")
  
  
  if KEY(KEY_BACKSPACE):
    STR("(PAUSED)",110,60,"black",backcolor)
    STR("Press [Backspack] to Resume",15,100,"blue",backcolor)
    while KEY(KEY_BACKSPACE):
      pass
    while not KEY(KEY_BACKSPACE):
      pass
    while KEY(KEY_BACKSPACE):
      STR("        ",110,60,backcolor,backcolor)
      STR("                            ",15,100,backcolor,backcolor)
      pass

 
FILL(0,0,322,222,"black")
STR("GAME OVER",100,100,"green","black")      
STR("SCORE:"+str(pscore),100,140,"white","black")    
from tkinter import *
import random
import time
import clscoord
import clsgame
import clssprite
import MB
g = clsgame.Game()
app=MB.mb(g)

platform1 = clssprite.PlatformSprite(g, PhotoImage(file="platform1.gif"), 0, 500,500,900)
platform2 = clssprite.PlatformSprite(g, PhotoImage(file="E.png"),440, 0,100,100)
platform3 = clssprite.PlatformSprite(g, PhotoImage(file="E.png"),340, 0,10,10)
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
sf=clssprite.StickFigureSprite(g)

g.sprites.append(sf)
g.mainloop()

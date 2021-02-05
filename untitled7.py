# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:16:34 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
time.sleep(5)

x=85.0
y=133.0
z=240.0

mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1


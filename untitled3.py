# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:23:14 2021

@author: USER
"""

import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    
    ()x,y,z=mc.player.getTilePos
    mc.setBlocks(x-25,y-1,z-25,x+25,y-1,z+25,46)
    time.sleep(0.5)
    
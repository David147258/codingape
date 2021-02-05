# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:35:02 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(10):
    r=random.randrange(1,5)
    if r ==1:
        mc.setBlocks(x,y,z,x+4,y,z,46)
        x=x+4
    elif r ==2:
        mc.setBlocks(x,y,z,x-4,y,z,46)
        x=x-4
        mc.setBlocks(x,y,z,x,y,z+4,46)
        z=z+4
        mc.setBlocks(x,y,z,x,y,z-4,46)
        z=z-4
        
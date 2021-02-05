# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:53:33 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def planttree(x,y,z):
    mc.setBlocks(x,y+3,z,x,y,z,17)
    mc.setBlocks(x-1,y+4,z-1,x+1,y+6,z+1,426)

x,y,z=mc.player.getTilePos()
for i in range(10):
    for f in range(10):
        planttree(x+i*5,y+f*i,z)

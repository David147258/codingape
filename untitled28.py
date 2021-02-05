# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:49:02 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def planttree(x,y,z):
    mc.setBlocks(x,y+3,z,x,y,z,17)
    mc.setBlocks(x-1,y+4,z-1,x+1,y+6,z+1,46)

x,y,z=mc.player.getTilePos()
for i in range(0,100,5):
    planttree(x+i,y,z)

    
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:51:15 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
for i in range(0,20,1):
    mc.setBlock(x+i,y-1,z+i,7)
    mc.setBlock(x+i-1,y-1,z+i,7)
    mc.setBlock(x+i+1,y-1,z+i,7)
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:33:46 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()


def planttree():
    mc.setBlocks(x,y+3,z,x,y,z,17)
    mc.setBlocks(x-1,y+4,z-1,x+1,y+6,z+1,46)

a=0
while a<500:
    planttree()

    a=a+1
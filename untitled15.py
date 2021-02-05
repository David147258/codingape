# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:54:37 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y ,z = mc.player.getTilePos()
a=0
while a<10:
    mc.setBlocks(x-100,y-100,z,x+100,y+100,z,19)
    z=z+5
    a=a+1
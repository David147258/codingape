# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:14:58 2021

@author: USER
"""
import random
import timefrom mcpi.minecraft import Minecraft
mc = Minecraf
t.create()
while True:
    x,y,z=mc.player.getTilePos()
    a = mc.getBlock(x,y-1,z-1)
    b = mc.getBlock(x,y-1,z+1)
    c = mc.getBlock(x-1,y-1,z)
    d = mc.getBlock(x+1,y-1,z)
    
    if a==8 or b==8 or c==9 or d==9 or b==9 or c==9 or d==9:
        mc.setBlocks(x-100,y-1,z-100,x+100,y-1,z+100,46)
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:13:41 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
a=0
while a<500:
    x,y,z=mc.player.getPos()
    mc.spawnEntity(x,y,z,93)
    a=a+1
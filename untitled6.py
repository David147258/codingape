# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:16:49 2021

@author: USER
"""
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    
    x,y,z=mc.player.getTilePos()
    y=y-1
    mc.setBlock(x,y,z,50)
    time.sleep(0.2)
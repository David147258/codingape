# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:36:57 2021

@author: USER
"""
import random
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
flower=38
a=0
while a<100: 
    
    x,y,z=mc.player.getTilePos()
    color =random .randint(0,8)
    mc.setBlock(x,y,z,flower,color)
    time.sleep(0.5)
    a=a+1
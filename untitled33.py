# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:53:46 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create("35.229.251.147")
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+500,y+100,z+500,0)

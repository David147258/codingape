# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:35:54 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x=100.0
y=100.0
z=100.0


print(mc.player.setPos(x,y,z))
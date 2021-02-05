# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:03:36 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y ,z = mc.player.getPos()
mc.setSign(x,y,z,63,0,"hi","aaa","bbb","ccc")
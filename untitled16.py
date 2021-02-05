# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:18:58 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y ,z = mc.player.getTilePos()
try:
    blocktype = int(input("輸入你要放的方塊 ID:"))
    mc.setBlock(x, y ,z,blocktype)
except:
    print("只能輸入數字!!!!!!!!!!!!!!!!")
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:55:08 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time

n=1
mc = Minecraft.create()
for i in range(5):
    for j in range(n):
        mc.spawnEntity(x,y,z,96)
    n=n*2
    mc.postToChat("這次生成)了" + str(n)+"隻蠹魚")
    time.sleep(1)
    





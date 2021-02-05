# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:44:47 2021

@author: USER
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create("35.229.251.147")
x,y,z=mc.player.getTilePos()
a=50
b=50
c=50
        
       
mc.setBlocks(x,y,z,x+c,y+b,z+a,155) 
mc.setBlocks(x+1,y+1,z+1,x+c-1,y+b-1,z+a-1,0)
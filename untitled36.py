# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:20:14 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
while True:
    mc.executeCommand("time add 500")
    sleep(0.2)
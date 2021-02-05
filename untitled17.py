# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:00:29 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
userName = input("請輸入姓名: ")
message = input("請輸入發言: ")
mc.postToChat(" ["+userName + "] " + message)
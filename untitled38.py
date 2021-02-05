# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:29:05 2021

@author: USER
"""

from random import randrange
from time import sleep
r=randrange(0,16)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        date=block.data
        if  date==r:
            mc.postToChat("啊!被找到了")
            mc.setBlock(hit.pos,57)
            break
        elif  date<r:
            mc.postToChat("找大一點的")
        elif  date>r:
            mc.postToChat("找小一點的")
            
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:01:05 2020

@author: user
"""

from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()
color=random.randrange(0,16)
while True:
    color=random.randrange(0,16)
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y,z,38,color)
    time.sleep(3)
    
    
    
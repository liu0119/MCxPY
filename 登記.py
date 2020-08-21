# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:35:39 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()



while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        if block==68 or block==63:
            x,y,z=mc.getTilePos()
            line1=mc.postToChat int(input"請輸入你的名字())
            mc.setSign(x+1,y,z,63,str(line1))

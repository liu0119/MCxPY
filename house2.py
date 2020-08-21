# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:03:47 2020

@author: user
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
BT=int(input("請輸入ID: "))
l=int(input("請輸入長度: "))
w=int(input("請輸入寬度: "))
h=int(input("請輸入高度: "))
mc.setBlocks(x,y,z,x+l,y+h,z+w,BT)
time.sleep(0.5)

mc.setBlocks(x+1,y,z+1,x+l-1,y+h-1,z+w-1,0)
time.sleep(0.5)

mc.setBlocks(x+1,y,z,x+1,y+1,z,0)
time.sleep(0.5)

mc.setBlocks(x+1,y+h,z+1,x+l-1,y+h,z+w-1,169)
time.sleep(0.5)

a=4
while a<h:
    mc.setBlocks(x+1,y+a,z+1,x+l-1,y+a,z+w-1,169)
    mc.setBlocks(x+2,y+a,z+2,x+l-2,y+a,z+w-2,0)
    a=a+4
mc.setBlocks(x+l+20,y-1,z+20+w,x-20,y-1,z-20,1)
mc.setBlock(x+1,y,z,64)
mc.setBlocks(x+2,y,z,x,y+2,z-4,57)
mc.setBlocks(x+1,y+2,z-4,x+1,y,z,169)
mc.setBlocks(x+1,y+1,z-4,x+1,y,z,0)
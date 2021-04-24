from mcpi.minecraft import Minecraft
import random
import time
mc = Minecraft.create()

while True:
    pos = mc.player.getPos()
    x = pos.x+random.uniform(-20,20)
    z = pos.z+random.uniform(-20,20)
    y = pos.y+30
    mc.spawnEntity(x,y,z,54)
    time.sleep(0.1)


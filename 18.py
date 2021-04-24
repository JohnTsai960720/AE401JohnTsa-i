from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()
mc.setSign(x,y,z,68,0,"hi"," hi","  hi","   hi")
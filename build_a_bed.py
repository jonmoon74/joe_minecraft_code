#import modules
from mcpi import minecraft
from mcpi import block

#where am i
mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
x, y, z = mc.player.getPos()

#set block names
wool = block.WOOL.id

#build bed
mc.setBlock(x+1, y, z, wool, 3)
mc.setBlock(x+2, y, z, wool, 3)
mc.setBlock(x+3, y, z, wool, 1)

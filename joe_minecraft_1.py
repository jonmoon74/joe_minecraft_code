from mcpi import minecraft
from mcpi import block
from time import sleep

mc = minecraft.Minecraft.create()
mc.postToChat("Working on it, Joe...")
pos = mc.player.getPos()
pos = mc.player.getPos()
x, y, z = mc.player.getPos()
x, y, z = mc.player.getPos()
#mc.player.setPos(x+3, y, z+10)
#mc.player.setPos(x-3, y, z-10)
#mc.player.setPos(x+5, y+10, z)
#mc.setBlock(x+1, y, z, 1)
#mc.setBlock(x+1, y, z, 3)
#mc.setBlock(x+1, y, z, 46)
#mc.setBlock(x+1, y, z, 46, 1)
#mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 46, 1)
#mc.setBlock(x+3, y, z, block.STONE.id)
#mc.setBlock(x+4, y, z, block.GOLD_ORE.id)
#mc.player.setPos(x-4,y-3 ,z)
#mc.setBlocks(x+1, y+1, z+1, x+20, y+20, z+20, 46,1)
#mc.player.setPos(x, y+2, z)

#set block names
obsidian = block.OBSIDIAN.id
tnt = block.TNT.id
wool = block.WOOL.id
lava = block.LAVA.id
water = block.WATER.id
air = block.AIR.id
bed = block.BED.id

mc.setBlock(x+3, y+3, z, lava)
sleep(30)
mc.setBlock(x+3, y+5, z, water)
sleep(4)
mc.setBlock(x+3, y+5, z, air)
#mc.setBlock(x+1, y, z, bed)
#mc.setBlock(x+1, y, z, wool)
#mc.setBlock(x+1, y, z, obsidian)
#mc.setBlocks(x+1, y+1, z+1, x+20, y+20, z+20, tnt, 1)

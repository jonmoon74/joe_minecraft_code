def BuildBed(wide, sheet, pillow):
	
	#import modules
	from mcpi import minecraft
	from mcpi import block

	#where am i
	mc = minecraft.Minecraft.create()
	pos = mc.player.getPos()
	x, y, z = mc.player.getPos()

	#set block names
	wool = block.WOOL.id
	
	if wide == "single":
		#build bed
		mc.setBlock(x+1, y, z, wool, sheet)
		mc.setBlock(x+2, y, z, wool, sheet)
		mc.setBlock(x+3, y, z, wool, pillow)
	elif wide == "double":
		mc.setBlock(x+1, y, z, wool, sheet)
		mc.setBlock(x+2, y, z, wool, sheet)
		mc.setBlock(x+3, y, z, wool, pillow)
		mc.setBlock(x+1, y, z+1, wool, sheet)
		mc.setBlock(x+2, y, z+1, wool, sheet)
		mc.setBlock(x+3, y, z+1, wool, pillow)
	else:
		mc.postToChat("You didn't build a bed")

def SingleBridge():
	#import modules
	from mcpi import minecraft
	from mcpi import block

	#where am i
	mc = minecraft.Minecraft.create()
	pos = mc.player.getPos()
	x, y, z = mc.player.getPos()

	#set block names
	wool = block.WOOL.id
	brick = block.BRICK_BLOCK.id

	#build a bridge
	mc.setBlock(x+1, y, z, brick)
	mc.setBlock(x+2, y, z, brick)
	mc.setBlock(x+2, y+1, z, brick)
	mc.setBlock(x+3, y+1, z, brick)
	mc.setBlock(x+3, y+2, z, brick)
	mc.setBlock(x+4, y+2, z, brick)
	mc.setBlock(x+5, y+2, z, brick)
	mc.setBlock(x+5, y+1, z, brick)
	mc.setBlock(x+6, y+1, z, brick)
	mc.setBlock(x+6, y, z, brick)
	mc.setBlock(x+7, y, z, brick)

def DoubleBridge():
	#import modules
	from mcpi import minecraft
	from mcpi import block

	#where am i
	mc = minecraft.Minecraft.create()
	pos = mc.player.getPos()
	x, y, z = mc.player.getPos()

	#set block names
	wool = block.WOOL.id
	brick = block.BRICK_BLOCK.id

	#build a bridge
	mc.setBlock(x+1, y, z, brick)
	mc.setBlock(x+2, y, z, brick)
	mc.setBlock(x+2, y+1, z, brick)
	mc.setBlock(x+3, y+1, z, brick)
	mc.setBlock(x+3, y+2, z, brick)
	mc.setBlock(x+4, y+2, z, brick)
	mc.setBlock(x+5, y+2, z, brick)
	mc.setBlock(x+5, y+1, z, brick)
	mc.setBlock(x+6, y+1, z, brick)
	mc.setBlock(x+6, y, z, brick)
	mc.setBlock(x+7, y, z, brick)

	mc.setBlock(x+1, y, z+1, brick)
	mc.setBlock(x+2, y, z+1, brick)
	mc.setBlock(x+2, y+1, z+1, brick)
	mc.setBlock(x+3, y+1, z+1, brick)
	mc.setBlock(x+3, y+2, z+1, brick)
	mc.setBlock(x+4, y+2, z+1, brick)
	mc.setBlock(x+5, y+2, z+1, brick)
	mc.setBlock(x+5, y+1, z+1, brick)
	mc.setBlock(x+6, y+1, z+1, brick)
	mc.setBlock(x+6, y, z+1, brick)
	mc.setBlock(x+7, y, z+1, brick)
	


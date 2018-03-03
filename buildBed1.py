def buildbed(wide, sheet, pillow):
	
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
		mc.setblock(x+1, y, z+1, wool, sheet)
		mc.setblock(x+2, y, z+1, wool, sheet)
		mc.setBlock(x+3, y, z+1, wool, pillow)
	else:
		mc.postToChat("You didn't build a bed")
		

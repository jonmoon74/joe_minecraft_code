def buildBridge(bridgeLength, material):
    
    #NEED TO PUT A EVEN NUMBER CHECKER FOR brigdeLength
    if bridgeLength % 2 = 0:  
        #import modules
        from mcpi import minecraft
        from mcpi import block
        #get player co-ordinates
        mc = minecraft.Minecraft.create()
        pos = mc.player.getPos()
        x, y, z = mc.player.getPos()
        #set dictionary for block types
        wool = block.WOOL.id
        brick = block.BRICK_BLOCK.id
        wood = block.WOOD_PLANKS.id
        stone = block.STONE.id
        #establish key variables for looping
        i = 2
        iTwo = 0
        iThree = bridgeLength/2
        iFour = iThree-1
        iFive = iThree+1
        #build the ascending half of the bridge
        mc. setBlock(x+1, y, z, material)
        while i < iFive:
            #set a block in front of Steve
            mc.setBlock(x+i, y, z+iTwo, material)
            iTwo += 1
            mc.setBlock(x+i, y, z+iTwo, material)
            i += 1
        #build the middle of the bridge   
        mc.setBlock(x+iFive, y, z+iFour, material)
        iFour -= 1
        mc.setBlock(x+iFive, y, z+iFour, material)
        iFive += 1
        #build the descending half of the bridge
        while iFive < bridgeLength:
            mc.setBlock(x+iFive, y, z+iFour, material)
            iFour -= 1
            mc.setBlock(x+iFive, y, z+iFour, material)
            iFive += 1
        #build the final step down   
        mc.setBlock(x+bridgeLength, y, z, material)
    else:
        print("You must use a even number for your bridge")
        



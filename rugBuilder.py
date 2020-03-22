from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()


#where am i

pos = mc.player.getPos()
x, y, z = mc.player.getPos()

#create block

def rugSquare(x, y, z, col):
    wool = 35
    mc.setBlock(x, y, z, wool, col)
    
#setblock

k = 1
j = 1

while k < 7:
   
    i = 0
    while i < 6:
        
        rugSquare(x+k, y, z+i, j)
        i += 1
        j += 1
    k += 1
    j += 1


  

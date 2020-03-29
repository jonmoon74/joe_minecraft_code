from mcpi import minecraft
# from mcpi import block

mc = minecraft.Minecraft.create()


# where am i

pos = mc.player.getPos()
x, y, z = mc.player.getPos()

# create block


def rugSquare(x, y, z, col):
    wool = 35
    mc.setBlock(x, y, z, wool, col)

# set pattern for rug as array


rugColors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# set blocks in place

k = 1
j = 0

while k < 7:
    i = 0
    while i < 6:
        rugSquare(x + k, y, z + i, rugColors[j])
        i += 1
        j += 1
    k += 1

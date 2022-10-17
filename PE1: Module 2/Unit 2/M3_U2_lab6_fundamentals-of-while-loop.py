blocks = int(input("Enter the number of blocks: "))
# Number of blocks needed to build the next level
nextLevel = 1 
# Current height of the pyramid
height = 0
while blocks:
    blocks -= nextLevel
    # Exit once there is no more blocks
    if blocks < 0: 
        break
    nextLevel = nextLevel + 1
    height += 1
print("The height of the pyramid is:", height)
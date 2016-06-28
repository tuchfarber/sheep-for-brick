from PIL import Image
import random

new_img = Image.new('RGB',(578,512),(20,20,20))

xtiles = {
    '0': [3,114],
    '1': [4,57],
    '2': [5,0],
    '3': [4,57],
    '4': [3,114]
}
tile_files = [
    'tile_brick.png',
    'tile_brick.png',
    'tile_brick.png',
    'tile_desert.png',
    'tile_forest.png',
    'tile_forest.png',
    'tile_forest.png',
    'tile_forest.png',
    'tile_grass.png',
    'tile_grass.png',
    'tile_grass.png',
    'tile_grass.png',
    'tile_mountain.png',
    'tile_mountain.png',
    'tile_mountain.png',
    'tile_plain.png',
    'tile_plain.png',
    'tile_plain.png',
    'tile_plain.png',    
    ]
random.shuffle(tile_files)
for i in xrange(5):
    numxtiles = xtiles[str(i)][0]
    for j in xrange(numxtiles):
        x = (j*128 + xtiles[str(i)][1])-(16*j)
        y = (i*128) - (32*i)
        tile = Image.open('tiles/' + tile_files.pop()).resize((128,128))
        new_img.paste(tile,(x,y),tile)
    
new_img.save('boards/new_board.png')
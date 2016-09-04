
from  PIL import Image
from random import randrange


im = Image.open("C:/users/user/downloads/cat.jpg")
pixels = im.load()
x, y = im.size


for i in range(x):  
    for j in range(y):

        r, g, b = pixels[i, j]
        pixels[i, j] = r, b, g
        
im.show()



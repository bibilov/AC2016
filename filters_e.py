from  PIL import Image
from random import randrange


im = Image.open("D:/MCloud/Photos/IMG_0372.JPG")
pixels = im.load()
x, y = im.size


for i in range(x):  
    for j in range(y):

        r, g, b = pixels[i, j]
        bw = (r + g + b) // 3
        if bw > 20:
            pixels[i, j] = 255, 255, 255
im.show()

'''
чем хорош этот фильтр?
тем что такой фильтр можно использовать в распознавателях и
за счет данного фильтра можно будет избавиться от шума на изображении
'''

#менялка цвета
from  PIL import Image
from random import randrange

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

im = Image.open("CFancy.jpg")
pixels = im.load()
x, y = im.size

print("ВВедите какие цвета будем менять")
rChoise = int(input("Красный: "))
gChoise = int(input("Зеленый: "))
bChoise = int(input("Синий: "))


for i in range(x):  
    for j in range(y):

        r, g, b = pixels[i, j]
        pixels[i, j] = r + rChoise, g + gChoise, b + bChoise
        r = constrain(r,0,255)
        g = constrain(g,0,255)
        b = constrain(b,0,255)

im.save("CFancy2.jpg")       
im.show()

#Грубая иммитация фотошоп кривой
from  PIL import Image
from random import randrange

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


im = Image.open("CFancy.jpg")
im2 = Image.open("CFancy.jpg")
pixels = im.load()
pixels2 = im2.load()
x, y = im.size

bX, bY= [], []


print("Введите колличество точек:")
n = int(input())
for i in range(n):
	bX.append(int(input("Точка {} яркость: ".format(i+1))))
	bY.append(int(input("Точка {} предел: ".format(i+1))))
	bY[i] = constrain(bY[i],0,255)




for i in range(x):  
    for j in range(y):

        r, g, b = pixels[i, j]

        br = round(0.3*r + 0.5*g + 0.11*b)
        for k in range(n):
        	#меняем яркость пикселя если она ниже значения точки. Для последующих точек проверяем диапазоны
	        if (br < bY[k] and k == 0) or (br < max(bY[k],bY[k-1]) and br > min(bY[k],bY[k-1])):
	       		r, g, b = r + bX[k], g + bX[k], b + bX[k] 
	        	r = constrain(r,0,255)
	        	g = constrain(g,0,255)
	        	b = constrain(b,0,255)

        pixels[i, j] = r, g, b

im.save("CFancy2.jpg")       
im.show()

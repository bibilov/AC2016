from  PIL import Image
from random import randint


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

#ч-б
def black(r,g,b,bl):
	mid = (r+g+b) // 3
	if mid > (255 + bl) // 2:
		r, g, b = 255, 255, 255
	else:
		r, g, b = 0, 0, 0
	return r, g, b

#сепия
def sepia(r,g,b,dep):
	mid = (r+g+b) // 3
	r, g, b = mid + dep * 2, mid + dep, mid
	r = constrain(r,0,255)
	g = constrain(g,0,255)
	b = constrain(b,0,255)
	return r, g, b
#шум
def noise(r,g,b,fac):
	rand = randint(-fac,fac)
	r, g, b = r + rand, g + rand, b + rand
	r = constrain(r,0,255)
	g = constrain(g,0,255)
	b = constrain(b,0,255)
	return r, g, b

#яркость
def brightness(r,g,b,br):
	r, g, b = r + br, g + br, b + br
	r = constrain(r,0,255)
	g = constrain(g,0,255)
	b = constrain(b,0,255)
	return r, g, b

def corner(r,g,b,i,j,x,y,dim):
	rand = randint(0,9)
	if i not in range(dim, x-dim) or j not in range(dim, y-dim):
		if not rand:
			r, g, b = 0, 0, 0
	return r, g, b

im = Image.open("CFancy.jpg")
pixels = im.load()
x, y = im.size
print("Введите название фильтра: black, sepia, noise, bright, corner")
mode = input()
if mode == "black":
    bl = int(input("Введите параметр: "))
if mode == "sepia":
    dep = int(input("Введите глубину: "))
if mode == "noise":
    fac = int(input("Введите степень шума: "))
if mode == "bright":
    br = int(input("Введите знчаение яркости: "))

for i in range(x):  
	for j in range(y):

		r, g, b = pixels[i, j]
		#чб
		if mode == "black":
			pixels[i, j] = black(r,g,b,bl)
		
		#сепия
		elif mode == "sepia":
			pixels[i, j] = sepia(r,g,b,dep)

		#шум
		elif mode == "noise":
			pixels[i, j] = noise(r,g,b,fac)

		#яркость
		elif mode == "bright":
			pixels[i, j] = brightness(r,g,b,br)

		elif mode == "corner":
			pixels[i, j] = corner(r,g,b,i,j,x,y,50)
		else:
			if (r+g+b) // 3 > 100:
				r, g, b = r//3, g//3, 255
			else:
				r, g, b = r//2, g//2, b//2
			pixels[i, j] = r, g, b

im.save("CFancy2.jpg")       
im.show()

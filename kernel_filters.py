from  PIL import Image
from random import randrange

#соответствие диапазону
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

#функция наложения матрицы
def kernel(pixels,mat,l,div):
	rRes, gRes, bRes = 0, 0, 0
	for c in range(l):
		for k in range(l):
			rBuf, gBuf, bBuf = pixels[i - l // 2 + c, j - l // 2 + k]
			rBuf, gBuf, bBuf= rBuf * mat[c][k] , gBuf * mat[c][k] , bBuf * mat[c][k]
			rRes  += rBuf
			gRes  += gBuf
			bRes  += bBuf  

	rRes = round(rRes / div)
	gRes = round(gRes / div)
	bRes = round(bRes / div)

	rRes = constrain(rRes,0,255)
	bRes = constrain(bRes,0,255)
	gRes = constrain(gRes,0,255)

	return rRes, gRes, bRes


#матрицы фильтров
blur = [[1, 2, 1],
		[2, 4, 2],
		[1, 2, 1]]


emboss = [[-2, -1, 0],
		 [-1, 1, 1],
		 [0, 1, 2]]

sharpen = [[0, -1, 0],
		  [-1, 5, -1],
		  [0, -1, 0]]

edged = [[0, 1, 0],
		 [1, -4, 1],
		 [0, 1, 0]]

edgee = [[0, 0, 0],
		 [-1, 1, 0],
		 [0, 0, 0]]

sobelh = [[1, 2, 1],
		  [0, 0, 0],
		  [-1, -2, -1]]

sobelv = [[1, 0, -1],
		 [2, 0, -2],
		 [1, 0, -1]]

bblur = [[1, 1, 1],
		 [1, 1, 1],
		 [1, 1, 1]]

#осторожно!!!
mblur =   [[1, 0, 0, 0, 0, 0, 0, 0, 0],
		  [0, 1, 0, 0, 0, 0, 0, 0, 0],
		  [0, 0, 1, 0, 0, 0, 0, 0, 0],
		  [0, 0, 0, 1, 0, 0, 0, 0, 0],
		  [0, 0, 0, 0, 1, 0, 0, 0, 0],
		  [0, 0, 0, 0, 0, 1, 0, 0, 0],
		  [0, 0, 0, 0, 0, 0, 1, 0, 0],
		  [0, 0, 0, 0, 0, 0, 0, 1, 0],
		  [0, 0, 0, 0, 0, 0, 0, 0, 1]]

#кофэициент
div = 1

#путь к картинке
path = "CFancy.jpg"

#куда сохранить картинку
spath = "CFancy2.jpg"

mat = blur
im = Image.open(path)
im2 = Image.open(path)
pixels = im.load()
pixels2 = im2.load()
x, y = im.size
print("Введите название фильтра: blur, emboss, sharpen, edged, edgee, sobelh, sobelv, mblur")
mode = input()
if mode == "blur":
	mat = blur
	div = 16
if mode == "emboss":
	mat = emboss
if mode == "sharpen":
	mat = sharpen
if mode == "edged":
	mat = edged
if mode == "edgee":
	mat = edgee
if mode == "sobelh":
	mat = sobelh
if mode == "sobelv":
	mat = sobelv
if mode == "mblur":
	mat = mblur
	div = 9


l = len(mat)
for i in range(x):  
	for j in range(y):
		r, g, b = pixels[i, j]
		if i in range(l // 2, x - l // 2) and j in range(l // 2, y - l//2):
			r, g, b = kernel(pixels, mat,l,div)
		pixels2[i, j] = r, g, b

im2.save(spath)       
im2.show()

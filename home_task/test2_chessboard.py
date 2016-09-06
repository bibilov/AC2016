#test1.py

# шахматная доска

from PIL import Image

# длина/ширина кубика
BLOCK_LENGTH = 50



img = Image.open("img/small-image.jpg")
ps = img.load()
w, h = img.size


def is_white(x, y):
  width_even = (x // BLOCK_LENGTH) % 2 == 0
  height_even = (y // BLOCK_LENGTH) % 2 == 0
  # if both are even or both are odd
  return width_even == height_even


for i in range(w):
  for j in range(h):
    p = ps[i, j]
    if (is_white(i, j)):
      p = p[0]//2, p[1]//2, p[2]//2
    else:
      p = p[0]*2, p[1]*2, p[2]*2
    ps[i, j] = p


img.show()

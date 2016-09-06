#test1.py

# flip by X

from PIL import Image

img = Image.open("img/small-image.jpg")
ps = img.load()
w, h = img.size


last_pixel_index = w-1
for i in range(w//2):
  for j in range(h):
    p1 = ps[i, j]
    p2 = ps[last_pixel_index-i, j]
    ps[last_pixel_index-i, j] = p1
    ps[i, j] = p2


img.show()

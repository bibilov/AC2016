from PIL import Image
from random import randint

im = Image.open("../cat.jpg")
pixels = im.load()
x, y = im.size

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]

        # случайное число влияющее на шум. Чем больше разброс, тем больше шумов.
        random_value = randint(-200, 200)

        # формируем шум
        r += random_value
        g += random_value
        b += random_value

        pixels[i, j] = r, g, b

im.show()

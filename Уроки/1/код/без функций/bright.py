from PIL import Image

im = Image.open("../cat.jpg")
pixels = im.load()
x, y = im.size

k = -150  # коэффицент влияющий на величину яркости (рекомендуемое значение от -150 до 150)

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]

        # формируем яркость
        r += k
        g += k
        b += k

        pixels[i, j] = r, g, b

im.show()

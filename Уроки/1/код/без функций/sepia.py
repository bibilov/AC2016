from PIL import Image


im = Image.open("../cat.jpg")
pixels = im.load()
x, y = im.size

k = 200  # коэффицент влияющий на глубину сепии

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]

        # находим среднее значени нужное для сепии
        middle_value = (r + g + b) // 3

        # формируем сепию
        r = middle_value + 2 * k
        g = middle_value + k
        b = middle_value
        pixels[i, j] = r, g, b

im.show()

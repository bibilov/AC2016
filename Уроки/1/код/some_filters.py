from PIL import Image
from random import randint


# Сепия
def sepia(pixels, k):
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            middle_value = (r + g + b) // 3
            r = middle_value + 2 * k
            g = middle_value + k
            b = middle_value

            pixels[i, j] = r, g, b


# Негатив
def negative(pixels):
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = 255-r, 255-g, 255-b


# Шум
def noise(pixels, k):
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            random_value = randint(-k, k)
            r = r+random_value
            g = g+random_value
            b = b+random_value
            pixels[i, j] = r, g, b


# Яркость
def bright(pixels, k):
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = r+k, g+k, b+k


im = Image.open("cat.jpg")
pixels = im.load()
x, y = im.size

entry = ''
k = 0

while entry != 'нет':
    entry = input('Введите нужный фильтр: сепия, шум, яркость, негатив: ')
    if entry == 'сепия':
        k = int(input('Введите коэффицент(число) глубины для сепии: '))
        sepia(pixels, k)
    elif entry == 'шум':
        k = int(input('Введите коэффицент(число) для шума(Чем больше число, тем больше шумов): '))
        noise(pixels, k)
    elif entry == 'яркость':
        k = int(input('Введите коэффицент(число) для яркости(рекомендуемое значение от -150 до 150): '))
        bright(pixels, k)
    elif entry == 'негатив':
        negative(pixels)
    else:
        print('Вы ввели не правильное значение, попробуйте еще раз')
        continue

    im.show()

    entry = input("Желаете наложить новый фильтр? ('нет' - выход из программы): ")

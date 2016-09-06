#task3.py

from PIL import Image
from math import sin, cos


turns = int(input('Введите градус скручивания (+-): ')) # обороты (окружности (незамкнутые))
if turns == 0: raise ValueError('Cannot be zero')
ROTATE_DEGREE = turns * 360
WEIGHT = 3 # толщина заливки

class SimplePen:
  def __init__(self, weight, draw_point):
    self.weight = weight // 2
    self.draw_point = draw_point
  def draw(self, x, y):
    for i in range(x - self.weight, x + self.weight + 1):
      for j in range(y - self.weight, y + self.weight + 1):
        self.draw_point(i, j)
      


img = Image.open("img/small-image.jpg")
ps = img.load()
w, h = img.size


centerX, centerY = w//2, h//2
diagonal = int((w*w + h*h)**.5 // 2) # диагональ от центра до угла

# рост радиуса (фикс. зн.) и сам радиус (переменная (на матем. языке))
r_inc = diagonal / ROTATE_DEGREE
r = r_inc

last_w = w-1
last_h = h-1
ensure_x = lambda x: 0 if x < 0 else last_w if x > last_w else x
ensure_y = lambda y: 0 if y < 0 else last_h if y > last_h else y


def draw(x, y): ps[ensure_x(x), ensure_y(y)] = 0, 0, 0 # color
def draw_negate(x, y):
  x, y = ensure_x(x), ensure_y(y)
  color = ps[x, y]
  ps[x, y] = 255 - color[0], 255 - color[1], 255 - color[2]
  
pen = SimplePen(WEIGHT, draw)

for deg in range(0, ROTATE_DEGREE, 1 if ROTATE_DEGREE > 0 else -1):
  x = centerX + int(r * cos(deg))
  y = centerY + int(r * sin(deg))
  pen.draw(x, y)
  r += r_inc


img.show()

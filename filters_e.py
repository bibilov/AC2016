from  PIL import Image
from random import randrange


im = Image.open("D:/MCloud/Photos/IMG_0372.JPG")
pixels = im.load()
x, y = im.size


for i in range(x):  
    for j in range(y):

        r, g, b = pixels[i, j]
        bw = (r + g + b) // 3
        if bw > 20:
            pixels[i, j] = 255, 255, 255
im.show()

'''
С‡РµРј С…РѕСЂРѕС€ СЌС‚РѕС‚ С„РёР»СЊС‚СЂ?
С‚РµРј С‡С‚Рѕ С‚Р°РєРѕР№ С„РёР»СЊС‚СЂ РјРѕР¶РЅРѕ РёСЃРїРѕР»СЊР·РѕРІР°С‚СЊ РІ СЂР°СЃРїРѕР·РЅР°РІР°С‚РµР»СЏС… Рё
Р·Р° СЃС‡РµС‚ РґР°РЅРЅРѕРіРѕ С„РёР»СЊС‚СЂР° РјРѕР¶РЅРѕ Р±СѓРґРµС‚ РёР·Р±Р°РІРёС‚СЊСЃСЏ РѕС‚ С€СѓРјР° РЅР° РёР·РѕР±СЂР°Р¶РµРЅРёРё
'''

import image_slicer
import os
from PIL import Image, ImageEnhance

tiles = image_slicer.slice('farm.jpg', 32)

sum = []

for i in range(1,7):
    arr = []
    for j in range(1,7):
        imageString = 'farm_0' + str(i) + "_0" + str(j) + '.png'
        im = Image.open(imageString, 'r')
        pix_val = list(im.getdata())
        sum = 0
        for k in range(len(pix_val)):
            green_value = pix_val[k][1]
            sum+=green_value
        print(sum)

image = Image.open("farm_01_01.png")

enhancer = ImageEnhance.Sharpness(image)
image = enhancer.enhance(100000.0)
image.save('farm_01_01.png')


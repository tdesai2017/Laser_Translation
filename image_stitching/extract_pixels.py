# from PIL import Image
# import numpy as np
# im = Image.open('/Users/tushardesai/Documents/all_things_code/projects/laser_video/data/frame37.jpg', 'r')
# img = np.asarray(im) # convert it to ndarray
# print(len(img))

# https://www.youtube.com/watch?time_continue=2&v=oYndcjlzwX8&feature=emb_logo

from PIL import Image, ImageFilter
from matplotlib import pyplot as plt


def imageprepare(argv):
    """
    This function returns the pixel values.
    The imput is a png file location.
    """
    im = Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L', (28, 28), (255))  # creates white canvas of 28x28 pixels

    if width > height:  # check which dimension is bigger
        # Width is bigger. Width becomes 20 pixels.
        nheight = int(round((20.0 / width * height), 0))  # resize height according to ratio width
        if (nheight == 0):  # rare case but minimum is 1 pixel
            nheight = 1
            # resize and sharpen
        img = im.resize((20, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
        newImage.paste(img, (4, wtop))  # paste resized image on white canvas
    else:
        # Height is bigger. Heigth becomes 20 pixels.
        nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
        if (nwidth == 0):  # rare case but minimum is 1 pixel
            nwidth = 1
            # resize and sharpen
        img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical pozition
        newImage.paste(img, (wleft, 4))  # paste resized image on white canvas

    # newImage.save("sample.png

    tv = list(newImage.getdata())  # get pixel values

    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    return tva







x=[imageprepare('/Users/tushardesai/Documents/all_things_code/projects/laser_video/data/frame37.jpg')]#file path here
#print(len(x))# mnist IMAGES are 28x28=784 pixels
#print(x[0])
#Now we convert 784 sized 1d array to 24x24 sized 2d array so that we can visualize it
newArr=[[0 for d in range(28)] for y in range(28)]
k = 0
for i in range(28):
    for j in range(28):
        newArr[i][j]=x[0][k]
        k=k+1

#rounds every number to two decimal places
for row in range(len(newArr)):
  for col in  range(len(newArr[row])):
    newArr[row][col] = round(newArr[row][col], 2)

    #finds if there is anything close to target and prints the location
    if newArr[row][col] - 0.14 == 0:
      print (f"{newArr[row][col]}: {row, col}")
  
  

    #.14, .13 is our target here

# prints entire array
# for row in newArr:
#   print(row)

# print(newArr)
plt.imshow(newArr, interpolation='nearest')
plt.savefig('MNIST_IMAGE.png')#save MNIST image
plt.show()#Show / plot that image



"""

[[  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0  15  97 106 144 206 255
  232  31   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0  25 139 209 230 254 194 132 115  55
  236  36   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0  32 147 231 231 221 159  76  15   0   0  68 225
  130   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0  90 184  91   0   0   0   0   0   6 125 248 138
    7   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0  11   7   0   0   0   0  14  98 184 214  59   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0  60 193 215  89   0   0   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0  52 152 248 124  19   0   0   0   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0  92 239 250 254 156  55   7   0   0   0   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0  64 134 187 209 249 243 197 121  81   3   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0  26  23  96 166 254 177  58
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  40 174 255
  144   9   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   3  80
  221 176   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   31 253 117   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0  11   3   0   0   0   0   0   0
    0 162 194   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   9 205  15   0   0   0   0   0   0
    0 105 211   5   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0 158  67   0   0   0   0   0   0   0
    0 136 212   5   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0 179  45   0   0   0   0   0   0   0
   18 241 132   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0 104 200  23   0   0   0   0   0  25
  204 226  20   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0 107 248 181 120 121 142 190 232
  165  18   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0  55 139 201 224 179 127  25
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0   0   0   0   0   0   0   0   0   0]]

    """
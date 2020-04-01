from PIL import Image, ImageFilter
from matplotlib import pyplot as plt

def imageprepare(argv):
    """
    This function returns the pixel values as one array with 784 pixel values normalized
    so that 255 is 1 and 0 is 0.
    
    """
    im = Image.open(argv).convert('L')
    img = im.resize((28, 28), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
    tv = list(img.getdata()) 
    
    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    return tva

def reshape_pixel_array(pixel_arr):
   """ Takes flat array of 784 values and turns it into a 2d array with 28 rows of size 28 """
   reshaped_pixel_arr = []
   n = 28
   while n <= len(pixel_arr):
      reshaped_pixel_arr.append(pixel_arr[n-28:n])
      n+=28

   return reshaped_pixel_arr

def main():
  #Respective Image location
   pixel_array = imageprepare('/Users/tushardesai/Documents/all_things_code/projects/laser_video/data/frame37.jpg')

   #Reshapes array to 28x28 board
   newArr = reshape_pixel_array(pixel_array)
      
   plt.imshow(newArr, interpolation='nearest')
   plt.savefig('MNIST_IMAGE.png')#save MNIST image
   plt.show()#Show / plot that image

if __name__ == "__main__":
    main()

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
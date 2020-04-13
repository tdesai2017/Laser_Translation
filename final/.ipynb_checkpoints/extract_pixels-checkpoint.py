from PIL import Image, ImageFilter
from matplotlib import pyplot as plt

class PixelExtractor:
    def __init__(self, image_path, color = 'g'):
        """Image represents file path to target file """
        self.image_path = image_path
        self.color = color
        
        
    def imageprepare(self, argv):
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

    def reshape_pixel_array(self, pixel_arr):
        """ Takes flat array of 784 values and turns it into a 2d array with 28 rows of size 28 """
        reshaped_pixel_arr = []
        n = 28
        while n <= len(pixel_arr):
            reshaped_pixel_arr.append(pixel_arr[n-28:n])
            n+=28

        return reshaped_pixel_arr
    
    def extract_target_pixel_location(self):
        """ Returns list of target pixel locations """
        #Respective Image location
        pixel_array = self.imageprepare(self.image_path)

        #Select less_than_target color point --> must be calibrated
        #?? Should we use an abstract class here instead of an if statment ??
        if self.color == "g":
            less_than_target = .15
        else:
            raise ValueError("Unknown color value")

        #Chooses target pixels as well as it's location
        target_pixels = []
        for pixel in enumerate(pixel_array):
            if pixel[1] < less_than_target:
                target_pixels.append(pixel[0])

        return target_pixels
    
    def draw_image(self):
        """ Draws the image representation of the rgb pixel valued image """
      
        pixel_array = self.imageprepare(self.image_path)
        newArr = self.reshape_pixel_array(pixel_array)
        plt.imshow(newArr, interpolation='nearest')
        plt.savefig('MNIST_IMAGE.png')#save MNIST image
        plt.show()#Show / plot that image
    
# x = PixelExtractor('data/frame10.jpg', 'g')
# print(x.extract_target_pixel_location())
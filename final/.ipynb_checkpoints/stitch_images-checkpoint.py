import os
from extract_pixels import PixelExtractor
from matplotlib import pyplot as plt


class ImageStitcher:
    def __init__(self, directory_path = 'data'):
        """ Directory Path represents directory containing spliced images """

        self.directory_path = directory_path
    def create_composite_image_list (self):
        """ 
        Takes a directory and overlays its content images together based on 
        PixelExtractor's conditions
    
        """

        directory = os.fsencode(self.directory_path)
        #255 represents a black cell
        #0 represents a white cell
        composite_image_list = [0 for i in range(784)]

        for file in os.listdir(directory):
            filename = os.fsdecode(file)

          #creates pixel_extractor instance
        pixel_extractor = PixelExtractor(self.directory_path + '/' + filename, 'g')
        target_pixel_locations = pixel_extractor.extract_target_pixel_location()
        for loc in target_pixel_locations:
            composite_image_list[loc] = 255


        return composite_image_list
    
    
    def draw_image(self):
        """Draws the image representation of the composite image"""

        composite_image_list = self.create_composite_image_list()

        reshaped_composite_image = self.reshape_pixel_array(composite_image_list)

        plt.imshow(reshaped_composite_image, cmap='Greys',  interpolation='nearest')
        # plt.savefig('MNIST_IMAGE.png')#save MNIST image
        plt.show()#Show / plot that image
        return composite_image_list
    
    def reshape_pixel_array(self, composite_image_list):
        """ Takes flat array of 784 values and turns it into a 2d array with 28 rows of size 28 """
        reshaped_composite_image = []
        n = 28
        while n <= len(composite_image_list):
            reshaped_composite_image.append(composite_image_list[n-28:n])
            n+=28

        return reshaped_composite_image

  


  


# x = ImageStitcher()
# x.create_composite_image_list()


  


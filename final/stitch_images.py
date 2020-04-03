import os
from extract_pixels import PixelExtractor
from matplotlib import pyplot as plt



directory = os.fsencode('data')
#255 represents a black cell
#0 represents a white cell
composite_image_list = [0 for i in range(784)]

for file in os.listdir(directory):
  filename = os.fsdecode(file)
  pixel_extractor = PixelExtractor("data/" + filename, 'g')
  target_pixel_locations = pixel_extractor.extract_target_pixel_location()
  for loc in target_pixel_locations:
    composite_image_list[loc] = 255


reshaped_composite_image = []
n = 28
while n <= len(composite_image_list):
    reshaped_composite_image.append(composite_image_list[n-28:n])
    n+=28

plt.imshow(reshaped_composite_image, cmap='Greys',  interpolation='nearest')
plt.savefig('MNIST_IMAGE.png')#save MNIST image
plt.show()#Show / plot that image





  



    #  if filename.endswith(".asm") or filename.endswith(".py"): 
    #      # print(os.path.join(directory, filename))
    #      continue
    #  else:
    #      continue
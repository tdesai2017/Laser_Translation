import numpy as np
import cv2
import os

# filename_one = "data/frame13.jpg"


# image_one = Image.open(filename_one, 'r')

# pix_val = list(image_one.getdata())

# del image_one


# filename_1 = "data/frame13.jpg"
# filename_2 = "data/frame34.jpg"
# filename_3 = "data/frame26.jpg"

# image_1 = Image.open(filename_1)
# image_2 = Image.open(filename_2)
# image_3 = Image.open(filename_3)




# blendedImage = .5 * image_1 + .5 * image_2 

# images =  os.listdir('data')
# num_images = len(images)
# final_image = None
 
# for image in images:

#     if final_image != None:
#         image = cv2.imread('data/' + image,1)
#         print(image)
#         final_image += image * 1 / num_images
#     else:
#         final_image = cv2.imread('data/' + image,1)


# print(final_image)





img1 = cv2.imread('data/frame13.jpg',1)
img2 = cv2.imread('data/frame39.jpg',1)
img3 = cv2.imread('data/frame26.jpg',1)
img4 = cv2.imread('data/frame45.jpg',1)
img5 = cv2.imread('data/frame67.jpg',1)
img6 = cv2.imread('data/frame18.jpg',1)
img7 = cv2.imread('data/frame76.jpg',1)
img8 = cv2.imread('data/frame33.jpg',1)
img9 = cv2.imread('data/frame55.jpg',1)
img10 = cv2.imread('data/frame34.jpg',1)
img = (img1 * .1 + img2 * .1 + img3 * .1 + img4 * .1 + img5 * .1 + img6 * .1 + img7 * .1+ img8 * .1+ img9 * .1 + img10 * .1) /255
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


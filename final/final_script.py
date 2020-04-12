from video_to_images_converter import VideoToImageConverter
from stitch_images import ImageStitcher
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

#converts video into a collection of images saved in a folder ./data - Eric's Part
loaded_model = joblib.load("/Users/zumaad/Laser_Translation/final/k1_model.sav")
data = pd.read_csv("/Users/zumaad/Laser_Translation/final/train.csv")
features  = data.drop("label", axis = 1)
target = data["label"]
X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=3000)

vti_converter = VideoToImageConverter('3Video.mp4')
vti_converter.splice_video('data')


#Aside: Uses extract_pixels (Pixel Extractor) in its own code as a dependency
image_stitcher = ImageStitcher()

""" The digit array is what will be fed to the model """
digit_array = image_stitcher.create_composite_image_list()

#turn pixel array into DF that model expect. The model expects a dataframe with 1 row
#and 784 columns
pixel_dataframe = pd.DataFrame([[0,digit_array]])


#Draws Image from digit_array representation - used for validation when testing
image_stitcher.draw_image()

"""Input Srinath's Part"""
   

# if __name__ == "__main__":
#     main()
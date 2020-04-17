from video_to_images_converter import VideoToImageConverter
from stitch_images import ImageStitcher
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

#converts video into a collection of images saved in a folder ./data
# loaded_model = joblib.load("/Users/zumaad/Laser_Translation/final/k1_model.sav")

vti_converter = VideoToImageConverter('5.mp4')
vti_converter.splice_video('data')

#Aside: Uses extract_pixels (Pixel Extractor) in its own code as a dependency
image_stitcher = ImageStitcher()

""" The digit array is what will be fed to the model """

pixel_array = image_stitcher.draw_image()

pixel_dataframe = pd.DataFrame([pixel_array])

# loaded_model.predict()pixel_dataframe



# if __name__ == "__main__":
#     main()
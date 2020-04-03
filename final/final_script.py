from video_to_images_converter import VideoToImageConverter
from stitch_images import ImageStitcher


def main():
   #converts video into a collection of images saved in a folder ./data - Eric's Part
   vti_converter = VideoToImageConverter('3Video.mp4')
   vti_converter.splice_video('data')


   #Aside: Uses extract_pixels (Pixel Extractor) in its own code as a dependency
   image_stitcher = ImageStitcher()

   """ The digit array is what will be fed to the model """
   digit_array = image_stitcher.create_composite_image_list()
   print(digit_array)

   #Draws Image from digit_array representation - used for validation when testing
   image_stitcher.draw_image()


   """Input Srinath's Part"""
   

if __name__ == "__main__":
    main()
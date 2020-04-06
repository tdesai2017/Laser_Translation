'''
Using OpenCV takes a mp4 video and produces a number of images.
Requirements
----
You require OpenCV 3.2 to be installed.
Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py
Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
'''
import cv2
# import numpy as np
import os
import shutil


class VideoToImageConverter:

    def __init__(self, video_path):
        self.video_path = video_path

    def splice_video(self, destination_path = 'data'):
        """ 
        Splices given video to individual images and 
        writes them to a folder specified by destination_path

        *Don't name your destination path a folder that is important,
        since this folder will be deleted and populated with images
        """

        # Playing video from file:
        vidcap = cv2.VideoCapture(self.video_path)

        #Saves to respective folder
        try:
            if os.path.exists(destination_path):
                #Deletes any folder currently named ./data if it exists
                shutil.rmtree(destination_path, ignore_errors=True)
                print("Deleting current '" + destination_path + "' folder" )


            print("Creating new '" + destination_path + "' folder" )
            os.makedirs(destination_path)

        except OSError:
            print ('Error: Creating directory of data')

        currentFrame = 0
        while(True):
            # Capture frame-by-frame

            hasFrames,image = vidcap.read()

            if hasFrames:

                # Saves image of the current frame in jpg file
                name = './data/frame' + str(currentFrame) + '.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, image)

                # To stop duplicate images
                currentFrame += 1

            else:
                break

        # When everything done, release the capture
        vidcap.release()
        cv2.destroyAllWindows()



x = VideoToImageConverter('3Video.mp4')
x.splice_video()
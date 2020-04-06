import cv2
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
            print ('Error: Cannot create directory')

        frame_count = 0

        while(True):
            # Capture frame-by-frame

            hasFrames,image = vidcap.read()

            if hasFrames:

                # Saves image of the current frame in jpg file
                name = './'+ destination_path +'/frame' + str(frame_count) + '.jpg'
                print ('Spliced ' + name)
                cv2.imwrite(name, image)
                frame_count += 1

            else:
                break

        # When everything done, release the capture
        vidcap.release()
        cv2.destroyAllWindows()



# x = VideoToImageConverter('3Video.mp4')
# x.splice_video()



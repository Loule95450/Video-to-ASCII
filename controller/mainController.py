"""
This is the main controller of the program.
This is the controller that will be used to control the program.
"""
import os
import sys
import calendar;
import time;

import ascii_magic
import cv2
import glob
from moviepy.editor import *
from pygame import mixer  # Load the popular external library
from mutagen.mp3 import MP3

args = sys.argv


def remove_folders():
    """
    This function will remove all the folders in the directory.
    """
    try:
        files = os.listdir('./video/images')
        for i in range(0, len(files)):
            os.remove('./video/images' + '/' + files[i])

        return True
    except:
        return False


def images_to_ascii(images):
    images.sort()

    start_at = calendar.timegm(time.gmtime())

    mixer.init()
    mixer.music.load('./video/images/audio.mp3')
    mixer.music.play()

    for image in images:
        image_id = image.split('/')[-1].split('.')[0]
        last_image = int(images[len(images) - 1].split('/')[-1].split('.')[0])
        video_duration = round(MP3('./video/images/audio.mp3').info.length)
        actual_time = calendar.timegm(time.gmtime())
        time_elapsed = actual_time - start_at
        fps_recommanded = last_image / video_duration

        try:
            fps = round(int(image_id) / (actual_time - start_at))
        except:
            fps = fps_recommanded

        if fps < fps_recommanded:
            pass
        else:
            # Return to line 50 times
            my_art = ascii_magic.from_image_file(image)
            ascii_magic.to_terminal(my_art)
            print("> " + str(time_elapsed) + "s/" + str(video_duration) + "s - " + str(fps) + "/fps")


def video_to_images(video_path):
    # Opens the Video file
    video = cv2.VideoCapture(video_path)
    i = 0
    images = glob.glob("./video/images/*.jpg")
    start_at = calendar.timegm(time.gmtime())

    while (video.isOpened()):
        ret, frame = video.read()
        if ret == False:
            break

        file_name = str(i).zfill(5)
        cv2.imwrite('./video/images/' + str(file_name) + '.jpg', frame)
        print(chr(27) + "[2J")
        actual_time = calendar.timegm(time.gmtime())
        try:
            print("Downloding video - " + str(round(i * 100 / video.get(cv2.CAP_PROP_FRAME_COUNT))) + '% done - ' + str(i) + '/' + str(video.get(cv2.CAP_PROP_FRAME_COUNT)) + ' - ' + str(round(((video.get(cv2.CAP_PROP_FRAME_COUNT) - i) / i) * (actual_time - start_at))) + " seconds")
        except:
            print("Downloding video - " + str(round(i * 100 / video.get(cv2.CAP_PROP_FRAME_COUNT))) + '% done - ' + str(i) + '/' + str(video.get(cv2.CAP_PROP_FRAME_COUNT)))
        i += 1


    images.sort()


# pass the image as command line argument
video_path = args[1]

print("Traitement de : " + video_path + " merci de patienter...")

# remove all the images in the directory before starting
def video_to_audio(video_path):
    mp4_file = video_path
    mp3_file = r'./video/images/audio.mp3'

    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()


if remove_folders() == True:
    video_to_audio(video_path)
    # convert the video to images
    video_to_images(video_path)

    # convert the images to ascii
    images_to_ascii(glob.glob("./video/images/*.jpg"))

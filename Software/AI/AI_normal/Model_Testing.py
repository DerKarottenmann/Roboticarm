# Dateiname: image_classification.py

import cv2 as cv
import numpy as np
import requests
from tensorflow.keras import models
from PIL import Image
from io import BytesIO

def load_and_preprocess_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.convert('L') #graustufen
    img = cv.resize(np.array(img), (28, 28))  
    img = img / 255.0
    img = np.expand_dims(img, axis=-1)  
    img = np.expand_dims(img, axis=0)  
    return img

def main():
   
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfFGp5r2AhHK2JoxyC6_tx6-8EsPAOxpn2HT6DLkGTCrUt8xG0ymrkqzz_CCqfxq8W3nE&usqp=CAU'
 
    img = load_and_preprocess_image(url)

   
    model = models.load_model('mnist_classifier.model')
    prediction = model.predict(img)
    predicted_label = np.argmax(prediction)
    class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(f"Vorhergesagte Klasse: {class_names[predicted_label]}")

if __name__ == "__main__":
    main()



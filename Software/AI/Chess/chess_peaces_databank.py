import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Pfad zu den Bilddaten
data_dir = 'Schachdatenbank'

# Zielgröße der Bilder
target_size = (128, 128)

# Klassenordner
classes = ['Bauer', 'Turm', 'Springer', 'Läufer', 'Dame', 'König']

# Bilddaten und Labels sammeln
image_data = []
labels = []

for class_index, class_name in enumerate(classes):
    class_dir = os.path.join(data_dir, class_name)
    for filename in os.listdir(class_dir):
        img_path = os.path.join(class_dir, filename)
        img = load_img(img_path, target_size=target_size)
        img_array = img_to_array(img)
        image_data.append(img_array)
        labels.append(class_index)

# In NumPy-Arrays konvertieren und normalisieren
image_data = np.array(image_data)
image_data = image_data / 255.0
labels = np.array(labels)

# Datenbank speichern
np.savez('schachfiguren_datenbank.npz', images=image_data, labels=labels)


import numpy as np
from tensorflow.keras import models

# Datenbank laden
data = np.load('schachfiguren_datenbank.npz')
image_data = data['images']
labels = data['labels']

# Dein bestehendes CNN-Modell laden
model = models.load_model('chess_pieces_classifier.model')

# Modell trainieren
model.fit(image_data, labels, epochs=10)

# Modell speichern
model.save('chess_pieces_classifier.model')

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models

# MNIST-Datenbank laden
(training_images, training_labels), (testing_images, testing_labels) = datasets.mnist.load_data()

# Bilder normalisieren
training_images = training_images / 255.0
testing_images = testing_images / 255.0

# Bilder reshapen, um sie für Conv2D kompatibel zu machen
training_images = np.expand_dims(training_images, axis=-1)
testing_images = np.expand_dims(testing_images, axis=-1)

# Klassen für MNIST-Daten
class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Visualisierung der ersten 16 Trainingsbilder
for i in range(16):
    plt.subplot(4, 4, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(training_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[training_labels[i]])
# plt.show()

# Modell definieren
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Modell kompilieren
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Modell trainieren
model.fit(training_images, training_labels, epochs=10, validation_data=(testing_images, testing_labels))

# Modell evaluieren
loss, accuracy = model.evaluate(testing_images, testing_labels)
print(f"Loss: {loss}")
print(f"Accuracy: {accuracy}")

# Modell speichern
model.save('mnist_classifier.model')


# model = models.load_model('mnist_classifier.model')

    
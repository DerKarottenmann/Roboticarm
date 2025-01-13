import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def segment_chessboard_by_color(img_path):
    # Bild laden
    img = cv.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Das Bild konnte nicht geladen werden. Überprüfe den Pfad: {img_path}")

    # Bild in HSV konvertieren
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Definieren der Farbbereiche für Schwarz und Beige
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])
    
    lower_beige = np.array([0, 0, 50])
    upper_beige = np.array([180, 50, 255])

    # Masken für Schwarz und Beige erstellen
    mask_black = cv.inRange(hsv, lower_black, upper_black)
    mask_beige = cv.inRange(hsv, lower_beige, upper_beige)

    # Konturen für Schwarz und Beige finden
    contours_black, _ = cv.findContours(mask_black, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_beige, _ = cv.findContours(mask_beige, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Konturen kombinieren
    contours = contours_black + contours_beige

    # Größte Kontur finden (angenommen, dies ist das Schachbrett)
    if not contours:
        raise ValueError("Keine Konturen gefunden. Stelle sicher, dass das Bild ein Schachbrett enthält.")

    max_contour = max(contours, key=cv.contourArea)
    
    # Begrenzungsrechteck um das Schachbrett finden
    x, y, w, h = cv.boundingRect(max_contour)
    chessboard = img[y:y+h, x:x+w]

    # Größe des Schachbrettbildes anpassen, um 8x8 Felder zu gewährleisten
    square_size = w // 8
    squares = []

    for i in range(8):
        for j in range(8):
            square = chessboard[i*square_size:(i+1)*square_size, j*square_size:(j+1)*square_size]
            squares.append(square)

    return squares

# Beispielbild eines Schachbretts segmentieren
chessboard_img_path = 'C:/Users/Yannik/OneDrive/Desktop/Schach.jpg'  # Ersetze dies durch den Pfad zu deinem Schachbrettbild
squares = segment_chessboard_by_color(chessboard_img_path)

# Anzeigen der segmentierten Felder
fig, axes = plt.subplots(8, 8, figsize=(8, 8))
axes = axes.ravel()

for i in range(64):
    axes[i].imshow(cv.cvtColor(squares[i], cv.COLOR_BGR2RGB))
    axes[i].axis('off')

plt.show()



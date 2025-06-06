import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import tensorflow as tf
from keras.models import load_model
import math

# Load the trained Keras model and labels
model_path = r"E:\current project\AI_PROJECT\AI_MODEL\keras_model.h5"
labels_path = r"E:\current project\AI_PROJECT\AI_MODEL\labels.txt"

print("Loading Model...")
model = load_model(model_path)
print("Model Loaded Successfully!")

# Load class labels
with open(labels_path, "r") as f:
    labels = [line.strip() for line in f.readlines()]
print("Labels Loaded:", labels)

# Open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open Camera.")
    exit()

detector = HandDetector(maxHands=1)
offset = 20
imgSize = 224

try:
    print("Starting Hand Detection...")
    while True:
        success, img = cap.read()
        if not success:
            print("Error: Failed to capture image.")
            break

        print("Frame Captured!")
        imgOutput = img.copy()
        hands, img = detector.findHands(img)

        if hands:
            print("Hand Detected!")
            hand = hands[0]
            x, y, w, h = hand['bbox']
            print(f"Hand Bounding Box: {x}, {y}, {w}, {h}")

            # Crop the hand region
            y1, y2 = max(0, y - offset), min(img.shape[0], y + h + offset)
            x1, x2 = max(0, x - offset), min(img.shape[1], x + w + offset)
            imgCrop = img[y1:y2, x1:x2]

            if imgCrop.size > 0:
                print("Processing Hand Image...")
                imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
                aspectRatio = h / w

                if aspectRatio > 1:
                    k = imgSize / h
                    wCal = math.ceil(k * w)
                    imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                    wGap = math.ceil((imgSize - wCal) / 2)
                    imgWhite[:, wGap:wGap + imgResize.shape[1]] = imgResize
                else:
                    k = imgSize / w
                    hCal = math.ceil(k * h)
                    imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                    hGap = math.ceil((imgSize - hCal) / 2)
                    imgWhite[hGap:hGap + imgResize.shape[0], :] = imgResize

                # Normalize and prepare input for model
                imgWhite = imgWhite / 255.0
                imgWhite = np.expand_dims(imgWhite, axis=0)

                # Predict gesture
                prediction = model.predict(imgWhite)
                classIndex = np.argmax(prediction)
                confidence = prediction[0][classIndex]
                label = f"{labels[classIndex]} ({confidence:.2f})"
                print(f"Prediction: {label}")

                # Display label
                cv2.putText(imgOutput, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (0, 0, 255), 2)

        cv2.imshow('Image', imgOutput)
        key = cv2.waitKey(1)
        if key == ord('q'):
            print("Exiting on user request.")
            break

except KeyboardInterrupt:
    print("Program interrupted. Exiting...")

finally:
    cap.release()
    cv2.destroyAllWindows()

# Sign-Language-Detection-System-complete-
This is a complete sign language detection System trained and tested on locally collected images of hand gestures


The project is an AI-based system to detect hand gestures used in sign language. It uses your webcam to capture hand signs and identifies them using a trained deep learning model.


**Files in the Project:**

* `DataCollection.py` – Used to collect hand gesture images for training
* `test.py` – Used to test and run real-time predictions
* `keras_model_custom2.h5` – Trained Keras model
* `labels.txt` – Names of the gestures (classes)
* hand gesture image samples (7800)


Make sure you have Python 3.10 or lower (down to 3.7) installed because MediaPipe is not compatible with the latest Python versions.

**Libraries Required:**

You need to install these Python libraries before running the project:

```
pip install opencv-python cvzone numpy tensorflow mediapipe
```
or simply run

pip install -r requirements.txt
---

**List of Gestures Detected:**

The system can recognize the following gestures (from `labels.txt`):

```
Bye, Call, Good Luck, Hello, I Love You, Left, Loser, Nice, No, Not okay,
Ok, Peace, Please, Power, Right, Rock, Smile, Stop, Thank you, Yes
```

**How to Collect Data:**

1. Open `DataCollection.py`
2. Change this line to match the gesture you're saving:

   ```
   from pathlib import Path
   folder = Path("Data") / "YourGesture"
   ```
3. Run the script:

   ```
   python DataCollection.py
   ```
4. Stand in front of the webcam and press **`s`** to save hand images.
5. It will save cropped hand images in that folder.


**How to Run Gesture Prediction:**
1. Ensure the model and label paths in `test.py` point to the `AI_MODEL` folder:

   ```python
   from pathlib import Path
   BASE_DIR = Path(__file__).resolve().parent.parent
   model_path = BASE_DIR / "AI_MODEL" / "keras_model.h5"
   labels_path = BASE_DIR / "AI_MODEL" / "labels.txt"
   ```
2. Run the test script:

   ```bash
   python test.py
   ```
3. It will open the webcam and start detecting gestures in real time.
4. Press **`q`** to quit.
**How it Works:**

* The program uses **OpenCV** and **cvzone** to detect hands.
* The hand image is cropped, resized, and passed to the model.
* The model predicts the gesture based on what it learned during training.


**Tips:**

* Use a plain background (preferably white) for better accuracy.
* Use proper lighting while collecting data and testing.
* You can connect your phone camera using DroidCam if your laptop camera is not good.


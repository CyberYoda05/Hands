try:
    import cv2
    import mediapipe as mp
    import time
    from tensorflow.keras.models import load_model
    import numpy as np
except ImportError:
    import os
    print  ("Htm bindings requires the following modules:\n  -> opencv-python\n  -> mediapipe\ninstalling modules now...")
    os.system('cmd /k "pip install opencv-python"')
    os.system('cmd /k "pip install mediapipe"')
    raise

class Handtracking():
    def __init__(self, maxhands: object = 1, mode: object = False, detCon: object = 0.5, trackCon: object = 0.5, complex: object = 1):
        self.maxhands = maxhands
        self.mode = mode
        self.detcon = detCon
        self.trackcon = trackCon
        self.complex = complex
        self.mHands = mp.solutions.hands
        self.hands = self.mHands.Hands(self.mode, self.maxhands, self.complex, self.detcon, self.trackcon)
        self.mpDraw = mp.solutions.drawing_utils
    def findh(self, img, draw = True):
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mHands.HAND_CONNECTIONS)
        return img


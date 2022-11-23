try:
    import cv2
    import mediapipe as mp
    import time
    from tensorflow.keras.models import load_model
    import numpy as np
    import v2
except ImportError:
    import os
    print  ("Htm bindings requires the following modules:\n  -> opencv-python\n  -> mediapipe\ninstalling modules now...")
    os.system('cmd /k "pip install opencv-python"')
    os.system('cmd /k "pip install mediapipe"')
    raise


def main():
    i = 0
    lastclass = ''
    time1 = 0
    time2 = 0
    f = open('gesture.names', 'r')
    classNames = f.read().split('\n')
    f.close()
    # print(classNames)
    model = load_model('mp_hand_gesture')
    camera = cv2.VideoCapture(0)
    detector = v2.Handtracking()
    while (cv2.waitKey(1) & 0xFF != ord('1')):
        frame, image = camera.read()
        image = detector.findh(image)
        x, y, c, = image.shape
        image = cv2.flip(image, 1)
        imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = detector.hands.process(imagergb)
        # print(result)
        className = ''
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:  #
                for lm in handslms.landmark:
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)
                    landmarks.append([lmx, lmy])
                prediction = model.predict([landmarks])
                classID = np.argmax(prediction)
                className = classNames[classID]
                print(className)
                if className == lastclass:
                    i += 1
                else:
                    i = 0
                print(i)
                lastclass = className
                if i == 5:
                    print(True)
                    if className == "call me":
                        print("okay")
                        i = 0

        cv2.imshow("Hello world!", image)


if __name__ == "__main__":
    main()
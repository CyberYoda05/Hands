import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
import time
import Handy_program as Hp
import Settings

def main():
    Stop = False #additional stoping conditions
    handy = Hp.Hfunctions() #calls the hand gestures
    last_name, className = '', '' #used for identifying classes
    gesture_times_called = 0
    gesture_times_fps = 20 #used for wait period before gesture is called
    model = load_model('mp_hand_gesture')
    mphands = mp.solutions.hands
    hands = mphands.Hands(static_image_mode=False, #calls the hand tracking function
                          max_num_hands=1,
                          model_complexity=1,
                          min_detection_confidence=0.5,
                          min_tracking_confidence=0.5)
    mpDraw = mp.solutions.drawing_utils
    time2 = 0
    camera = cv2.VideoCapture(0) # initiates camera
    f = open('gesture.names', 'r') #opens gesture
    classNames = f.read().split('\n')
    f.close()
    while (cv2.waitKey(1) & 0xFF != ord('q')) and Stop == False:
        className = ''
        #defining camera
        ret, frame = camera.read()
        frame = cv2.flip(frame, 1)
        # flips image
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # this line allows changes the color type of the image to RGB
        x, y, c, = image.shape
        result = hands.process(image)
        # processes the image and turns it into the hand landmarks
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
            mpDraw.draw_landmarks(frame, handslms, mphands.HAND_CONNECTIONS)
        time1 = time.time()
        fps = 1 / (time1 - time2)
        time2 = time1
        if last_name == className: # calls the gesture after detected
            if gesture_times_called == gesture_times_fps:
                gesture_times_called = 0
                if className == 'thumbs up':
                    handy.increase()
                if className == 'thumbs down':
                    handy.decrease()
                if className == 'call me':
                    handy.youtube()
                if className == 'stop':
                    handy.up()
                if className == 'live long':
                    handy.tab()
                if className == 'okay':
                    handy.windows()
                if className == 'fist':
                    handy.close_tab()
                if className == 'rock':
                    handy.down_key()
                if className == 'peace':
                    handy.enter()
            else:
                gesture_times_called += 1

        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3) # shows FPS
        cv2.imshow('HTM', frame)
        last_name = className
        if cv2.waitKey(1) & 0xFF == ord('s'): # settings open key
            try:
                cv2.destroyWindow('HTM')
            except:
                pass
            settings = Settings.Settings(str(className), str(landmarks)) # opens settings
            settings.main()
            # Stop = settings.stop()

    cv2.destroyWindow('HTM')
    camera.release()


if __name__ == '__main__':
    main()
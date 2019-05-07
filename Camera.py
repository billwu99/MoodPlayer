import numpy as np
import cv2
import MusicPlayer
import EmotionDetection

cap = cv2.VideoCapture(0)

# Resize window
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480);

detector = EmotionDetection.EmotionDetection()
player = MusicPlayer.MusicPlayer()
musicPlaying = False
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)

    # Take a picture, quit or continue
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('w'):
        if musicPlaying == False:
            cv2.imwrite('snapshot.png', frame)
            mood = detector.getEmotion()
            player.play(mood)
            musicPlaying = True
    elif key == 32:
        if musicPlaying:
            player.stop()
            musicPlaying = False

        


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
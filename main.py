import cv2
import serial
from cvzone.HandTrackingModule import HandDetector

pythoncap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)

bt = serial.Serial("COM6", 9600, timeout=1)

while True:
    ret, frame = pythoncap.read()
    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame)

    if hands:
        hand1 = hands[0]
        fingers = detector.fingersUp(hand1)
        count = fingers.count(1)
        print(count)

        command = str({
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4'
        }.get(count, '0'))

        bt.write(command.encode("utf-8"))
    else:
        print("No hands detected")

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

pythoncap.release()
cv2.destroyAllWindows()

import cv2
import winsound

cap = cv2.VideoCapture(0)
i = 0
while (1):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('D:/Workspace/OpencvVideo/' + str(i) + '.jpg', frame)
        i += 1
        winsound.Beep(3000, 600)
    cv2.imshow("capture", frame)
cap.release()
cv2.destroyAllWindows()

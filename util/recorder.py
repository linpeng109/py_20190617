import datetime
import random
import string
import winsound

import cv2
import numpy as np

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

text = '测试'
img = np.zeros((320, 320, 3), np.uint8)
org = (10, 180)
fontFace = cv2.FONT_HERSHEY_TRIPLEX
fontScale = 0.5
fontcolor = (0, 0, 255)
thickness = 1
lineType = 4
bottomLeftOrigin = 1
cv2.putText(img, text, org, fontFace, fontScale, fontcolor, thickness, lineType)

fpt = int(capture.get(cv2.CAP_PROP_FPS))
size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
path = 'D:/Workspace/OpencvVideo/'
profile = ''.join(random.sample(string.ascii_letters + string.digits, 8)) + '_'
filename = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.avi'
fullpath = path + profile + filename

out = cv2.VideoWriter(fullpath, fourcc, fpt, size)
while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        out.write(frame)
        cv2.imshow("click 'q' to exit", frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            winsound.Beep(3000, 600)
            break
    else:
        break
print(fullpath)

capture.release()
out.release()
cv2.destroyAllWindows()

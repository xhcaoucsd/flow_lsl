import cv2
from pylsl import StreamInfo, StreamOutlet
import numpy as np

WC_WIDTH = 640
WC_HEIGHT = 480
WC_CHNS = 3
SAMPLE_RATE = 10


#cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

stream_info_webcam = StreamInfo('Webcam', 'Experiment', WC_WIDTH * WC_HEIGHT * WC_CHNS, SAMPLE_RATE, 'int32', 'webcamid_1')

outlet_webcam = StreamOutlet(stream_info_webcam)

while rval:
    #cv2.imshow("preview", frame)
    outlet_webcam.push_sample(frame.flatten())
    print(frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
vc.release()
#cv2.destroyWindow("preview")

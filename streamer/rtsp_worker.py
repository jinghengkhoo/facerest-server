import cv2
import gi
import cv2
import argparse

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject

cap = cv2.VideoCapture("rtsp://root:pass@192.168.0.91:554/axis-media/media.amp")

while True:
    ret, frame = cap.read()

    if ret:


    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

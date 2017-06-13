import cv2

class EyeTracker:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

    def track(self, image):
        faceRects = self.faceCascade.detectMultiScale(image,scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
        rects = []
        for (fX, fY, fW, fH) in faceRects:
            faceROI = image[fY:fY + fH, fX:fX + fW]
            rects.append((fX, fY, fX + fW, fY + fH))

            eyeRects = self.eyeCascade.detectMultiScale(faceROI, scaleFactor = 1.1, minNeighbors = 10, minSize = (20, 20), flags = cv2.CASCADE_SCALE_IMAGE)

            for (eX, eY, eW, eH) in eyeRects:
                rects.append((fX + eX, fY + eY, fX + eX + eW, fY + eY + eH))

        return rects

def resize(image, width=None, height=None,inter =cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height/float(h)
        dim = (int(w*r), height)
    else:
        r = width/float(w)
        dim = (width, int(h*r))
    resized = cv2.resize(image,dim,interpolation=inter)
    return resized

et = EyeTracker()
cam = cv2.VideoCapture(0)

while True:
    frame = cam.read()[1]
    frame = resize(frame, width=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = et.track(gray)

    for rect in rects:
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()

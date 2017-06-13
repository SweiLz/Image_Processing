import cv2

class FaceDetector:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def detect(self, image, scaleFactor=1.1, minNeighbors=5, minSize = (30, 30)):
        rects = self.faceCascade.detectMultiScale(image,
        scaleFactor = scaleFactor,
        minNeighbors = minNeighbors, minSize = minSize,
        flags = cv2.CASCADE_SCALE_IMAGE)
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

fd = FaceDetector()
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    frame = resize(frame, width=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    frameClone = frame.copy()

    for (fX, fY, fW, fH) in faceRects:
        cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 255, 0), 2)

    cv2.imshow("Face", frameClone)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()
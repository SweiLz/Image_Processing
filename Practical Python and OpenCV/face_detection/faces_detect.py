import cv2

class FaceDetector:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def detect(self, image, scaleFactor = 1.1, minNeighbors = 5,minSize = (30, 30)):
        rects = self.faceCascade.detectMultiScale(image,
        scaleFactor = scaleFactor,
        minNeighbors = minNeighbors, minSize = minSize,
        flags = cv2.CASCADE_SCALE_IMAGE)
        return rects


fd = FaceDetector()

image = cv2.imread("face_detect_1.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 5,minSize = (30, 30))
print("I found {} face(s)".format(len(faceRects)))

for (x, y, w, h) in faceRects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Faces", image)
cv2.waitKey(0)




image = cv2.imread("face_detect_2.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faceRects = fd.detect(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (30, 30))
print("I found {} face(s)".format(len(faceRects)))

for (x, y, w, h) in faceRects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)
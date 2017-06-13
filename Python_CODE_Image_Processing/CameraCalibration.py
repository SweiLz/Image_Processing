import numpy as np
import cv2

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((9*6,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

cap = cv2.VideoCapture(1)

text_file = open("Output.txt", "w")
i=0
while(cap.isOpened()):
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    ret,img = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (9,6),None) #(img,pattern,conners)

    # If found, add object points, image points (after refining them)
    if ret == True:

        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(9,6),(-1,-1),criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (9,6), corners2,ret)

        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1] , None, None)

        h, w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
        dst = cv2.undistort(img, mtx, dist, None, newcameramtx)


        cv2.imshow('img',img)
        cv2.imshow('dst',dst)
    else:
        cv2.imshow('img',img)

    userKey = cv2.waitKey(100)

    if userKey==27:
        break
    elif userKey == 73:
        i+=1
        cv2.imwrite('CameraCarlibration/'+str(i)+'.jpg',img)
        print('Saved CameraCarlibration/'+str(i)+'.jpg')


cv2.destroyAllWindows()
text_file.close()
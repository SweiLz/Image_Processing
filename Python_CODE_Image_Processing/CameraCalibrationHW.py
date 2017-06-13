import numpy as np
import cv2

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((9*6,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)



for i in range(1,9):

    img = cv2.imread('CameraCarlibration/'+str(i)+'.jpg')

    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

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

        i+=1
        cv2.imwrite('CameraCarlibration/A' + str(i) + '.jpg',dst)
        print('Writted CameraCarlibration/A'+ str(i) + '.jpg')

        fileName = 'CameraCarlibration/data'+str(i)+'.txt'
        text_file = open(fileName, 'w')
        text_file.writelines('Intrinsic Camera Matrix\n')
        text_file.writelines(np.array_str(mtx))
        text_file.writelines('\n\nDistortion Coefficient\n')
        text_file.writelines(np.array_str(dist))
        text_file.writelines('\n\nExtrinsic Camera Matrix\n')
        text_file.writelines('Rotation Matrix\n')
        text_file.writelines(str(rvecs))
        text_file.writelines('\nTranslation Matrix\n')
        text_file.writelines(str(tvecs))
        text_file.close()

cv2.destroyAllWindows()

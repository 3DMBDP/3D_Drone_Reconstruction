import cv2
import numpy as np


img1 = cv2.imread('/home/ayush34/Desktop/Project/seg1.png',0)
img1 = cv2.resize(img1, (600, 800))
img2 = cv2.imread('/home/ayush34/Desktop/Project/seg2.png',0)

surf = cv2.xfeatures2d.SURF_create()
 
orb = cv2.ORB_create(nfeatures=1500)
 
keypoints, descriptors = orb.detectAndCompute(img1, None)
 
img1 = cv2.drawKeypoints(img1, keypoints, None)
 
cv2.imshow("Image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



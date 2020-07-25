import numpy as np
import cv2

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("image_1.jpg")

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey(-1)
cv2.destroyAllWindows()
import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)  # returns a tuple of number of rows, columns and channels
print(img.size)  # returns total numer of pixels accessed
print(img.dtype)  # returns image datatype

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# ROI = Region Of Interest - Point in the image we care about

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# resize images
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# img3 = cv2.add(img, img2)
img3 = cv2.addWeighted(img, 0.8, img2, 0.2, 0)

cv2.imshow('Messi Ya Boy', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
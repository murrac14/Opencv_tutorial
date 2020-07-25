import cv2

# Reading an image
img = cv2.imread('lena.jpg', -1)
print(img)

cv2.imshow('First Image', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Write an image
    cv2.imwrite('Lena Clone.png', img)
    cv2.destroyAllWindows()
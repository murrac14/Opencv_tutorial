import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    '''if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 0), 1)
        cv2.imshow('Clicker', img)'''

    '''if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 1)
        cv2.imshow('Clicker', img)'''

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('Clicker', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        myColourImage = np.zeros((512, 512, 3), np.uint8)

        myColourImage[:] = [blue, green, red]

        cv2.imshow('Colour', myColourImage)

img = cv2.imread('lena.jpg')
cv2.imshow('Clicker', img)
points = []
cv2.setMouseCallback('Clicker', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
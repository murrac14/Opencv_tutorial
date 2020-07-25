import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        read_points.append((x, y))

        if len(read_points) >= 2:
            # Set points
            roi_width = abs(read_points[-2][0] - read_points[-1][0])
            roi_height = abs(read_points[-2][1] - read_points[-1][1])
            leftmost_point = min(read_points[-2][0], read_points[-1][0])
            rightmost_point = leftmost_point + roi_width
            upmost_point = min(read_points[-2][1], read_points[-1][1])
            downmost_point = upmost_point + roi_height

            print('x: ' + str(leftmost_point) + ' - ' + str(rightmost_point))
            print('y: ' + str(upmost_point) + ' - ' + str(downmost_point))
            roi = img[upmost_point:downmost_point, leftmost_point:rightmost_point]

            print(str(leftmost_point) + ', ' + str(upmost_point))
            img[0: downmost_point - upmost_point, 0 : rightmost_point - leftmost_point] = roi[0:, 0:]

            read_points.clear()
            print(len(read_points))
            cv2.imshow('Copy Stuff', img)
            roi = []


img = cv2.imread('messi5.jpg')

read_points = []

cv2.imshow('Copy Stuff', img)
cv2.setMouseCallback('Copy Stuff', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
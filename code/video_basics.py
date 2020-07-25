import cv2
import datetime


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Checking the fourcc code of the video format and passing it as an argument
fourcc = cv2.VideoWriter_fourcc(*'XVID')

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Change the frame size. Can only be set to my cameras default values ie, 640x480 or 1280x720...
cap.set(3, 1280)
cap.set(4, 720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create an instance of our cv2 output creator takes file-name, fourcc code, fps and tuple of dimensions (w, h)
out = cv2.VideoWriter('Output.avi', fourcc, 20, (640, 480))

# Set the font etc. of the text
font = cv2.FONT_HERSHEY_COMPLEX
text = 'Resolution: ' + str(int(cap.get(3))) + 'x' + str(int(cap.get(4)))

while cap.isOpened():

    # Read from the camera instance named cap
    ret, frame = cap.read()
    if ret is True:
        # Write the resolution text
        frame = cv2.putText(frame, text, (10, 50), font, 1, (125, 125, 0), 2, cv2.LINE_AA)
        # Date and Time
        currentDateTime = str(datetime.datetime.now())
        frame = cv2.putText(frame, currentDateTime, (10, 100), font, 1, (125, 125, 0), 2, cv2.LINE_AA)

        # Output the frame
        out.write(frame)

        grey_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Home Video', grey_vid)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()

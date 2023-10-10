
"""import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('C://Users//Vikas Yadav//Desktop//test.jpg',-1)
print img
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
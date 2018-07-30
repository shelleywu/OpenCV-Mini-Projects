import numpy as np
import cv2
#This code was before realizing that I misread what a "drawing app" meant.

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
color1 = (0, 255, 0)
color2 = (0, 0, 0)
currentColor = color1

line_width = 3
radius = 100
point = (0,0)

# click callback
def click(event, x, y, flags, param):
    global canvas, point, pressed, currentColor
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x,y)
        if x > 250:
            currentColor = color2
        if x < 250:
            currentColor = color1
        print("LButton Down")
    elif event == cv2.EVENT_MOUSEMOVE:
        print("Mouse Move")
    elif event == cv2.EVENT_LBUTTONUP:
        print("LButton Up")

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:
    
    cv2.imshow("canvas",canvas)
    cv2.circle(canvas, point, radius, currentColor, line_width)
    # key capture every 1ms
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()

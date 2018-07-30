import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
color1 = (0, 255, 0)
color2 = (0, 0, 0)
currentColor = color1

line_width = -1
radius = 12
pressed = False

# click callback
def click(event, x, y, flags, param):
    global canvas, pressed, currentColor
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(canvas, (x,y), radius, currentColor, line_width)
        pressed = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if pressed:
            cv2.circle(canvas, (x,y), radius, currentColor, line_width)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:
    
    cv2.imshow("canvas",canvas)        # key capture every 1ms
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('c'):
        currentColor = color2


cv2.destroyAllWindows()

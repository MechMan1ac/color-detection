import cv2 
import color
from PIL import Image

video = cv2.VideoCapture(0)

def dectect_color(frame, lower_color, upper_color):
    blurred_frame = cv2.GaussianBlur(frame, (71, 71), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)

    return mask

def draw_boundary(frame, mask, text):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 200:
            x1, y1, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (255, 0, 255), 2)
            cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 255), 2, cv2.LINE_AA)

    

while True:
    ret, frame = video.read()

    draw_boundary(frame, dectect_color(frame, *color.blue), 'blue')
    draw_boundary(frame, dectect_color(frame, *color.red), 'red')
    draw_boundary(frame, dectect_color(frame, *color.yellow), 'yellow')
    draw_boundary(frame, dectect_color(frame, *color.green), 'green')

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
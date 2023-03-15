import cv2
import numpy as np

img = cv2.imread("smarties.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.medianBlur(gray_img, 5)

circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT,
                           1, 20, param1=100, param2=30, minRadius=5, maxRadius=50)

if type(circles) == type(None):
    circles = []

circles = np.uint16(np.around(circles[0, :]))
print(circles)

for circle in circles:
    cv2.circle(img, (circle[0], circle[1]), circle[2]+3, (0, 0, 0), 2)

cv2.imshow("Original img", img)
# cv2.imshow("Blur img", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

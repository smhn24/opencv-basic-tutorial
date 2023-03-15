import cv2
import numpy as np
from datetime import datetime


# cap = cv2.VideoCapture('vtest.avi')

# FONT = cv2.FONT_HERSHEY_COMPLEX

# while cap.isOpened():
#     ret, frame = cap.read()

#     if ret:
#         # height, width, channels = frame.shape
#         height, width = frame.shape[:2]
#         # cv2.putText(frame, "Hello", (10, 50), FONT, 1, (0, 255, 0), 2)
#         cv2.putText(frame, f"{width}x{height}",
#                     (10, 50), FONT, 1, (0, 255, 0), 2)
#         cv2.putText(frame, f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}",
#                     (10, 90), FONT, 1, (255, 0, 0), 2)
#         cv2.line(frame, (10, 60), (200, 60), (0, 0, 0), 2)
#         # cv2.arrowedLine(frame, (10, 60), (200, 60), (0, 0, 0), 2)
#         # cv2.circle(frame, (200, 200), 50, (255, 255, 255), 3)
#         # cv2.circle(frame, (200, 200), 50, (255, 255, 255), -1)
#         #! x1,y1 ------
#         #! |          |
#         #! |          |
#         #! |          |
#         #! --------x2,y2
#         # cv2.rectangle(frame, (300, 300), (600, 400), (255, 255, 0), 3)
#         # cv2.rectangle(frame, (300, 300), (600, 400), (255, 255, 0), -1)
#         # print(frame.shape)
#         cv2.imshow("Frame", frame)
#         # flip_image = cv2.flip(frame, 1)
#         # cv2.imshow("Flip", flip_image)

#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break

#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()

img = np.zeros((200, 200, 3), np.uint8)
img[0:200, 0:100] = cv2.bitwise_not(img[0:200, 0:100])

img2 = cv2.imread('binary_img.jpg')
reverse = cv2.bitwise_not(img2)

colored_img = np.full((200, 200, 3), (255, 0, 0), np.uint8)

cv2.imshow("Colored img", colored_img)

# cv2.imshow("Orginal", img2)
# cv2.imshow("Reversed", reverse)

# cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

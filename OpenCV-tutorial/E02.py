# import cv2

# img = cv2.imread("butterfly.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # img[0:200, 0:200] = (23, 177, 243)
# cv2.imshow("Image", img)
# cv2.imshow("Gray Image", gray)
# # cv2.imshow("Custom Image", img[0:250, 0:100])
# print(gray[200, 200])
# if cv2.waitKey(0) & 0xFF == ord("s"):
#     cv2.imwrite("out_image.jpg", img)
# cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('vtest.avi')
# fourcc = cv2.VideoWriter_fourcc("X", "V", "I", "D")
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output_video.avi", fourcc, 25, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        output.write(frame)
        cv2.imshow("Stream", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

output.release()
cap.release()
cv2.destroyAllWindows()

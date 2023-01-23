import cv2 as cv

cam=cv.VideoCapture(0)
while True:
    check,frame=cam.read()
    cv.imshow('video',frame)
    key=cv.waitKey(1)
    if key==27:
        break

cam.release()
cv.destroyAllWindows()
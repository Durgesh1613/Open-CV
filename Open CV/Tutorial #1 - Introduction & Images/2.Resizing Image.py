import cv2

img = cv2.imread('images/logo.jpg', -1)
#img = cv2.resize(img, (400,400))
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
(1) Pixel:img = cv2.resize(img, (400,400))
(2) Fraction:img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    (a)0.5 = Half The Size Of original Image
    (b)2 = Double The Size Of original Image
"""
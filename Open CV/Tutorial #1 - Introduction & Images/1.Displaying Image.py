import cv2

img = cv2.imread('images/logo.jpg', -1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
(1)cv2.IMREAD_COLOUR, -1:Colour Image
(2)cv2.IMREAD_GRAYSCALE,  0:Grayscale Image
(3)cv2.IMREAD_UNCHANGED,  1:Transparent Pixel Image
"""

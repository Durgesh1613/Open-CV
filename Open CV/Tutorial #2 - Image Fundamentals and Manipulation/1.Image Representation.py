import cv2

img = cv2.imread('images/logo.jpg', -1)

print(img)
print(type(img))
print(img.shape)

"""
img.shape
img.shape = 1st Value='600' Height
img.shape = 2nd Value='600' Width
img.shape = 3rd Value='3' Channels

Order = (Heigth, Width, Channels)
"""
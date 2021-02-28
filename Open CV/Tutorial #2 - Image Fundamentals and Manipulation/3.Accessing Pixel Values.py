import cv2

img = cv2.imread('images/logo.jpg', -1)

print(img[0])#First Row Of The Image
print(' ')
print(img[257][45:400])
print(' ')
print(img[257][400])
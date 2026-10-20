import cv2

# Задание 1

img = cv2.imread('var6.png')

height, width = img.shape[:2]

cv2.resize(img, (width*2, height*2))
cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
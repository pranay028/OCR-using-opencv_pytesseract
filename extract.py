import cv2
import pytesseract

img = cv2.imread("1.jpg")
    # print(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray, config=r' --psm 6 --oem 3')
print(text)
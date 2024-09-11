import cv2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Users/MuhammadAli_Adam\AppData/Local/Programs/Tesseract-OCR/tesseract.exe"


image_path = r"eng2.png"
  
# Opening the image & storing it in an image object 
img = Image.open(image_path) 
  
# Passing the image object to  
# image_to_string() function 
# This function will 
# extract the text from the image 
# text = pytesseract.image_to_string(img) 
config = ('-l eng --oem 1 --psm 3')
text = pytesseract.image_to_string(img, config=config).split()
# Displaying the extracted text 
print(text)
# image = cv2.imread('eng2.png')

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (3,3), 0)
# thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# # Morph open to remove noise and invert image
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
# invert = 255 - opening

# # Perform text extraction
# data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
# print(data)

# cv2.imshow('thresh', thresh)
# cv2.imshow('opening', opening)
# cv2.imshow('invert', invert)
# cv2.waitKey()
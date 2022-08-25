import cv2 as cv2
import pytesseract

def tesseract_read(image):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    extracted_information = (pytesseract.image_to_string(image)).lower()
    formatted_information = extracted_information.translate({ord('\n'): " "}).split(" ")

    return formatted_information

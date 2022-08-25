from Utils import separate_articles
from Tesseract import tesseract_read


def process_image(image):
    information_extracted_from_image = tesseract_read(image)
    articles = separate_articles(information_extracted_from_image)
    return articles

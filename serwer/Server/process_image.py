from Server.Utils import seperate_articles
from Tesseract import tesseract_read


def process_image(image):

    information_extracted_from_image = tesseract_read(image)

    articles = seperate_articles(information_extracted_from_image)
    
from Tesseract import tesseract_read
import cv2 as cv2
import numpy as np

def process_image(image):

    # Redukcja cienia
    rgb_planes = cv2.split(image)
    result_planes = []
    result_norm_planes = []

    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    result_norm = cv2.merge(result_norm_planes)

    # kontrast
    contrast_img = cv2.addWeighted(result_norm, 1, np.zeros(result_norm.shape, result_norm.dtype), 0, 0)

    # Czarno białe
    gray_img = cv2.cvtColor(contrast_img, cv2.COLOR_BGR2GRAY)

    # Redukcja rozmycia
    sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpen = cv2.filter2D(gray_img, -1, sharpen_kernel)

    (thresh, image_grayscale) = cv2.threshold(sharpen, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return image_grayscale


def read_from_image(image):
    information_extracted_from_image = tesseract_read(image)
    #articles = separate_articles(information_extracted_from_image)
    return information_extracted_from_image #articles


# Works bad.
def separate_articles(data):
    pocz = kon = 0

    # szukamy słów "paragon fiskalny" oraz "suma"
    for (index, word) in enumerate(data):
        if word == 'fiskalny':
            pocz = index

        if word == 'suma':
            kon = index

    if kon and pocz and pocz < kon:
        print("pocz: ", pocz, "kon: ", kon)
        return data[pocz + 1:kon]
    else:
        return None
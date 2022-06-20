# text recognition
import cv2 as cv
import numpy as np
import time
from PIL import ImageGrab

    
class Camera:
    def __init__(self, bbox, config, fx, fy):
        self.bbox = bbox
        self.config = config
        self.fx = fx
        self.fy = fy
    
    def capture(self, path = None):
        if path is None:
            screenshot = ImageGrab.grab(bbox=self.bbox)
        else:
            screenshot = cv.imread(path)
        return screenshot
        
    def pre_processing(self, image):
        """
        This function take one argument as
        input. this function will convert
        input image to binary image
        :param image: image
        :return: thresholded image
        """

        image = np.array(image)
        image = cv.resize(image, None, fx=self.fx, fy=self.fy)
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # converting it to binary image
        threshold_img = cv.threshold(gray_image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]

        return threshold_img

    def parse_text_data(self, threshold_img, config = r'--oem 1 --psm 1'):
        """
        This function take one argument as
        input. this function will feed input
        image to tesseract to predict text.
        :param threshold_img: image
        return: meta-data dictionary
        """
        # now feeding image to tesseract
        # details = pytesseract.image_to_data(threshold_img, output_type=pytesseract.Output.DICT,
        #                                     config=config, lang='eng')
        pass

    def parse_text_string(self, threshold_img):
        """
        This function take one argument as
        input. this function will feed input
        image to tesseract to predict text.
        :param threshold_img: image
        return: meta-data string
        """
        # now feeding image to tesseract
        pass

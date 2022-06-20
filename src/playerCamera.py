from camera import Camera
import cv2 as cv
import pytesseract

# pytessercat
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ChatCamera(Camera):
    def __init__(self, bbox, config):
        super().__init__(bbox, config)
        

    def parse_text_string(self, img, debug = False):
        img = super().pre_processing(img)
        if debug:
            cv.imshow('img', img)
        details = pytesseract.image_to_string(img, lang='eng').split('\n')
        ret = []
        for n in details:
            ret.append(n)
        return ret
    


if __name__ == '__main__':
    # pic = capture(bbox=(0,0,1100,1080))
    c = ChatCamera(bbox=(0,530,470,1080), config = r'--oem 1 --psm 1')
    s = c.capture("playerlist.png")
    s = c.parse_text_string(s, debug = True)
    print(s)


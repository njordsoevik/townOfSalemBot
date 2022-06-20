from camera import Camera
import cv2 as cv
import pytesseract

# pytessercat
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ChatCamera(Camera):
    def __init__(self, bbox, config, fx, fy):
        super().__init__(bbox, config)
        

    def parse_text_string(self, img, debug = False):
        img = super().pre_processing(img)
        if debug:
            cv.imshow('img', img)
            k = cv.waitKey(0)
            if k == 27:         # wait for ESC key to exit
                cv.destroyAllWindows()
        details = pytesseract.image_to_string(img, lang='eng', config = self.config)
        ret = []
        for n in details.split('\n'):
            if "@" in n:
                ret.append(n[n.index("@")+2 : len(n)] )
        return ret
    


if __name__ == '__main__':
    c = ChatCamera(bbox=(0,530,470,1080), config = r'--oem 1 --psm 1', fx = 2, fy = 2)
    s = c.capture("test.png")
    s = c.parse_text_string(s, debug = True)
    print(s)


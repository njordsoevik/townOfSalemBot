from camera import Camera
import cv2 as cv
import pytesseract
import re

# pytessercat
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ChatCamera(Camera):
    def __init__(self, bbox, config, fx, fy):
        super().__init__(bbox, config, fx, fy)
        

    def parse_text_string(self, img, debug = False):
        img = super().pre_processing(img)
        if debug:
            cv.imshow('img', img)
            k = cv.waitKey(0)
            if k == 27:         # wait for ESC key to exit
                cv.destroyAllWindows()
        details = pytesseract.image_to_string(img, lang = 'eng', config= self.config)
        print(details)
        ret = []
        for n in details.split('\n'):
            if n != '':
                endWord = n.split(" ")[-1]
                # Incase role is after name
                if ('(' in endWord or ')' in endWord):
                    endWord = n.split(" ")[-2]
                # Remove non alphabetic
                print(endWord)
                endword = re.sub("[^a-zA-Z]", "", endWord)
                endword = ''.join(filter(str.isalnum, endword))
                ret.append(endWord)
                
        return ret
    


if __name__ == '__main__':
    c = ChatCamera(bbox=(0,530,470,1080), config="--oem 1 --psm 1", fx = 3, fy = 3)
    s = c.capture("playerlist.png")
    s = c.parse_text_string(s, debug = True)
    print(s)


import imageCapture
import player
import cv2
from time import sleep

NAMES_CONFIG = r'--oem 3 --psm 6'
CHAT_CONFIG = r'--oem 3 --psm 6'

class Town:
    def __init__(self):
        self.players = []
    
    def start_game(self):
        ########### Player Creation ###########
        
        # Retrieve names
        image = pre_processing(capture())
        # Add to player set
        #players = {}
        #for i in range(2):
        #    self.players.add("p")
        
        ########### Chat Image Logging ###########

        # Create image parser
        while (True):
            
            threshold_img = pre_processing("img/sample_image.png", debug = True)
            textDict = parse_text_data(threshold_img)
            print(textDict["text"])
            text = parse_text_string(threshold_img)

            print(text.split("\n"))
            time.sleep(5)
            break
    
    def clear_votes():
        for player in self.players:
            player.setVote(None)
    


if __name__ == "__main__":
    town = Town()
    town.start_game()

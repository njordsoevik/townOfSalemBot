class Player:
    def __init__(self, name: str):
        self.name = name
        self.isJailor = False
        self.suspicision = 0
        self.chat_log = []
        self.whispers = []
        self.vote_log = []
        self.vote = None
        
    def addChat(text: str):
        self.chatLogs.append(text)
        
    def getChat():
        return self.chatLogs;
    
    def setSuspicision():
        pass
    
    def flagJailor():
        self.isJailor = True
        
    def getJailor():
        return self.isJailor
    
    def setVote(name: str):
        self.vote = name
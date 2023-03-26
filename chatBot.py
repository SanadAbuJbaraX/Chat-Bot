#######################################################################################
#                           Made By Sanad AbuJbara                                    #
#                                                                                     #
#                               Chat Bot                                              #
#                                                                                     #
#                                 Usage                                               #                             #
#               Chat With the bot and ask it any question!                            #
#                                                                                     #
#                               Error Handling                                        #
#  Make Sure that all libaries are installed properly                                 #
#                                                                                     #
# Made in python 3.11.2                                                               #
# Contact Me at discord : SANAD#5640                                                  #
#######################################################################################




# imports
from PyQt6.QtWidgets import *
from bot import ChatBot
from threading import Thread
import sys

# Main App Screen Class
class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Chat Bot
        self.chatBot = ChatBot()

        # Screen properties
        self.setMinimumSize(650,400)
        self.setWindowTitle('Chat Bot (Made By Sanad Abujbara)')

        # Chat area properties
        self.chatArea = QTextEdit(self)
        self.chatArea.setGeometry(10,10,480,320)
        self.chatArea.setReadOnly(True)

        # Input Field properties
        self.inputField = QLineEdit(self)
        self.inputField.setGeometry(10,340,480,40)

        # Send Button properties
        self.pushButton = QPushButton("Send",self)
        self.pushButton.setGeometry(500,340,100,40)
        self.pushButton.clicked.connect(self.prompt)

        # display screen
        self.show()
        
    def prompt(self):
        # Get User Prompt
        userPrompt = self.inputField.text().strip()
        # Clear Input Field
        self.inputField.clear()
        # Append the prompt to the chat area
        self.chatArea.append(f"<p style='color:#333333;' >You: {userPrompt}</p>")
        # Start a thread that gets the response and displays it
        thread = Thread(target=self.get_response,args=(userPrompt,))
        thread.start()

    def get_response(self,userPrompt):
        # Get Response From Bot
        response = f"{self.chatBot.get_response(userPrompt)}"
        # Display Response
        self.chatArea.append(f"<p style='color:#333333; background-color=#E9E9E9'>Bot: {response}</p>")

app = QApplication(sys.argv)
screen = MainScreen()
sys.exit(app.exec())
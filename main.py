from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
from backend import Chatbot


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()

        self.setMinimumSize(500, 500)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 400)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 420, 480, 30)
        self.input_field.returnPressed.connect(self.send_message)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setGeometry(220, 460, 60, 30)
        self.show()

    def send_message(self):
        question = self.input_field.text().strip()
        self.input_field.clear()
        self.chat_area.append(f"Me: {question}")
        response = self.chatbot.get_response(question)
        # self.chat_area.append(f"AI: {response}")
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>AI: {response}</p>")



app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())



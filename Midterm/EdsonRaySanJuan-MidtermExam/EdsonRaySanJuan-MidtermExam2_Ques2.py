import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton

class Ques_No2(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP"
        self.x = 300
        self.y = 300
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(1, 2)
        self.button = QPushButton("Click to change color", self)
        self.button.clicked.connect(self.changeColor)
        self.layout.addWidget(self.button, 1, 1)


    def changeColor(self):
        self.button.setStyleSheet("background-color: yellow")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ques_No2()
    sys.exit(app.exec_())

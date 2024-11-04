import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton

class Ques_No3(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Midterm in OOP"
        self.x = 300
        self.y = 300
        self.width = 400
        self.height = 200
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

        self.Label1 = QLabel('Enter your Fullname: ')
        self.layout.addWidget(self.Label1, 0, 0)

        self.Entry4 = QLineEdit()
        self.layout.addWidget(self.Entry4, 0, 1)

        self.button = QPushButton("Click to display your Fullname", self)
        self.button.clicked.connect(self.showFullname)
        self.layout.addWidget(self.button, 1, 0)
        self.Entry5 = QLineEdit()
        self.layout.addWidget(self.Entry5, 1, 1)

        self.displayLabel = QLabel('')
        self.layout.addWidget(self.displayLabel, 1, 1)

    def showFullname(self):
        fullname = self.Entry4.text()
        self.displayLabel.setText(fullname)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ques_No3()
    sys.exit(app.exec_())

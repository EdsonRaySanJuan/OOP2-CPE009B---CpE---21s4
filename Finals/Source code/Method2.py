import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class LargestNumberApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Find the Largest Number")
        self.setGeometry(100, 100, 400, 300)

        # Create widgets
        self.lbl1 = QLabel("The Program that Finds the Largest Number")
        self.lbl2 = QLabel("Enter the first number:")
        self.conOfEnt2 = QLineEdit()

        self.lbl3 = QLabel("Enter the second number:")
        self.conOfEnt3 = QLineEdit()

        self.lbl4 = QLabel("Enter the third number:")
        self.conOfEnt4 = QLineEdit()

        self.btn1 = QPushButton("Find the largest number")
        self.btn1.clicked.connect(self.findLargest)

        self.lbl5 = QLabel("The largest number:")
        self.conOfLargest = QLineEdit()
        self.conOfLargest.setReadOnly(True)

        # Layouts
        layout = QVBoxLayout()
        layout.addWidget(self.lbl1)

        layout.addWidget(self.lbl2)
        layout.addWidget(self.conOfEnt2)

        layout.addWidget(self.lbl3)
        layout.addWidget(self.conOfEnt3)

        layout.addWidget(self.lbl4)
        layout.addWidget(self.conOfEnt4)

        layout.addWidget(self.btn1)

        layout.addWidget(self.lbl5)
        layout.addWidget(self.conOfLargest)

        self.setLayout(layout)

    def findLargest(self):
        try:
            # Get numbers from input fields
            num1 = float(self.conOfEnt2.text())
            num2 = float(self.conOfEnt3.text())
            num3 = float(self.conOfEnt4.text())

            # Find the largest number
            largest = max(num1, num2, num3)

            # Display the largest number
            self.conOfLargest.setText(str(largest))
        except ValueError:
            self.conOfLargest.setText("Invalid input")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LargestNumberApp()
    window.show()
    sys.exit(app.exec_())

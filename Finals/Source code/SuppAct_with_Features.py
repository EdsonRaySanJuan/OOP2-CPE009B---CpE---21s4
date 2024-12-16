import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QListWidget, QMessageBox
from PyQt5.QtCore import Qt
import math

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.history = []  # To store the history of operations

    def initUI(self):
        self.setWindowTitle("Advanced Calculator")
        self.setGeometry(100, 100, 400, 400)

        # Layouts
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        # Input fields
        self.entry1 = QLineEdit(self)
        self.entry2 = QLineEdit(self)
        self.result_label = QLabel("Result: ", self)

        # History list
        self.history_list = QListWidget(self)

        # Buttons
        self.add_button = QPushButton("Add", self)
        self.subtract_button = QPushButton("Subtract", self)
        self.multiply_button = QPushButton("Multiply", self)
        self.divide_button = QPushButton("Divide", self)
        self.sqrt_button = QPushButton("Square Root", self)
        self.power_button = QPushButton("Power", self)
        self.clear_button = QPushButton("Clear", self)

        # Connecting buttons to functions
        self.add_button.clicked.connect(self.add)
        self.subtract_button.clicked.connect(self.subtract)
        self.multiply_button.clicked.connect(self.multiply)
        self.divide_button.clicked.connect(self.divide)
        self.sqrt_button.clicked.connect(self.sqrt)
        self.power_button.clicked.connect(self.power)
        self.clear_button.clicked.connect(self.clear)

        # Adding widgets to layouts
        input_layout.addWidget(QLabel("Enter first number:"))
        input_layout.addWidget(self.entry1)
        input_layout.addWidget(QLabel("Enter second number:"))
        input_layout.addWidget(self.entry2)

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.subtract_button)
        main_layout.addWidget(self.multiply_button)
        main_layout.addWidget(self.divide_button)
        main_layout.addWidget(self.sqrt_button)
        main_layout.addWidget(self.power_button)
        main_layout.addWidget(self.clear_button)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(QLabel("History:"))
        main_layout.addWidget(self.history_list)

        self.setLayout(main_layout)

    def validate_input(self):
        """ Validate if the inputs are numeric. """
        try:
            num1 = float(self.entry1.text())
            num2 = float(self.entry2.text())
            return num1, num2
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values.")
            return None, None

    def add(self):
        num1, num2 = self.validate_input()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.result_label.setText(f"Result: {result}")
            self.history.append(f"{num1} + {num2} = {result}")
            self.update_history()

    def subtract(self):
        num1, num2 = self.validate_input()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.result_label.setText(f"Result: {result}")
            self.history.append(f"{num1} - {num2} = {result}")
            self.update_history()

    def multiply(self):
        num1, num2 = self.validate_input()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.result_label.setText(f"Result: {result}")
            self.history.append(f"{num1} * {num2} = {result}")
            self.update_history()

    def divide(self):
        num1, num2 = self.validate_input()
        if num1 is not None and num2 is not None:
            if num2 != 0:
                result = num1 / num2
                self.result_label.setText(f"Result: {result}")
                self.history.append(f"{num1} / {num2} = {result}")
                self.update_history()
            else:
                QMessageBox.warning(self, "Math Error", "Error! Division by zero.")

    def sqrt(self):
        num1, _ = self.validate_input()
        if num1 is not None:
            if num1 >= 0:
                result = math.sqrt(num1)
                self.result_label.setText(f"Result: {result}")
                self.history.append(f"√({num1}) = {result}")
                self.update_history()
            else:
                QMessageBox.warning(self, "Math Error", "Error! Cannot take square root of a negative number.")

    def power(self):
        num1, num2 = self.validate_input()
        if num1 is not None and num2 is not None:
            result = math.pow(num1, num2)
            self.result_label.setText(f"Result: {result}")
            self.history.append(f"{num1} ^ {num2} = {result}")
            self.update_history()

    def clear(self):
        """ Clear the input fields and result. """
        self.entry1.clear()
        self.entry2.clear()
        self.result_label.setText("Result: ")
        self.history.clear()
        self.history_list.clear()

    def update_history(self):
        """ Update the history list widget. """
        self.history_list.clear()
        for entry in self.history:
            self.history_list.addItem(entry)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())

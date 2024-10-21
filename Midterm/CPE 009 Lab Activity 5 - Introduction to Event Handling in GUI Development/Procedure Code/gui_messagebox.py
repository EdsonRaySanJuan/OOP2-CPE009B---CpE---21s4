from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

@pyqtSlot()
def on_click(self):
    buttonReply = QMessageBox.question(self, "Testing Response", "Do you like PyQt5?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    if buttonReply == QMessageBox.Yes:
            QMessage.warning(self, "Evaluation", "User clicked Yes", QMessageBox.Ok, QMessageBox.Ok)
    else:
        QMessageBox.information(self, "Evaluation", "User clicked Yes", QMessage.Ok.QMessage.Ok)


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
from window import main_line

win = QWidget()
win.resize(500, 500)
win.setWindowTitle("Memory Card")
win.setLayout(main_line)

win.show()
app.exec_()
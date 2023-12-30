from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
from window import *

win = QWidget()
win.resize(500, 500)
win.setWindowTitle("Memory Card")
win.setLayout(main_line)
def answer_click():
    if answer_btn.text() == "Відповісти":
        group_box.hide()
        result_box.show()
        answer_btn.setText("Наступе питання")
    else:
        result_box.show()
        result_box.hide
        answer_btn.setText("Відповісти")

answer_btn.clcked.connect(answer_click)

win.show()
app.exec_()
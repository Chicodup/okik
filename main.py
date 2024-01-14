from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import choice,shuffle
from random import shuffle
app = QApplication([])
from window import*
from window import main_line

class Question():
    current = None
    def __init__(self,text,right_ans,ans2,ans3,ans4):
        self.text = text
        self.right_ans = right_ans
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4= ans4

questions = [
    Question("вісім", "eight", "eythf", "eighy", "eigt"),
    Question("один", "one", "uoe", "uno", "ok"),
    Question("наполеон?", "bonapart", "ya idu v kino", "napon", "octopus"),
    Question("сім", "seven", "siven", "za scho", "za nashih oi"),
    Question("ok?", "ko", "ou", "roblox", "blox fruits"),
    Question("121b top?", "ta", "ni", "no", "pravilna vidpovid ta")
]

radio_list = [btn1,btn2,btn3,btn4]


win = QWidget()
win.resize(500, 500)
win.setWindowTitle("Memory Card")
win.setLayout(main_line)




def next_question():
    Question.current = choice(questions)
    question_lb.setText(Question.current.text)
    shuffle(radio_list)
    radio_list[0].setText(Question.current.right_ans)
    radio_list[1].setText(Question.current.ans2)
    radio_list[2].setText(Question.current.ans3)
    radio_list[3].setText(Question.current.ans4)


def answer_click():
    if answer_btn.text() == "Відповісти":
        group_box.hide()
        result_box.show()
        answer_btn.setText("Наступе питання")
    else:
        next_question()
        group_box.show()
        result_box.hide()
        answer_btn.setText("Відповісти")

answer_btn.clicked.connect(answer_click)
next_question()
win.show()
app.exec_()
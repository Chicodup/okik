from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import choice,shuffle
from random import shuffle
app = QApplication([])
from time import sleep
from window import*
from window import main_line
from menu import *

class Question():
    current = None
    count_ans = 0
    count_right_ans = 0

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

def check_answer():
    Question.count_ans += 1
    if radio_list[0].isChecked():
        Question.count_right_ans += 1
        result_text.setText("Правильно")
    else:
        result_text.setText("Неправильно")

    radio_group.setExclusive(False)
    for btn in radio_list:  
        btn.setChecked(False)
    radio_group.setExclusive(True)




def answer_click():
    if answer_btn.text() == "Відповісти":
        if radio_group.checkedButton():
            check_answer()
            group_box.hide()
            result_box.show()
            answer_btn.setText("Наступне питання")
    else:
        next_question()
        group_box.show()
        result_box.hide()
        answer_btn.setText("Відповісти")

def show_menu():
    count_lb.setText("Разів відповіли:" + str(Question.count_ans))
    right_lb.setText("Правильних відповідей:" + str(Question.count_right_ans))
    try:
        succes = round(Question.count_right_ans / Question.count_ans * 100,2)
    except:
        succes = 0
    succes_lb.setText("Успішність:" + str(succes))
    win.hide()
    menu_win.show()

def hide_menu():
    win.show()
    menu_win.hide()

def relax():
    pause_time = int(time_spin.value())* 60
    win.hide()
    sleep(pause_time)
    win.show()
answer_btn.clicked.connect(answer_click)
menu_btn.clicked.connect(show_menu)
back_btn.clicked.connect(hide_menu)
rest_btn.clicked.connect(relax)

next_question()
win.show()
app.exec_()
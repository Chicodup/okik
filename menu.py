from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox,QButtonGroup, QWidget, QPushButton, QLabel,QHBoxLayout,QRadioButton, QVBoxLayout, QSpinBox

menu_win = QWidget()
menu_win.setWindowTitle("Memory Card Menu")
menu_win.resize(400,200)
menu_win.move(200,200)

title_lb = QLabel("Статистика")
count_lb = QLabel("Разів відповіли")
right_lb = QLabel("Правильних відповідей:")
succes_lb = QLabel("Успішність")

back_btn = QPushButton("Назад")

v_line = QVBoxLayout()
v_line.addWidget(title_lb)
v_line.addWidget(count_lb)
v_line.addWidget(right_lb)
v_line.addWidget(succes_lb)
v_line.addWidget(back_btn)

menu_win.setLayout(v_line)
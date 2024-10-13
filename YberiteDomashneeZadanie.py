from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QRadioButton, QButtonGroup

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('YouTube Quiz')
        self.setGeometry(100, 100, 300, 200)

        question = QLabel('В якому році канал отримав "золоту кнопку" від YouTube?')

        self.radio1 = QRadioButton('2005')
        self.radio2 = QRadioButton('2010')
        self.radio3 = QRadioButton('2015')
        self.radio4 = QRadioButton('2020')

        self.group = QButtonGroup()
        self.group.addButton(self.radio1)
        self.group.addButton(self.radio2)
        self.group.addButton(self.radio3)
        self.group.addButton(self.radio4)

        submit_btn = QPushButton('OK')
        submit_btn.clicked.connect(self.check_answer)

        layout = QVBoxLayout()
        layout.addWidget(question)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)
        layout.addWidget(submit_btn)
        self.setLayout(layout)

    def check_answer(self):
        if self.radio3.isChecked():
            QMessageBox.information(self, 'Result', 'Правильно! Ви виграли гіроскутер.')
        else:
            QMessageBox.information(self, 'Result', 'Hi, в 2015 році. Ви виграли фірмовий плакат.')

app = QApplication([]) 
window = QuizApp()
window.show()
app.exec_()

import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.count_1 = 0
        uic.loadUi('design.ui',self) 
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton.clicked.connect(self.finish)
        
    def run(self):
        self.a, self.b = random.randint(0, 100), random.randint(0, 100)
        self.s = random.choice(['+', '-', '*', '/'])
        self.label.setText(f'{self.a} {self.s} {self.b}')
        
    def finish(self):
        if str(self.label) == str(self.a + self.b):
            if int(self.lineEdit.text()) == self.a + self.b:
                self.count += 1
                self.label_2.setText(str(self.count))
                self.lineEdit.clear()
                self.label_4.setText(str(self.a + self.b))
                self.run()
            
            elif int(self.lineEdit.text()) != self.a + self.b:
                self.count_1 += 1
                self.label_3.setText(str(self.count_1))
                self.lineEdit.clear()
                self.label_4.setText(str(self.a + self.b))
                self.run()        
 

sys.excepthook = except_hook
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
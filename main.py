from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QMessageBox
import sys
import math


class Window(QWidget):

    fst = 0
    oper = ''

    def __init__(self):
        super(Window, self).__init__()  # переопределение методов родительского класса
        self.set_ui()

    def set_ui(self):
        self.setGeometry(200, 200, 400, 420)
        self.setWindowTitle('Калькулятор')

        self.le = QLineEdit(self)
        self.le.setGeometry(50, 50, 300, 30)
        self.le.setReadOnly(True)

        self.btn0 = QPushButton(self)
        self.btn0.setGeometry(50, 100, 50, 50)
        self.btn0.setText('0')
        self.btn0.clicked.connect(self.click_event0)

        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(110, 100, 50, 50)
        self.btn1.setText('1')
        self.btn1.clicked.connect(self.click_event1)

        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(170, 100, 50, 50)
        self.btn2.setText('2')
        self.btn2.clicked.connect(self.click_event2)

        self.btn3 = QPushButton(self)
        self.btn3.setGeometry(230, 100, 50, 50)
        self.btn3.setText('3')
        self.btn3.clicked.connect(self.click_event3)

        self.btn4 = QPushButton(self)
        self.btn4.setGeometry(290, 100, 50, 50)
        self.btn4.setText('4')
        self.btn4.clicked.connect(self.click_event4)

        self.btn5 = QPushButton(self)
        self.btn5.setGeometry(50, 160, 50, 50)
        self.btn5.setText('5')
        self.btn5.clicked.connect(self.click_event5)

        self.btn6 = QPushButton(self)
        self.btn6.setGeometry(110, 160, 50, 50)
        self.btn6.setText('6')
        self.btn6.clicked.connect(self.click_event6)

        self.btn7 = QPushButton(self)
        self.btn7.setGeometry(170, 160, 50, 50)
        self.btn7.setText('7')
        self.btn7.clicked.connect(self.click_event7)

        self.btn8 = QPushButton(self)
        self.btn8.setGeometry(230, 160, 50, 50)
        self.btn8.setText('8')
        self.btn8.clicked.connect(self.click_event8)

        self.btn9 = QPushButton(self)
        self.btn9.setGeometry(290, 160, 50, 50)
        self.btn9.setText('9')
        self.btn9.clicked.connect(self.click_event9)

        self.btnp = QPushButton(self)
        self.btnp.setGeometry(50, 220, 50, 50)
        self.btnp.setText('+')
        self.btnp.clicked.connect(self.click_eventp)

        self.btnmi = QPushButton(self)
        self.btnmi.setGeometry(110, 220, 50, 50)
        self.btnmi.setText('-')
        self.btnmi.clicked.connect(self.click_eventmi)

        self.btnmu = QPushButton(self)
        self.btnmu.setGeometry(170, 220, 50, 50)
        self.btnmu.setText('*')
        self.btnmu.clicked.connect(self.click_eventmu)

        self.btnd = QPushButton(self)
        self.btnd.setGeometry(230, 220, 50, 50)
        self.btnd.setText('/')
        self.btnd.clicked.connect(self.click_eventd)

        self.btnsq = QPushButton(self)
        self.btnsq.setGeometry(290, 220, 50, 50)
        self.btnsq.setText('x'+ chr(178))
        self.btnsq.clicked.connect(self.click_eventsq)

        self.btnsin = QPushButton(self)
        self.btnsin.setGeometry(50, 280, 50, 50)
        self.btnsin.setText('Sin')
        self.btnsin.clicked.connect(self.click_eventsin)

        self.btncos = QPushButton(self)
        self.btncos.setGeometry(110, 280, 50, 50)
        self.btncos.setText('Cos')
        self.btncos.clicked.connect(self.click_eventcos)

        self.btnsqrt = QPushButton(self)
        self.btnsqrt.setGeometry(170, 280, 50, 50)
        self.btnsqrt.setText(chr(8730) + 'x')
        self.btnsqrt.clicked.connect(self.click_eventsqrt)

        self.btnclr = QPushButton(self)
        self.btnclr.setGeometry(230, 280, 50, 50)
        self.btnclr.setText('CE')
        self.btnclr.clicked.connect(self.click_eventclr)

        self.btneq = QPushButton(self)
        self.btneq.setGeometry(290, 280, 50, 50)
        self.btneq.setText('=')
        self.btneq.clicked.connect(self.click_eventeq)

        self.btndot = QPushButton(self)
        self.btndot.setGeometry(50, 340, 50, 50)
        self.btndot.setText('.')
        self.btndot.clicked.connect(self.click_eventdot)

        self.show()

    def without_part(self, nom):
        if nom == '' or nom[len(nom)-1] == '.':
            return nom
        else:
            if math.modf(float(nom))[0] == 0.0:
                return str(math.trunc(float(nom)))
            else:
                return nom

    def click_event0(self):
        self.le.setText(self.without_part(self.le.text()) + '0')

    def click_event1(self):
        self.le.setText(self.without_part(self.le.text()) + '1')

    def click_event2(self):
        self.le.setText(self.without_part(self.le.text()) + '2')

    def click_event3(self):
        self.le.setText(self.without_part(self.le.text()) + '3')

    def click_event4(self):
        self.le.setText(self.without_part(self.le.text()) + '4')

    def click_event5(self):
        self.le.setText(self.without_part(self.le.text()) + '5')

    def click_event6(self):
        self.le.setText(self.without_part(self.le.text()) + '6')

    def click_event7(self):
        self.le.setText(self.without_part(self.le.text()) + '7')

    def click_event8(self):
        self.le.setText(self.without_part(self.le.text()) + '8')

    def click_event9(self):
        self.le.setText(self.without_part(self.le.text()) + '9')

    def click_eventdot(self):
        if self.le.text().find('.') != -1:
            QMessageBox.about(self, "Error", "Enter field correctly.")
        else:
            self.le.setText(self.le.text() + '.')

    def click_eventp(self):
        global fst
        global oper
        fst = float(self.le.text())
        oper = 'p'
        self.le.setText('')

    def click_eventmi(self):
        global fst
        global oper
        fst = float(self.le.text())
        oper = 'mi'
        self.le.setText('')

    def click_eventmu(self):
        global fst
        global oper
        fst = float(self.le.text())
        oper = 'mu'
        self.le.setText('')

    def click_eventd(self):
        global fst
        global oper
        fst = float(self.le.text())
        oper = 'd'
        self.le.setText('')

    def click_eventsq(self):
        global fst
        global oper
        fst = 0.0
        oper = ''
        self.le.setText(str(float(self.le.text())**2))
        self.le.setText(self.without_part(self.le.text()))

    def click_eventsin(self):
        global fst
        global oper
        fst = 0
        oper = ''
        self.le.setText(str(math.sin(int(self.le.text()))))
        self.le.setText(self.without_part(self.le.text()))

    def click_eventcos(self):
        global fst
        global oper
        fst = 0
        oper = ''
        self.le.setText(str(math.cos(int(self.le.text()))))
        self.le.setText(self.without_part(self.le.text()))

    def click_eventd(self):
        global fst
        global oper
        fst = float(self.le.text())
        oper = 'd'
        self.le.setText('')
        self.le.setText(self.without_part(self.le.text()))

    def click_eventsqrt(self):
        global fst
        global oper
        fst = 0
        oper = ''
        self.le.setText(str(math.sqrt(float(self.le.text()))))
        self.le.setText(self.without_part(self.le.text()))

    def click_eventeq(self):
        global fst
        global oper
        second = float(self.le.text())
        try:
            if oper == 'p':
                self.le.setText(str(fst + second))
                self.le.setText(self.without_part(self.le.text()))
                fst = 0
                oper = ''
            elif oper == 'mi':
                self.le.setText(str(fst - second))
                self.le.setText(self.without_part(self.le.text()))
                fst = 0
                oper = ''
            elif oper == 'mu':
                self.le.setText(str(fst * second))
                self.le.setText(self.without_part(self.le.text()))
                fst = 0
                oper = ''
            elif oper == 'd':
                self.le.setText(str(fst / second))
                self.le.setText(self.without_part(self.le.text()))
                fst = 0
                oper = ''
            else:
                QMessageBox.about(self, "Error", "Inner error.")
                self.le.setText('')
                fst = 0
                oper = ''
        except:
            QMessageBox.about(self, "Error", "Inner error.")
            self.le.setText('')
            fst = 0
            oper = ''

    def click_eventclr(self):
        global oper
        global fst
        oper = ''
        fst = 0
        self.le.setText('')




if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = Window()
    sys.exit(app.exec_())
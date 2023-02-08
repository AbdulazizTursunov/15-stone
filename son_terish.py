from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import  QFont
import random



class Windov(QWidget):
    def __init__(self):
        # self.post().hide()
        super().__init__()

        self.str_styl = """QPushButton{
            color:red;
            background-color:silver;
            border: 1px solid black;
            border-radius: 50;
            font: bold 12pt;
        }
        """

        self.setWindowTitle("son terish")
        self.setFixedSize(342,420)

        self.gr_lay = QGridLayout()
        self.h_btn_lay = QHBoxLayout()
        self.lb_lay = QHBoxLayout()
        self.v_main = QVBoxLayout()
        self.lst1 = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,""]

        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")     
        self.btn10 = QPushButton("10")
        self.btn11 = QPushButton("11")
        self.btn12 = QPushButton("12")
        self.btn13= QPushButton("13")
        self.btn14= QPushButton("14")
        self.btn15= QPushButton("15")
        self.btn16= QPushButton("")


        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8,
                     self.btn9, self.btn10, self.btn11, self.btn12, self.btn13, self.btn14, self.btn15, self.btn16]

        
        k = 0
        for i in range(4):
            for j in range(4):
                self.gr_lay.addWidget(self.lst[k],i,j)
                self.lst[k].setFixedSize(80,90)
                self.setFont(QFont("times", 12))
                self.setStyleSheet(self.str_styl)
                k += 1

        self.restart_btn = QPushButton("RESTART")
        self.restart_btn.setStyleSheet("background-color:green;")
                                         
        self.restart_btn.clicked.connect(self.restart)

        self.close_btn = QPushButton("CLOSE")
        self.close_btn.setStyleSheet("background-color:blue;")
        self.close_btn.clicked.connect(self.close)


        self.h_btn_lay.addWidget(self.restart_btn)
        self.h_btn_lay.addWidget(self.close_btn)

        self.v_main.addLayout(self.gr_lay)
        self.v_main.addLayout(self.lb_lay)
        self.v_main.addLayout(self.h_btn_lay)

        self.btn1.clicked.connect(self.btn_1)
        self.btn2.clicked.connect(self.btn_2)
        self.btn3.clicked.connect(self.btn_3)
        self.btn4.clicked.connect(self.btn_4)
        self.btn5.clicked.connect(self.btn_5)
        self.btn6.clicked.connect(self.btn_6)
        self.btn7.clicked.connect(self.btn_7)
        self.btn8.clicked.connect(self.btn_8)
        self.btn9.clicked.connect(self.btn_9)
        self.btn10.clicked.connect(self.btn_10)
        self.btn11.clicked.connect(self.btn_11)
        self.btn12.clicked.connect(self.btn_12)
        self.btn13.clicked.connect(self.btn_13)
        self.btn14.clicked.connect(self.btn_14)
        self.btn15.clicked.connect(self.btn_15)
        self.btn16.clicked.connect(self.btn_16)

        # asosiy
        self.setLayout(self.v_main)


    def btn_1(self):
        svo = ""
        zan = ""
        if self.btn1.text() != "":
            if self.btn2.text() == "":
                zan = self.btn1.text()
                self.btn2.setText(zan)
                self.btn1.setText(svo)
            if self.btn5.text() == "":
                zan = self.btn1.text()
                self.btn5.setText(zan)
                self.btn1.setText(svo)
            
    def btn_2(self):
          svo = ""
          zan = ""
          if self.btn2.text() != "":
            if self.btn1.text() == "":
                zan = self.btn2.text()
                self.btn1.setText(zan)
                self.btn2.setText(svo)
            if self.btn3.text() == "":
                zan = self.btn2.text()
                self.btn3.setText(zan)
                self.btn2.setText(svo)
            if self.btn6.text() == "":
                zan = self.btn2.text()
                self.btn6.setText(zan)
                self.btn2.setText(svo)

    def btn_3 (self):
          svo = ""
          zan = ""
          if self.btn3.text() != "":
            if self.btn2.text() == "":
                zan = self.btn3.text()
                self.btn2.setText(zan)
                self.btn3.setText(svo)
            if self.btn4.text() == "":
                zan = self.btn3.text()
                self.btn4.setText(zan)
                self.btn3.setText(svo)
            if self.btn7.text() == "":
                zan = self.btn3.text()
                self.btn7.setText(zan)
                self.btn3.setText(svo)
        
    def btn_4(self):
          svo = ""
          zan = ""
          if self.btn4.text() != "":
            if self.btn3.text() == "":
                zan = self.btn4.text()
                self.btn3.setText(zan)
                self.btn4.setText(svo)
            if self.btn8.text() == "":
                zan = self.btn4.text()
                self.btn8.setText(zan)
                self.btn4.setText(svo)

    def btn_5(self):
          svo = ""
          zan = ""
          if self.btn5.text() != "":
            if self.btn1.text() == "":
                zan = self.btn5.text()
                self.btn1.setText(zan)
                self.btn5.setText(svo)
            if self.btn6.text() == "":
                zan = self.btn5.text()
                self.btn6.setText(zan)
                self.btn5.setText(svo)
            if self.btn9.text() == "":
                zan = self.btn5.text()
                self.btn9.setText(zan)
                self.btn5.setText(svo)
        
    def btn_6(self):
          svo = ""
          zan = ""
          if self.btn6.text() != "":
            if self.btn2.text() == "":
                zan = self.btn6.text()
                self.btn2.setText(zan)
                self.btn6.setText(svo)
            if self.btn7.text() == "":
                zan = self.btn6.text()
                self.btn7.setText(zan)
                self.btn6.setText(svo)
            if self.btn10.text() == "":
                zan = self.btn6.text()
                self.btn10.setText(zan)
                self.btn6.setText(svo)
            if self.btn5.text() == "":
                zan = self.btn6.text()
                self.btn5.setText(zan)
                self.btn6.setText(svo)

    def btn_7(self):
          svo = ""
          zan = ""
          if self.btn7.text() != "":
            if self.btn3.text() == "":
                zan = self.btn7.text()
                self.btn3.setText(zan)
                self.btn7.setText(svo)
            if self.btn8.text() == "":
                zan = self.btn7.text()
                self.btn8.setText(zan)
                self.btn7.setText(svo)
            if self.btn11.text() == "":
                zan = self.btn7.text()
                self.btn11.setText(zan)
                self.btn7.setText(svo)
            if self.btn6.text() == "":
                zan = self.btn7.text()
                self.btn6.setText(zan)
                self.btn7.setText(svo)
        
    def btn_8(self):
          svo = ""
          zan = ""
          if self.btn8.text() != "":
            if self.btn4.text() == "":
                zan = self.btn8.text()
                self.btn4.setText(zan)
                self.btn8.setText(svo)
            if self.btn7.text() == "":
                zan = self.btn8.text()
                self.btn7.setText(zan)
                self.btn8.setText(svo)
            if self.btn12.text() == "":
                zan = self.btn8.text()
                self.btn12.setText(zan)
                self.btn8.setText(svo)
        
    def btn_9(self):
          svo = ""
          zan = ""
          if self.btn9.text() != "":
            if self.btn5.text() == "":
                zan = self.btn9.text()
                self.btn5.setText(zan)
                self.btn9.setText(svo)
            if self.btn10.text() == "":
                zan = self.btn9.text()
                self.btn10.setText(zan)
                self.btn9.setText(svo)
            if self.btn13.text() == "":
                zan = self.btn9.text()
                self.btn13.setText(zan)
                self.btn9.setText(svo) 

    def btn_10(self):
          svo = ""
          zan = ""
          if self.btn10.text() != "":
            if self.btn6.text() == "":
                zan = self.btn10.text()
                self.btn6.setText(zan)
                self.btn10.setText(svo)
            if self.btn11.text() == "":
                zan = self.btn10.text()
                self.btn11.setText(zan)
                self.btn10.setText(svo)
            if self.btn14.text() == "":
                zan = self.btn10.text()
                self.btn14.setText(zan)
                self.btn10.setText(svo)
            if self.btn9.text() == "":
                zan = self.btn10.text()
                self.btn9.setText(zan)
                self.btn10.setText(svo)

    def btn_11(self):
          svo = ""
          zan = ""
          if self.btn11.text() != "":
            if self.btn7.text() == "":
                zan = self.btn11.text()
                self.btn7.setText(zan)
                self.btn11.setText(svo)
            if self.btn12.text() == "":
                zan = self.btn11.text()
                self.btn12.setText(zan)
                self.btn11.setText(svo)
            if self.btn15.text() == "":
                zan = self.btn11.text()
                self.btn15.setText(zan)
                self.btn11.setText(svo)
            if self.btn10.text() == "":
                zan = self.btn11.text()
                self.btn10.setText(zan)
                self.btn11.setText(svo)

    def btn_12(self):
          svo = ""
          zan = ""
          if self.btn12.text() != "":
            if self.btn8.text() == "":
                zan = self.btn12.text()
                self.btn8.setText(zan)
                self.btn12.setText(svo)
            if self.btn11.text() == "":
                zan = self.btn12.text()
                self.btn11.setText(zan)
                self.btn12.setText(svo)
            if self.btn16.text() == "":
                zan = self.btn12.text()
                self.btn16.setText(zan)
                self.btn12.setText(svo)

    def btn_13(self):
          svo = ""
          zan = ""
          if self.btn13.text() != "":
            if self.btn9.text() == "":
                zan = self.btn13.text()
                self.btn9.setText(zan)
                self.btn13.setText(svo)
            if self.btn14.text() == "":
                zan = self.btn13.text()
                self.btn14.setText(zan)
                self.btn13.setText(svo)

    def btn_14(self):
          svo = ""
          zan = ""
          if self.btn14.text() != "":
            if self.btn13.text() == "":
                zan = self.btn14.text()
                self.btn13.setText(zan)
                self.btn14.setText(svo)
            if self.btn10.text() == "":
                zan = self.btn14.text()
                self.btn10.setText(zan)
                self.btn14.setText(svo)
            if self.btn15.text() == "":
                zan = self.btn14.text()
                self.btn15.setText(zan)
                self.btn14.setText(svo)

    def btn_15(self):
          svo = ""
          zan = ""
          if self.btn15.text() != "":
            if self.btn16.text() == "":
                zan = self.btn15.text()
                self.btn16.setText(zan)
                self.btn15.setText(svo)
            if self.btn14.text() == "":
                zan = self.btn16.text()
                self.btn14.setText(zan)
                self.btn16.setText(svo)
            if self.btn11.text() == "":
                zan = self.btn16.text()
                self.btn11.setText(zan)
                self.btn16.setText(svo)

    def btn_16(self):
          svo = ""
          zan = ""
          if self.btn16.text() != "":
            if self.btn12.text() == "":
                zan = self.btn16.text()
                self.btn12.setText(zan)
                self.btn16.setText(svo)
            if self.btn15.text() == "":
                zan = self.btn16.text()
                self.btn15.setText(zan)
                self.btn16.setText(svo)
   
    # sochib beradi
    def restart(self):
        random.shuffle(self.lst1)
        q = 0
        w = 0
        for i in self.lst1:
            q = i
            self.lst[w].setText(str(q))
            w += 1



app = QApplication([])
oyna = Windov()
oyna.show()
app.exec_()



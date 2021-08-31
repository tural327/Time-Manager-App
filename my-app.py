from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLabel,QSlider
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import Qt,QTimer
from PyQt5 import QtGui
import playsound
import sys
import datetime




class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setFixedWidth(600)
        self.setFixedHeight(400)
        self.setWindowTitle("Your Time Manager")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.initUI()


    def initUI(self):

 ##################       #Working min ################
        # Text work
        self.input_1 = QtWidgets.QLabel(self)
        self.input_1.setText("Your Wroking min is :")
        self.input_1.setFont(QFont("Times",13))
        self.input_1.setGeometry(20,50,200,25)
        self.input_1.move(20,10)
        #Display min of work
        self.label_1_slider = QLabel('', self)
        self.label_1_slider.setFont(QFont("Times",13))
        self.label_1_slider.move(185,8)
        # Work slider
        self.mySlider_work = QSlider(Qt.Horizontal, self)
        self.mySlider_work.setMaximum(90)
        self.mySlider_work.setMinimum(0)
        self.mySlider_work.setGeometry(17, 50, 200, 30)
        self.mySlider_work.valueChanged[int].connect(self.display_work_input)

 ###################       # Resting min ########################
        # Text Rest
        self.input_2 = QtWidgets.QLabel(self)
        self.input_2.setText("Your Resting min is :")
        self.input_2.setFont(QFont("Times",13))
        self.input_2.setGeometry(20,50,200,25)
        self.input_2.move(240,10)
        # Display Rest
        self.label_2_slider = QLabel('', self)
        self.label_2_slider.setFont(QFont("Times",13))
        self.label_2_slider.move(405,7)
                # Slider Rest
        self.mySlider_rest = QSlider(Qt.Horizontal, self)
        self.mySlider_rest.setMaximum(15)
        self.mySlider_rest.setMinimum(0)
        self.mySlider_rest.setGeometry(245, 50, 200, 30)
        self.mySlider_rest.valueChanged[int].connect(self.display_rest_input)
       ###### Current time ######

        self.input_2 = QtWidgets.QLabel(self)
        self.input_2.setText("Current time")
        self.input_2.setFont(QFont("Times",13))
        self.input_2.setGeometry(20,50,200,25)
        self.input_2.move(470,10)

        self.display = QLabel('' , self)
        self.display.setFont(QFont("Times",16))
        self.display.move(480,40)

#################### button ###############################################

        self.button_start = QPushButton('Start', self)
        self.button_start.setGeometry(100,50,380,50)
        self.button_start.setFont(QFont("Times",15))
        self.button_start.move(5,80)

        self.button_set = QPushButton('Set again', self)
        self.button_set.setGeometry(100,50,130,50)
        self.button_set.setFont(QFont("Times",15))
        self.button_set.move(465,80)

        self.label_back = QLabel("Please click 'I am here' button when you come back to work!", self)
        self.label_back.setFont(QFont("Times", 15))
        self.label_back.setGeometry(500, 100, 700, 50)
        self.label_back.move(70, 160)

        self.button_back = QPushButton("I am here", self)
        self.button_back.setGeometry(100,50,240,100)
        self.button_back.setFont(QFont("Times",25))
        self.button_back.move(170,220)

        self.display_main = QLabel( self)
        self.main_img = QPixmap("main.jpg")
        self.main_img_1 = self.main_img.scaled(520,220)
        self.display_main.setPixmap(self.main_img_1)
        self.display_main.resize(self.main_img_1.width(),
                                 self.main_img_1.height())
        self.display_main.move(45,160)

        self.display_work = QLabel(self)
        self.wokr_img = QPixmap("work2.jpg")
        self.display_work_1 = self.wokr_img.scaled(520, 220)
        self.display_work.setPixmap(self.display_work_1)
        self.display_work.resize(self.display_work_1.width(),
                                 self.display_work_1.height())
        self.display_work.move(45, 170)
        self.display_work.hide()

        self.display_rest = QLabel(self)
        self.relax_img = QPixmap("relax.jpg")
        self.relax_img_1 = self.relax_img.scaled(520, 220)
        self.display_rest.setPixmap(self.relax_img_1)
        self.display_rest.resize(self.display_work_1.width(),
                                 self.display_work_1.height())
        self.display_rest.move(45, 170)
        self.display_rest.hide()

        self.label_work = QLabel("The future depends on what you do today.Work Hard!", self)
        self.label_work.setFont(QFont("Times", 15))
        self.label_work.setGeometry(500, 100, 700, 50)
        self.label_work.move(5, 125)
        self.label_work.hide()

        self.button_start.pressed.connect(self.show_res)
        self.button_back.pressed.connect(self.show_res)
        self.button_back.pressed.connect(self.i_back_to_work)
        self.button_set.pressed.connect(self.setting_but)


        self.back_to_work = False

        self.value_h = ["sec"]
        self.value_m = ["sec"]
        self.value_s = ["sec"]

        self.value_work_h = ["sec"]
        self.value_work_s = ["sec"]
        self.value_work_m = ["sec"]

        timer = QTimer(self)
        timer.timeout.connect(self.calculate)
        timer.start(100)

    def calculate(self):

        current_time = datetime.datetime.now()
        hours = str(current_time.hour)
        minutes = str(current_time.minute)
        seconds = str(current_time.second)
        dis_time = hours + ":" + minutes + ":" + seconds
        self.display.setText(dis_time)


        sec_value = int(current_time.second)
        min_value = int(current_time.minute)
        min_hour = int(current_time.hour)




        if self.value_s[0]==sec_value and self.value_m[0] == min_value and self.value_h[0]==min_hour:

            self.back_to_work =True

            while self.back_to_work==True:
                self.display_work.hide()
                self.label_work.hide()
                self.display_rest.hide()
                self.label_back.show()
                self.button_back.show()

                playsound.playsound("rest.mp3")
            
        elif self.value_work_s[0] == sec_value and self.value_work_m[0] == min_value and self.value_work_h[0]==min_hour:
            self.display_rest.show()
            self.label_work.hide()
            self.display_work.hide()
            playsound.playsound("work.mp3")

    def setting_but(self):
        self.mySlider_rest.show()
        self.mySlider_work.show()
        self.button_start.show()
        self.value = [30]
        self.value_work = [30]
        self.back_to_work = False
        self.display_main.show()
        self.display_work.hide()
        self.label_work.hide()
        self.display_rest.hide()

    def i_back_to_work(self):
        self.label_work.show()
        self.display_work.show()
        self.back_to_work=False
    
    def show_res(self):
        def convert(h,m,s,r):
            second = ''
            minut = ''
            hour = ''

            if (s+r)>60:
                m1 = int(str((s+r)/60).split(".")[0])
                s1 = (s+r) - 60*(m1)
                second = s1
                minut = m1
                hour = h
                if (m1+m)>60:
                    h1 = int(str((m1+m)/60).split(".")[0])
                    h_end =h1 + h
                    m_end = (m1+m) - 60
                    second = s1
                    minut = m_end
                    hour = h_end
                elif (m1+m)<60:
                    m_end = m1 + m
                    s1 = (s + r) - 60 * (m1)
                    minut = m_end
                    hour = h
                    second = s1
            elif (s+r)<60:
                second = s+r
                minut = m
                hour = h
            
            return hour,minut,second

        current_time = datetime.datetime.now()

        work = self.mySlider_work.value()
        sec_value = int(current_time.second)
        min_value = int(current_time.minute)
        hour_value = int(current_time.hour)
        convert(hour_value,min_value,sec_value,work)


        self.value_work_s[0] = convert(hour_value,min_value,sec_value,work)[2]
        self.value_work_m[0] = convert(hour_value, min_value, sec_value, work)[1]
        self.value_work_h[0] = convert(hour_value, min_value, sec_value, work)[0]

        rest = self.mySlider_rest.value() + self.mySlider_work.value()
        sec_value = int(current_time.second)
        min_value = int(current_time.minute)
        hour_value = int(current_time.hour)

        self.value_s[0] = convert(hour_value,min_value,sec_value,rest)[2]
        self.value_m[0] = convert(hour_value, min_value, sec_value, rest)[1]
        self.value_h[0] = convert(hour_value, min_value, sec_value, rest)[0]
        self.mySlider_work.hide()
        self.mySlider_rest.hide()
        self.button_start.hide()
        self.label_back.hide()
        self.button_back.hide()
        self.display_work.show()
        self.display_main.hide()
        self.label_work.show()


    def display_work_input(self,value):
        self.label_1_slider.setText(str(value))
    
    def display_rest_input(self,value):
        self.label_2_slider.setText(str(value))




def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()


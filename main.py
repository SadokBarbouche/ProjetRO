# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projet.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pl1
import pl2
import pl3
import pl4
import pl5
import pl6
import pl7
import pl9


class Ui_MainWindow(object):
    def openExercice1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pl1.PL1_Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def openExercice2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pl2.PL2_Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def openExercice3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pl3.PL3_Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def openExercice4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pl4.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def openExercice5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pl5.PL5_Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def openExercice6(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pl6.PL6_Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def openExercice7(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pl7.PL7_Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def openExercice9(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pl9.PL9_Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.openExercice1)
        self.pushButton.setGeometry(QtCore.QRect(70, 430, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.openExercice2)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 430, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.clicked.connect(self.openExercice3)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 430, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.clicked.connect(self.openExercice4)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 430, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.clicked.connect(self.openExercice5)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 430, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(630, 430, 93, 28))
        self.pushButton_6.clicked.connect(self.openExercice6)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.clicked.connect(self.openExercice7)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 470, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 470, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.clicked.connect(self.openExercice9)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 470, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 390, 761, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 150, 20, 111))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 230, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 230, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 180, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 320, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Exercice 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Exercice 2"))
        self.pushButton_3.setText(_translate("MainWindow", "Exercice 3"))
        self.pushButton_4.setText(_translate("MainWindow", "Exercice 4"))
        self.pushButton_5.setText(_translate("MainWindow", "Exercice 5"))
        self.pushButton_6.setText(_translate("MainWindow", "Exercice 6"))
        self.pushButton_7.setText(_translate("MainWindow", "Exercice 7"))
        self.pushButton_8.setText(_translate("MainWindow", "Exercice 8"))
        self.pushButton_9.setText(_translate("MainWindow", "Exercice 9"))
        self.label.setText(_translate("MainWindow", "Projet : Recherche Operationnelle"))
        self.label_2.setText(_translate("MainWindow", "Elaboré par :"))
        self.label_3.setText(_translate("MainWindow", "Mtiri Wissem"))
        self.label_4.setText(_translate("MainWindow", "Barbouche Sadok"))
        self.label_5.setText(_translate("MainWindow", "Bouzid Med Aziz"))
        self.label_6.setText(_translate("MainWindow", "Bacha Nermine"))
        self.label_7.setText(_translate("MainWindow", "Saadani Abdelkhalek"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    style = """
    
            QWidget{
                background: #262D37;
                margin: "auto";
            }
            QLabel{
                color: #fff;
            }
            QLabel#round_count_label, QLabel#highscore_count_label{
               border: 1px solid #fff;
                border-radius: 8px;
                padding: 2px;
            }
            QPushButton
            {
                color: white;
                background: #0577a8;
                border: 1px #DADADA solid;
                padding: 5px 5px;
                border-radius: 2px;
                font-weight: bold;
                font-size: 9pt;
                outline: none;
                transition:1s;
            }
            QPushButton:hover{
                border: 1px #C6C6C6 solid;
                color: #fff;
                background: #0892D0;
            }
            QLineEdit {
                padding: 1px;
                color: #fff;
                border-style: solid;
                border: 2px solid #fff;
                border-radius: 8px;
            }
        """
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercice7.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import gurobipy as gb
import pandas as pd

class PL7_Ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(300, 180, 41, 22))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(160, 130, 55, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(350, 180, 41, 22))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(450, 150, 41, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(360, 130, 55, 16))
        self.label_20.setObjectName("label_20")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 150, 41, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(150, 210, 41, 22))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 210, 55, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_43.setGeometry(QtCore.QRect(450, 300, 41, 22))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_35.setGeometry(QtCore.QRect(450, 270, 41, 22))
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_42.setGeometry(QtCore.QRect(150, 300, 41, 22))
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_34.setGeometry(QtCore.QRect(150, 270, 41, 22))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(450, 210, 41, 22))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_46.setGeometry(QtCore.QRect(400, 300, 41, 22))
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(460, 130, 55, 16))
        self.label_22.setObjectName("label_22")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_36.setGeometry(QtCore.QRect(200, 270, 41, 22))
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(80, 180, 55, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(400, 150, 41, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 150, 41, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(80, 300, 55, 16))
        self.label_14.setObjectName("label_14")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(260, 130, 55, 16))
        self.label_18.setObjectName("label_18")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(80, 270, 55, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_32.setGeometry(QtCore.QRect(300, 240, 41, 22))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 150, 55, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(400, 180, 41, 22))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(210, 130, 55, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_30.setGeometry(QtCore.QRect(400, 240, 41, 22))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(450, 180, 41, 22))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 150, 41, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_44.setGeometry(QtCore.QRect(200, 300, 41, 22))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_33.setGeometry(QtCore.QRect(250, 270, 41, 22))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(200, 180, 41, 22))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_48.setGeometry(QtCore.QRect(300, 300, 41, 22))
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(310, 130, 55, 16))
        self.label_19.setObjectName("label_19")
        self.resoudre1 = QtWidgets.QPushButton(self.centralwidget)
        self.resoudre1.clicked.connect(self.PL7)
        self.resoudre1.setGeometry(QtCore.QRect(620, 60, 93, 471))
        self.resoudre1.setObjectName("resoudre1")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_45.setGeometry(QtCore.QRect(350, 300, 41, 22))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_26.setGeometry(QtCore.QRect(150, 240, 41, 22))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_28.setGeometry(QtCore.QRect(200, 240, 41, 22))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(200, 210, 41, 22))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_29.setGeometry(QtCore.QRect(350, 240, 41, 22))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 150, 41, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setGeometry(QtCore.QRect(350, 210, 41, 22))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setGeometry(QtCore.QRect(400, 210, 41, 22))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 560, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(150, 180, 41, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setGeometry(QtCore.QRect(250, 240, 41, 22))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(80, 240, 55, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(250, 210, 41, 22))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setGeometry(QtCore.QRect(300, 210, 41, 22))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_41.setGeometry(QtCore.QRect(250, 300, 41, 22))
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_40.setGeometry(QtCore.QRect(300, 270, 41, 22))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_37.setGeometry(QtCore.QRect(350, 270, 41, 22))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_38.setGeometry(QtCore.QRect(400, 270, 41, 22))
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(250, 180, 41, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 150, 41, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(410, 130, 55, 16))
        self.label_21.setObjectName("label_21")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_27.setGeometry(QtCore.QRect(450, 240, 41, 22))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_39.setGeometry(QtCore.QRect(510, 270, 41, 22))
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(520, 130, 55, 16))
        self.label_23.setObjectName("label_23")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(510, 180, 41, 22))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_47.setGeometry(QtCore.QRect(510, 300, 41, 22))
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(510, 150, 41, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setGeometry(QtCore.QRect(510, 210, 41, 22))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_31.setGeometry(QtCore.QRect(510, 240, 41, 22))
        self.lineEdit_31.setObjectName("lineEdit_31")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label_16.setText(_translate("MainWindow", "P1"))
        self.label.setText(_translate("MainWindow", "PL 7:"))
        self.label_20.setText(_translate("MainWindow", "P5"))
        self.label_11.setText(_translate("MainWindow", "3"))
        self.label_22.setText(_translate("MainWindow", "P7"))
        self.label_10.setText(_translate("MainWindow", "2"))
        self.label_14.setText(_translate("MainWindow", "6"))
        self.label_18.setText(_translate("MainWindow", "P3"))
        self.label_13.setText(_translate("MainWindow", "5"))
        self.label_9.setText(_translate("MainWindow", "1"))
        self.label_17.setText(_translate("MainWindow", "P2"))
        self.label_19.setText(_translate("MainWindow", "P4"))
        self.resoudre1.setText(_translate("MainWindow", "Résoudre"))
        self.label_12.setText(_translate("MainWindow", "4"))
        self.label_21.setText(_translate("MainWindow", "P6"))
        self.label_23.setText(_translate("MainWindow", "P8"))

    def PL7(self):
        # =========================MODEL

        PL7 = gb.Model("PL7")
        Offre = [
                 [int(self.lineEdit.text()),int(self.lineEdit_2.text()),int(self.lineEdit_3.text()),int(self.lineEdit_4.text()),int(self.lineEdit_5.text()),int(self.lineEdit_6.text()),int(self.lineEdit_7.text()),int(self.lineEdit_8.text())],
                 [int(self.lineEdit_10.text()), int(self.lineEdit_12.text()), int(self.lineEdit_9.text()),int(self.lineEdit_16.text()), int(self.lineEdit_13.text()), int(self.lineEdit_14.text()),int(self.lineEdit_11.text()), int(self.lineEdit_15.text())],
                 [int(self.lineEdit_18.text()), int(self.lineEdit_20.text()), int(self.lineEdit_17.text()),int(self.lineEdit_24.text()), int(self.lineEdit_21.text()), int(self.lineEdit_22.text()),int(self.lineEdit_19.text()), int(self.lineEdit_23.text())],
                 [int(self.lineEdit_26.text()), int(self.lineEdit_28.text()), int(self.lineEdit_25.text()),int(self.lineEdit_32.text()), int(self.lineEdit_29.text()), int(self.lineEdit_30.text()),int(self.lineEdit_27.text()), int(self.lineEdit_31.text())],
                 [int(self.lineEdit_34.text()), int(self.lineEdit_36.text()), int(self.lineEdit_33.text()),int(self.lineEdit_40.text()), int(self.lineEdit_37.text()), int(self.lineEdit_38.text()),int(self.lineEdit_35.text()), int(self.lineEdit_39.text())],
                 [int(self.lineEdit_42.text()), int(self.lineEdit_44.text()), int(self.lineEdit_41.text()),int(self.lineEdit_48.text()), int(self.lineEdit_45.text()), int(self.lineEdit_46.text()),int(self.lineEdit_43.text()), int(self.lineEdit_47.text())],
        ]
        res = [[PL7.addVar(vtype=gb.GRB.BINARY, name='X' + str(i + 1) + str(j + 1)) for i in range(8)] for j in
               range(6)]
        for i in range(6):
            for j in range(8):
                if Offre[i][j] == 0:
                    Offre[i][j] = 10 ** 6

        for j in range(8):
            PL7.addConstr(sum(res[i][j] for i in range(6)) == 1)

        for i in range(6):
            PL7.addConstr(sum(res[i][j] for j in range(8)) <= 2)

        Cout = sum(res[i][j] * Offre[i][j] for i in range(6) for j in range(8))
        PL7.setObjective(Cout, gb.GRB.MINIMIZE)

        PL7.optimize()
        with open("Resolutions/PL7.txt", "w") as f:
            sys.stdout = f
            sheet = {}
            vars = PL7.getVars()
            for var in vars:
                print(var.varName, var.x)
                sheet.update({var.varName : [var.x]})
            df = pd.DataFrame(sheet)
            df.to_excel("Resolution_excel/pl7.xlsx")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PL7_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

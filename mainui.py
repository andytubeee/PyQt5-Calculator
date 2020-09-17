from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
import sys
from PySide2.QtWidgets import QApplication, QPushButton, QMessageBox
from decimal import Decimal


class Ui_MainUI(object):
    def setupUi(self, MainUI):
        MainUI.setObjectName("MainUI")
        MainUI.setWindowModality(QtCore.Qt.WindowModal)
        MainUI.resize(334, 155)
        self.centralwidget = QtWidgets.QWidget(MainUI)
        self.centralwidget.setObjectName("centralwidget")
        self.first_num = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.first_num.setGeometry(QtCore.QRect(130, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.first_num.setFont(font)
        self.first_num.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.first_num.setObjectName("first_num")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sec_num = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sec_num.setGeometry(QtCore.QRect(130, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sec_num.setFont(font)
        self.sec_num.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.sec_num.setObjectName("sec_num")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add_onclick)

        self.sub_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sub_btn.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.sub_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sub_btn.setObjectName("sub_btn")
        self.sub_btn.clicked.connect(self.sub_onclick)

        self.mul_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mul_btn.setGeometry(QtCore.QRect(170, 90, 75, 23))
        self.mul_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mul_btn.setObjectName("mul_btn")
        self.mul_btn.clicked.connect(self.mul_onclick)

        self.div_btn = QtWidgets.QPushButton(self.centralwidget)
        self.div_btn.setGeometry(QtCore.QRect(250, 90, 75, 23))
        self.div_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.div_btn.setObjectName("div_btn")
        self.div_btn.clicked.connect(self.div_onclick)

        MainUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 21))
        self.menubar.setObjectName("menubar")
        MainUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainUI)
        self.statusbar.setObjectName("statusbar")
        MainUI.setStatusBar(self.statusbar)

        self.retranslateUi(MainUI)
        QtCore.QMetaObject.connectSlotsByName(MainUI)

    def retranslateUi(self, MainUI):
        _translate = QtCore.QCoreApplication.translate
        MainUI.setWindowTitle(_translate("MainUI", "Calculator"))
        self.first_num.setWhatsThis(_translate("MainUI", "first_num"))
        self.label.setText(_translate("MainUI", "First Number:"))
        self.sec_num.setWhatsThis(_translate("MainUI", "first_num"))
        self.label_2.setText(_translate("MainUI", "Second Number:"))
        self.add_btn.setText(_translate("MainUI", "Add"))
        self.sub_btn.setText(_translate("MainUI", "Subtract"))
        self.mul_btn.setText(_translate("MainUI", "Multiply"))
        self.div_btn.setText(_translate("MainUI", "Divide"))

    def add_onclick(self):

        try:
            if (len(str(self.first_num.toPlainText())) > 0 and len(str(self.sec_num.toPlainText())) > 0):
                ans = QMessageBox()
                ans.setIcon(QMessageBox.Information)

                if "." in str(self.first_num.toPlainText()) or "." in str(self.sec_num.toPlainText()):
                    sum = float(float(self.first_num.toPlainText()) +
                                float(self.sec_num.toPlainText()))

                    if str(sum)[-2:] == '.0':
                        sum = str(sum)[:-2]
                else:
                    sum = int(int(self.first_num.toPlainText()) +
                              int(self.sec_num.toPlainText()))
                ans.setText(
                    f"The sum of {self.first_num.toPlainText().strip()} and {self.sec_num.toPlainText().strip()} is {sum}")
                ans.setWindowTitle("Addition / Sum")
                ans.setStandardButtons(QMessageBox.Ok)
                x = ans.exec_()
            else:
                ans = QMessageBox()
                ans.setIcon(QMessageBox.Critical)
                ans.setText(
                    f"Input value cannot be empty!")
                ans.setWindowTitle("Error")
                ans.setStandardButtons(QMessageBox.Ok)
                x = ans.exec_()
        except ValueError:
            ans = QMessageBox()
            ans.setIcon(QMessageBox.Critical)
            ans.setText(
                f"Input value must me a number!")
            ans.setWindowTitle("Error")
            ans.setStandardButtons(QMessageBox.Ok)
            x = ans.exec_()

    def sub_onclick(self):
        try:
            if (len(str(self.first_num.toPlainText())) > 0 and len(str(self.sec_num.toPlainText())) > 0):
                ans = QMessageBox()
                ans.setIcon(QMessageBox.Information)

                if "." in str(self.first_num.toPlainText()) or "." in str(self.sec_num.toPlainText()):
                    diff = float(float(self.first_num.toPlainText()
                                       ) - float(self.sec_num.toPlainText()))

                    if str(diff)[-2:] == '.0':
                        diff = str(diff)[:-2]
                else:
                    diff = int(int(self.first_num.toPlainText()) -
                               int(self.sec_num.toPlainText()))

                ans.setText(
                    f"{self.first_num.toPlainText().strip()} subtracted by {self.sec_num.toPlainText().strip()} is {diff}")
                ans.setWindowTitle("Subtraction")
                ans.setStandardButtons(QMessageBox.Ok)
                x = ans.exec_()
            else:
                ans = QMessageBox()
                ans.setIcon(QMessageBox.Critical)
                ans.setText(
                    f"Input value cannot be empty!")
                ans.setWindowTitle("Error")
                ans.setStandardButtons(QMessageBox.Ok)
                x = ans.exec_()
        except ValueError:
            ans = QMessageBox()
            ans.setIcon(QMessageBox.Critical)
            ans.setText(
                f"Input value must me a number!")
            ans.setWindowTitle("Error")
            ans.setStandardButtons(QMessageBox.Ok)
            x = ans.exec_()

    def mul_onclick(self):
        try:
            if (len(str(self.first_num.toPlainText()).strip()) > 0 and len(str(self.sec_num.toPlainText()).strip()) > 0):
                ans = QMessageBox()
                ans.setIcon(QMessageBox.Information)

                if "." in str(self.first_num.toPlainText()) or "." in str(self.sec_num.toPlainText()):
                    prod = float(float(self.first_num.toPlainText())
                                 * float(self.sec_num.toPlainText()))

                    if str(prod)[-2:] == '.0':
                        prod = str(prod)[:-2]

                else:
                    prod = int(int(self.first_num.toPlainText())
                               * int(self.sec_num.toPlainText()))

                ans.setText(
                    f"The product of {self.first_num.toPlainText().strip()} and {self.sec_num.toPlainText().strip()} is {prod}")
                ans.setWindowTitle("Multiplication / Product")
                ans.setStandardButtons(QMessageBox.Ok)
                x = ans.exec_()
            else:
                ans = QMessageBox()
                ans.setIcon(QMessageBox.Critical)
                ans.setText(
                    f"Input value cannot be empty!")
                ans.setWindowTitle("Error")
                ans.setStandardButtons(QMessageBox.Ok)
                x = ans.exec_()
        except ValueError:
            ans = QMessageBox()
            ans.setIcon(QMessageBox.Critical)
            ans.setText(
                f"Input value must me a number!")
            ans.setWindowTitle("Error")
            ans.setStandardButtons(QMessageBox.Ok)
            x = ans.exec_()

    def div_onclick(self):
        try:
            if str(self.sec_num.toPlainText().strip()) == "0":
                ans = QMessageBox()
                ans.setIcon(QMessageBox.Critical)
                ans.setText(
                    f"You can't divide by zero!")
                ans.setWindowTitle("Error")
                ans.setStandardButtons(QMessageBox.Ok)
                x = ans.exec_()
            else:
                if (len(str(self.first_num.toPlainText()).strip()) > 0 and len(str(self.sec_num.toPlainText()).strip()) > 0):
                    ans = QMessageBox()
                    ans.setIcon(QMessageBox.Information)

                    quo = float(float(self.first_num.toPlainText())
                                / float(self.sec_num.toPlainText()))

                    if str(quo)[-2:] == ".0":
                        quo = str(quo)[:-2]

                    ans.setText(
                        f"The quotient of {self.first_num.toPlainText().strip()} and {self.sec_num.toPlainText().strip()} is {quo}")
                    ans.setWindowTitle("Division / Quotient")
                    ans.setStandardButtons(QMessageBox.Ok)
                    x = ans.exec_()
                else:
                    ans = QMessageBox()
                    ans.setIcon(QMessageBox.Critical)
                    ans.setText(
                        f"Input value cannot be empty!")
                    ans.setWindowTitle("Error")
                    ans.setStandardButtons(QMessageBox.Ok)
                    x = ans.exec_()
        except ValueError:
            ans = QMessageBox()
            ans.setIcon(QMessageBox.Critical)
            ans.setText(
                f"Input value must me a number!")
            ans.setWindowTitle("Error")
            ans.setStandardButtons(QMessageBox.Ok)
            x = ans.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainUI = QtWidgets.QMainWindow()
    ui = Ui_MainUI()
    ui.setupUi(MainUI)
    MainUI.setFixedSize(MainUI.size())
    MainUI.setWindowFlags(QtCore.Qt.WindowCloseButtonHint |
                          QtCore.Qt.WindowMinimizeButtonHint)
    MainUI.show()

    sys.exit(app.exec_())

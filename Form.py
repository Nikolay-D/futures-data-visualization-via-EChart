# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Damon(object):
    def setupUi(self, Damon):
        Damon.setObjectName("Damon")
        Damon.resize(1553, 925)
        self.title = QtWidgets.QLabel(Damon)
        self.title.setGeometry(QtCore.QRect(660, 20, 251, 21))
        self.title.setStyleSheet("font: 75 14pt \"宋体\";")
        self.title.setObjectName("title")
        self.comboBox = QtWidgets.QComboBox(Damon)
        self.comboBox.setGeometry(QtCore.QRect(120, 770, 61, 24))
        self.comboBox.setObjectName("comboBox")
        self.DataPathL = QtWidgets.QLabel(Damon)
        self.DataPathL.setGeometry(QtCore.QRect(20, 720, 181, 18))
        self.DataPathL.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.DataPathL.setObjectName("DataPathL")
        self.BrowseB1 = QtWidgets.QPushButton(Damon)
        self.BrowseB1.setGeometry(QtCore.QRect(680, 720, 71, 34))
        self.BrowseB1.setStyleSheet("font: 75 10pt \"新宋体\";\n"
"")
        self.BrowseB1.setObjectName("BrowseB1")
        self.DataFramL = QtWidgets.QLabel(Damon)
        self.DataFramL.setGeometry(QtCore.QRect(20, 770, 111, 18))
        self.DataFramL.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.DataFramL.setObjectName("DataFramL")
        self.StartDateL = QtWidgets.QLabel(Damon)
        self.StartDateL.setGeometry(QtCore.QRect(270, 770, 131, 18))
        self.StartDateL.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.StartDateL.setObjectName("StartDateL")
        self.EndDateL = QtWidgets.QLabel(Damon)
        self.EndDateL.setGeometry(QtCore.QRect(590, 770, 131, 18))
        self.EndDateL.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.EndDateL.setObjectName("EndDateL")
        self.StartTimeL = QtWidgets.QLabel(Damon)
        self.StartTimeL.setGeometry(QtCore.QRect(270, 820, 131, 18))
        self.StartTimeL.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.StartTimeL.setObjectName("StartTimeL")
        self.EndTimeL = QtWidgets.QLabel(Damon)
        self.EndTimeL.setGeometry(QtCore.QRect(590, 820, 131, 18))
        self.EndTimeL.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.EndTimeL.setObjectName("EndTimeL")
        self.ChartTypeL = QtWidgets.QLabel(Damon)
        self.ChartTypeL.setGeometry(QtCore.QRect(20, 820, 131, 18))
        self.ChartTypeL.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.ChartTypeL.setObjectName("ChartTypeL")
        self.comboBox_3 = QtWidgets.QComboBox(Damon)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 820, 91, 24))
        self.comboBox_3.setObjectName("comboBox_3")
        self.dp_le = QtWidgets.QLineEdit(Damon)
        self.dp_le.setGeometry(QtCore.QRect(190, 720, 481, 31))
        self.dp_le.setObjectName("dp_le")
        self.ed_le = QtWidgets.QLineEdit(Damon)
        self.ed_le.setGeometry(QtCore.QRect(680, 770, 161, 31))
        self.ed_le.setObjectName("ed_le")
        self.st_le = QtWidgets.QLineEdit(Damon)
        self.st_le.setGeometry(QtCore.QRect(370, 820, 161, 31))
        self.st_le.setObjectName("st_le")
        self.et_le = QtWidgets.QLineEdit(Damon)
        self.et_le.setGeometry(QtCore.QRect(680, 820, 161, 31))
        self.et_le.setObjectName("et_le")
        self.ed_le_2 = QtWidgets.QLineEdit(Damon)
        self.ed_le_2.setGeometry(QtCore.QRect(370, 770, 161, 31))
        self.ed_le_2.setObjectName("ed_le_2")
        self.pushButton = QtWidgets.QPushButton(Damon)
        self.pushButton.setGeometry(QtCore.QRect(1270, 720, 271, 131))
        self.pushButton.setObjectName("pushButton")
        self.webView = QtWebKitWidgets.QWebView(Damon)
        self.webView.setGeometry(QtCore.QRect(20, 60, 1521, 631))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.label = QtWidgets.QLabel(Damon)
        self.label.setGeometry(QtCore.QRect(1440, 890, 101, 31))
        self.label.setObjectName("label")
        self.DataPathL_2 = QtWidgets.QLabel(Damon)
        self.DataPathL_2.setGeometry(QtCore.QRect(900, 720, 181, 18))
        self.DataPathL_2.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.DataPathL_2.setObjectName("DataPathL_2")
        self.ed_le_3 = QtWidgets.QLineEdit(Damon)
        self.ed_le_3.setGeometry(QtCore.QRect(1080, 720, 121, 31))
        self.ed_le_3.setObjectName("ed_le_3")
        self.DataPathL_3 = QtWidgets.QLabel(Damon)
        self.DataPathL_3.setGeometry(QtCore.QRect(900, 770, 101, 20))
        self.DataPathL_3.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.DataPathL_3.setObjectName("DataPathL_3")
        self.ed_le_4 = QtWidgets.QLineEdit(Damon)
        self.ed_le_4.setGeometry(QtCore.QRect(940, 770, 91, 31))
        self.ed_le_4.setObjectName("ed_le_4")
        self.DataPathL_4 = QtWidgets.QLabel(Damon)
        self.DataPathL_4.setGeometry(QtCore.QRect(1050, 770, 121, 18))
        self.DataPathL_4.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.DataPathL_4.setObjectName("DataPathL_4")
        self.ed_le_5 = QtWidgets.QLineEdit(Damon)
        self.ed_le_5.setGeometry(QtCore.QRect(1110, 770, 91, 31))
        self.ed_le_5.setObjectName("ed_le_5")
        self.DataPathL_5 = QtWidgets.QLabel(Damon)
        self.DataPathL_5.setGeometry(QtCore.QRect(900, 820, 131, 20))
        self.DataPathL_5.setStyleSheet("font: 75 11pt \"新宋体\";")
        self.DataPathL_5.setObjectName("DataPathL_5")
        self.ed_le_6 = QtWidgets.QLineEdit(Damon)
        self.ed_le_6.setGeometry(QtCore.QRect(1030, 820, 171, 31))
        self.ed_le_6.setObjectName("ed_le_6")

        self.retranslateUi(Damon)
        QtCore.QMetaObject.connectSlotsByName(Damon)

    def retranslateUi(self, Damon):
        _translate = QtCore.QCoreApplication.translate
        Damon.setWindowTitle(_translate("Damon", "Form"))
        self.title.setText(_translate("Damon", "Output HTML for Analysis"))
        self.DataPathL.setText(_translate("Damon", "*Data Path(CSV/MAT):"))
        self.BrowseB1.setText(_translate("Damon", "Browse"))
        self.DataFramL.setText(_translate("Damon", "*Data Frame:"))
        self.StartDateL.setText(_translate("Damon", "*Start Date:"))
        self.EndDateL.setText(_translate("Damon", "*End Date:"))
        self.StartTimeL.setText(_translate("Damon", "*Start Time:"))
        self.EndTimeL.setText(_translate("Damon", "*End Time:"))
        self.ChartTypeL.setText(_translate("Damon", "*Chart Type:"))
        self.pushButton.setText(_translate("Damon", "Output"))
        self.label.setText(_translate("Damon", "Created by Damon"))
        self.DataPathL_2.setText(_translate("Damon", "*Symbol Name(MongoDB):"))
        self.DataPathL_3.setText(_translate("Damon", "*IP:"))
        self.DataPathL_4.setText(_translate("Damon", "*PORT:"))
        self.DataPathL_5.setText(_translate("Damon", "*Database Name:"))

from PyQt5 import QtWebKitWidgets

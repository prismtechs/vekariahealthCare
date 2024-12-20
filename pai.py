# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Patient-info.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtCore  import Qt
# from wifi_final import WifiPage
# from wifi_update import WifiStatusLabel
# from globalvar import globaladc as buzzer
import json
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
import os
# from flicker_demo import FlickerController
import subprocess
# from CustomLineEdit import QtWidgets.QTextEdit



class Patient_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1031, 586)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet("background-color:black;\n"
"border:none;")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.form  = Form
        self.frame_2.setGeometry(QtCore.QRect(20, 120, 981, 460))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.frame_2.setFont(font)

        
        # Radio buttons setup with new styling
        
        self.frame_2.setStyleSheet("background-color:black;\n"
"color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(0, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.frame_2.setStyleSheet("""
            
            QFrame {
                border: none;
                background: transparent;
                color:white;
            }
            
            QRadioButton {
                color: white;
                border-radius: 10px;
            }
            
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border-radius: 9px;
                
            }
            
            QRadioButton::indicator:checked {
                background-color: #42A5F5;
                
            }
            

        """)
        self.textEdit.setGeometry(QtCore.QRect(139, 20, 190, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setStyleSheet(" QTextEdit {\n"
"                background-color: #334155;\n"
"                border:1px solid white;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }\n"
"\n"
"\n"
"QTextEdit {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"    QTextBrowser {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"\n"
"QTextEdit QScrollBar:vertical {\n"
"        width: 0px;  /* This hides the vertical scrollbar */\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 0px;  /* This hides the horizontal scrollbar */\n"
"    }")
        self.textEdit.setObjectName("textEdit")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(344, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setGeometry(QtCore.QRect(491, 20, 165, 31))
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_2.setGeometry(QtCore.QRect(491, 20, 165, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(" QTextEdit {\n"
"                background-color: #334155;\n"
"                border:1px solid white;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }\n"
"\n"
"\n"
"QTextEdit {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"    QTextBrowser {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"\n"
"QTextEdit QScrollBar:vertical {\n"
"        width: 0px;  /* This hides the vertical scrollbar */\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 0px;  /* This hides the horizontal scrollbar */\n"
"    }")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_3.setGeometry(QtCore.QRect(801, 20, 175, 31))
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet(" QTextEdit {\n"
"                background-color: #334155;\n"
"                border:1px solid white;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }\n"
"\n"
"\n"
"QTextEdit {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"    QTextBrowser {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"\n"
"QTextEdit QScrollBar:vertical {\n"
"        width: 0px;  /* This hides the vertical scrollbar */\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 0px;  /* This hides the horizontal scrollbar */\n"
"    }")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(670, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(0, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_4.setGeometry(QtCore.QRect(141, 80, 190, 31))
        self.textEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet(" QTextEdit {\n"
"                background-color: #334155;\n"
"                border:1px solid white;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }\n"
"\n"
"\n"
"QTextEdit {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"    QTextBrowser {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"\n"
"QTextEdit QScrollBar:vertical {\n"
"        width: 0px;  /* This hides the vertical scrollbar */\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 0px;  /* This hides the horizontal scrollbar */\n"
"    }")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(0, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(346, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_5.setGeometry(QtCore.QRect(487, 80, 165, 31))
        self.textEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setStyleSheet(" QTextEdit {\n"
"                background-color: #334155;\n"
"                border:1px solid white;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }\n"
"\n"
"\n"
"QTextEdit {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"    QTextBrowser {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"\n"
"QTextEdit QScrollBar:vertical {\n"
"        width: 0px;  /* This hides the vertical scrollbar */\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 0px;  /* This hides the horizontal scrollbar */\n"
"    }")
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(676, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.textEdit_6 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_6.setGeometry(QtCore.QRect(802, 80, 175, 31))
        self.textEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setStyleSheet(" QTextEdit {\n"
"                background-color: #334155;\n"
"                border:1px solid white;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }\n"
"\n"
"\n"
"QTextEdit {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"    QTextBrowser {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"\n"
"QTextEdit QScrollBar:vertical {\n"
"        width: 0px;  /* This hides the vertical scrollbar */\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 0px;  /* This hides the horizontal scrollbar */\n"
"    }")
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(0, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_22 = QtWidgets.QLabel(self.frame_2)
        self.label_22.setGeometry(QtCore.QRect(0, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(450, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.Diabetes_text = QtWidgets.QTextEdit(self.frame_2)
        self.Diabetes_text.setGeometry(QtCore.QRect(830, 260, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Diabetes_text.setFont(font)
        self.Diabetes_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Diabetes_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Diabetes_text.setStyleSheet(" QTextEdit {\n"
"                background-color: #334155;\n"
"                border:1px solid white;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }\n"
"\n"
"\n"
"QTextEdit {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"    QTextBrowser {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"\n"
"QTextEdit QScrollBar:vertical {\n"
"        width: 0px;  /* This hides the vertical scrollbar */\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 0px;  /* This hides the horizontal scrollbar */\n"
"    }")
        self.Diabetes_text.setObjectName("Diabetes_text")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(450, 200, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setGeometry(QtCore.QRect(0, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.Diabetes_text_2 = QtWidgets.QTextEdit(self.frame_2)
        self.Diabetes_text_2.setGeometry(QtCore.QRect(830, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Diabetes_text_2.setFont(font)
        self.Diabetes_text_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Diabetes_text_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Diabetes_text_2.setStyleSheet(" QTextEdit {\n"
"                background-color: #334155;\n"
"                border:1px solid white;\n"
"                border-radius: 10px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }\n"
"\n"
"\n"
"QTextEdit {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"    QTextBrowser {\n"
"        padding: 0px;\n"
"        margin: 0px;\n"
"    }\n"
"\n"
"QTextEdit QScrollBar:vertical {\n"
"        width: 0px;  /* This hides the vertical scrollbar */\n"
"    }\n"
"    QTextEdit QScrollBar:horizontal {\n"
"        height: 0px;  /* This hides the horizontal scrollbar */\n"
"    }")
        self.Diabetes_text_2.setObjectName("Diabetes_text_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 390, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: transparent;\n"
"        color: white;\n"
"        border: 1px solid white;\n"
"        padding: 10px 20px;\n"
"        font-size: 24px;\n"
"        border-radius: 1px;\n"
"        font-weight: bold;\n"
"        transition: all 0.3s;\n"
"        margin: 2px;\n"
"        /* Add subtle initial shadow */\n"
"        border-bottom: 1px solid white;\n"
"        border-right: 1px solid white;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: rgba(33, 150, 243, 0.1);\n"
"        border: 2px solid #64B5F6;\n"
"        color: #64B5F6;\n"
"        /* Enhanced hover effect */\n"
"        border-bottom: 4px solid #42A5F5;\n"
"        border-right: 3px solid #42A5F5;\n"
"        margin: 2px;\n"
"    }\n"
"    \n"
"    QPushButton:pressed {\n"
"        background-color: rgba(33, 150, 243, 0.2);\n"
"        border: 2px solid white;\n"
"        /* Create pressed effect */\n"
"        border-bottom: 2px solid white;\n"
"        border-right: 2px solid white;\n"
"        margin-top: 4px;\n"
"        margin-left: 2px;\n"
"        padding-top: 11px;\n"
"        padding-left: 21px;\n"
"    }\n"
"    \n"
"    QPushButton:disabled {\n"
"        background-color: transparent;\n"
"        color: #B0B0B0;\n"
"        border: 2px solid #B0B0B0;\n"
"        border-bottom: 4px solid #909090;\n"
"        border-right: 3px solid #909090;\n"
"    }\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.Acho_no = QtWidgets.QRadioButton(self.frame_2)
        self.Acho_no.setGeometry(QtCore.QRect(276, 200, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Acho_no.setFont(font)
        self.Acho_no.setChecked(False)
        self.Acho_no.setObjectName("Acho_no")
        self.Alcho_yes = QtWidgets.QRadioButton(self.frame_2)
        self.Alcho_yes.setGeometry(QtCore.QRect(157, 200, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Alcho_yes.setFont(font)
        self.Alcho_yes.setObjectName("Alcho_yes")
        self.male = QtWidgets.QRadioButton(self.frame_2)
        self.male.setGeometry(QtCore.QRect(157, 140, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.male.setFont(font)
        self.male.setChecked(False)
        self.male.setObjectName("male")
        self.female = QtWidgets.QRadioButton(self.frame_2)
        self.female.setGeometry(QtCore.QRect(276, 140, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.female.setFont(font)
        self.female.setObjectName("female")
        self.Dia_yes = QtWidgets.QRadioButton(self.frame_2)
        self.Dia_yes.setGeometry(QtCore.QRect(660, 260, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Dia_yes.setFont(font)
        self.Dia_yes.setObjectName("Dia_yes")
        self.Dia_no = QtWidgets.QRadioButton(self.frame_2)
        self.Dia_no.setGeometry(QtCore.QRect(750, 260, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Dia_no.setFont(font)
        self.Dia_no.setChecked(False)
        self.Dia_no.setObjectName("Dia_no")
        self.Bp_yes = QtWidgets.QRadioButton(self.frame_2)
        self.Bp_yes.setGeometry(QtCore.QRect(660, 200, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Bp_yes.setFont(font)
        self.Bp_yes.setObjectName("Bp_yes")
        self.Bp_no = QtWidgets.QRadioButton(self.frame_2)
        self.Bp_no.setGeometry(QtCore.QRect(750, 200, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Bp_no.setFont(font)
        self.Bp_no.setChecked(False)
        self.Bp_no.setObjectName("Bp_no")
        self.Alcho_yes_2 = QtWidgets.QRadioButton(self.frame_2)
        self.Alcho_yes_2.setGeometry(QtCore.QRect(157, 260, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Alcho_yes_2.setFont(font)
        self.Alcho_yes_2.setObjectName("Alcho_yes_2")
        self.Acho_no_2 = QtWidgets.QRadioButton(self.frame_2)
        self.Acho_no_2.setGeometry(QtCore.QRect(276, 260, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Acho_no_2.setFont(font)
        self.Acho_no_2.setChecked(False)
        self.Acho_no_2.setObjectName("Acho_no_2")
        self.Alcho_yes_3 = QtWidgets.QRadioButton(self.frame_2)
        self.Alcho_yes_3.setGeometry(QtCore.QRect(157, 320, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Alcho_yes_3.setFont(font)
        self.Alcho_yes_3.setObjectName("Alcho_yes_3")
        self.Acho_no_3 = QtWidgets.QRadioButton(self.frame_2)
        self.Acho_no_3.setGeometry(QtCore.QRect(276, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Acho_no_3.setFont(font)
        self.Acho_no_3.setChecked(False)
        self.Acho_no_3.setObjectName("Acho_no_3")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(450, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(570, 130, 291, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.eye_R = QtWidgets.QRadioButton(self.frame_2)
        self.eye_R.setGeometry(QtCore.QRect(660, 140, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.eye_R.setFont(font)
        self.eye_R.setCheckable(True)
        self.eye_R.setChecked(True)
        self.eye_R.setObjectName("eye_R")
        self.eye_L = QtWidgets.QRadioButton(self.frame_2)
        self.eye_L.setGeometry(QtCore.QRect(750, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.eye_L.setFont(font)
        self.eye_L.setChecked(False)
        self.eye_L.setObjectName("eye_L")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 1011, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(1, 0, 1024, 40))
        self.frame_4.setStyleSheet("background-color:#101826;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(60, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:white;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(930, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:white;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(5, 8, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/newPrefix/Vekaria Healthcare Logo/VHC Logo.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        # self.wifiIcon = WifiStatusLabel(self.frame)
        # self.wifiIcon.setGeometry(QtCore.QRect(868, 5, 41, 31))
        # font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        # font.setPointSize(20)
        # font.setBold(True)
        # font.setWeight(75)
        # self.wifiIcon.setFont(font)
        # self.wifiIcon.setPixmap(QtGui.QPixmap(":/vlogo/logo12.png"))
        # self.wifiIcon.clicked.connect(self.open_wifi_page)
        

        #gender group
        self.gender_group = QtWidgets.QButtonGroup(self.frame_2)
        self.gender_group.addButton(self.male)
        self.gender_group.addButton(self.female)

        #alcohol group
        self.alcohol_group = QtWidgets.QButtonGroup(self.frame_2)
        self.alcohol_group.addButton(self.Alcho_yes)
        self.alcohol_group.addButton(self.Acho_no)

        #somke group
        self.smoke_group = QtWidgets.QButtonGroup(self.frame_2)
        self.smoke_group.addButton(self.Alcho_yes_2)
        self.smoke_group.addButton(self.Acho_no_2)

        #food habit group
        self.food_habit_group = QtWidgets.QButtonGroup(self.frame_2)
        self.food_habit_group.addButton(self.Alcho_yes_3)
        self.food_habit_group.addButton(self.Acho_no_3)

        #eye side group
        self.eye_side_group = QtWidgets.QButtonGroup(self.frame_2)
        self.eye_side_group.addButton(self.eye_R)
        self.eye_side_group.addButton(self.eye_L)
        self.pushButton_2.clicked.connect(self.save_patient_data)

        #diabetes group
        self.diabetes_group = QtWidgets.QButtonGroup(self.frame_2)      
        self.diabetes_group.addButton(self.Dia_yes)
        self.diabetes_group.addButton(self.Dia_no)




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def show_keyboard(self, event, text_edit):
        """Show onboard keyboard when text edit gains focus"""
        subprocess.Popen(['onboard'])
        text_edit.original_focusInEvent(event) if hasattr(text_edit, 'original_focusInEvent') else None

    def hide_keyboard(self, event, text_edit):
        """Hide onboard keyboard when text edit loses focus"""
        subprocess.run(['killall', 'onboard'])
        text_edit.original_focusOutEvent(event) if hasattr(text_edit, 'original_focusOutEvent') else None

    def open_wifi_page(self):
        # buzzer.buzzer_1()
        # if self.wifi_window is None:
        #     self.wifi_window = WifiPage()
        #     self.wifi_window.show()
        # else:
        #     self.wifi_window.activateWindow()
        pass

    def save_patient_data(self):
        # buzzer.buzzer_1()
        try:
                
                patient_data = {
                "first_name": self.textEdit.toPlainText().strip(),
                "middle_name": self.textEdit_2.toPlainText().strip(),
                "surname": self.textEdit_3.toPlainText().strip(),
                "dob": self.textEdit_4.toPlainText().strip(),
                "aadhaar": self.textEdit_5.toPlainText().strip(),
                "mobile": self.textEdit_6.toPlainText().strip(),
                "gender": "Male" if self.male.isChecked() else "Female",
                "alcohol": "Yes" if self.Alcho_yes.isChecked() else "No",
                "smoking": "Yes" if self.Alcho_yes_2.isChecked() else "No",
                "food_habit": "Veg" if self.Alcho_yes_3.isChecked() else "NON-Veg",
                "bp": {
                        "has_bp": "Yes" if self.Bp_yes.isChecked() else "No",
                        "value": self.Diabetes_text_2.toPlainText().strip()
                },
                "diabetes": {
                        "has_diabetes": "Yes" if self.Dia_yes.isChecked() else "No",
                        "value": self.Diabetes_text.toPlainText().strip()
                },
                "eye_side": "R" if self.eye_R.isChecked() else "L",
                "is_sync":False,
                "handler_id":0
                }
                
                current_login_usr = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_data", "latest_user.json")
                with open(current_login_usr, 'r') as f:
                     user_data = json.load(f)

                patient_data['handler_id'] = user_data['user_id']
                        
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"patient_{patient_data['first_name']}.json"
                filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "patient_data", filename)
                
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                
                with open(filepath, 'w') as f:
                        json.dump(patient_data, f, indent=4)

                self.form.hide()
                # self.flickerCon_window = QtWidgets.QWidget()
                # self.flickerCon = FlickerController()  
                # self.flickerCon.show()
                
                QMessageBox.information(None, "Success", "Patient data saved successfully!")
                
        except Exception as e:
                QMessageBox.critical(None, "Error", f"Error saving patient data: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "1st Name"))
        self.textEdit.setPlaceholderText("first name")
        self.label_9.setText(_translate("Form", "Mid. Name"))
        self.textEdit_2.setPlaceholderText("Middle Name")
        self.textEdit_3.setPlaceholderText("Surname")
        self.label_10.setText(_translate("Form", "Surname"))
        self.label_7.setText(_translate("Form", "DOB"))
        self.textEdit_4.setPlaceholderText("Date of Birth")
        self.label_8.setText(_translate("Form", "Gender"))
        self.label_11.setText(_translate("Form", "Aadhaar"))
        self.textEdit_5.setPlaceholderText("Aadhaar No")
        self.label_12.setText(_translate("Form", "Mobile"))
        self.textEdit_6.setPlaceholderText("+91XXXXXXXXX")
        self.label_13.setText(_translate("Form", "Alchohol "))
        self.label_22.setText(_translate("Form", "Smoking"))
        self.label_23.setText(_translate("Form", "Diabetes"))
        self.Diabetes_text.setPlaceholderText("97")
        self.label_24.setText(_translate("Form", "Blood Pressure"))
        self.label_26.setText(_translate("Form", "Food Habit"))
        self.Diabetes_text_2.setPlaceholderText("80/120")
        self.pushButton_2.setText(_translate("Form", "SUBMIT"))
        self.Acho_no.setText(_translate("Form", "No"))
        self.Alcho_yes.setText(_translate("Form", "Yes"))
        self.male.setText(_translate("Form", "Male"))
        self.female.setText(_translate("Form", "Female"))
        self.Dia_yes.setText(_translate("Form", "Yes"))
        self.Dia_no.setText(_translate("Form", "No"))
        self.Bp_yes.setText(_translate("Form", "Yes"))
        self.Bp_no.setText(_translate("Form", "No"))
        self.Alcho_yes_2.setText(_translate("Form", "Yes"))
        self.Acho_no_2.setText(_translate("Form", "No"))
        self.Alcho_yes_3.setText(_translate("Form", "Veg"))
        self.Acho_no_3.setText(_translate("Form", "NON-Veg"))
        self.label_14.setText(_translate("Form", "Eye Side"))
        self.eye_R.setText(_translate("Form", "R"))
        self.eye_L.setText(_translate("Form", "L"))
        self.label_4.setText(_translate("Form", "Macular Densitometer                                                  Patient-Registration"))
        self.label_15.setText(_translate("Form", "Vekaria Healthcare"))
        self.label_16.setText(_translate("Form", "V1.0"))



import vekarialogo_rc
import wifi_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Patient_UI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

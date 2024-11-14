from PyQt5.QtCore import Qt, QRect, QTimer, QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        Form.setStyleSheet("background-color:black;")
        Form.setWindowFlags(Qt.FramelessWindowHint)
        
        # Initialize keyboard tracking variables
        self.current_focused_widget = None
        self.keyboard_process = None

        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 40))
        self.frame.setStyleSheet("background-color:#1f2836;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 0, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(930, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")

        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(5, 8, 44, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/Vekaria Healthcare Logo/VHC Logo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(870, 4, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/vlogo/logo12.png"))

        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 50, 1024, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica Rounded")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("QFrame{\n"
"background:none;\n"
"color:#f2f5f3;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(200, 115, 624, 430))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:#1f2836;\n"
"border-radius:30px;\n"
"border:1px solid white;\n"
"\n"
"};\n"
"color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        # Username field setup
        self.username = QtWidgets.QLineEdit(self.frame_2)
        self.username.setGeometry(QtCore.QRect(62, 50, 500, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.username.setFont(font)
        self.username.setStyleSheet(" QLineEdit {\n"
"                background-color: #334155;\n"
"                border:1px solid white;\n"
"                border-radius: 15px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }")
        self.username.setObjectName("username")
        # self.username.installEventFilter(self)

        # Password field setup
        self.password = QtWidgets.QLineEdit(self.frame_2)
        self.password.setGeometry(QtCore.QRect(62, 140, 500, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.password.setFont(font)
        self.password.setStyleSheet(" QLineEdit {\n"
"                background-color: #334155;\n"
"                border: 1px solid white;\n"
"                border-radius: 15px;\n"
"                padding: 5px;\n"
"                padding-left: 30px;\n"
"                color: #94a3b8;\n"
"            }")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.password.installEventFilter(self)

        # Password toggle button
        self.togglePassword = QtWidgets.QPushButton(self.frame_2)
        self.togglePassword.setGeometry(QtCore.QRect(570, 155, 30, 30))
        self.togglePassword.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                color: white;
            }
        """)
        self.togglePassword.setText("👁")
        self.togglePassword.clicked.connect(self.toggle_password_visibility)
        self.password_visible = False

        self.login = QtWidgets.QPushButton(self.frame_2)
        self.login.setGeometry(QtCore.QRect(230, 350, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setStyleSheet("\n"
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
"        border-bottom: 1px solid white;\n"
"        border-right: 1px solid white;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(33, 150, 243, 0.1);\n"
"        border: 2px solid #64B5F6;\n"
"        color: #64B5F6;\n"
"        border-bottom: 4px solid #42A5F5;\n"
"        border-right: 3px solid #42A5F5;\n"
"        margin: 2px;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(33, 150, 243, 0.2);\n"
"        border: 2px solid white;\n"
"        border-bottom: 2px solid white;\n"
"        border-right: 2px solid white;\n"
"        margin-top: 4px;\n"
"        margin-left: 2px;\n"
"        padding-top: 11px;\n"
"        padding-left: 21px;\n"
"    }\n"
"    QPushButton:disabled {\n"
"        background-color: transparent;\n"
"        color: #B0B0B0;\n"
"        border: 2px solid #B0B0B0;\n"
"        border-bottom: 4px solid #909090;\n"
"        border-right: 3px solid #909090;\n"
"    }")
        self.login.setObjectName("login")

        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(112, 210, 400, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("QFrame{\n"
"backgorund:none;\n"
"border:none;\n"
"color:#f2f5f3;\n"
"}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(110, 270, 491, 41))
        self.frame_3.setStyleSheet("border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        # Radio buttons setup with new styling
        self.frame_3.setStyleSheet("""
            QFrame {
                border: none;
                background: transparent;
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
            
            QRadioButton:checked {
                background-color: rgba(66, 165, 245, 0.2);
                
            }
        """)

        # Radio buttons setup
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(11, 11, 106, 19))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setStyleSheet("QRadioButton{\n"
"color:white;\n"
"background:none;\n"
"}")
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 11, 80, 19))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
"color:white;\n"
"background:none;\n"
"align-item:center;\n"
"align-content:center;\n"
"justify-content:center;\n"
"}")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_3.setGeometry(QtCore.QRect(328, 11, 71, 19))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("QRadioButton{\n"
"color:white;\n"
"background:none;\n"
"}")
        self.radioButton_3.setObjectName("radioButton_3")

        # Time and date labels
        self.Time = QtWidgets.QLabel(Form)
        self.Time.setGeometry(QtCore.QRect(960, 550, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.Time.setFont(font)
        self.Time.setStyleSheet("color:white;")
        self.Time.setObjectName("Time")

        self.date = QtWidgets.QLabel(Form)
        self.date.setGeometry(QtCore.QRect(934, 570, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.date.setFont(font)
        self.date.setStyleSheet("color:white;")
        self.date.setObjectName("date")

        # Setup timer for date and time updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Update every second
        
        # Initial datetime update
        self.update_datetime()
        self.username.focusInEvent = lambda event: self.handle_focus_in(event, self.username)
        self.username.focusOutEvent = lambda event: self.handle_focus_out(event)
        
        self.password.focusInEvent = lambda event: self.handle_focus_in(event, self.password)
        self.password.focusOutEvent = lambda event: self.handle_focus_out(event)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def update_datetime(self):
        """Update the date and time labels with current values"""
        current_datetime = QDateTime.currentDateTime()
        self.Time.setText(current_datetime.toString('HH:mm'))
        self.date.setText(current_datetime.toString('dd-MM-yyyy'))

    def eventFilter(self, obj, event):
        """Handle focus events for text input fields"""
        if obj in [self.username, self.password]:
            if event.type() == QtCore.QEvent.FocusIn:
                self.handle_focus_in(obj)
            elif event.type() == QtCore.QEvent.FocusOut:
                # Only hide keyboard if focus is not moving to another input field
                if not self.username.hasFocus() and not self.password.hasFocus():
                    self.hide_keyboard()
        return super().eventFilter(obj, event)

    def handle_focus_in(self, widget):
        """Handle focus in event for text fields"""
        if self.current_focused_widget != widget:
            self.current_focused_widget = widget
            self.show_keyboard()

    def show_keyboard(self):
        """Show the on-screen keyboard"""
        try:
            # Kill any existing keyboard instance
            self.hide_keyboard()
            
            # Calculate keyboard position to be at bottom of screen
            screen = QtWidgets.QApplication.primaryScreen().geometry()
            keyboard_height = 200  # Adjust this value based on your needs
            y_position = screen.height() - keyboard_height
            
            # Set environment variables for keyboard
            os.environ['ONBOARD_WINDOW_STATE_STICKY'] = '1'
            os.environ['ONBOARD_XEMBED_ASPECT_CHANGE'] = '1'
            
            # Launch keyboard with specific positioning
            self.keyboard_process = subprocess.Popen([
                'onboard',
                '--layout', 'Full',
                '--size', f'{screen.width()}x{keyboard_height}',
                '--x', '0',
                '--y', str(y_position),
                '--dock-window-enabled'
            ])
        except Exception as e:
            print(f"Error showing keyboard: {e}")

    def hide_keyboard(self):
        """Hide the on-screen keyboard"""
        try:
            if self.keyboard_process:
                self.keyboard_process.terminate()
                self.keyboard_process = None
            subprocess.run(['killall', 'onboard'], stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Error hiding keyboard: {e}")

    def toggle_password_visibility(self):
        """Toggle password field visibility"""
        self.password_visible = not self.password_visible
        if self.password_visible:
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.togglePassword.setText("🔒")
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.togglePassword.setText("👁")

    def closeEvent(self, event):
        """Clean up keyboard process when closing the application"""
        self.hide_keyboard()
        event.accept()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Vekaria Healthcare"))
        self.label_3.setText(_translate("Form", "V1.0"))
        self.label_4.setText(_translate("Form", "Macular Densitometer"))
        self.username.setPlaceholderText(_translate("Form", "Username"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.login.setText(_translate("Form", "LOGIN"))
        self.label_7.setText(_translate("Form", "Operation Mode"))
        self.radioButton.setText(_translate("Form", "Eye Camp"))
        self.radioButton_2.setText(_translate("Form", "Clinic"))
        self.radioButton_3.setText(_translate("Form", "Demo"))


    def handle_focus_in(self, event, widget):
        """Handle focus in event for text fields"""
        if self.current_focused_widget != widget:
            self.current_focused_widget = widget
            self.show_keyboard()
            
    def handle_focus_out(self, event):
        """Handle focus out event for text fields"""
        if not self.username.hasFocus() and not self.password.hasFocus():
            self.hide_keyboard()

import vekarialogo_rc
import wifi_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

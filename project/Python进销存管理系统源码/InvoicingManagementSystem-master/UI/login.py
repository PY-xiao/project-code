# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 682)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/resource/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_Shadow = QtWidgets.QFrame(self.centralwidget)
        self.frame_Shadow.setGeometry(QtCore.QRect(10, 10, 452, 660))
        self.frame_Shadow.setAutoFillBackground(False)
        self.frame_Shadow.setStyleSheet("QFrame{\n"
"border:0px;\n"
" background: rgb(235, 235, 235);\n"
" border-radius: 10px;\n"
"}")
        self.frame_Shadow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Shadow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Shadow.setObjectName("frame_Shadow")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_Shadow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_Object = QtWidgets.QFrame(self.frame_Shadow)
        self.frame_Object.setStyleSheet("QFrame{\n"
"border:0px;\n"
" background: none;\n"
"}z")
        self.frame_Object.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Object.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Object.setObjectName("frame_Object")
        self.pushButton_Login = QtWidgets.QPushButton(self.frame_Object)
        self.pushButton_Login.setGeometry(QtCore.QRect(160, 570, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Login.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    background-color: rgb(115, 176, 250);\n"
"    color:#fff;\n"
"    font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(105, 112, 255);\n"
"    border-radius: 15px;\n"
"    border:1px solid rgb(105, 112, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.lbl_NewUser = QtWidgets.QLabel(self.frame_Object)
        self.lbl_NewUser.setGeometry(QtCore.QRect(70, 510, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lbl_NewUser.setFont(font)
        self.lbl_NewUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbl_NewUser.setStyleSheet("QLabel{\n"
"    color:  rgb(115, 176, 250);\n"
"}\n"
"")
        self.lbl_NewUser.setObjectName("lbl_NewUser")
        self.lbl_UserLogin = QtWidgets.QLabel(self.frame_Object)
        self.lbl_UserLogin.setGeometry(QtCore.QRect(110, 300, 241, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_UserLogin.setFont(font)
        self.lbl_UserLogin.setStyleSheet("QLabel{\n"
"color:rgb(115, 176, 250);\n"
"font-size:23px;\n"
"}")
        self.lbl_UserLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_UserLogin.setObjectName("lbl_UserLogin")
        self.lineEdit_Login = QtWidgets.QLineEdit(self.frame_Object)
        self.lineEdit_Login.setGeometry(QtCore.QRect(60, 370, 341, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lineEdit_Login.setFont(font)
        self.lineEdit_Login.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(238, 238, 236);\n"
"    border-radius: 20px;\n"
"    padding: 15px;\n"
"    background-color: #fff;\n"
"    color: rgb(115, 176, 250);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(186, 189, 182);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid   rgb(114, 159, 207);\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.lineEdit_Login.setText("")
        self.lineEdit_Login.setObjectName("lineEdit_Login")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.frame_Object)
        self.lineEdit_Password.setGeometry(QtCore.QRect(60, 440, 341, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lineEdit_Password.setFont(font)
        self.lineEdit_Password.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(238, 238, 236);\n"
"    border-radius: 20px;\n"
"    padding: 15px;\n"
"    background-color: #fff;\n"
"    color: rgb(115, 176, 250);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(186, 189, 182);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid   rgb(114, 159, 207);\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.lineEdit_Password.setText("")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.frame_Logo = QtWidgets.QFrame(self.frame_Object)
        self.frame_Logo.setGeometry(QtCore.QRect(130, 70, 201, 211))
        self.frame_Logo.setStyleSheet("QFrame{\n"
"border:0px;\n"
" background: url(\":/logo/resource/logo.png\");\n"
"  background-repeat: no-repeat;\n"
" border-radius: 10px;\n"
"}\n"
"")
        self.frame_Logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Logo.setObjectName("frame_Logo")
        self.comboBox_department = QtWidgets.QComboBox(self.frame_Object)
        self.comboBox_department.setGeometry(QtCore.QRect(166, 510, 231, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_department.setFont(font)
        self.comboBox_department.setStyleSheet("QComboBox {\n"
"    border: 1px solid rgb(238, 238, 236);\n"
"    background-color: #fff;\n"
"    border-radius: 15px;   /* 圆角 */\n"
"    padding: 1px 18px 1px 3px;   /* 字体填衬 */\n"
"    color: rgb(115, 176, 250);\n"
"}\n"
"QComboBox:hover {\n"
"    border: 1px solid rgb(186, 189, 182);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 1px solid   rgb(114, 159, 207);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"/* 下拉箭头样式 */\n"
" QComboBox::down-arrow {\n"
"　　width: 15px; /* 下拉箭头的宽度 */ \n"
"　　background: transparent; /* 下拉箭头的的背景色 */ \n"
"　　padding: 0px 0px 0px 0px; /* 上内边距、右内边距、下内边距、左内边距 */\n"
"　　image: url(\":/downarrow/resource/down-arrow.png\");\n"
" } \n"
"")
        self.comboBox_department.setObjectName("comboBox_department")
        self.comboBox_department.addItem("")
        self.comboBox_department.addItem("")
        self.comboBox_department.addItem("")
        self.frame_TopBar = QtWidgets.QFrame(self.frame_Object)
        self.frame_TopBar.setGeometry(QtCore.QRect(0, 0, 456, 41))
        self.frame_TopBar.setMinimumSize(QtCore.QSize(456, 41))
        self.frame_TopBar.setMaximumSize(QtCore.QSize(456, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.frame_TopBar.setFont(font)
        self.frame_TopBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_TopBar.setStyleSheet("QFrame{\n"
"    background-color:rgb(208, 208, 208);\n"
"}")
        self.frame_TopBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TopBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_TopBar.setObjectName("frame_TopBar")
        self.pushButton_Exit = QtWidgets.QPushButton(self.frame_TopBar)
        self.pushButton_Exit.setGeometry(QtCore.QRect(410, 5, 41, 31))
        self.pushButton_Exit.setMinimumSize(QtCore.QSize(41, 0))
        self.pushButton_Exit.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Exit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_Exit.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    background-color:  rgb(115, 176, 250);\n"
"    color:rgb(255, 255, 255)/*rgb(91, 91, 91)*/;\n"
"    font-size:20px;\n"
"    text-align:center;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(105, 112, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_Exit.setText("×")
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.lbl_welcome = QtWidgets.QLabel(self.frame_TopBar)
        self.lbl_welcome.setGeometry(QtCore.QRect(20, 5, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lbl_welcome.setFont(font)
        self.lbl_welcome.setStyleSheet("QLabel{\n"
"\n"
"color:  rgb(255, 255, 255)/*rgb(115, 176, 250)*/;\n"
"\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(115, 176, 250);\n"
"}")
        self.lbl_welcome.setObjectName("lbl_welcome")
        self.verticalLayout.addWidget(self.frame_Object)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "医药进销存管理系统"))
        self.pushButton_Login.setText(_translate("MainWindow", "登录"))
        self.pushButton_Login.setShortcut(_translate("MainWindow", "Return"))
        self.lbl_NewUser.setText(_translate("MainWindow", "请选择部门："))
        self.lbl_UserLogin.setText(_translate("MainWindow", "医药进销存管理系统"))
        self.lineEdit_Login.setPlaceholderText(_translate("MainWindow", "账号"))
        self.lineEdit_Password.setPlaceholderText(_translate("MainWindow", "密码"))
        self.comboBox_department.setItemText(0, _translate("MainWindow", "销售部门"))
        self.comboBox_department.setItemText(1, _translate("MainWindow", "仓库部门"))
        self.comboBox_department.setItemText(2, _translate("MainWindow", "采购部门"))
        self.lbl_welcome.setText(_translate("MainWindow", "欢迎使用医药进销存管理系统"))
import main_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

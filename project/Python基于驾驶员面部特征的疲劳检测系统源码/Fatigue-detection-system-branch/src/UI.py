# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(274, 1, 20, 641))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(80, 50, 201, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Cam_Select = QtWidgets.QComboBox(self.centralwidget)
        self.Cam_Select.setGeometry(QtCore.QRect(10, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Cam_Select.setFont(font)
        self.Cam_Select.setObjectName("Cam_Select")
        self.Cam_Select.addItem("")
        self.Cam_Select.addItem("")
        self.Cam_Select.addItem("")
        self.Button_OpenVideo = QtWidgets.QPushButton(self.centralwidget)
        self.Button_OpenVideo.setGeometry(QtCore.QRect(150, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Button_OpenVideo.setFont(font)
        self.Button_OpenVideo.setObjectName("Button_OpenVideo")
        self.Button_Start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Start.setGeometry(QtCore.QRect(150, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Button_Start.setFont(font)
        self.Button_Start.setObjectName("Button_Start")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 30, 271, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 71, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.offDuty_Check = QtWidgets.QCheckBox(self.centralwidget)
        self.offDuty_Check.setGeometry(QtCore.QRect(10, 220, 87, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.offDuty_Check.setFont(font)
        self.offDuty_Check.setObjectName("offDuty_Check")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.offDuty_Time = QtWidgets.QSpinBox(self.centralwidget)
        self.offDuty_Time.setGeometry(QtCore.QRect(210, 220, 46, 31))
        self.offDuty_Time.setObjectName("offDuty_Time")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(80, 200, 201, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 300, 71, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.output_Window = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_Window.setGeometry(QtCore.QRect(11, 331, 261, 301))
        self.output_Window.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 119));")
        self.output_Window.setObjectName("output_Window")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(300, 50, 730, 550))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(80, 300, 201, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.Button_End = QtWidgets.QPushButton(self.centralwidget)
        self.Button_End.setGeometry(QtCore.QRect(150, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Button_End.setFont(font)
        self.Button_End.setObjectName("Button_End")
        self.Button_AdjustCamera_Location = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AdjustCamera_Location.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Button_AdjustCamera_Location.setFont(font)
        self.Button_AdjustCamera_Location.setObjectName("Button_AdjustCamera_Location")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 160, 141, 31))
        self.widget.setObjectName("widget")
        self.video = QtWidgets.QCheckBox(self.widget)
        self.video.setGeometry(QtCore.QRect(10, 0, 87, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.video.setFont(font)
        self.video.setChecked(False)
        self.video.setAutoExclusive(True)
        self.video.setObjectName("video")
        self.cam = QtWidgets.QCheckBox(self.widget)
        self.cam.setGeometry(QtCore.QRect(70, 0, 87, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.cam.setFont(font)
        self.cam.setChecked(True)
        self.cam.setAutoExclusive(True)
        self.cam.setObjectName("cam")
        self.show_key_point = QtWidgets.QCheckBox(self.centralwidget)
        self.show_key_point.setGeometry(QtCore.QRect(10, 270, 87, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.show_key_point.setFont(font)
        self.show_key_point.setObjectName("show_key_point")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(80, 250, 201, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 71, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.show_head = QtWidgets.QCheckBox(self.centralwidget)
        self.show_head.setGeometry(QtCore.QRect(220, 270, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.show_head.setFont(font)
        self.show_head.setObjectName("show_head")
        self.show_eye = QtWidgets.QCheckBox(self.centralwidget)
        self.show_eye.setGeometry(QtCore.QRect(90, 270, 51, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.show_eye.setFont(font)
        self.show_eye.setObjectName("show_eye")
        self.show_eye.setChecked(True)
        self.show_mouth = QtWidgets.QCheckBox(self.centralwidget)
        self.show_mouth.setGeometry(QtCore.QRect(160, 270, 51, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.show_mouth.setFont(font)
        self.show_mouth.setObjectName("show_mouth")
        self.show_mouth.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "参数设置"))
        self.label_2.setText(_translate("MainWindow", "视频设置"))
        self.Cam_Select.setItemText(0, _translate("MainWindow", "摄像头1"))
        self.Cam_Select.setItemText(1, _translate("MainWindow", "摄像头2"))
        self.Cam_Select.setItemText(2, _translate("MainWindow", "摄像头3"))
        self.Button_OpenVideo.setText(_translate("MainWindow", "打开视频文件"))
        self.Button_Start.setText(_translate("MainWindow", "开始"))
        self.label_5.setText(_translate("MainWindow", "脱岗检测"))
        self.offDuty_Check.setText(_translate("MainWindow", "脱岗检测"))
        self.label_6.setText(_translate("MainWindow", "脱离时间(s)："))
        self.label_9.setText(_translate("MainWindow", "状态输出"))
        self.Button_End.setText(_translate("MainWindow", "结束"))
        self.Button_AdjustCamera_Location.setText(_translate("MainWindow", "调整摄像头位置"))
        self.video.setText(_translate("MainWindow", "视频"))
        self.cam.setText(_translate("MainWindow", "摄像头"))
        self.show_key_point.setText(_translate("MainWindow", "关键点"))
        self.label_8.setText(_translate("MainWindow", "显示设置"))
        self.show_head.setText(_translate("MainWindow", "头部"))
        self.show_eye.setText(_translate("MainWindow", "眼睛"))
        self.show_mouth.setText(_translate("MainWindow", "嘴巴"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

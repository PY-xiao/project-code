# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'novel.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(671, 533)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setGeometry(QtCore.QRect(550, 20, 111, 41))
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(Form)
        self.button2.setGeometry(QtCore.QRect(550, 70, 111, 91))
        self.button2.setObjectName("button2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 21, 87, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 421, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.previous = QtWidgets.QPushButton(Form)
        self.previous.setGeometry(QtCore.QRect(540, 320, 93, 28))
        self.previous.setObjectName("previous")
        self.next = QtWidgets.QPushButton(Form)
        self.next.setGeometry(QtCore.QRect(540, 380, 93, 28))
        self.next.setObjectName("next")
        self.Page = QtWidgets.QLabel(Form)
        self.Page.setGeometry(QtCore.QRect(550, 440, 101, 16))
        self.Page.setText("")
        self.Page.setObjectName("Page")
        self.content = QtWidgets.QTableWidget(Form)
        self.content.setGeometry(QtCore.QRect(10, 60, 511, 441))
        self.content.setRowCount(30)
        self.content.setObjectName("content")
        self.content.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.content.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.content.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.content.setHorizontalHeaderItem(2, item)
        self.refresh = QtWidgets.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(540, 350, 93, 28))
        self.refresh.setObjectName("refresh")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(550, 170, 111, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "小说下载器"))
        self.button1.setText(_translate("Form", "搜索"))
        self.button2.setText(_translate("Form", "下载"))
        self.comboBox.setItemText(0, _translate("Form", "笔趣阁"))
        self.comboBox.setItemText(1, _translate("Form", "69书屋"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入书名"))
        self.previous.setText(_translate("Form", "上一页"))
        self.next.setText(_translate("Form", "下一页"))
        item = self.content.horizontalHeaderItem(0)
        item.setText(_translate("Form", "书名"))
        item = self.content.horizontalHeaderItem(1)
        item.setText(_translate("Form", "作者"))
        item = self.content.horizontalHeaderItem(2)
        item.setText(_translate("Form", "链接"))
        self.refresh.setText(_translate("Form", "刷新"))
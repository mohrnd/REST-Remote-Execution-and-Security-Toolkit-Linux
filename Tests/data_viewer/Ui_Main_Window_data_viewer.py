# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\data_viewer\Main_Window_data_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 886)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TableWidget = TableWidget(self.centralwidget)
        self.TableWidget.setGeometry(QtCore.QRect(10, 30, 371, 191))
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setColumnCount(1)
        self.TableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, item)
        self.TableWidget_2 = TableWidget(self.centralwidget)
        self.TableWidget_2.setGeometry(QtCore.QRect(390, 30, 411, 191))
        self.TableWidget_2.setObjectName("TableWidget_2")
        self.TableWidget_2.setColumnCount(1)
        self.TableWidget_2.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget_2.setHorizontalHeaderItem(0, item)
        self.customframe_2 = QtWidgets.QFrame(self.centralwidget)
        self.customframe_2.setGeometry(QtCore.QRect(10, 310, 791, 531))
        self.customframe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.customframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.customframe_2.setObjectName("customframe_2")
        self.TicksForm = LineEdit(self.centralwidget)
        self.TicksForm.setGeometry(QtCore.QRect(400, 230, 71, 33))
        self.TicksForm.setObjectName("TicksForm")
        self.SubtitleLabel = SubtitleLabel(self.centralwidget)
        self.SubtitleLabel.setGeometry(QtCore.QRect(10, 0, 241, 28))
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        # self.TimePicker_4 = TimePicker(self.centralwidget)
        # self.TimePicker_4.setGeometry(QtCore.QRect(140, 230, 240, 30))
        # self.TimePicker_4.setObjectName("TimePicker_4")
        # self.TimePicker_3 = TimePicker(self.centralwidget)
        # self.TimePicker_3.setGeometry(QtCore.QRect(140, 270, 240, 30))
        # self.TimePicker_3.setObjectName("TimePicker_3")
        self.EndDate = CalendarPicker(self.centralwidget)
        self.EndDate.setGeometry(QtCore.QRect(10, 270, 112, 32))
        self.EndDate.setObjectName("EndDate")
        self.StartDate = CalendarPicker(self.centralwidget)
        self.StartDate.setGeometry(QtCore.QRect(10, 230, 112, 32))
        self.StartDate.setObjectName("StartDate")
        self.PlotButton = PrimaryPushButton(self.centralwidget)
        self.PlotButton.setGeometry(QtCore.QRect(400, 270, 71, 32))
        self.PlotButton.setObjectName("PlotButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 21))
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
        item = self.TableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "CPU cores"))
        item = self.TableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Total Ram"))
        item = self.TableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total Disk"))
        item = self.TableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Network cards"))
        item = self.TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sytem data"))
        self.TableWidget.setColumnWidth(0,305)
        item = self.TableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Uptime"))
        item = self.TableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cpu usage"))
        item = self.TableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ram usage"))
        item = self.TableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Disk usage"))
        item = self.TableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Network Up"))
        item = self.TableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Network Down"))
        item = self.TableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Current system data"))
        self.TableWidget_2.setColumnWidth(0,315)
        self.TicksForm.setPlaceholderText(_translate("MainWindow", "Ticks"))
        self.SubtitleLabel.setText(_translate("MainWindow", "Machine name: Null"))
        self.EndDate.setText(_translate("MainWindow", "End Date"))
        self.StartDate.setText(_translate("MainWindow", "Start Date"))
        self.PlotButton.setText(_translate("MainWindow", "Plot"))
from qfluentwidgets import CalendarPicker, LineEdit, PrimaryPushButton, SubtitleLabel, TableWidget, TimePicker

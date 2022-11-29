# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
import resource
dir_path = os.path.dirname(os.path.abspath(__file__))
dir_path = os.path.dirname(os.path.dirname(os.path.dirname(dir_path)))
# print(dir_path)
sys.path.append(dir_path)
from require.GUI.GUI_for_saprate_window.TransportHandshake import *
from require.GUI.GUI_for_saprate_window.Create_Subscribe import *
from require.GUI.GUI_for_saprate_window.Supervision_Connection import *
from require.GUI.GUI_for_saprate_window.Fault_Mgmt import *
from require.GUI.GUI_for_saprate_window.SW_Mgmt import *
from require.GUI.GUI_for_saprate_window.Access_Control import *
from require.GUI.GUI_for_saprate_window.RU_Configurability import *
from require.GUI.GUI_for_saprate_window.Log_Mgmt import *
from require.GUI.GUI_for_saprate_window.RU_Info import Ui_RU_Information


class Main_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        print(self.centralwidget.geometry())
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HomeScreen = QtWidgets.QWidget(self.centralwidget)
        self.HomeScreen.setStyleSheet("*{\n"
        "    background: transparent;\n"
        "    color: rgb(211, 215, 207);\n"
        "    border: 1px solid}\n"
        "#HomeScreen{\n"
        "    background-color: #020912;\n"
        "}\n"
        "QPushButton{\n"
        "    background-color: #293340;\n"
        "    border-radius: 5px\n"
        "}\n"
        "")
        self.HomeScreen.setObjectName("HomeScreen")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.HomeScreen)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Status_Bar = QtWidgets.QFrame(self.HomeScreen)
        self.Status_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Status_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Status_Bar.setObjectName("Status_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Status_Bar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.build_name_label = QtWidgets.QLabel(self.Status_Bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.build_name_label.sizePolicy().hasHeightForWidth())
        self.build_name_label.setSizePolicy(sizePolicy)
        self.build_name_label.setObjectName("build_name_label")
        self.horizontalLayout.addWidget(self.build_name_label)
        self.max_min_frame = QtWidgets.QFrame(self.Status_Bar)
        self.max_min_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.max_min_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.max_min_frame.setObjectName("max_min_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.max_min_frame)
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minimizwe = QtWidgets.QPushButton(self.max_min_frame)
        self.minimizwe.setStyleSheet("color: rgb(255, 255, 255);")
        self.minimizwe.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizwe.setIcon(icon)
        self.minimizwe.setObjectName("minimizwe")
        self.horizontalLayout_3.addWidget(self.minimizwe)
        self.maximize = QtWidgets.QPushButton(self.max_min_frame)
        self.maximize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize.setIcon(icon1)
        self.maximize.setObjectName("maximize")
        self.horizontalLayout_3.addWidget(self.maximize)
        self.quit = QtWidgets.QPushButton(self.max_min_frame)
        self.quit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit.setIcon(icon2)
        self.quit.setObjectName("quit")
        self.horizontalLayout_3.addWidget(self.quit)
        self.horizontalLayout.addWidget(self.max_min_frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.Status_Bar, 0, QtCore.Qt.AlignTop)
        self.widget = QtWidgets.QWidget(self.HomeScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sideMenu_Frame = QtWidgets.QFrame(self.widget)
        self.sideMenu_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideMenu_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideMenu_Frame.setObjectName("sideMenu_Frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.sideMenu_Frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menu = QtWidgets.QPushButton(self.sideMenu_Frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu.setIcon(icon3)
        self.menu.setObjectName("menu")
        self.verticalLayout_3.addWidget(self.menu)
        self.configuration = QtWidgets.QPushButton(self.sideMenu_Frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.configuration.setIcon(icon4)
        self.configuration.setObjectName("configuration")
        self.verticalLayout_3.addWidget(self.configuration)
        self.report = QtWidgets.QPushButton(self.sideMenu_Frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/download-cloud.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.report.setIcon(icon5)
        self.report.setObjectName("report")
        self.verticalLayout_3.addWidget(self.report)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.help = QtWidgets.QPushButton(self.sideMenu_Frame)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon6)
        self.help.setObjectName("help")
        self.verticalLayout_3.addWidget(self.help)
        self.horizontalLayout_2.addWidget(self.sideMenu_Frame, 0, QtCore.Qt.AlignLeft)
        self.centerScreen_frame = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerScreen_frame.sizePolicy().hasHeightForWidth())
        self.centerScreen_frame.setSizePolicy(sizePolicy)
        self.centerScreen_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.centerScreen_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.centerScreen_frame.setObjectName("centerScreen_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centerScreen_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centerScreen_frame)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("M Plane Conformance Test Cases")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.TestCaseFrame = QtWidgets.QFrame(self.centerScreen_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TestCaseFrame.sizePolicy().hasHeightForWidth())
        self.TestCaseFrame.setSizePolicy(sizePolicy)
        self.TestCaseFrame.setMinimumSize(QtCore.QSize(600, 0))
        self.TestCaseFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.TestCaseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TestCaseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TestCaseFrame.setObjectName("TestCaseFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.TestCaseFrame)
        self.gridLayout.setObjectName("gridLayout")
        ################################################################################
        ## Place Holders and class name in dictionary 
        ################################################################################
        self.placeholder = {'Transport and HandShake' : self.TransportHandshake,
                        'Subscription to Notifications' : self.Create_Subscribe,
                        'M-Plane connection supervision' : self.Supervision,
                        'Retrieval of O-RU\'s information elements' : self.RU_Information,
                        'Fault Management' : self.Fault_Mgmt,
                        'O-RU Software Update' : self.SW_Mgmt,
                        'Access Control' : self.Access_Control,
                        'O-RU Configurability' : self.RU_Config,
                        'Log Management' : self.Log_Mgmt}
        ################################################################################
        ## pushButton Function and class name in dictionary
        ################################################################################
        iter = 1
        self.testCaseButtons = {}
        for key,val in self.placeholder.items():
            self.pushbutton = QtWidgets.QPushButton(self.TestCaseFrame)
            self.pushbutton.setText(key)
            self.testCaseButtons[self.pushbutton] = val
            self.gridLayout.addWidget(self.pushbutton, iter, 0, 1, 1)
            self.pushbutton.clicked.connect(val)
            iter+=1
        self.ald_cumm = QtWidgets.QPushButton(self.TestCaseFrame)
        self.ald_cumm.setText('ALD Communications')
        self.gridLayout.addWidget(self.ald_cumm, iter+1, 0, 1, 1)
        # print(self.testCaseButtons)
        self.run_all = QtWidgets.QPushButton(self.TestCaseFrame)
        self.run_all.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.504739, cy:0.506, radius:1.97128, fx:0.5, fy:0.5, stop:0.18408 rgba(1, 47, 8, 255), stop:1 rgba(236, 233, 255, 255));")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run_all.setIcon(icon7)
        self.run_all.setText('Run All')
        self.gridLayout.addWidget(self.run_all, iter+2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.TestCaseFrame, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.centerScreen_frame)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout.addWidget(self.HomeScreen)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "O-RAN Test Automation Suit"))
        self.build_name_label.setText(_translate("MainWindow", "Sofware Name"))
        self.menu.setText(_translate("MainWindow", "Menu"))
        self.configuration.setText(_translate("MainWindow", "Configuration"))
        self.report.setText(_translate("MainWindow", "Report"))
        self.help.setText(_translate("MainWindow", "Help"))


    def TransportHandshake(self):
        self.window = QtWidgets.QMainWindow()
        self.testCaseUI = Ui_TransportHandshake()
        self.window.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.testCaseUI.setupUi(self.window)
        self.window.showMaximized()
    
    def Create_Subscribe(self):
        self.window = QtWidgets.QMainWindow()
        self.testCaseUI = Ui_Create_Subscribe()
        self.window.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.testCaseUI.setupUi(self.window)
        self.window.showMaximized()
    
    def Supervision(self):
        self.window = QtWidgets.QMainWindow()
        self.testCaseUI = Ui_Supervision()
        self.window.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.testCaseUI.setupUi(self.window)
        self.window.showMaximized()

    def RU_Information(self):
        self.window = QtWidgets.QMainWindow()
        self.testCaseUI = Ui_RU_Information()
        self.window.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.testCaseUI.setupUi(self.window)
        self.window.showMaximized()

    def Fault_Mgmt(self):
        self.window = QtWidgets.QMainWindow()
        self.testCaseUI = Ui_Fault_Mgmt()
        self.window.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.testCaseUI.setupUi(self.window)
        self.window.showMaximized()
    
    def SW_Mgmt(self):
        self.window = QtWidgets.QMainWindow()
        self.testCaseUI = Ui_SW_Mgmt()
        self.window.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.testCaseUI.setupUi(self.window)
        self.window.showMaximized()

    def Access_Control(self):
        self.window = QtWidgets.QMainWindow()
        self.testCaseUI = Ui_Access_Control()
        self.window.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.testCaseUI.setupUi(self.window)
        self.window.showMaximized()

    def RU_Config(self):
        self.window = QtWidgets.QMainWindow()
        self.testCaseUI = Ui_RU_Config()
        self.window.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.testCaseUI.setupUi(self.window)
        self.window.showMaximized()

    def Log_Mgmt(self):
        self.window = QtWidgets.QMainWindow()
        self.testCaseUI = Ui_Log_Mgmt()
        self.window.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.testCaseUI.setupUi(self.window)
        self.window.showMaximized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main_UI()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
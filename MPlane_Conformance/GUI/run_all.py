# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'run_all.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resource


class Ui_Run_ALL(object):
    def setupUi(self, run_all_tc):
        run_all_tc.setObjectName("run_all_tc")
        run_all_tc.resize(638, 544)
        self.centralwidget = QtWidgets.QWidget(run_all_tc)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("*{\n"
"    border:1px solid;\n"
"}\n"
"#centralwidget{\n"
"    background-color: #edeef0;"
"}\n"
"""#test_case_frame{
    min-width:300px;
    background-color: qlineargradient(spread:pad, x1:0.488, y1:0.0397727, x2:0.522388, y2:1, stop:0 rgba(3, 96, 109, 255), stop:1 rgba(173, 160, 255, 255));
}
"""
# "#OutputFrame, #InputFrame{\n"
# "    background-color: #16191d;\n"
# "    color: rgb(211, 215, 207);"
# "}\n"
"""QLabel{
	background-color: qlineargradient(spread:pad, x1:0.483025, y1:0.256, x2:0.522388, y2:1, stop:0 rgba(4, 108, 124, 255), stop:1 rgba(165, 156, 191, 255));
}"""
"""QCheckBox{
    border:none;
}"""
"QLineEdit, QComboBox{background-color: rgba(0,0,0,0);\n"
"    border:none;\n"
"    border-bottom:2px solid rgba(46,82,101,200);\n"
"    color: blue;\n"
"    padding-bottom:7px;\n"
"}\n"
"""QListView
{
background-color : #edeef0;
}"""
"""
QFrame{
    border:none;
}
#InputFrame, #OutputFrame{
    background-color: white;
}
QPushButton{
	background-color: qlineargradient(spread:pad, x1:0.488, y1:0.0397727, x2:0.522388, y2:1, stop:0 rgba(3, 96, 109, 255), stop:1 rgba(173, 160, 255, 255));
    border:none;
    border-radius:4px;
    width:100px;
    height:25px;
}
QPushButton:hover{
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.512438 rgba(20, 113, 60, 255), stop:1 rgba(0, 0, 0, 255));
}
QLineEdit[text=\"\"], QComboBox[text=\"\"]{
        color:blue;
}
QPlainTextEdit{
        border: 2px dashed;
        background-color: #edeef0;
        color:black;
}
"""
)
        
        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.test_case_frame = QtWidgets.QFrame(self.centralwidget)
        self.test_case_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test_case_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test_case_frame.setObjectName("test_case_frame")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.test_case_frame)
        self.verticalLayout1.setObjectName("verticalLayout")


        self.M_CTC_ID_001 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_001.setObjectName("M_CTC_ID_001")
        self.M_CTC_ID_001.setText('M_CTC_ID_001')
        self.verticalLayout1.addWidget(self.M_CTC_ID_001)

        self.M_CTC_ID_002 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_002.setObjectName("M_CTC_ID_002")
        self.M_CTC_ID_002.setText('M_CTC_ID_002')
        self.verticalLayout1.addWidget(self.M_CTC_ID_002)

        self.M_CTC_ID_003 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_003.setObjectName("M_CTC_ID_003")
        self.M_CTC_ID_003.setText('M_CTC_ID_003')
        self.verticalLayout1.addWidget(self.M_CTC_ID_003)

        self.M_CTC_ID_007 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_007.setObjectName("M_CTC_ID_007")
        self.M_CTC_ID_007.setText('M_CTC_ID_007')
        self.verticalLayout1.addWidget(self.M_CTC_ID_007)

        self.M_CTC_ID_008 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_008.setObjectName("M_CTC_ID_008")
        self.M_CTC_ID_008.setText('M_CTC_ID_008')
        self.verticalLayout1.addWidget(self.M_CTC_ID_008)

        self.M_CTC_ID_009 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_009.setObjectName("M_CTC_ID_009")
        self.M_CTC_ID_009.setText('M_CTC_ID_009')
        self.verticalLayout1.addWidget(self.M_CTC_ID_009)

        self.M_CTC_ID_010 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_010.setObjectName("M_CTC_ID_010")
        self.M_CTC_ID_010.setText('M_CTC_ID_010')
        self.verticalLayout1.addWidget(self.M_CTC_ID_010)

        self.M_CTC_ID_011 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_011.setObjectName("M_CTC_ID_011")
        self.M_CTC_ID_011.setText('M_CTC_ID_011')
        self.verticalLayout1.addWidget(self.M_CTC_ID_011)

        self.M_CTC_ID_012 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_012.setObjectName("M_CTC_ID_012")
        self.M_CTC_ID_012.setText('M_CTC_ID_012')
        self.verticalLayout1.addWidget(self.M_CTC_ID_012)

        self.M_CTC_ID_013 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_013.setObjectName("M_CTC_ID_013")
        self.M_CTC_ID_013.setText('M_CTC_ID_013')
        self.verticalLayout1.addWidget(self.M_CTC_ID_013)

        self.M_CTC_ID_014 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_014.setObjectName("M_CTC_ID_014")
        self.M_CTC_ID_014.setText('M_CTC_ID_014')
        self.verticalLayout1.addWidget(self.M_CTC_ID_014)
        
        self.M_CTC_ID_015 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_015.setObjectName("M_CTC_ID_015")
        self.M_CTC_ID_015.setText('M_CTC_ID_015')
        self.verticalLayout1.addWidget(self.M_CTC_ID_015)

        self.M_CTC_ID_016 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_016.setObjectName("M_CTC_ID_016")
        self.M_CTC_ID_016.setText('M_CTC_ID_016')
        self.verticalLayout1.addWidget(self.M_CTC_ID_016)

        self.M_CTC_ID_017 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_017.setObjectName("M_CTC_ID_017")
        self.M_CTC_ID_017.setText('M_CTC_ID_017')
        self.verticalLayout1.addWidget(self.M_CTC_ID_017)

        self.M_CTC_ID_018 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_018.setObjectName("M_CTC_ID_018")
        self.M_CTC_ID_018.setText('M_CTC_ID_018')
        self.verticalLayout1.addWidget(self.M_CTC_ID_018)

        self.M_CTC_ID_019 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_019.setObjectName("M_CTC_ID_019")
        self.M_CTC_ID_019.setText('M_CTC_ID_019')
        self.verticalLayout1.addWidget(self.M_CTC_ID_019)

        self.M_CTC_ID_020 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_020.setObjectName("M_CTC_ID_020")
        self.M_CTC_ID_020.setText('M_CTC_ID_020')
        self.verticalLayout1.addWidget(self.M_CTC_ID_020)

        self.M_CTC_ID_021 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_021.setObjectName("M_CTC_ID_021")
        self.M_CTC_ID_021.setText('M_CTC_ID_021')
        self.verticalLayout1.addWidget(self.M_CTC_ID_021)

        self.M_CTC_ID_022 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_022.setObjectName("M_CTC_ID_022")
        self.M_CTC_ID_022.setText('M_CTC_ID_022')
        self.verticalLayout1.addWidget(self.M_CTC_ID_022)

        self.M_CTC_ID_023 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_023.setObjectName("M_CTC_ID_023")
        self.M_CTC_ID_023.setText('M_CTC_ID_023')
        self.verticalLayout1.addWidget(self.M_CTC_ID_023)

        self.M_CTC_ID_026 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_026.setObjectName("M_CTC_ID_026")
        self.M_CTC_ID_026.setText('M_CTC_ID_026')
        self.verticalLayout1.addWidget(self.M_CTC_ID_026)

        self.M_CTC_ID_027 = QtWidgets.QCheckBox(self.test_case_frame)
        self.M_CTC_ID_027.setObjectName("M_CTC_ID_027")
        self.M_CTC_ID_027.setText('M_CTC_ID_027')
        self.verticalLayout1.addWidget(self.M_CTC_ID_027)
        self.checkboxes = [self.M_CTC_ID_001,self.M_CTC_ID_002, self.M_CTC_ID_003,self.M_CTC_ID_011, 
                    self.M_CTC_ID_012, self.M_CTC_ID_013, self.M_CTC_ID_015, self.M_CTC_ID_014, self.M_CTC_ID_016,
                    self.M_CTC_ID_017, self.M_CTC_ID_018, self.M_CTC_ID_019, self.M_CTC_ID_020, self.M_CTC_ID_021, self.M_CTC_ID_022,
                    self.M_CTC_ID_023,self.M_CTC_ID_026, self.M_CTC_ID_027, self.M_CTC_ID_010, self.M_CTC_ID_007, self.M_CTC_ID_008,
                    self.M_CTC_ID_009, ]
        self.select_all = QtWidgets.QCheckBox(self.test_case_frame)
        self.select_all.setObjectName("select_all")
        self.select_all.setText('select_all')
        self.select_all.stateChanged.connect(self.checked_all)
        self.verticalLayout1.addWidget(self.select_all)

        self.horizontalLayout1.addWidget(self.test_case_frame, 0, QtCore.Qt.AlignLeft)

        self.Execution_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Execution_frame.sizePolicy().hasHeightForWidth())
        self.Execution_frame.setSizePolicy(sizePolicy)
        self.Execution_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Execution_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Execution_frame.setObjectName("frame")
        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.Execution_frame)
        self.verticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.newWindow = QtWidgets.QWidget(self.Execution_frame)
        self.newWindow.setObjectName("newWindow")
        self.verticalLayout = QtWidgets.QGridLayout(self.newWindow)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.InputFrame = QtWidgets.QFrame(self.newWindow)
        self.InputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InputFrame.setObjectName("InputFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.InputFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.InputLabel = QtWidgets.QLabel(self.InputFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.InputLabel.setFont(font)
        self.InputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InputLabel.setObjectName("InputLabel")
        self.verticalLayout_3.addWidget(self.InputLabel)
        self.input_frame = QtWidgets.QFrame(self.InputFrame)
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.input_frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_01 = QtWidgets.QLineEdit(self.input_frame)
        self.input_01.setObjectName("input_01")
        self.gridLayout_2.addWidget(self.input_01, 0, 0, 1, 1)
        self.input_02 = QtWidgets.QLineEdit(self.input_frame)
        self.input_02.setObjectName("input_02")
        self.gridLayout_2.addWidget(self.input_02, 0, 1, 1, 1)
        self.input_03 = QtWidgets.QLineEdit(self.input_frame)
        self.input_03.setObjectName("input_03")
        self.gridLayout_2.addWidget(self.input_03, 0, 2, 1, 1)
        self.input_04 = QtWidgets.QLineEdit(self.input_frame)
        self.input_04.setObjectName("input_04")
        self.gridLayout_2.addWidget(self.input_04, 0, 3, 1, 1)
        self.input_05 = QtWidgets.QLineEdit(self.input_frame)
        self.input_05.setObjectName("input_05")
        self.gridLayout_2.addWidget(self.input_05, 0, 4, 1, 1)
        self.input_06 = QtWidgets.QLineEdit(self.input_frame)
        self.input_06.setObjectName("input_06")
        self.gridLayout_2.addWidget(self.input_06, 0, 5, 1, 1)
        self.input_07 = QtWidgets.QLineEdit(self.input_frame)
        self.input_07.setObjectName("input_07")
        self.gridLayout_2.addWidget(self.input_07, 0, 6, 1, 1)
        self.input_08 = QtWidgets.QComboBox(self.input_frame)
        bandwidths = ['PTP & SYNCE Port..','1','2']
        self.input_08.addItems(bandwidths)
        self.gridLayout_2.addWidget(self.input_08, 1, 0, 1, 1)
        self.input_09 = QtWidgets.QLineEdit(self.input_frame)
        self.input_09.setObjectName("input_09")
        self.gridLayout_2.addWidget(self.input_09, 1, 1, 1, 1)
        self.input_10 = QtWidgets.QComboBox(self.input_frame)
        bandwidths = ['Bandwidths..','10','20','30','40','80','100']
        self.input_10.addItems(bandwidths)
        self.gridLayout_2.addWidget(self.input_10, 1, 2, 1, 1)
        self.input_11 = QtWidgets.QLineEdit(self.input_frame)
        self.input_11.setObjectName("input_11")
        self.gridLayout_2.addWidget(self.input_11, 1, 3, 1, 1)
        self.input_12 = QtWidgets.QLineEdit(self.input_frame)
        self.input_12.setObjectName("input_12")
        self.gridLayout_2.addWidget(self.input_12, 1, 4, 1, 1)
        self.input_13 = QtWidgets.QLineEdit(self.input_frame)
        self.input_13.setObjectName("input_13")
        self.gridLayout_2.addWidget(self.input_13, 1, 5, 1, 1)
        self.input_14 = QtWidgets.QLineEdit(self.input_frame)
        self.input_14.setObjectName("input_14")
        self.gridLayout_2.addWidget(self.input_14, 1, 6, 1, 1)
        self.input_16 = QtWidgets.QComboBox(self.input_frame)
        duplex_list = ['Duplex Type..','TDD','FDD']
        self.input_16.addItems(duplex_list)
        self.gridLayout_2.addWidget(self.input_16, 2, 0, 1, 1)
        self.input_19 = QtWidgets.QComboBox(self.input_frame)
        scs_value = ['SCS Value..','KHZ_15', 'KHZ_30', 'KHZ_60', 'KHZ_120', 'KHZ_240']
        self.input_19.addItems(scs_value)
        self.gridLayout_2.addWidget(self.input_19, 2, 1, 1, 1)
        self.input_20 = QtWidgets.QLineEdit(self.input_frame)
        self.input_20.setObjectName("input_20")
        self.input_20.setPlaceholderText('SFTP Username')
        self.gridLayout_2.addWidget(self.input_20, 2, 2, 1, 1)
        self.input_15 = QtWidgets.QLineEdit(self.input_frame)
        self.input_15.setObjectName("input_15")
        self.gridLayout_2.addWidget(self.input_15, 2, 3, 1, 1)
        self.input_17 = QtWidgets.QLineEdit(self.input_frame)
        self.input_17.setObjectName("input_17")
        self.gridLayout_2.addWidget(self.input_17, 2, 4, 1, 1)
        self.input_18 = QtWidgets.QLineEdit(self.input_frame)
        self.input_18.setObjectName("input_17")
        self.gridLayout_2.addWidget(self.input_18, 2, 5, 1, 1)
        self.verticalLayout_3.addWidget(self.input_frame)
        self.buttons = QtWidgets.QFrame(self.InputFrame)
        self.buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submitBtn = QtWidgets.QPushButton(self.buttons)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/zap.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submitBtn.setIcon(icon)
        self.submitBtn.setObjectName("submitBtn")
        # self.submitBtn.clicked.connect(self.checked_mul)
        self.horizontalLayout.setContentsMargins(2,2,2,2)
        self.horizontalLayout.addWidget(self.submitBtn, 0, QtCore.Qt.AlignRight)
        self.runBtn = QtWidgets.QPushButton(self.buttons)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runBtn.setIcon(icon)
        self.runBtn.setObjectName("runBtn")
        self.runBtn.setContentsMargins(1,1,1,1)
        self.runBtn.setText('RUN')
        # self.submitBtn.clicked.connect(self.checked_mul)
        self.horizontalLayout.setContentsMargins(2,2,2,2)
        self.horizontalLayout.addWidget(self.runBtn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.buttons)
        self.verticalLayout.addWidget(self.InputFrame)
        self.OutputFrame = QtWidgets.QFrame(self.newWindow)
        self.OutputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OutputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OutputFrame.setObjectName("OutputFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.OutputFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.outputLabel = QtWidgets.QLabel(self.OutputFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.outputLabel.setFont(font)
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout_2.addWidget(self.outputLabel, 0, QtCore.Qt.AlignTop)
        self.consoleEdit = QtWidgets.QPlainTextEdit(self.OutputFrame)
        self.consoleEdit.setObjectName("consoleEdit")
        self.verticalLayout_2.addWidget(self.consoleEdit)
        self.verticalLayout.addWidget(self.OutputFrame)
        self.verticalLayout2.addWidget(self.newWindow)
        self.horizontalLayout1.addWidget(self.Execution_frame)
        run_all_tc.setCentralWidget(self.centralwidget)

        self.retranslateUi(run_all_tc)
        QtCore.QMetaObject.connectSlotsByName(run_all_tc)

    def retranslateUi(self, run_all_tc):
        _translate = QtCore.QCoreApplication.translate
        run_all_tc.setWindowTitle(_translate("run_all_tc", "O-RAN Test Automation Suit: Execute Multiple Test Case"))
        self.InputLabel.setText(_translate("run_all_tc", "Test Cases and User Input"))
        self.input_02.setPlaceholderText(_translate("run_all_tc", "Sudo Password"))
        self.input_11.setPlaceholderText(_translate("run_all_tc", "TX Arfcn"))
        self.input_03.setPlaceholderText(_translate("run_all_tc", "NMS Username"))
        self.input_06.setPlaceholderText(_translate("run_all_tc", "fm-pm password"))
        self.input_01.setPlaceholderText(_translate("run_all_tc", "Sudo Username"))
        self.input_04.setPlaceholderText(_translate("run_all_tc", "NMS Password"))
        self.input_05.setPlaceholderText(_translate("run_all_tc", "fm-pm username"))
        self.input_09.setPlaceholderText(_translate("run_all_tc", "RU Fronthaul Interface Name"))
        self.input_12.setPlaceholderText(_translate("run_all_tc", "RX Arfcn"))
        self.input_07.setPlaceholderText(_translate("run_all_tc", "Paragon IP"))
        self.input_08.setPlaceholderText(_translate("run_all_tc", "PTP & SYNCE Port"))
        self.input_13.setPlaceholderText(_translate("run_all_tc", "{Eg:3.6[GHz]}TX Center Freq."))
        self.input_14.setPlaceholderText(_translate("run_all_tc", "{Eg:3.6[GHz]}RX Center Freq."))
        self.input_15.setPlaceholderText(_translate("run_all_tc", "SFTP Password"))
        # self.input_16.setPlaceholderText(_translate("run_all_tc", "Duplex Scheme"))
        self.input_17.setPlaceholderText(_translate("run_all_tc", "Software FIle Path"))
        self.input_18.setPlaceholderText(_translate("run_all_tc", "Currupt FIle Path"))
        self.submitBtn.setText(_translate("run_all_tc", "Submit"))
        self.outputLabel.setText(_translate("run_all_tc", "Output"))

    def checked_all(self,state):
        self.data = []
        for check in self.checkboxes:
            if state:
                self.data.append(check.text())
                check.setCheckState(state)	
            else:
                check.setCheckState(state)	
        # print(self.data)
        pass

    def checked_mul(self):
        self.data = []
        for check in self.checkboxes:
            if check.isChecked():
                self.data.append(check.text())
            else:
                pass
        # print(self.data)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    run_all_tc = QtWidgets.QMainWindow()
    ui = Ui_Run_ALL()
    ui.setupUi(run_all_tc)
    run_all_tc.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NetPanelAnalysis_V1_1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_MainWindow(object):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.setupUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget_all = QtWidgets.QTabWidget(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_all.setFont(font)
        self.tabWidget_all.setObjectName("tabWidget_all")
        
        self.tab_RingNet = QtWidgets.QWidget()
        self.tab_RingNet.setObjectName("tab_RingNet")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_RingNet)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_horizontal = QtWidgets.QSplitter(self.tab_RingNet)
        self.splitter_horizontal.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_horizontal.setObjectName("splitter_horizontal")
        self.widget = QtWidgets.QWidget(self.splitter_horizontal)
        self.widget.setObjectName("widget")
        self.verticalLayout_input_output = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_input_output.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_input_output.setObjectName("verticalLayout_input_output")
        
        self.groupBox_input = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_input.sizePolicy().hasHeightForWidth())
        self.groupBox_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_input.setFont(font)
        self.groupBox_input.setObjectName("groupBox_input")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_input)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_input = QtWidgets.QFormLayout()
        self.formLayout_input.setContentsMargins(0, -1, -1, -1)
        self.formLayout_input.setSpacing(10)
        self.formLayout_input.setObjectName("formLayout_input")
        
        self.label_input_width = QtWidgets.QLabel(self.groupBox_input)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_input_width.setFont(font)
        self.label_input_width.setObjectName("label_input_width")
        self.formLayout_input.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_input_width)
        
        self.value_input_width = QtWidgets.QLineEdit(self.groupBox_input)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_input_width.setFont(font)
        self.value_input_width.setObjectName("value_input_width")
        self.formLayout_input.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.value_input_width)
        
        self.label_input_height = QtWidgets.QLabel(self.groupBox_input)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_input_height.setFont(font)
        self.label_input_height.setObjectName("label_input_height")
        self.formLayout_input.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_input_height)
        
        self.value_input_height = QtWidgets.QLineEdit(self.groupBox_input)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_input_height.setFont(font)
        self.value_input_height.setObjectName("value_input_height")
        self.formLayout_input.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_input_height)
        
        self.label_input_nw = QtWidgets.QLabel(self.groupBox_input)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_input_nw.setFont(font)
        self.label_input_nw.setObjectName("label_input_nw")
        self.formLayout_input.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_input_nw)
        
        self.value_input_nw = QtWidgets.QSpinBox(self.groupBox_input)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_input_nw.setFont(font)
        self.value_input_nw.setObjectName("value_input_nw")
        self.value_input_nw.setValue(3)
        self.formLayout_input.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.value_input_nw)
        
        self.label_input_D = QtWidgets.QLabel(self.groupBox_input)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_input_D.setFont(font)
        self.label_input_D.setObjectName("label_input_D")
        self.formLayout_input.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_input_D)
        
        self.value_input_D = QtWidgets.QLineEdit(self.groupBox_input)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_input_D.setFont(font)
        self.value_input_D.setObjectName("value_input_D")
        self.formLayout_input.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.value_input_D)
        
        self.label_input_Dmin = QtWidgets.QLabel(self.groupBox_input)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_input_Dmin.setFont(font)
        self.label_input_Dmin.setObjectName("label_input_Dmin")
        self.formLayout_input.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_input_Dmin)
        
        self.value_input_Dmin = QtWidgets.QLineEdit(self.groupBox_input)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_input_Dmin.setFont(font)
        self.value_input_Dmin.setObjectName("value_input_Dmin")
        self.formLayout_input.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.value_input_Dmin)
       
        self.label_input_Rp = QtWidgets.QLabel(self.groupBox_input)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_input_Rp.setFont(font)
        self.label_input_Rp.setObjectName("label_input_Rp")
        self.formLayout_input.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_input_Rp)

        self.value_input_Rp = QtWidgets.QLineEdit(self.groupBox_input)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_input_Rp.setFont(font)
        self.value_input_Rp.setObjectName("value_input_Rp")
        self.formLayout_input.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.value_input_Rp)
        self.horizontalLayout_3.addLayout(self.formLayout_input)
        self.verticalLayout_input_output.addWidget(self.groupBox_input)
        
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(245, 45))
        self.pushButton.setMaximumSize(QtCore.QSize(1800, 45))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_input_output.addWidget(self.pushButton)
        
        self.groupBox_output = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_output.sizePolicy().hasHeightForWidth())
        self.groupBox_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_output.setFont(font)
        self.groupBox_output.setObjectName("groupBox_output")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_output)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_output = QtWidgets.QFormLayout()
        self.formLayout_output.setHorizontalSpacing(35)
        self.formLayout_output.setVerticalSpacing(10)
        self.formLayout_output.setObjectName("formLayout_output")
       
        self.label_output1 = QtWidgets.QLabel(self.groupBox_output)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_output1.setFont(font)
        self.label_output1.setObjectName("label_output1")
        self.formLayout_output.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_output1)
        
        self.value_output1 = QtWidgets.QLineEdit(self.groupBox_output)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_output1.setFont(font)
        self.value_output1.setObjectName("value_output1")
        self.formLayout_output.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.value_output1)
        
        self.label_output2 = QtWidgets.QLabel(self.groupBox_output)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_output2.setFont(font)
        self.label_output2.setObjectName("label_output2")
        self.formLayout_output.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_output2)
       
        self.value_output2 = QtWidgets.QLineEdit(self.groupBox_output)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_output2.setFont(font)
        self.value_output2.setObjectName("value_output2")
        self.formLayout_output.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_output2)
        
        self.label_output3 = QtWidgets.QLabel(self.groupBox_output)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_output3.setFont(font)
        self.label_output3.setObjectName("label_output3")
        self.formLayout_output.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_output3)
        
        self.value_output3 = QtWidgets.QSpinBox(self.groupBox_output)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_output3.setFont(font)
        self.value_output3.setObjectName("value_output3")
        self.formLayout_output.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.value_output3)
        
        self.label_output4 = QtWidgets.QLabel(self.groupBox_output)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_output4.setFont(font)
        self.label_output4.setObjectName("label_output4")
        self.formLayout_output.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_output4)
        
        self.value_output4 = QtWidgets.QLineEdit(self.groupBox_output)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_output4.setFont(font)
        self.value_output4.setObjectName("value_output4")
        self.formLayout_output.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.value_output4)
        
        self.label_output5 = QtWidgets.QLabel(self.groupBox_output)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_output5.setFont(font)
        self.label_output5.setObjectName("label_output5")
        self.formLayout_output.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_output5)
        
        self.value_output5 = QtWidgets.QLineEdit(self.groupBox_output)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_output5.setFont(font)
        self.value_output5.setObjectName("value_output5")
        self.formLayout_output.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.value_output5)
        
        self.label_output6 = QtWidgets.QLabel(self.groupBox_output)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_output6.setFont(font)
        self.label_output6.setObjectName("label_output6")
        self.formLayout_output.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_output6)
        
        self.value_output6 = QtWidgets.QLineEdit(self.groupBox_output)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.value_output6.setFont(font)
        self.value_output6.setObjectName("value_output6")
        self.formLayout_output.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.value_output6)
        self.horizontalLayout_4.addLayout(self.formLayout_output)
        self.verticalLayout_input_output.addWidget(self.groupBox_output)
        
        self.groupBox_drawing = QtWidgets.QGroupBox(self.splitter_horizontal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_drawing.sizePolicy().hasHeightForWidth())
        self.groupBox_drawing.setSizePolicy(sizePolicy)
        self.groupBox_drawing.setObjectName("groupBox_drawing")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_drawing)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.stackedWidget_drawing = QtWidgets.QStackedWidget(self.groupBox_drawing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_drawing.sizePolicy().hasHeightForWidth())
        self.stackedWidget_drawing.setSizePolicy(sizePolicy)
        self.stackedWidget_drawing.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget_drawing.setObjectName("stackedWidget_drawing")

        self.area = PaintArea()
        self.stacked_page1 = QtWidgets.QWidget()
        self.stacked_page1.setObjectName("stacked_page1")
        self.stackedWidget_drawing.addWidget(self.area)

        self.stacked_page2 = QtWidgets.QWidget()
        self.stacked_page2.setObjectName("stacked_page2")
        self.stackedWidget_drawing.addWidget(self.stacked_page2)
        self.horizontalLayout.addWidget(self.stackedWidget_drawing)
        self.gridLayout.addWidget(self.splitter_horizontal, 0, 0, 1, 1)
        self.tabWidget_all.addTab(self.tab_RingNet, "")
        
        self.tab_OtherNet = QtWidgets.QWidget()
        self.tab_OtherNet.setObjectName("tab_OtherNet")
        self.tabWidget_all.addTab(self.tab_OtherNet, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_all)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 30))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(8)
        self.toolBar.setFont(font)
        self.toolBar.setObjectName("toolBar")
        
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPython = QtWidgets.QAction(MainWindow)
        self.actionPython.setObjectName("actionPython")
        
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuNew.addAction(self.actionPython)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
  
        self.tabWidget_all.setCurrentIndex(0)

        MainWindow.setWindowTitle("MainWindow")
        
        self.groupBox_input.setTitle("Input")
        self.label_input_width.setText("width (m)")
        self.value_input_width.setText("2.95")
        self.label_input_height.setText("height(m)")
        self.value_input_height.setText("2.95")
        self.label_input_nw.setText("nw (1)")
        self.label_input_D.setText("D (mm)")
        self.value_input_D.setText("300")
        self.label_input_Dmin.setText("Dmin (mm)")
        self.value_input_Dmin.setText("3.0")
        self.label_input_Rp.setText("Rp (m)")
        self.value_input_Rp.setText("0.5")
        self.pushButton.setText("Computing and Drawing")
        self.groupBox_output.setTitle("Output")
        self.label_output1.setText("output1")
        self.value_output1.setText("value_output1")
        self.label_output2.setText("output2")
        self.value_output2.setText("value_output2")
        self.label_output3.setText("output3")
        self.label_output4.setText("output4")
        self.value_output4.setText("value_output4")
        self.label_output5.setText("output5")
        self.value_output5.setText("value_output5")
        self.label_output6.setText("output6")
        self.value_output6.setText("value_output6")
        self.groupBox_drawing.setTitle("Drawing")
        self.tabWidget_all.setTabText(self.tabWidget_all.indexOf(self.tab_RingNet),  "Ring Net")
        self.tabWidget_all.setTabText(self.tabWidget_all.indexOf(self.tab_OtherNet), "Other Net")
        self.menuEdit.setTitle("Edit")
        self.menuView.setTitle("View")
        self.menuSetting.setTitle("Setting")
        self.menuhelp.setTitle("help")
        self.menuFile.setTitle("File")
        self.menuNew.setTitle("New")
        self.toolBar.setWindowTitle("toolBar")
        self.action_Open.setText("Open")
        self.action_Open.setShortcut("Ctrl+O")
        self.actionSave.setText("Save")
        self.actionExit.setText("Print")
        self.actionUndo.setText("Undo")
        self.actionRedo.setText("Redo")
        self.actionCut.setText("Cut")
        self.actionCopy.setText("Copy")
        self.actionPaste.setText("Paste")
        self.actionPython.setText("Python")

        self.pushButton.clicked.connect(self.slot_compute)

        self.value_input_height.textChanged.connect(self.slot_height_change)
        self.value_input_width.textChanged.connect(self.slot_width_change)
        self.value_input_nw.valueChanged.connect(self.slot_nw_change)


    def slot_height_change(self):
        value = self.value_input_height.text()
        try:
            float(value)
            self.area.setHeightValue(abs(float(value)))
        except ValueError:
            self.area.setHeightValue(1)

    def slot_width_change(self):
        value = self.value_input_width.text()
        try:
            float(value)
            self.area.setWidthValue(abs(float(value)))
        except ValueError:
            self.area.setWidthValue(1)

    def slot_nw_change(self):
        value = self.value_input_nw.value()
        self.area.setPenWidth(value)

    def slot_compute(self):

        a = float(self.value_input_width.text())
        b = float(self.value_input_height.text())
        c = a+b
        self.value_output1.setText(str(float(c)))
        self.value_output2.setText('2')
        self.value_output3.setValue(3)
        self.value_output4.setText('4')
        self.value_output5.setText('5')
        self.value_output6.setText('6')


class PaintArea(QtWidgets.QWidget):

    def __init__(self):
        super(PaintArea, self).__init__()
        self.NetHeightValue = 3
        self.NetWidthValue = 3

        self.mypen = QtGui.QPen()
        self.mypen.setColor(QtGui.QColor(25, 0, 0))
        self.mypen.setWidth(2)
        self.mypen.setCapStyle(QtCore.Qt.RoundCap)
        self.mybrush = QtGui.QBrush()

    def setHeightValue(self, value):
        print(value)
        self.NetHeightValue = value
        self.update()

    def setWidthValue(self, value):
        print(value)
        self.NetWidthValue = value
        self.update()

    def setPenWidth(self, value):
        self.mypen.setWidth(round(value/2))
        self.update()

    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter(self)
        qp.setPen(self.mypen)
        value_of_width = self.NetWidthValue
        value_of_height = self.NetHeightValue
        diameter_of_ring = 0.3  # m

        # 修复bug：输入0.1~0.5程序由于for循环中出现range(-1)而卡死
        number_of_width = max(round((value_of_width / diameter_of_ring - 1) / (2 ** 0.5) + 1), 1)
        number_of_height = max(round((value_of_height / diameter_of_ring - 1) / (2 ** 0.5) + 1), 1)

        ring_radius = min(self.width() / (2.828 * number_of_width), self.height() / (2.828 * number_of_height))
        offset_w = 0.5 * (self.width() - 2.6 * ring_radius * (number_of_width - 1) - 2 * ring_radius)
        offset_h = 0.5 * (self.height() - 2.6 * ring_radius * (number_of_height - 1) - 2 * ring_radius)

        for i in range(number_of_width):
            i = i + 1
            qp.setBrush(QtGui.QColor(255, 0, 0, 50))
            for j in range(number_of_height):
                j = j + 1
                qp.drawEllipse(offset_w + (i - 1) * 2.6 * ring_radius, offset_h + (j - 1) * 2.6 * ring_radius,
                               2 * ring_radius, 2 * ring_radius)

        for k in range(number_of_width - 1):
            k = k + 1
            qp.setBrush(QtGui.QColor(0, 0, 255, 50))
            for l in range(number_of_height - 1):
                l = l + 1
                qp.drawEllipse(offset_w + (k - 1) * 2.6 * ring_radius + 1.3 * ring_radius,
                               offset_h + (l - 1) * 2.6 * ring_radius + 1.3 * ring_radius, 2 * ring_radius,
                               2 * ring_radius)


class ComputePart():
    pass
# -*- coding: utf-8 -*-
# -*- coding: UTF-8 -*-
# NetPanelAnalysis_V1_0_2界面

import numpy as np
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        sizePolicy00 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy00.setHorizontalStretch(0)
        sizePolicy00.setVerticalStretch(0)

        sizePolicy11 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(1)
        sizePolicy11.setVerticalStretch(1)

        sizePolicy20 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy20.setHorizontalStretch(2)
        sizePolicy20.setVerticalStretch(0)

        font_menuBar = QtGui.QFont()
        font_menuBar.setFamily("等线")
        font_menuBar.setPointSize(10)

        font_toolBar = QtGui.QFont()
        font_toolBar.setFamily("等线")
        font_toolBar.setPointSize(8)
 
        font_tab = QtGui.QFont()
        font_tab.setFamily("Arial")
        font_tab.setPointSize(10)
        font_tab.setBold(False)
        font_tab.setUnderline(False)
        font_tab.setWeight(60)

        font_group = QtGui.QFont()
        font_group.setFamily("Times New Roman")
        font_group.setPointSize(10)
        font_group.setBold(True)
        font_group.setWeight(75)

        font_label = QtGui.QFont()
        font_label.setFamily("Times New Roman")
        font_label.setPointSize(12)
        font_label.setBold(True)
        font_label.setItalic(False)
        font_label.setWeight(60)

        font_value = QtGui.QFont()
        font_value.setFamily("Times New Roman")
        font_value.setPointSize(10)
        font_value.setBold(True)
        font_value.setWeight(50)

        font_button = QtGui.QFont()
        font_button.setFamily("Arial")
        font_button.setPointSize(10)
        font_button.setBold(True)
        font_button.setUnderline(False)
        font_button.setWeight(75)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)   
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy00.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy00)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.tabWidget_all = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_all.setFont(font_tab)
        self.tabWidget_all.setObjectName("tabWidget_all")

        self.tab_RingNet = QtWidgets.QWidget()
        self.tab_RingNet.setObjectName("tab_RingNet")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_RingNet)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_horizontal = QtWidgets.QSplitter(self.tab_RingNet)
        self.splitter_horizontal.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_horizontal.setObjectName("splitter_horizontal")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_horizontal)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_input_output = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_input_output.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_input_output.setObjectName("verticalLayout_input_output")

        self.groupBox_input = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy11.setHeightForWidth(self.groupBox_input.sizePolicy().hasHeightForWidth())
        self.groupBox_input.setSizePolicy(sizePolicy11)

        self.groupBox_input.setFont(font_group)
        self.groupBox_input.setObjectName("groupBox_input")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_input)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_input = QtWidgets.QFormLayout()
        self.formLayout_input.setContentsMargins(10,10, 10, 10)
        self.formLayout_input.setSpacing(10)
        self.formLayout_input.setObjectName("formLayout_input")

        self.label_input_width = QtWidgets.QLabel(self.groupBox_input)
        self.label_input_width.setFont(font_label)
        self.label_input_width.setObjectName("label_input_width")
        self.formLayout_input.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_input_width)

        self.value_input_width = QtWidgets.QLineEdit(self.groupBox_input)
        self.value_input_width.setFont(font_value)
        self.value_input_width.setObjectName("value_input_width")
        self.formLayout_input.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.value_input_width)

        self.label_input_height = QtWidgets.QLabel(self.groupBox_input)
        self.label_input_height.setFont(font_label)
        self.label_input_height.setObjectName("label_input_height")
        self.formLayout_input.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_input_height)

        self.value_input_height = QtWidgets.QLineEdit(self.groupBox_input)
        self.value_input_height.setFont(font_value)
        self.value_input_height.setObjectName("value_input_height")
        self.formLayout_input.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_input_height)

        self.label_input_nw = QtWidgets.QLabel(self.groupBox_input)
        self.label_input_nw.setFont(font_label)
        self.label_input_nw.setObjectName("label_input_nw")
        self.formLayout_input.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_input_nw)

        self.value_input_nw = QtWidgets.QSpinBox(self.groupBox_input)
        self.value_input_nw.setFont(font_value)
        self.value_input_nw.setObjectName("value_input_nw")
        self.formLayout_input.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.value_input_nw)

        self.label_input_D = QtWidgets.QLabel(self.groupBox_input)
        self.label_input_D.setFont(font_label)
        self.label_input_D.setObjectName("label_input_D")
        self.formLayout_input.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_input_D)

        self.value_input_D = QtWidgets.QLineEdit(self.groupBox_input)
        self.value_input_D.setFont(font_value)
        self.value_input_D.setObjectName("value_input_D")
        self.formLayout_input.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.value_input_D)

        self.label_input_ks = QtWidgets.QLabel(self.groupBox_input)
        self.label_input_ks.setFont(font_label)
        self.label_input_ks.setObjectName("label_input_ks")
        self.formLayout_input.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_input_ks)

        self.value_input_ks = QtWidgets.QLineEdit(self.groupBox_input)
        self.value_input_ks.setFont(font_value)
        self.value_input_ks.setObjectName("value_input_ks")
        self.formLayout_input.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.value_input_ks)

        self.label_input_Rp = QtWidgets.QLabel(self.groupBox_input)
        self.label_input_Rp.setFont(font_label)
        self.label_input_Rp.setObjectName("label_input_Rp")
        self.formLayout_input.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_input_Rp)

        self.value_input_Rp = QtWidgets.QLineEdit(self.groupBox_input)
        self.value_input_Rp.setFont(font_value)
        self.value_input_Rp.setObjectName("value_input_Rp")
        self.formLayout_input.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.value_input_Rp)

        self.horizontalLayout_3.addLayout(self.formLayout_input)
        self.verticalLayout_input_output.addWidget(self.groupBox_input)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy11.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy11)
        self.pushButton.setMinimumSize(QtCore.QSize(180, 45))
        self.pushButton.setMaximumSize(QtCore.QSize(1800, 45))

        self.pushButton.setFont(font_button)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_input_output.addWidget(self.pushButton)

        self.groupBox_output = QtWidgets.QGroupBox(self.layoutWidget)

        sizePolicy11.setHeightForWidth(self.groupBox_output.sizePolicy().hasHeightForWidth())
        self.groupBox_output.setSizePolicy(sizePolicy11)

        self.groupBox_output.setFont(font_group)
        self.groupBox_output.setObjectName("groupBox_output")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_output)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_output = QtWidgets.QFormLayout()
        self.formLayout_output.setHorizontalSpacing(10)
        self.formLayout_output.setVerticalSpacing(10)
        self.formLayout_output.setObjectName("formLayout_output")

        self.label_output1 = QtWidgets.QLabel(self.groupBox_output)
        self.label_output1.setFont(font_label)
        self.label_output1.setObjectName("label_output1")
        self.formLayout_output.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_output1)

        self.value_output1 = QtWidgets.QLineEdit(self.groupBox_output)
        self.value_output1.setFont(font_value)
        self.value_output1.setObjectName("value_output1")
        self.formLayout_output.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.value_output1)

        self.label_output2 = QtWidgets.QLabel(self.groupBox_output)
        self.label_output2.setFont(font_label)
        self.label_output2.setObjectName("label_output2")
        self.formLayout_output.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_output2)

        self.value_output2 = QtWidgets.QLineEdit(self.groupBox_output)
        self.value_output2.setFont(font_value)
        self.value_output2.setObjectName("value_output2")
        self.formLayout_output.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_output2)

        self.label_output3 = QtWidgets.QLabel(self.groupBox_output)
        self.label_output3.setFont(font_label)
        self.label_output3.setObjectName("label_output3")
        self.formLayout_output.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_output3)

        self.value_output3 = QtWidgets.QLineEdit(self.groupBox_output)
        self.value_output3.setFont(font_value)
        self.value_output3.setObjectName("value_output3")
        self.formLayout_output.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.value_output3)

        self.label_output4 = QtWidgets.QLabel(self.groupBox_output)
        self.label_output4.setFont(font_label)
        self.label_output4.setObjectName("label_output4")
        self.formLayout_output.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_output4)

        self.value_output4 = QtWidgets.QLineEdit(self.groupBox_output)
        self.value_output4.setFont(font_value)
        self.value_output4.setObjectName("value_output4")
        self.formLayout_output.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.value_output4)

        self.label_output5 = QtWidgets.QLabel(self.groupBox_output)
        self.label_output5.setFont(font_label)
        self.label_output5.setObjectName("label_output5")
        self.formLayout_output.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_output5)

        self.value_output5 = QtWidgets.QLineEdit(self.groupBox_output)
        self.value_output5.setFont(font_value)
        self.value_output5.setObjectName("value_output5")
        self.formLayout_output.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.value_output5)

        self.label_output6 = QtWidgets.QLabel(self.groupBox_output)
        self.label_output6.setFont(font_label)
        self.label_output6.setObjectName("label_output6")
        self.formLayout_output.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_output6)

        self.value_output6 = QtWidgets.QLineEdit(self.groupBox_output)
        self.value_output6.setFont(font_value)
        self.value_output6.setObjectName("value_output6")
        self.formLayout_output.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.value_output6)

        self.horizontalLayout_4.addLayout(self.formLayout_output)
        self.verticalLayout_input_output.addWidget(self.groupBox_output)
        self.groupBox_drawing = QtWidgets.QGroupBox(self.splitter_horizontal)
        sizePolicy20.setHeightForWidth(self.groupBox_drawing.sizePolicy().hasHeightForWidth())       
        self.groupBox_drawing.setSizePolicy(sizePolicy20)
        self.groupBox_drawing.setFont(font_group)
        self.groupBox_drawing.setObjectName("groupBox_drawing")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_drawing)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.stackedWidget_drawingRN = QtWidgets.QStackedWidget(self.groupBox_drawing)
        sizePolicy20.setHeightForWidth(self.stackedWidget_drawingRN.sizePolicy().hasHeightForWidth())
        self.stackedWidget_drawingRN.setSizePolicy(sizePolicy20)
        self.stackedWidget_drawingRN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget_drawingRN.setObjectName("stackedWidget_drawing")

        ####################################################################################################################
        # 创建参数化绘图区域
        self.areaRN = PaintAreaRN()
        self.stackedWidget_drawingRN.addWidget(self.areaRN)
        ####################################################################################################################

        self.horizontalLayout.addWidget(self.stackedWidget_drawingRN)
        self.gridLayout.addWidget(self.splitter_horizontal, 0, 0, 1, 1)  # 第0行第0列占1行占1列
        self.tabWidget_all.addTab(self.tab_RingNet, "")
 
        self.tab_CableNet = QtWidgets.QWidget()
        self.tab_CableNet.setObjectName("tab_CableNet")

        self.gridLayoutCN = QtWidgets.QGridLayout(self.tab_CableNet)
        self.gridLayoutCN.setObjectName("gridLayoutCN")
        self.splitter_horizontalCN = QtWidgets.QSplitter(self.tab_CableNet)
        self.splitter_horizontalCN.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_horizontalCN.setObjectName("splitter_horizontalCN")
        self.layoutWidgetCN = QtWidgets.QWidget(self.splitter_horizontalCN)
        self.layoutWidgetCN.setObjectName("layoutWidgetCN")
        self.verticalLayout_input_outputCN = QtWidgets.QVBoxLayout(self.layoutWidgetCN)
        self.verticalLayout_input_outputCN.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_input_outputCN.setObjectName("verticalLayout_input_outputCN")

        self.groupBox_inputCN = QtWidgets.QGroupBox(self.layoutWidgetCN)
        sizePolicy11.setHeightForWidth(self.groupBox_inputCN.sizePolicy().hasHeightForWidth())
        self.groupBox_inputCN.setSizePolicy(sizePolicy11)
        self.groupBox_inputCN.setFont(font_group)
        self.groupBox_inputCN.setObjectName("groupBox_inputCN")

        self.horizontalLayout_3CN = QtWidgets.QHBoxLayout(self.groupBox_inputCN)
        self.horizontalLayout_3CN.setObjectName("horizontalLayout_3CN")

        self.gridLayout_inputCN = QtWidgets.QGridLayout()
        self.gridLayout_inputCN.setHorizontalSpacing(10)
        self.gridLayout_inputCN.setVerticalSpacing(10)
        self.gridLayout_inputCN.setColumnMinimumWidth(3, 20)
        self.label_input_E_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_E_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_E_CN, 0, 0)
        self.label_input_E_CN.setText('E (Pa)')

        self.value_input_E_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_E_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_E_CN, 0, 1)
        self.value_input_E_CN.setText('100e9')

        self.label_input_ET_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_ET_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_ET_CN, 0, 2)
        self.label_input_ET_CN.setText('E<sub>T</sub> (Pa)')

        self.value_input_ET_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_ET_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_ET_CN, 0, 3)
        self.value_input_ET_CN.setText('10e9')

        self.label_input_sigmau_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_sigmau_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_sigmau_CN, 1, 0)
        self.label_input_sigmau_CN.setText('σ<sub>u</sub> (Pa)')

        self.value_input_sigmau_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_sigmau_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_sigmau_CN, 1, 1)
        self.value_input_sigmau_CN.setText('1570e6')

        self.label_input_epsilonu_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_epsilonu_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_epsilonu_CN, 1, 2)
        self.label_input_epsilonu_CN.setText('ε<sub>u</sub> (1)')

        self.value_input_epsilonu_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_epsilonu_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_epsilonu_CN, 1, 3)
        self.value_input_epsilonu_CN.setText('0.05')

        self.label_input_Acable_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_Acable_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_Acable_CN, 2, 0)
        self.label_input_Acable_CN.setText('A<sub>cable</sub> (mm<sup>2</sup>)')

        self.value_input_Acable_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_Acable_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_Acable_CN, 2, 1)
        self.value_input_Acable_CN.setText('314')

        self.label_input_Rp_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_Rp_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_Rp_CN, 2, 2)
        self.label_input_Rp_CN.setText('R<sub>p</sub> (m)')

        self.value_input_Rp_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_Rp_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_Rp_CN, 2, 3)
        self.value_input_Rp_CN.setText('0.5')

        self.label_input_ex_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_ex_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_ex_CN, 3, 0)
        self.label_input_ex_CN.setText('e<sub>x</sub> (m)')

        self.value_input_ex_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_ex_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_ex_CN, 3, 1)
        self.value_input_ex_CN.setText('0.0')

        self.label_input_ey_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_ey_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_ey_CN, 3, 2)
        self.label_input_ey_CN.setText('e<sub>y</sub> (m)')

        self.value_input_ey_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_ey_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_ey_CN, 3, 3)
        self.value_input_ey_CN.setText('0.0')

        self.label_input_d1_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_d1_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_d1_CN, 4, 0)
        self.label_input_d1_CN.setText('d<sub>1</sub> (m)')

        self.value_input_d1_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_d1_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_d1_CN, 4, 1)
        self.value_input_d1_CN.setText('0.3')

        self.label_input_d2_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_d2_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_d2_CN, 4, 2)
        self.label_input_d2_CN.setText('d<sub>2</sub> (m)')

        self.value_input_d2_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_d2_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_d2_CN, 4, 3)
        self.value_input_d2_CN.setText('0.3')

        self.label_input_alpha1_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_alpha1_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_alpha1_CN, 5, 0)
        self.label_input_alpha1_CN.setText('α<sub>1</sub> (°)')

        self.value_input_alpha1_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_alpha1_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_alpha1_CN, 5, 1)
        self.value_input_alpha1_CN.setText('0')

        self.label_input_alpha2_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_alpha2_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_alpha2_CN, 5, 2)
        self.label_input_alpha2_CN.setText('α<sub>2</sub> (°)')

        self.value_input_alpha2_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_alpha2_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_alpha2_CN, 5, 3)
        self.value_input_alpha2_CN.setText('90')

        self.label_input_x1y1_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_x1y1_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_x1y1_CN, 6, 0)
        self.label_input_x1y1_CN.setText('(x<sub>1</sub>,y<sub>1</sub>) (m)')

        self.value_input_x1y1_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_x1y1_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_x1y1_CN, 6, 1)
        self.value_input_x1y1_CN.setText('1.5, 1.5')

        self.label_input_x2y2_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_x2y2_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_x2y2_CN, 6, 2)
        self.label_input_x2y2_CN.setText('(x<sub>2</sub>,y<sub>2</sub>) (m)')

        self.value_input_x2y2_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_x2y2_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_x2y2_CN, 6, 3)
        self.value_input_x2y2_CN.setText('-1.5, 1.5')

        self.label_input_x3y3_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_x3y3_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_x3y3_CN, 7, 0)
        self.label_input_x3y3_CN.setText('(x<sub>3</sub>,y<sub>3</sub>) (m)')

        self.value_input_x3y3_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_x3y3_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_x3y3_CN, 7, 1)
        self.value_input_x3y3_CN.setText('-1.5, 1.5')

        self.label_input_x4y4_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_x4y4_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_x4y4_CN, 7, 2)
        self.label_input_x4y4_CN.setText('(x<sub>4</sub>,y<sub>4</sub>) (m)')

        self.value_input_x4y4_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_x4y4_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_x4y4_CN, 7, 3)
        self.value_input_x4y4_CN.setText('-1.5, 1.5')

        self.label_input_ks12_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_ks12_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_ks12_CN, 8, 0)
        self.label_input_ks12_CN.setText('k<sub>s12</sub> (N/m)')

        self.value_input_ks12_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_ks12_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_ks12_CN, 8, 1)
        self.value_input_ks12_CN.setText('1e15')

        self.label_input_ks23_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_ks23_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_ks23_CN, 8, 2)
        self.label_input_ks23_CN.setText('k<sub>s23</sub> (N/m)')

        self.value_input_ks23_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_ks23_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_ks23_CN, 8, 3)
        self.value_input_ks23_CN.setText('1e15')

        self.label_input_ks34_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_ks34_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_ks34_CN, 9, 0)
        self.label_input_ks34_CN.setText('k<sub>s34</sub> (N/m)')

        self.value_input_ks34_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_ks34_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_ks34_CN, 9, 1)
        self.value_input_ks34_CN.setText('1e15')

        self.label_input_ks41_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_ks41_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_ks41_CN, 9, 2)
        self.label_input_ks41_CN.setText('k<sub>s41</sub> (N/m)')

        self.value_input_ks41_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_ks41_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_ks41_CN, 9, 3)
        self.value_input_ks41_CN.setText('1e15')

        self.label_input_initial_sag_CN = QtWidgets.QLabel(self.groupBox_inputCN)
        self.label_input_initial_sag_CN.setFont(font_label)
        self.gridLayout_inputCN.addWidget(self.label_input_initial_sag_CN, 10, 0, 1, 2)
        self.label_input_initial_sag_CN.setText('Initial Sag of Cable Net (m)')

        self.value_input_initial_sag_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
        self.value_input_initial_sag_CN.setFont(font_value)
        self.gridLayout_inputCN.addWidget(self.value_input_initial_sag_CN, 10, 2, 1, 2)
        self.value_input_initial_sag_CN.setText('0.55')

        self.horizontalLayout_3CN.addLayout(self.gridLayout_inputCN)
        self.verticalLayout_input_outputCN.addWidget(self.groupBox_inputCN)

        self.pushButtonCN = QtWidgets.QPushButton(self.layoutWidgetCN)
        sizePolicy11.setHeightForWidth(self.pushButtonCN.sizePolicy().hasHeightForWidth())
        self.pushButtonCN.setSizePolicy(sizePolicy11)
        self.pushButtonCN.setMinimumSize(QtCore.QSize(180, 45))
        self.pushButtonCN.setMaximumSize(QtCore.QSize(1800, 45))
        self.pushButtonCN.setFont(font_button)
        self.pushButtonCN.setObjectName("pushButtonCN")
        self.verticalLayout_input_outputCN.addWidget(self.pushButtonCN)

        self.groupBox_outputCN = QtWidgets.QGroupBox(self.layoutWidgetCN)
        sizePolicy11.setHeightForWidth(self.groupBox_outputCN.sizePolicy().hasHeightForWidth())
        self.groupBox_outputCN.setSizePolicy(sizePolicy11)

        self.groupBox_outputCN.setFont(font_group)
        self.groupBox_outputCN.setObjectName("groupBox_outputCN")
        self.horizontalLayout_4CN = QtWidgets.QHBoxLayout(self.groupBox_outputCN)
        self.horizontalLayout_4CN.setObjectName("horizontalLayout_4CN")
        self.formLayout_outputCN = QtWidgets.QFormLayout()
        self.formLayout_outputCN.setHorizontalSpacing(10)
        self.formLayout_outputCN.setVerticalSpacing(10)
        self.formLayout_outputCN.setObjectName("formLayout_outputCN")

        self.label_outputCN = QtWidgets.QLabel(self.groupBox_outputCN)  
        self.label_outputCN.setFont(font_label)
        self.label_outputCN.setObjectName("label_outputCN")
        self.formLayout_outputCN.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_outputCN)

        self.value_outputCN = QtWidgets.QLineEdit(self.groupBox_outputCN)  
        self.value_outputCN.setFont(font_value)
        self.value_outputCN.setObjectName("value_output1")
        self.formLayout_outputCN.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.value_outputCN)

        self.horizontalLayout_4CN.addLayout(self.formLayout_outputCN)
        self.verticalLayout_input_outputCN.addWidget(self.groupBox_outputCN)
        self.groupBox_drawingCN = QtWidgets.QGroupBox(self.splitter_horizontalCN)

        sizePolicy20.setHeightForWidth(self.groupBox_drawingCN.sizePolicy().hasHeightForWidth())
        self.groupBox_drawingCN.setSizePolicy(sizePolicy20)
        self.groupBox_drawingCN.setFont(font_group)
        self.groupBox_drawingCN.setObjectName("groupBox_drawingCN")
        self.horizontalLayoutCN = QtWidgets.QHBoxLayout(self.groupBox_drawingCN)
        self.horizontalLayoutCN.setObjectName("horizontalLayoutCN")
        self.stackedWidget_drawingCN = QtWidgets.QStackedWidget(self.groupBox_drawingCN)

        sizePolicy20.setHeightForWidth(self.stackedWidget_drawingCN.sizePolicy().hasHeightForWidth())
        self.stackedWidget_drawingCN.setSizePolicy(sizePolicy20)
        self.stackedWidget_drawingCN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget_drawingCN.setObjectName("stackedWidget_drawing")

        ####################################################################################################################
        # 创建参数化绘图区域
        self.areaCN = PaintAreaCN()
        self.stackedWidget_drawingCN.addWidget(self.areaCN)
        ####################################################################################################################

        self.horizontalLayoutCN.addWidget(self.stackedWidget_drawingCN)
        self.gridLayoutCN.addWidget(self.splitter_horizontalCN, 0, 0, 1, 1)
        self.tabWidget_all.addTab(self.tab_CableNet, "")
 
        self.tab_OtherNet = QtWidgets.QWidget()
        self.tab_OtherNet.setObjectName("tab_OtherNet")
        self.tabWidget_all.addTab(self.tab_OtherNet, "")

        self.horizontalLayout_2.addWidget(self.tabWidget_all)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 30))
        self.menubar.setFont(font_menuBar)
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
        self.toolBar.setFont(font_toolBar)
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

        self.value_input_nw.setValue(7)

        self.retranslateUi(MainWindow)
        self.tabWidget_all.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Net Panel Analysis V1.0.2"))
        self.groupBox_input.setTitle(_translate("MainWindow", "Input"))
        self.groupBox_inputCN.setTitle(_translate("MainWindow", "Input"))
        self.label_input_width.setText(_translate("MainWindow", "width (m)"))
        self.value_input_width.setText(_translate("MainWindow", "2.95"))
        self.label_input_height.setText(_translate("MainWindow", "height(m)"))
        self.value_input_height.setText(_translate("MainWindow", "2.95"))
        self.label_input_nw.setText(_translate("MainWindow", "n<sub>w</sub> (1)"))
        self.label_input_D.setText(_translate("MainWindow", "D (mm)"))
        self.value_input_D.setText(_translate("MainWindow", "300"))
        self.label_input_ks.setText(_translate("MainWindow", "k<sub>s</sub> (N/m)"))
        self.value_input_ks.setText(_translate("MainWindow", "10000000000"))
        self.label_input_Rp.setText(_translate("MainWindow", "R<sub>p</sub> (m)"))
        self.value_input_Rp.setText(_translate("MainWindow", "0.5"))

        self.pushButton.setText(_translate("MainWindow", "Computing and Drawing"))
        self.pushButtonCN.setText(_translate("MainWindow", "Computing and Drawing"))

        self.groupBox_output.setTitle(_translate("MainWindow", "Output"))
        self.groupBox_outputCN.setTitle(_translate("MainWindow", "Output"))
        self.label_output1.setText(_translate("MainWindow", "Displacement"))
        self.value_output1.setText(_translate("MainWindow", "output1"))
        self.label_outputCN.setText(_translate("MainWindow", "Displacement"))
        self.value_outputCN.setText(_translate("MainWindow", "output1"))
        self.label_output2.setText(_translate("MainWindow", "Force"))
        self.value_output2.setText(_translate("MainWindow", "output2"))
        self.label_output3.setText(_translate("MainWindow", "Energy"))
        self.value_output3.setText(_translate("MainWindow", "output3"))
        self.label_output4.setText(_translate("MainWindow", "γ<sub>Nmax</sub>"))
        self.value_output4.setText(_translate("MainWindow", "output4"))
        self.label_output5.setText(_translate("MainWindow", "spring length"))
        self.value_output5.setText(_translate("MainWindow", "output5"))
        self.label_output6.setText(_translate("MainWindow", "fiber length"))
        self.value_output6.setText(_translate("MainWindow", "output6"))

        self.groupBox_drawing.setTitle(_translate("MainWindow", "Drawing"))
        self.groupBox_drawingCN.setTitle(_translate("MainWindow", "Drawing"))

        self.tabWidget_all.setTabText(self.tabWidget_all.indexOf(self.tab_RingNet), _translate("MainWindow", "Ring Net"))
        self.tabWidget_all.setTabText(self.tabWidget_all.indexOf(self.tab_CableNet), _translate("MainWindow", "Cable Net"))
        self.tabWidget_all.setTabText(self.tabWidget_all.indexOf(self.tab_OtherNet), _translate("MainWindow", "Other Net"))

        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Open.setText(_translate("MainWindow", "Open"))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Print"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPython.setText(_translate("MainWindow", "Python"))


class PaintAreaRN(QtWidgets.QWidget):

    def __init__(self):
        super(PaintAreaRN, self).__init__()

        self.NetHeightValue = 3
        self.NetWidthValue = 3

        self.mypen = QtGui.QPen()
        self.mypen.setColor(QtGui.QColor(25, 0, 0))
        self.mypen.setWidth(2)
        self.mypen.setCapStyle(QtCore.Qt.RoundCap)
        self.mybrush = QtGui.QBrush()

    def setHeightValue(self, value):
        self.NetHeightValue = value
        self.update()

    def setWidthValue(self, value):
        self.NetWidthValue = value
        self.update()

    def setPenWidth(self, value):
        self.mypen.setWidth(round(value / 2))
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


class PaintAreaCN(QtWidgets.QWidget):

    def __init__(self):
        super(PaintAreaCN, self).__init__()

        self.NetHeightValue = 3
        self.NetWidthValue = 3

        self.mypen = QtGui.QPen()
        self.mypen.setColor(QtGui.QColor(25, 0, 0))
        self.mypen.setWidth(2)
        self.mypen.setCapStyle(QtCore.Qt.RoundCap)
        self.mybrush = QtGui.QBrush()

    def setHeightValue(self, value):
        self.NetHeightValue = value
        self.update()

    def setWidthValue(self, value):
        self.NetWidthValue = value
        self.update()

    def setPenWidth(self, value):
        self.mypen.setWidth(round(value / 2))
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


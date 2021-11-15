# -*- coding: utf-8 -*-
# -*- coding: UTF-8 -*-
# NetPanelAnalysis_V1_0_2界面

import numpy as np
#from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
import NPA_cable_net_v1_POP

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
		font_menuBar.setFamily("Arial")
		font_menuBar.setPointSize(10)

		font_toolBar = QtGui.QFont()
		font_toolBar.setFamily("Arial")
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
		font_group.setWeight(60)

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
		font_value.setWeight(60)

		font_button = QtGui.QFont()
		font_button.setFamily("Arial")
		font_button.setPointSize(10)
		font_button.setBold(True)
		font_button.setUnderline(False)
		font_button.setWeight(60)

		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1440, 900)   
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
		self.splitter_horizontal.setSizes([self.width()*0.4,self.width()*0.6])
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
		self.splitter_horizontal.setSizes([self.width()*0.4,self.width()*0.6])
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
		self.gridLayout_inputCN.setHorizontalSpacing(5)
		self.gridLayout_inputCN.setVerticalSpacing(10)
		self.gridLayout_inputCN.setColumnMinimumWidth(0, 5)
		self.gridLayout_inputCN.setColumnMinimumWidth(1, 5)
		self.gridLayout_inputCN.setColumnMinimumWidth(2, 5)
		self.gridLayout_inputCN.setColumnMinimumWidth(3, 5)

		self.label_input_E_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_E_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_E_CN, 0, 0)
		self.label_input_E_CN.setText('E (GPa)')

		self.value_input_E_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_E_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_E_CN, 0, 1)
		self.value_input_E_CN.setText('91.304')

		self.label_input_ET_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_ET_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_ET_CN, 0, 2)
		self.label_input_ET_CN.setText('E<sub>T</sub> (GPa)')

		self.value_input_ET_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_ET_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_ET_CN, 0, 3)
		self.value_input_ET_CN.setText('25.0')

		self.label_input_sigmay_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_sigmay_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_sigmay_CN, 1, 0)
		self.label_input_sigmay_CN.setText('σ<sub>y</sub> (MPa)')

		self.value_input_sigmay_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_sigmay_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_sigmay_CN, 1, 1)
		self.value_input_sigmay_CN.setText('1050')

		self.label_input_sigmau_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_sigmau_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_sigmau_CN, 1, 2)
		self.label_input_sigmau_CN.setText('σ<sub>u</sub> (MPa)')

		self.value_input_sigmau_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_sigmau_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_sigmau_CN, 1, 3)
		self.value_input_sigmau_CN.setText('1350')

		self.label_input_Acable_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_Acable_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_Acable_CN, 2, 0)
		self.label_input_Acable_CN.setText('A<sub>cable</sub> (mm<sup>2</sup>)')

		self.value_input_Acable_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_Acable_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_Acable_CN, 2, 1)
		self.value_input_Acable_CN.setText('30.148')

		self.label_input_Rp_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_Rp_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_Rp_CN, 2, 2)
		self.label_input_Rp_CN.setText('R<sub>p</sub> (m)')

		self.value_input_Rp_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_Rp_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_Rp_CN, 2, 3)
		self.value_input_Rp_CN.setText('0.6')

		self.label_input_ex_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_ex_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_ex_CN, 3, 0)
		self.label_input_ex_CN.setText('e<sub>x</sub> (m)')

		self.value_input_ex_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_ex_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_ex_CN, 3, 1)
		self.value_input_ex_CN.setText('-0.2')

		self.label_input_ey_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_ey_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_ey_CN, 3, 2)
		self.label_input_ey_CN.setText('e<sub>y</sub> (m)')

		self.value_input_ey_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_ey_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_ey_CN, 3, 3)
		self.value_input_ey_CN.setText('0.3')

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
		self.value_input_alpha1_CN.setText('-30')

		self.label_input_alpha2_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_alpha2_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_alpha2_CN, 5, 2)
		self.label_input_alpha2_CN.setText('α<sub>2</sub> (°)')

		self.value_input_alpha2_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_alpha2_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_alpha2_CN, 5, 3)
		self.value_input_alpha2_CN.setText('60')

		self.label_input_x1y1_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_x1y1_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_x1y1_CN, 6, 0)
		self.label_input_x1y1_CN.setText('(x<sub>1</sub>,y<sub>1</sub>) (m)')

		self.value_input_x1y1_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_x1y1_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_x1y1_CN, 6, 1)
		self.value_input_x1y1_CN.setText('1.0, -1.5')

		self.label_input_x2y2_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_x2y2_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_x2y2_CN, 6, 2)
		self.label_input_x2y2_CN.setText('(x<sub>2</sub>,y<sub>2</sub>) (m)')

		self.value_input_x2y2_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_x2y2_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_x2y2_CN, 6, 3)
		self.value_input_x2y2_CN.setText('2.0, 1.0')

		self.label_input_x3y3_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_x3y3_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_x3y3_CN, 7, 0)
		self.label_input_x3y3_CN.setText('(x<sub>3</sub>,y<sub>3</sub>) (m)')

		self.value_input_x3y3_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_x3y3_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_x3y3_CN, 7, 1)
		self.value_input_x3y3_CN.setText('-1.8, 2.2')

		self.label_input_x4y4_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_x4y4_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_x4y4_CN, 7, 2)
		self.label_input_x4y4_CN.setText('(x<sub>4</sub>,y<sub>4</sub>) (m)')

		self.value_input_x4y4_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_x4y4_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_x4y4_CN, 7, 3)
		self.value_input_x4y4_CN.setText('-2.0, -1.0')

		self.label_input_ks12_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_ks12_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_ks12_CN, 8, 0)
		self.label_input_ks12_CN.setText('k<sub>s12</sub> (N/m)')

		self.value_input_ks12_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_ks12_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_ks12_CN, 8, 1)
		self.value_input_ks12_CN.setText('10000000000000')

		self.label_input_ks23_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_ks23_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_ks23_CN, 8, 2)
		self.label_input_ks23_CN.setText('k<sub>s23</sub> (N/m)')

		self.value_input_ks23_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_ks23_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_ks23_CN, 8, 3)
		self.value_input_ks23_CN.setText('10000000000000')

		self.label_input_ks34_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_ks34_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_ks34_CN, 9, 0)
		self.label_input_ks34_CN.setText('k<sub>s34</sub> (N/m)')

		self.value_input_ks34_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_ks34_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_ks34_CN, 9, 1)
		self.value_input_ks34_CN.setText('10000000000000')

		self.label_input_ks41_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_ks41_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_ks41_CN, 9, 2)
		self.label_input_ks41_CN.setText('k<sub>s41</sub> (N/m)')

		self.value_input_ks41_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_ks41_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_ks41_CN, 9, 3)
		self.value_input_ks41_CN.setText('10000000000000')

		self.label_input_initial_sag_CN = QtWidgets.QLabel(self.groupBox_inputCN)
		self.label_input_initial_sag_CN.setFont(font_label)
		self.gridLayout_inputCN.addWidget(self.label_input_initial_sag_CN, 10, 0, 1, 2)
		self.label_input_initial_sag_CN.setText('Initial Sag of Cable Net (m)')

		self.value_input_initial_sag_CN = QtWidgets.QLineEdit(self.groupBox_inputCN)
		self.value_input_initial_sag_CN.setFont(font_value)
		self.gridLayout_inputCN.addWidget(self.value_input_initial_sag_CN, 10, 2, 1, 2)
		self.value_input_initial_sag_CN.setText('0.20')

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

		self.label_output1CN = QtWidgets.QLabel(self.groupBox_outputCN)  
		self.label_output1CN.setFont(font_label)
		self.label_output1CN.setObjectName("label_output1CN")
		self.formLayout_outputCN.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_output1CN)

		self.value_output1CN = QtWidgets.QLineEdit(self.groupBox_outputCN)  
		self.value_output1CN.setFont(font_value)
		self.value_output1CN.setObjectName("value_output1CN")
		self.formLayout_outputCN.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.value_output1CN)

		self.label_output2CN = QtWidgets.QLabel(self.groupBox_outputCN)  
		self.label_output2CN.setFont(font_label)
		self.label_output2CN.setObjectName("label_output2CN")
		self.formLayout_outputCN.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_output2CN)

		self.value_output2CN = QtWidgets.QLineEdit(self.groupBox_outputCN)  
		self.value_output2CN.setFont(font_value)
		self.value_output2CN.setObjectName("value_output2CN")
		self.formLayout_outputCN.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_output2CN)

		self.label_output3CN = QtWidgets.QLabel(self.groupBox_outputCN)  
		self.label_output3CN.setFont(font_label)
		self.label_output3CN.setObjectName("label_output3CN")
		self.formLayout_outputCN.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_output3CN)

		self.value_output3CN = QtWidgets.QLineEdit(self.groupBox_outputCN)  
		self.value_output3CN.setFont(font_value)
		self.value_output3CN.setObjectName("value_output3CN")
		self.formLayout_outputCN.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.value_output3CN)

		self.label_output4CN = QtWidgets.QLabel(self.groupBox_outputCN)  
		self.label_output4CN.setFont(font_label)
		self.label_output4CN.setObjectName("label_output4CN")
		self.formLayout_outputCN.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_output4CN)

		self.value_output4CN = QtWidgets.QLineEdit(self.groupBox_outputCN)  
		self.value_output4CN.setFont(font_value)
		self.value_output4CN.setObjectName("value_output4CN")
		self.formLayout_outputCN.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.value_output4CN)

		self.label_output5CN = QtWidgets.QLabel(self.groupBox_outputCN)  
		self.label_output5CN.setFont(font_label)
		self.label_output5CN.setObjectName("label_output5CN")
		self.formLayout_outputCN.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_output5CN)

		self.value_output5CN = QtWidgets.QLineEdit(self.groupBox_outputCN)  
		self.value_output5CN.setFont(font_value)
		self.value_output5CN.setObjectName("value_output5CN")
		self.formLayout_outputCN.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.value_output5CN)

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

		self.label_output1CN.setText(_translate("MainWindow", "Breaking force of cable"))
		self.value_output1CN.setText(_translate("MainWindow", "output1"))
		self.label_output2CN.setText(_translate("MainWindow", "Failure strain of cable"))
		self.value_output2CN.setText(_translate("MainWindow", "output2"))
		self.label_output3CN.setText(_translate("MainWindow", "Displacement"))
		self.value_output3CN.setText(_translate("MainWindow", "output3"))
		self.label_output4CN.setText(_translate("MainWindow", "Force"))
		self.value_output4CN.setText(_translate("MainWindow", "output4"))
		self.label_output5CN.setText(_translate("MainWindow", "Energy"))
		self.value_output5CN.setText(_translate("MainWindow", "output5"))

		self.label_output1.setText(_translate("MainWindow", "Displacement"))
		self.value_output1.setText(_translate("MainWindow", "output1"))
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

		self.boundary_x1 = 1
		self.boundary_y1 = -1.5
		self.boundary_x2 = 2
		self.boundary_y2 = 1
		self.boundary_x3 = -1.8
		self.boundary_y3 = 2.2
		self.boundary_x4 = -2
		self.boundary_y4 = -1

		self.Rp_CN_draw = 0.6
		self.ex_CN_draw = -0.2
		self.ey_CN_draw = 0.3

		#self.x1_plus_draw = np.array([1.5,1.5,1.5,1.5])
		#self.y1_plus_draw = np.array([-0.45,-0.15,0.15,0.45])
		#self.x1_minu_draw = np.array([-1.5,-1.5,-1.5,-1.5]) 
		#self.y1_minu_draw = np.array([-0.45,-0.15,0.15,0.45]) 
		#self.x2_plus_draw = np.array([0.45,0.15,-0.15,-0.45]) 
		#self.y2_plus_draw = np.array([1.5,1.5,1.5,1.5]) 
		#self.x2_minu_draw = np.array([0.45,0.15,-0.15,-0.45])  
		#self.y2_minu_draw = np.array([-1.5,-1.5,-1.5,-1.5])

		self.alpha1_CN_draw = -30*np.pi/180
		self.alpha2_CN_draw = 60*np.pi/180
		self.d1_CN_draw = 0.3
		self.d2_CN_draw = 0.3 

		#self.penCN = QtGui.QPen()

	def set_boundary_x1(self, value):
		self.boundary_x1 = value
		self.update()

	def set_boundary_y1(self, value):
		self.boundary_y1 = value
		self.update()

	def set_boundary_x2(self, value):
		self.boundary_x2 = value
		self.update()

	def set_boundary_y2(self, value):
		self.boundary_y2 = value
		self.update()

	def set_boundary_x3(self, value):
		self.boundary_x3 = value
		self.update()

	def set_boundary_y3(self, value):
		self.boundary_y3 = value
		self.update()

	def set_boundary_x4(self, value):
		self.boundary_x4 = value
		self.update()

	def set_boundary_y4(self, value):
		self.boundary_y4 = value
		self.update()

	def set_Rp_CN_draw(self, value):
		self.Rp_CN_draw = value
		self.update()

	def set_ex_CN_draw(self, value):
		self.ex_CN_draw = value
		self.update()

	def set_ey_CN_draw(self, value):
		self.ey_CN_draw = value
		self.update()
	
	def set_alpha1_CN_draw(self, value):
		self.alpha1_CN_draw = value*np.pi/180
		self.update()
	
	def set_alpha2_CN_draw(self, value):
		self.alpha2_CN_draw = value*np.pi/180
		self.update()
	
	def set_d1_CN_draw(self, value):
		self.d1_CN_draw = value
		self.update()
	
	def set_d2_CN_draw(self, value):
		self.d2_CN_draw = value
		self.update()

	'''
	def set_xQ1_plus_CN_draw(self, value):
		self.xQ1_plus_CN_draw = value
		self.update()

	def set_yQ1_plus_CN_draw(self, value):
		self.yQ1_plus_CN_draw = value
		self.update()

	def set_xQ1_minu_CN_draw(self, value):
		self.xQ1_minu_CN_draw = value
		self.update()

	def set_yQ1_minu_CN_draw(self, value):
		self.yQ1_minu_CN_draw = value
		self.update()

	def set_xQ2_plus_CN_draw(self, value):
		self.xQ2_plus_CN_draw = value
		self.update()

	def set_yQ2_plus_CN_draw(self, value):
		self.yQ2_plus_CN_draw = value
		self.update()

	def set_xQ2_minu_CN_draw(self, value):
		self.xQ2_minu_CN_draw = value
		self.update()

	def set_yQ2_minu_CN_draw(self, value):
		self.yQ2_minu_CN_draw = value
		self.update()
	'''
	def paintEvent(self,QPaintEvent):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.draw_boundary(qp)
		self.draw_lines(qp)
		self.draw_load_lines(qp)
		self.draw_ellipse(qp)
		self.draw_origin_xy(qp)
		qp.end()

	def draw_origin_xy(self, qp):
		pen_origin_xy = QtGui.QPen()
		pen_origin_xy.setStyle(QtCore.Qt.SolidLine)
		pen_origin_xy.setWidth(1)
		pen_origin_xy.setBrush(QtGui.QColor(0,0,0,255))  # 最后一个数字为0-255之间，表示透明度
		pen_origin_xy.setCapStyle(QtCore.Qt.RoundCap)
		pen_origin_xy.setJoinStyle(QtCore.Qt.RoundJoin)

		qp.setPen(pen_origin_xy)
		qp.setBrush(QtGui.QColor(0,0,0,255))
		qp.drawEllipse(self.width()/2-4, self.height()/2-4, 8, 8)
		qp.drawLine(0.5*self.width(), 0.5*self.height(), 0.5*self.width()+50, 0.5*self.height())  # 绘制x轴
		qp.drawLine(0.5*self.width(), 0.5*self.height(), 0.5*self.width(), 0.5*self.height()-50)  # 绘制y轴
		
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(True)

		qp.setFont(font)
		qp.drawText(0.5*self.width()+55, 0.5*self.height(),"x")
		qp.drawText(0.5*self.width(), 0.5*self.height()-55,"y")


	def draw_boundary(self, qp):
		pen_boundary = QtGui.QPen()
		pen_boundary.setStyle(QtCore.Qt.SolidLine)
		pen_boundary.setWidth(4)
		pen_boundary.setBrush(QtGui.QColor(0,0,0, 255))  # 最后一个数字为0-255之间，表示透明度
		pen_boundary.setCapStyle(QtCore.Qt.RoundCap)
		pen_boundary.setJoinStyle(QtCore.Qt.RoundJoin)

		x1_origin = self.boundary_x1
		y1_origin = self.boundary_y1
		x2_origin = self.boundary_x2
		y2_origin = self.boundary_y2
		x3_origin = self.boundary_x3
		y3_origin = self.boundary_y3
		x4_origin = self.boundary_x4
		y4_origin = self.boundary_y4

		x_max = max(x1_origin, x2_origin, x3_origin, x4_origin)
		x_min = min(x1_origin, x2_origin, x3_origin, x4_origin)
		y_max = max(y1_origin, y2_origin, y3_origin, y4_origin)
		y_min = min(y1_origin, y2_origin, y3_origin, y4_origin)

		max_abs_xy = max(abs(x_max),abs(x_min),abs(y_max),abs(y_min))
		min_width_height = min(self.width(), self.height())
		self.scale_xy = 0.45*min_width_height/max_abs_xy

		x1_scale = self.scale_xy*x1_origin
		y1_scale = self.scale_xy*y1_origin
		x2_scale = self.scale_xy*x2_origin
		y2_scale = self.scale_xy*y2_origin
		x3_scale = self.scale_xy*x3_origin
		y3_scale = self.scale_xy*y3_origin
		x4_scale = self.scale_xy*x4_origin
		y4_scale = self.scale_xy*y4_origin	

		x1_translate = x1_scale+self.width()/2
		y1_translate = self.height()/2 - y1_scale

		x2_translate = x2_scale+self.width()/2
		y2_translate = self.height()/2 - y2_scale

		x3_translate = x3_scale+self.width()/2
		y3_translate = self.height()/2 - y3_scale

		x4_translate = x4_scale+self.width()/2
		y4_translate = self.height()/2 - y4_scale

		qp.setPen(pen_boundary)
		qp.drawLine(x1_translate, y1_translate, x2_translate, y2_translate)
		qp.drawLine(x2_translate, y2_translate, x3_translate, y3_translate)
		qp.drawLine(x3_translate, y3_translate, x4_translate, y4_translate)
		qp.drawLine(x4_translate, y4_translate, x1_translate, y1_translate)

		pen_point = QtGui.QPen()
		pen_point.setWidth(16)
		pen_point.setBrush(QtGui.QColor(0,0,0, 255))  # 最后一个数字为0-255之间，表示透明度

		qp.setPen(pen_point)
		qp.drawPoint(x1_translate, y1_translate)
		qp.drawPoint(x2_translate, y2_translate)
		qp.drawPoint(x3_translate, y3_translate)
		qp.drawPoint(x4_translate, y4_translate)
		
		#font = QtGui.QFont()
		#font.setFamily("Times New Roman")
		#font.setPointSize(14)
		#font.setBold(False)
		#font.setItalic(True)
		#qp.setFont(font)
		#qp.drawText(x1_translate, y1_translate," (x1, y1)")
		#qp.drawText(x2_translate, y2_translate," (x2, y2)")
		#qp.drawText(x3_translate, y3_translate," (x3, y3)")
		#qp.drawText(x4_translate, y4_translate," (x4, y4)")
#
		pixmap_x1y1 = QtGui.QPixmap('x1y1.svg')
		pixmap_x2y2 = QtGui.QPixmap('x2y2.svg')
		pixmap_x3y3 = QtGui.QPixmap('x3y3.svg')
		pixmap_x4y4 = QtGui.QPixmap('x4y4.svg')

		# 发现缩放后不清晰
		# pixmap_x1y1 = pixmap_x1y1.scaledToHeight(20)
		# pixmap_x2y2 = pixmap_x2y2.scaledToHeight(20) 
		# pixmap_x3y3 = pixmap_x3y3.scaledToHeight(20) 
		# pixmap_x4y4 = pixmap_x4y4.scaledToHeight(20) 

		qp.drawPixmap(x1_translate+10, y1_translate+10,pixmap_x1y1)
		qp.drawPixmap(x2_translate+10, y2_translate-20,pixmap_x2y2)
		qp.drawPixmap(x3_translate+10, y3_translate-20,pixmap_x3y3)
		qp.drawPixmap(x4_translate+10, y4_translate+10,pixmap_x4y4)

	def draw_ellipse(self, qp):
		pen_ellipse = QtGui.QPen()
		pen_ellipse.setStyle(QtCore.Qt.SolidLine)
		pen_ellipse.setWidth(4)
		pen_ellipse.setBrush(QtGui.QColor(0,0,0,255))  # 最后一个数字为0-255之间，表示透明度
		pen_ellipse.setCapStyle(QtCore.Qt.RoundCap)
		pen_ellipse.setJoinStyle(QtCore.Qt.RoundJoin)

		Rp_ellipse = self.scale_xy*self.Rp_CN_draw
		ex_ellipse = self.scale_xy*self.ex_CN_draw
		ey_ellipse = self.scale_xy*self.ey_CN_draw

		xc_ellipse = ex_ellipse + self.width()/2
		yc_ellipse = self.height()/2 - ey_ellipse

		h_ellipse = 2*Rp_ellipse
		w_ellipse = 2*Rp_ellipse

		x0_ellipse = xc_ellipse - Rp_ellipse
		y0_ellipse = yc_ellipse - Rp_ellipse

		qp.setPen(pen_ellipse)
		qp.setBrush(QtGui.QColor(255,255,255,200))
		qp.drawEllipse(x0_ellipse, y0_ellipse, w_ellipse,h_ellipse)


		pen_exey = QtGui.QPen()
		pen_exey.setStyle(QtCore.Qt.DashLine)
		pen_exey.setWidth(1)
		pen_exey.setBrush(QtGui.QColor(255,0,0,255))  # 最后一个数字为0-255之间，表示透明度
		pen_exey.setCapStyle(QtCore.Qt.RoundCap)
		pen_exey.setJoinStyle(QtCore.Qt.RoundJoin)
		qp.setPen(pen_exey)
		qp.setBrush(QtGui.QColor(255,0,0,255))

		qp.drawEllipse(xc_ellipse-4, yc_ellipse-4, 8,8)
		pixmap_exey = QtGui.QPixmap('exey.svg')
		qp.drawPixmap(xc_ellipse-50, yc_ellipse-30,pixmap_exey)
		qp.drawLine(xc_ellipse,yc_ellipse,self.width()/2,self.height()/2)

	def draw_lines(self, qp):
		pen_line = QtGui.QPen()
		pen_line.setStyle(QtCore.Qt.DashDotLine)
		pen_line.setWidth(1)
		pen_line.setBrush(QtGui.QColor(0,0,0, 255))  # 最后一个数字为0-255之间，表示透明度
		pen_line.setCapStyle(QtCore.Qt.RoundCap)
		pen_line.setJoinStyle(QtCore.Qt.RoundJoin)

		m1_lines = int(max(self.width(), self.height())/(self.d1_CN_draw*self.scale_xy))
		m2_lines = int(max(self.width(), self.height())/(self.d2_CN_draw*self.scale_xy))

		delta_max_draw = max(self.width(), self.height())/self.scale_xy
		x1_plus_draw_grid = np.empty(2*m1_lines)
		y1_plus_draw_grid = np.empty(2*m1_lines)
		x1_minu_draw_grid = np.empty(2*m1_lines)
		y1_minu_draw_grid = np.empty(2*m1_lines)

		x2_plus_draw_grid = np.empty(2*m2_lines)
		y2_plus_draw_grid = np.empty(2*m2_lines)
		x2_minu_draw_grid = np.empty(2*m2_lines)
		y2_minu_draw_grid = np.empty(2*m2_lines)

		if abs(np.sin(self.alpha1_CN_draw))<1e-8:
			x1_plus_draw_grid = (self.ex_CN_draw + delta_max_draw)*np.ones(2*m1_lines)
			y1_plus_draw_grid = self.ey_CN_draw + 0.5*self.d1_CN_draw + np.arange(-m1_lines,m1_lines)*self.d1_CN_draw
			x1_minu_draw_grid = (self.ex_CN_draw - delta_max_draw)*np.ones(2*m1_lines)
			y1_minu_draw_grid = self.ey_CN_draw + 0.5*self.d1_CN_draw + np.arange(-m1_lines,m1_lines)*self.d1_CN_draw
		elif abs(np.cos(self.alpha1_CN_draw))<1e-8<1e-8:
			x1_plus_draw_grid = self.ex_CN_draw + 0.5*self.d1_CN_draw + np.arange(-m1_lines,m1_lines)*self.d1_CN_draw
			y1_plus_draw_grid = (self.ey_CN_draw + delta_max_draw)*np.ones(2*m1_lines)
			x1_minu_draw_grid = self.ex_CN_draw + 0.5*self.d1_CN_draw + np.arange(-m1_lines,m1_lines)*self.d1_CN_draw
			y1_minu_draw_grid = (self.ey_CN_draw - delta_max_draw)*np.ones(2*m1_lines)

		else:
			for i1_lines in range(-m1_lines,m1_lines):
				x1_plus_draw_grid[i1_lines] = self.ex_CN_draw + self.d1_CN_draw*(0.5+i1_lines)/np.sin(self.alpha1_CN_draw) + delta_max_draw
				y1_plus_draw_grid[i1_lines] = self.ey_CN_draw + np.tan(self.alpha1_CN_draw)*delta_max_draw
				x1_minu_draw_grid[i1_lines] = self.ex_CN_draw + self.d1_CN_draw*(0.5+i1_lines)/np.sin(self.alpha1_CN_draw) - delta_max_draw
				y1_minu_draw_grid[i1_lines] = self.ey_CN_draw - np.tan(self.alpha1_CN_draw)*delta_max_draw

		if abs(np.sin(self.alpha2_CN_draw))<1e-8:
			x2_plus_draw_grid = (self.ex_CN_draw + delta_max_draw)*np.ones(2*m2_lines)
			y2_plus_draw_grid = self.ey_CN_draw + 0.5*self.d2_CN_draw + np.arange(-m2_lines,m2_lines)*self.d2_CN_draw
			x2_minu_draw_grid = (self.ex_CN_draw - delta_max_draw)*np.ones(2*m2_lines)
			y2_minu_draw_grid = self.ey_CN_draw + 0.5*self.d2_CN_draw + np.arange(-m2_lines,m2_lines)*self.d2_CN_draw
		elif abs(np.cos(self.alpha2_CN_draw))<1e-8:
			x2_plus_draw_grid = self.ex_CN_draw + 0.5*self.d2_CN_draw + np.arange(-m2_lines,m2_lines)*self.d2_CN_draw
			y2_plus_draw_grid = (self.ey_CN_draw + delta_max_draw)*np.ones(2*m2_lines)
			x2_minu_draw_grid = self.ex_CN_draw + 0.5*self.d2_CN_draw + np.arange(-m2_lines,m2_lines)*self.d2_CN_draw
			y2_minu_draw_grid = (self.ey_CN_draw - delta_max_draw)*np.ones(2*m2_lines)
		else:
			for i2_lines in range(-m2_lines,m2_lines):
				x2_plus_draw_grid[i2_lines] = self.ex_CN_draw + self.d2_CN_draw*(0.5+i2_lines)/np.sin(self.alpha2_CN_draw) + delta_max_draw
				y2_plus_draw_grid[i2_lines] = self.ey_CN_draw + np.tan(self.alpha2_CN_draw)*delta_max_draw
				x2_minu_draw_grid[i2_lines] = self.ex_CN_draw + self.d2_CN_draw*(0.5+i2_lines)/np.sin(self.alpha2_CN_draw) - delta_max_draw
				y2_minu_draw_grid[i2_lines] = self.ey_CN_draw - np.tan(self.alpha2_CN_draw)*delta_max_draw

		x1_plus_draw_grid_scale = self.scale_xy*x1_plus_draw_grid
		y1_plus_draw_grid_scale = self.scale_xy*y1_plus_draw_grid
		x1_minu_draw_grid_scale = self.scale_xy*x1_minu_draw_grid
		y1_minu_draw_grid_scale = self.scale_xy*y1_minu_draw_grid
		x2_plus_draw_grid_scale = self.scale_xy*x2_plus_draw_grid
		y2_plus_draw_grid_scale = self.scale_xy*y2_plus_draw_grid
		x2_minu_draw_grid_scale = self.scale_xy*x2_minu_draw_grid
		y2_minu_draw_grid_scale = self.scale_xy*y2_minu_draw_grid

		x1_plus_draw_grid_translate = x1_plus_draw_grid_scale + self.width()/2
		y1_plus_draw_grid_translate = self.height()/2 - y1_plus_draw_grid_scale
		x1_minu_draw_grid_translate = x1_minu_draw_grid_scale + self.width()/2
		y1_minu_draw_grid_translate = self.height()/2 - y1_minu_draw_grid_scale
		x2_plus_draw_grid_translate = x2_plus_draw_grid_scale + self.width()/2
		y2_plus_draw_grid_translate = self.height()/2 - y2_plus_draw_grid_scale
		x2_minu_draw_grid_translate = x2_minu_draw_grid_scale + self.width()/2
		y2_minu_draw_grid_translate = self.height()/2 - y2_minu_draw_grid_scale

		qp.setPen(pen_line)
		for i in range(2*m1_lines):
			qp.drawLine(x1_plus_draw_grid_translate[i], y1_plus_draw_grid_translate[i], x1_minu_draw_grid_translate[i], y1_minu_draw_grid_translate[i])
		for j in range(2*m2_lines):
			qp.drawLine(x2_plus_draw_grid_translate[j], y2_plus_draw_grid_translate[j], x2_minu_draw_grid_translate[j], y2_minu_draw_grid_translate[j])

	def draw_load_lines(self, qp):
		self.m1_draw = 2*NPA_cable_net_v1_POP.func_round(self.Rp_CN_draw/self.d1_CN_draw)  # 第1方向上与加载区域相交的钢丝绳数量（偶数）
		self.m2_draw = 2*NPA_cable_net_v1_POP.func_round(self.Rp_CN_draw/self.d2_CN_draw)  # 第2方向上与加载区域相交的钢丝绳数量（偶数）
		xP1_plus, yP1_plus, zP1_plus, xP1_minu, yP1_minu, zP1_minu = NPA_cable_net_v1_POP.func_CN1_loaded_xPyP(self.m1_draw, self.d1_CN_draw, self.alpha1_CN_draw, self.Rp_CN_draw, 0, self.ex_CN_draw, self.ey_CN_draw)  # 1方向钢丝绳与加载区域边缘交点坐标
		xP2_plus, yP2_plus, zP2_plus, xP2_minu, yP2_minu, zP2_minu = NPA_cable_net_v1_POP.func_CN1_loaded_xPyP(self.m2_draw, self.d2_CN_draw, self.alpha2_CN_draw, self.Rp_CN_draw, 0, self.ex_CN_draw, self.ey_CN_draw)  # 2方向钢丝绳与加载区域边缘交点坐标

		# 求解计算过程中钢丝绳网片边界上力的作用点（Q点）坐标，方向1与方向2，Q点坐标不随加载位移的变换改变
		A1_arr, B1_arr, C1_arr = NPA_cable_net_v1_POP.func_CN1_solve_ABC(xP1_minu, yP1_minu, xP1_plus, yP1_plus)  # 与加载区域边缘相交的1方向的钢丝绳直线方程系数A1x+B1y+C1=0
		A2_arr, B2_arr, C2_arr = NPA_cable_net_v1_POP.func_CN1_solve_ABC(xP2_minu, yP2_minu, xP2_plus, yP2_plus)  # 与加载区域边缘相交的2方向的钢丝绳直线方程系数A2x+B2y+C2=0
	
		A_line12, B_line12, C_line12 = NPA_cable_net_v1_POP.func_CN1_solve_ABC(self.boundary_x1, self.boundary_y1, self.boundary_x2, self.boundary_y2)  # 边界线方程（锚点之间的连接线）A_linex+B_liney+C_line=0
		A_line23, B_line23, C_line23 = NPA_cable_net_v1_POP.func_CN1_solve_ABC(self.boundary_x2, self.boundary_y2, self.boundary_x3, self.boundary_y3)
		A_line34, B_line34, C_line34 = NPA_cable_net_v1_POP.func_CN1_solve_ABC(self.boundary_x3, self.boundary_y3, self.boundary_x4, self.boundary_y4)
		A_line41, B_line41, C_line41 = NPA_cable_net_v1_POP.func_CN1_solve_ABC(self.boundary_x4, self.boundary_y4, self.boundary_x1, self.boundary_y1)
	
		xQ1_line12, yQ1_line12 = NPA_cable_net_v1_POP.func_CN1_xy_intersection(A1_arr, B1_arr, C1_arr, A_line12, B_line12, C_line12)  # 钢丝绳直线束与边界线（锚点1与锚点2连线）的交点，方向1
		xQ1_line23, yQ1_line23 = NPA_cable_net_v1_POP.func_CN1_xy_intersection(A1_arr, B1_arr, C1_arr, A_line23, B_line23, C_line23)  # 钢丝绳直线束与边界线（锚点2与锚点3连线）的交点，方向1
		xQ1_line34, yQ1_line34 = NPA_cable_net_v1_POP.func_CN1_xy_intersection(A1_arr, B1_arr, C1_arr, A_line34, B_line34, C_line34)  # 钢丝绳直线束与边界线（锚点3与锚点4连线）的交点，方向1
		xQ1_line41, yQ1_line41 = NPA_cable_net_v1_POP.func_CN1_xy_intersection(A1_arr, B1_arr, C1_arr, A_line41, B_line41, C_line41)  # 钢丝绳直线束与边界线（锚点4与锚点1连线）的交点，方向1
	
		xQ2_line12, yQ2_line12 = NPA_cable_net_v1_POP.func_CN1_xy_intersection(A2_arr, B2_arr, C2_arr, A_line12, B_line12, C_line12)  # 钢丝绳直线束与边界线（锚点1与锚点2连线）的交点，方向2
		xQ2_line23, yQ2_line23 = NPA_cable_net_v1_POP.func_CN1_xy_intersection(A2_arr, B2_arr, C2_arr, A_line23, B_line23, C_line23)  # 钢丝绳直线束与边界线（锚点2与锚点3连线）的交点，方向2
		xQ2_line34, yQ2_line34 = NPA_cable_net_v1_POP.func_CN1_xy_intersection(A2_arr, B2_arr, C2_arr, A_line34, B_line34, C_line34)  # 钢丝绳直线束与边界线（锚点3与锚点4连线）的交点，方向2
		xQ2_line41, yQ2_line41 = NPA_cable_net_v1_POP.func_CN1_xy_intersection(A2_arr, B2_arr, C2_arr, A_line41, B_line41, C_line41)  # 钢丝绳直线束与边界线（锚点4与锚点1连线）的交点，方向2
	
		xQ1_pick, yQ1_pick = NPA_cable_net_v1_POP.func_CN1_pick_xQyQ(self.m1_draw, xQ1_line12, yQ1_line12, xQ1_line23, yQ1_line23, xQ1_line34, yQ1_line34, xQ1_line41, yQ1_line41, self.boundary_x1, self.boundary_y1, self.boundary_x2, self.boundary_y2, self.boundary_x3, self.boundary_y3, self.boundary_x4, self.boundary_y4)  # 挑选出边界线段范围内的交点，方向1
		xQ2_pick, yQ2_pick = NPA_cable_net_v1_POP.func_CN1_pick_xQyQ(self.m2_draw, xQ2_line12, yQ2_line12, xQ2_line23, yQ2_line23, xQ2_line34, yQ2_line34, xQ2_line41, yQ2_line41, self.boundary_x1, self.boundary_y1, self.boundary_x2, self.boundary_y2, self.boundary_x3, self.boundary_y3, self.boundary_x4, self.boundary_y4)  # 挑选出边界线段范围内的交点，方向2
	
		xQ1_plus, yQ1_plus, xQ1_minu, yQ1_minu = NPA_cable_net_v1_POP.func_CN1_sort_xQyQ(self.m1_draw, xQ1_pick, yQ1_pick, xP1_plus, yP1_plus, xP1_minu, yP1_minu)  # 对挑选出来的交点进行重新排序，使得边界线上的交点与加载边缘上的交点一一对应，与实际钢丝绳网中匹配关系一致，方向1
		xQ2_plus, yQ2_plus, xQ2_minu, yQ2_minu = NPA_cable_net_v1_POP.func_CN1_sort_xQyQ(self.m2_draw, xQ2_pick, yQ2_pick, xP2_plus, yP2_plus, xP2_minu, yP2_minu)  # 对挑选出来的交点进行重新排序，使得边界线上的交点与加载边缘上的交点一一对应，与实际钢丝绳网中匹配关系一致，方向2
	
		self.x1_plus_draw = np.asarray(xQ1_plus,dtype='float')
		self.y1_plus_draw = np.asarray(yQ1_plus,dtype='float')
		self.x1_minu_draw = np.asarray(xQ1_minu,dtype='float')
		self.y1_minu_draw = np.asarray(yQ1_minu,dtype='float')
		self.x2_plus_draw = np.asarray(xQ2_plus,dtype='float')
		self.y2_plus_draw = np.asarray(yQ2_plus,dtype='float')
		self.x2_minu_draw = np.asarray(xQ2_minu,dtype='float')
		self.y2_minu_draw = np.asarray(yQ2_minu,dtype='float')

		x1_plus_draw_scale = self.scale_xy*self.x1_plus_draw
		y1_plus_draw_scale = self.scale_xy*self.y1_plus_draw
		x1_minu_draw_scale = self.scale_xy*self.x1_minu_draw
		y1_minu_draw_scale = self.scale_xy*self.y1_minu_draw
		x2_plus_draw_scale = self.scale_xy*self.x2_plus_draw
		y2_plus_draw_scale = self.scale_xy*self.y2_plus_draw
		x2_minu_draw_scale = self.scale_xy*self.x2_minu_draw
		y2_minu_draw_scale = self.scale_xy*self.y2_minu_draw

		x1_plus_draw_translate = x1_plus_draw_scale + self.width()/2
		y1_plus_draw_translate = self.height()/2 - y1_plus_draw_scale
		x1_minu_draw_translate = x1_minu_draw_scale + self.width()/2
		y1_minu_draw_translate = self.height()/2 - y1_minu_draw_scale
		x2_plus_draw_translate = x2_plus_draw_scale + self.width()/2
		y2_plus_draw_translate = self.height()/2 - y2_plus_draw_scale
		x2_minu_draw_translate = x2_minu_draw_scale + self.width()/2
		y2_minu_draw_translate = self.height()/2 - y2_minu_draw_scale

		pen_load_line1 = QtGui.QPen()
		pen_load_line1.setStyle(QtCore.Qt.SolidLine)
		pen_load_line1.setWidth(2)
		pen_load_line1.setBrush(QtGui.QColor(100, 149, 237, 255))  # 最后一个数字为0-255之间，表示透明度
		pen_load_line1.setCapStyle(QtCore.Qt.RoundCap)
		pen_load_line1.setJoinStyle(QtCore.Qt.RoundJoin)
		qp.setPen(pen_load_line1)

		for i in range(len(x1_plus_draw_translate)):
			qp.drawLine(x1_plus_draw_translate[i], y1_plus_draw_translate[i], x1_minu_draw_translate[i], y1_minu_draw_translate[i])
		
		pen_load_line2 = QtGui.QPen()
		pen_load_line2.setStyle(QtCore.Qt.SolidLine)
		pen_load_line2.setWidth(2)
		pen_load_line2.setBrush(QtGui.QColor(255,0,0, 255))  # 最后一个数字为0-255之间，表示透明度
		pen_load_line2.setCapStyle(QtCore.Qt.RoundCap)
		pen_load_line2.setJoinStyle(QtCore.Qt.RoundJoin)
		qp.setPen(pen_load_line2)

		for j in range(len(x2_plus_draw_translate)):
			qp.drawLine(x2_plus_draw_translate[j], y2_plus_draw_translate[j], x2_minu_draw_translate[j], y2_minu_draw_translate[j])

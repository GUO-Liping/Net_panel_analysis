#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Name： NetPanelAnalysis
Function: 计算环形网片顶破力、顶破位移、耗能能力
Note: 国际单位制
Version: 1.0.2
Author: Liping GUO
Date: 2020/3/5
Remark: 影响计算结果的因素还有：
	(1)直线传力纤维与变形后的环网曲面传力路径之间的角度差异; 
	(2)三环环链拉伸代表了一种网环受力的最不利情形，实际网片中传力路径上环网轴向应力发展程度可能高于环链试验值
log: 计算部分，未完全实现界面与逻辑的分离。
'''
from PyQt5.QtWidgets import QMainWindow
import numpy as np
from test_UI import *
import cable_net_v1_POP

#dd = np.asarray(a.split(','),dtype='float')  # 将坐标转换为数组
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 用于开始计算ring net
        self.pushButton.clicked.connect(self.slot_computeRN)
        # 用于绘图参数改变 ring net
        self.value_input_height.textChanged.connect(self.slot_height_change)
        self.value_input_width.textChanged.connect(self.slot_width_change)
        self.value_input_nw.valueChanged.connect(self.slot_nw_change)
        
        # 用于开始计算cable net
        self.pushButtonCN.clicked.connect(self.slot_computeCN)
        # 用于绘图参数改变 ring net
        self.value_input_x1y1_CN.textChanged.connect(self.slot_boundary_x1y1_change)
        self.value_input_x2y2_CN.textChanged.connect(self.slot_boundary_x2y2_change)
        self.value_input_x3y3_CN.textChanged.connect(self.slot_boundary_x3y3_change)
        self.value_input_x4y4_CN.textChanged.connect(self.slot_boundary_x4y4_change)

        self.value_input_Rp_CN.textChanged.connect(self.slot_input_Rp_CN_change)
        self.value_input_ex_CN.textChanged.connect(self.slot_input_ex_CN_change)
        self.value_input_ey_CN.textChanged.connect(self.slot_input_ey_CN_change)

        self.value_input_alpha1_CN.textChanged.connect(self.slot_input_alpha1_CN_change)
        self.value_input_alpha2_CN.textChanged.connect(self.slot_input_alpha2_CN_change)

        self.value_input_d1_CN.textChanged.connect(self.slot_input_d1_CN_change)
        self.value_input_d2_CN.textChanged.connect(self.slot_input_d2_CN_change)

    def slot_height_change(self):
        value = self.value_input_height.text()
        try:
            float(value)
            self.areaRN.setHeightValue(abs(float(value)))

        except ValueError:
            self.areaRN.setHeightValue(1)

    def slot_width_change(self):
        value = self.value_input_width.text()
        try:
            float(value)
            self.areaRN.setWidthValue(abs(float(value)))

        except ValueError:
            self.areaRN.setWidthValue(1)

    def slot_nw_change(self):
        value = self.value_input_nw.value()
        self.areaRN.setPenWidth(value)

    def slot_computeRN(self):
        self.nw = self.value_input_nw.value()
        self.wx_origin = float(self.value_input_width.text())
        self.wy_origin = float(self.value_input_height.text())
        self.ks = float(self.value_input_ks.text())
        self.d = float(self.value_input_D.text())/1000
        self.Rp = float(self.value_input_Rp.text())
        self.sigma_y = 1770e6
        self.ls0 = 0.05

        dmin = self.func_choose_dmin(self.nw)
        A = self.nw * np.pi * dmin ** 2 / 4  # 单肢截面面积
        wx = max(self.wx_origin, self.wy_origin) - self.ls0  # 指定最小尺寸的弹簧-纤维单元在x方向

        wy = min(self.wx_origin, self.wy_origin) - self.ls0  # 指定最小尺寸的弹簧-纤维单元不在y方向

        ax = np.pi * self.d / 2 * wy / (wx + wy)  # 加载区域x方向网环边长
        ay = np.pi * self.d / 2 * wx / (wx + wy)  # 加载区域y方向网环边长

        mx = self.func_round(self.Rp / ax)
        my = self.func_round(self.Rp / ay)

        # 环链试验----------------------------------------------------------------------------------- #
        FN1, FN2, lN0, lN1, lN2, gama_N1, gama_N2 = self.func_ringChianDataFit()
        Ef1 = FN1 * lN0 / (2 * A * (lN1 - lN0))
        Ef2 = (FN2 - FN1) * lN0 / (2 * A * (lN2 - lN1))

        h0 = 0
        L0_x = self.func_vector_x_direction(wx, mx, ax, wy, h0)
        L0_y = self.func_vector_y_direction(wy, my, ay, wx, h0)
        lf0_x = L0_x - self.ls0
        lf0_y = L0_y - self.ls0

        K1_x = 1 / (lf0_x / (Ef1 * A) + 1 / self.ks)
        K2_x = 1 / (lf0_x / (Ef2 * A) + 1 / self.ks)
        K1_y = 1 / (lf0_y / (Ef1 * A) + 1 / self.ks)
        K2_y = 1 / (lf0_y / (Ef2 * A) + 1 / self.ks)
        h1, h2 = self.compute_height(L0_x, K1_x, K2_x, gama_N1, gama_N2, A)
        # 计算变形----------------------------------------------------------------------------------- #
        L1_x = self.func_vector_x_direction(wx, mx, ax, wy, h1)
        L1_y = self.func_vector_x_direction(wy, my, ay, wx, h1)
        ls1_x = (Ef1 * A * (L1_x - lf0_x) + self.ks * self.ls0 * lf0_x) / (self.ks * lf0_x + Ef1 * A)
        ls1_y = (Ef1 * A * (L1_y - lf0_y) + self.ks * self.ls0 * lf0_y) / (self.ks * lf0_y + Ef1 * A)
        lf1_x = (self.ks * lf0_x * (L1_x - self.ls0) + Ef1 * A * lf0_x) / (self.ks * lf0_x + Ef1 * A)
        lf1_y = (self.ks * lf0_y * (L1_y - self.ls0) + Ef1 * A * lf0_y) / (self.ks * lf0_y + Ef1 * A)
        L2_x = self.func_vector_x_direction(wx, mx, ax, wy, h2)
        L2_y = self.func_vector_x_direction(wy, my, ay, wx, h2)
        ls2_x = (Ef2 * A / lf0_x * (L2_x - lf1_x) + self.ks * ls1_x) / (self.ks + Ef2 * A / lf0_x)
        ls2_y = (Ef2 * A / lf0_y * (L2_y - lf1_y) + self.ks * ls1_y) / (self.ks + Ef2 * A / lf0_y)
        lf2_x = (self.ks * (L2_x - ls1_x) + lf1_x * Ef2 * A / lf0_x) / (self.ks + Ef2 * A / lf0_x)
        lf2_y = (self.ks * (L2_y - ls1_y) + lf1_y * Ef2 * A / lf0_y) / (self.ks + Ef2 * A / lf0_y)
        # 计算顶破力----------------------------------------------------------------------------------- #
        F1_x = K1_x * (L1_x - L0_x)
        gama_N1_x = F1_x / (A * self.sigma_y)
        F1_y = K1_y * (L1_y - L0_y)
        gama_N1_y = F1_y / (A * self.sigma_y)
        # 初始化并修正单元轴力、轴向应力发展程度系数----------------------------------------------------------- #
        init_F2_x = F1_x + K2_x * (L2_x - L1_x)
        init_gama_N2_x = init_F2_x / (A * self.sigma_y)
        F2_x, gama_N2_x = self.func_correct_gamaAndForce(mx, init_gama_N2_x, gama_N1, init_F2_x, K1_x, L2_x, L0_x, A)
        init_F2_y = F1_y + K2_y * (L2_y - L1_y)
        init_gama_N2_y = init_F2_y / (A * self.sigma_y)
        F2_y, gama_N2_y = self.func_correct_gamaAndForce(my, init_gama_N2_y, gama_N1, init_F2_y, K1_y, L2_y, L0_y, A)
        # 计算能量----------------------------------------------------------------------------------- #
        Energy1_x = K1_x * (L1_x - L0_x) ** 2 / 2
        Energy2_x = K1_x * L2_x * (L1_x - L0_x) + K1_x * (L0_x ** 2 - L1_x ** 2) / 2 + K2_x * (L2_x - L1_x) ** 2 / 2
        Energy1_y = K1_y * (L1_y - L0_y) ** 2 / 2
        Energy2_y = K1_y * L2_y * (L1_y - L0_y) + K1_y * (L0_y ** 2 - L1_y ** 2) / 2 + K2_y * (L2_y - L1_y) ** 2 / 2
        self.displacement = h2
        self.Force = 4 * np.sum(F2_x * h2 / L2_x, axis=0) + 4 * np.sum(F2_y * h2 / L2_y, axis=0)
        self.Energy = 4 * np.sum(Energy2_x, axis=0) + 4 * np.sum(Energy2_y, axis=0)
        self.gama_N2 = gama_N2
        self.ls2_min = min(ls2_x)
        self.lf2_min = min(lf2_x)
        self.func_output()

    def func_choose_dmin(self, para_nw):
        if para_nw < 5:
            para_dmin = 0.0022
        else:
            para_dmin = 0.003
        return para_dmin

    def func_round(self, number):
        if number % 1 == 0.5:
            number = number + 0.5
        else:
            number = round(number)
        return int(number)

    def func_ringChianDataFit(self):
        nw_array_all = np.array(
            [3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 7, 7, 7, 9, 9, 9, 9, 9, 9, 12, 12, 12, 16, 16, 16, 16, 16, 16, 19, 19,
             19, ])
        gama_Nmax_all = np.array(
            [0.24401, 0.38275, 0.27866, 0.28444, 0.34242, 0.30484, 0.36479, 0.38741, 0.3253, 0.34, 0.36, 0.38, 0.42744,
             0.40375, 0.36293, 0.35164, 0.31833, 0.40301, 0.41, 0.38, 0.32, 0.39305, 0.36725, 0.34754, 0.49815, 0.38193,
             0.45116, 0.4, 0.44, 0.5, 0.45348, 0.43676, 0.431])

        poly_gama_Nmax_all = np.polyfit(nw_array_all, gama_Nmax_all, 1)
        gama_N2 = np.polyval(poly_gama_Nmax_all, self.nw) + 0.05
        nw_array = np.array([3, 4, 5, 7, 9, 12, 16, 19])
        lN0 = 0.3 * 3
        delta_lN2_array = 0.001 * np.array([543.68, 539.67, 534.59, 534.92, 521.44, 522.54, 517.36, 507.92],
                                           dtype='float')
        poly_delta_lN2 = np.polyfit(nw_array, delta_lN2_array, 1)
        delta_lN2 = np.polyval(poly_delta_lN2, self.nw)
        dmin34, dmin519 = 0.0022, 0.003

        if self.nw < 5:
            FN2 = gama_N2 * self.sigma_y * 2 * self.nw * np.pi / 4 * dmin34 ** 2
        else:
            FN2 = gama_N2 * self.sigma_y * 2 * self.nw * np.pi / 4 * dmin519 ** 2

        lN2 = lN0 + delta_lN2
        FN1 = FN2 * 0.15
        lN1 = lN0 + delta_lN2 * 0.85
        gama_N1 = gama_N2 * 0.15

        return FN1, FN2, lN0, lN1, lN2, gama_N1, gama_N2

    def func_vector_x_direction(self, para_wx, para_mx, para_ax, para_wy, para_h):
        index_xi = np.linspace(1, para_mx, para_mx, endpoint=True)
        xu = para_ax * (index_xi - 1 / 2)
        yu = np.sqrt(self.Rp ** 2 - (para_ax * index_xi - para_ax / 2) ** 2)
        zu = np.zeros(para_mx) + para_h
        xd = para_wx * (index_xi - 1 / 2) / (2 * para_mx + 1)
        yd = np.zeros(para_mx) + para_wy / 2
        zd = np.zeros(para_mx) + 0
        length_element_xi = np.sqrt((xu - xd) ** 2 + (yu - yd) ** 2 + (zu - zd) ** 2)
        return length_element_xi

    def func_vector_y_direction(self, para_wy, para_my, para_ay, para_wx, para_h):
        index_yi = np.linspace(1, para_my, para_my, endpoint=True)
        xu = np.sqrt(self.Rp ** 2 - (para_ay * index_yi - para_ay / 2) ** 2)
        yu = para_ay * (index_yi - 1 / 2)
        zu = np.zeros(para_my) + para_h
        xd = np.zeros(para_my) + para_wx / 2
        yd = para_wy * (index_yi - 1 / 2) / (2 * para_my + 1)
        zd = np.zeros(para_my) + 0
        length_element_y = np.sqrt((xu - xd) ** 2 + (yu - yd) ** 2 + (zu - zd) ** 2)
        return length_element_y

    def compute_height(self, L0_x, K1_x, K2_x, gama_N1, gama_N2, A):
        min_L0_x = min(L0_x)
        max_K1_x = max(K1_x)
        max_K2_x = max(K2_x)
        min_L1_x = min_L0_x + gama_N1 * self.sigma_y * A / max_K1_x
        min_L2_x = min_L1_x + (gama_N2 * self.sigma_y * A - max_K1_x * (min_L1_x - min_L0_x)) / max_K2_x
        min_L0 = min_L0_x
        min_L1 = min_L1_x
        min_L2 = min_L2_x
        height1 = np.sqrt(min_L1 ** 2 - min_L0 ** 2)
        height2 = np.sqrt(min_L2 ** 2 - min_L0 ** 2)
        return height1, height2

    def func_correct_gamaAndForce(self, mx, gama_N2_x, gama_N1, F2_x, K1_x, L2_x, L0_x, A):
        for i in range(mx):
            if gama_N2_x[i] < gama_N1:
                F2_x[i] = K1_x[i] * (L2_x[i] - L0_x[i])
                gama_N2_x[i] = F2_x[i] / (self.sigma_y * A)
            else:
                pass
        return F2_x, gama_N2_x

    def func_output(self):

        self.value_output1.setText(str(format(self.displacement, '0.2f'))+' m')
        self.value_output2.setText(str(format(self.Force/1000, '0.2f'))+' kN')
        self.value_output3.setText(str(format(self.Energy/1000, '0.2f'))+' kJ')
        self.value_output4.setText(str(format(self.gama_N2, '0.2f')))
        self.value_output5.setText(str(format(self.ls2_min, '0.2f'))+' m')
        self.value_output6.setText(str(format(self.lf2_min, '0.2f'))+' m')

# ------------------------------------------------------------------------------------------#
# 将更改后的输入值在图像中更新
    def slot_boundary_x1y1_change(self):
        value0 = np.asarray(self.value_input_x1y1_CN.text().split(','),dtype='float')[0]
        value1 = np.asarray(self.value_input_x1y1_CN.text().split(','),dtype='float')[1]
        try:
            float(value0)
            float(value1)
            self.areaCN.set_boundary_x1(float(value0))
            self.areaCN.set_boundary_y1(float(value1))
        except ValueError:
            self.areaCN.set_boundary_x1(1.5)
            self.areaCN.set_boundary_y1(-1.5)

    def slot_boundary_x2y2_change(self):
        value0 = np.asarray(self.value_input_x2y2_CN.text().split(','),dtype='float')[0]
        value1 = np.asarray(self.value_input_x2y2_CN.text().split(','),dtype='float')[1]
        try:
            float(value0)
            float(value1)
            self.areaCN.set_boundary_x2(float(value0))
            self.areaCN.set_boundary_y2(float(value1))
        except ValueError:
            self.areaCN.set_boundary_x2(1.5)
            self.areaCN.set_boundary_y2(1.5)

    def slot_boundary_x3y3_change(self):
        value0 = np.asarray(self.value_input_x3y3_CN.text().split(','),dtype='float')[0]
        value1 = np.asarray(self.value_input_x3y3_CN.text().split(','),dtype='float')[1]
        try:
            float(value0)
            float(value1)
            self.areaCN.set_boundary_x3(float(value0))
            self.areaCN.set_boundary_y3(float(value1))
        except ValueError:
            self.areaCN.set_boundary_x3(-1.5)
            self.areaCN.set_boundary_y3(1.5)

    def slot_boundary_x4y4_change(self):
        value0 = np.asarray(self.value_input_x4y4_CN.text().split(','),dtype='float')[0]
        value1 = np.asarray(self.value_input_x4y4_CN.text().split(','),dtype='float')[1]
        try:
            float(value0)
            float(value1)
            self.areaCN.set_boundary_x4(float(value0))
            self.areaCN.set_boundary_y4(float(value1))
        except ValueError:
            self.areaCN.set_boundary_x4(-1.5)
            self.areaCN.set_boundary_y4(-1.5)

    def slot_input_Rp_CN_change(self):
        value = self.value_input_Rp_CN.text()
        try:
            float(value)
            self.areaCN.set_Rp_CN_draw(float(value))
        except ValueError:
            self.areaCN.set_Rp_CN_draw(0.5)

    def slot_input_ex_CN_change(self):
        value = self.value_input_ex_CN.text()
        try:
            float(value)
            self.areaCN.set_ex_CN_draw(float(value))
        except ValueError:
            self.areaCN.set_ex_CN_draw(0.0)

    def slot_input_ey_CN_change(self):
        value = self.value_input_ey_CN.text()
        try:
            float(value)
            self.areaCN.set_ey_CN_draw(float(value))
        except ValueError:
            self.areaCN.set_ey_CN_draw(0.0)

    def slot_input_alpha1_CN_change(self):
        value = self.value_input_alpha1_CN.text()
        try:
            float(value)
            self.areaCN.set_alpha1_CN_draw(float(value))
        except ValueError:
            self.areaCN.set_alpha1_CN_draw(0.0)

    def slot_input_alpha2_CN_change(self):
        value = self.value_input_alpha2_CN.text()
        try:
            float(value)
            self.areaCN.set_alpha2_CN_draw(float(value))
        except ValueError:
            self.areaCN.set_alpha2_CN_draw(0.0)

    def slot_input_d1_CN_change(self):
        value = self.value_input_d1_CN.text()
        try:
            float(value)
            if float(value)==0:
                self.areaCN.set_d1_CN_draw(0.3)
            else:
                self.areaCN.set_d1_CN_draw(float(value))
        except ValueError:
            self.areaCN.set_d1_CN_draw(0.3)

    def slot_input_d2_CN_change(self):
        value = self.value_input_d2_CN.text()
        try:
            float(value)
            if float(value)==0:
                self.areaCN.set_d2_CN_draw(0.3)
            else:
                 self.areaCN.set_d2_CN_draw(float(value))
        except ValueError:
            self.areaCN.set_d2_CN_draw(0.3)


    def slot_computeCN(self):
        self.E_young = float(self.value_input_E_CN.text())
        self.E_tangent = float(self.value_input_ET_CN.text())
        self.sigma_u = float(self.value_input_sigmau_CN.text())
        self.sigma_y = float(self.value_input_sigmay_CN.text())
        self.A_fibre = float(self.value_input_Acable_CN.text())
        self.Rp = float(self.value_input_Rp_CN.text())
        self.ex = float(self.value_input_ex_CN.text())
        self.ey = float(self.value_input_ey_CN.text())

        self.d1 = float(self.value_input_d1_CN.text())
        self.d2 = float(self.value_input_d2_CN.text())
        self.alpha1 = float(self.value_input_alpha1_CN.text())
        self.alpha2 = float(self.value_input_alpha2_CN.text())

        self.x1 = np.asarray(self.value_input_x1y1_CN.text().split(','),dtype='float')[0]
        self.y1 = np.asarray(self.value_input_x1y1_CN.text().split(','),dtype='float')[1]
        self.x2 = np.asarray(self.value_input_x2y2_CN.text().split(','),dtype='float')[0]
        self.y2 = np.asarray(self.value_input_x2y2_CN.text().split(','),dtype='float')[1]
        self.x3 = np.asarray(self.value_input_x3y3_CN.text().split(','),dtype='float')[0]
        self.y3 = np.asarray(self.value_input_x3y3_CN.text().split(','),dtype='float')[1]
        self.x4 = np.asarray(self.value_input_x4y4_CN.text().split(','),dtype='float')[0]
        self.y4 = np.asarray(self.value_input_x4y4_CN.text().split(','),dtype='float')[1]

        self.ks12 = float(self.value_input_ks12_CN.text())
        self.ks23 = float(self.value_input_ks23_CN.text())
        self.ks34 = float(self.value_input_ks34_CN.text())
        self.ks41 = float(self.value_input_ks41_CN.text())
        self.initial_sag = float(self.value_input_initial_sag_CN.text())

        input_kargs1_CN = {'E_young':self.E_young, 'E_tangent':self.E_tangent, 'sigma_y':self.sigma_y, 'sigma_u':self.sigma_u, 'A_fibre':self.A_fibre, 'Rp':self.Rp, 'ex':self.ex, 'ey':self.ey}
        input_kargs2_CN = {'d1':self.d1, 'd2':self.d2, 'alpha1':self.alpha1, 'alpha2':self.alpha2, 'x1':self.x1, 'y1':self.y1, 'x2':self.x2, 'y2':self.y2, 'x3':self.x3, 'y3':self.y3, 'x4':self.x4, 'y4':self.y4}
        input_kargs3_CN = {'ks12':self.ks12, 'ks23':self.ks23, 'ks34':self.ks34, 'ks41':self.ks41, 'initial_sag':self.initial_sag}
        input_kargs_CN = {**input_kargs1_CN,**input_kargs2_CN,**input_kargs3_CN}  # 合并字典

        self.Breaking_force_CN = cable_net_v1_POP.func_main_cable_net(input_kargs_CN)[0]
        self.Failure_strain_CN = cable_net_v1_POP.func_main_cable_net(input_kargs_CN)[1]
        self.Height_CN = cable_net_v1_POP.func_main_cable_net(input_kargs_CN)[2]
        self.Force_CN = cable_net_v1_POP.func_main_cable_net(input_kargs_CN)[3]
        self.Energy_CN = cable_net_v1_POP.func_main_cable_net(input_kargs_CN)[4]
        self.func_outputCN()

    def func_outputCN(self):

        self.value_output1CN.setText(str(format(self.Breaking_force_CN/1000, '0.3f'))+' kN')
        self.value_output2CN.setText(str(format(self.Failure_strain_CN, '0.3f'))+' ')
        self.value_output3CN.setText(str(format(self.Height_CN, '0.3f'))+' m')
        self.value_output4CN.setText(str(format(self.Force_CN/1000, '0.3f'))+' kN')
        self.value_output5CN.setText(str(format(self.Energy_CN/1000, '0.3f'))+' kJ')


    # 窗口关闭时的二次确认消息窗体
    def closeEvent(self, event):

        reply = QtWidgets.QMessageBox.question(self,'Message',"Are you sure to quit?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

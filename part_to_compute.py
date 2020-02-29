#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Name： Analytical method 1st Edition
Function: 计算环形网片顶破力、顶破位移、耗能能力
Note: 采用国际单位制
Version: 1.0.1
Author: Liping GUO
Date: 2020/2/27
Remark: 影响计算结果的因素还有：
	(1)直线传力纤维与变形后的环网曲面传力路径之间的角度差异; 
	(2)三环环链拉伸代表了一种网环受力的最不利情形，实际网片中传力路径上环网轴向应力发展程度可能低于环链试验值
'''

import numpy as np
import matplotlib.pyplot as plt

def func_vector_x_direction(para_wx, para_mx, para_ax, para_wy, para_h):
    index_xi = np.linspace(1, para_mx, para_mx, endpoint=True)

    xu = para_ax * (index_xi - 1/2)
    yu = np.sqrt(Rp**2 - (para_ax*index_xi - para_ax/2)**2)
    zu = np.zeros(para_mx) + para_h
    xd = para_wx * (index_xi-1/2)/(2*para_mx + 1)
    yd = np.zeros(para_mx) + para_wy/2
    zd = np.zeros(para_mx) + 0

    length_element_xi = np.sqrt((xu-xd)**2 + (yu-yd)**2 + (zu-zd)**2)
    return length_element_xi

def func_vector_y_direction(para_wy, para_my, para_ay, para_wx, para_h):
    index_yi = np.linspace(1, para_my, para_my, endpoint=True)

    xu = np.sqrt(Rp**2 - (para_ay*index_yi - para_ay/2)**2)
    yu = para_ay * (index_yi - 1/2)
    zu = np.zeros(para_my) + para_h
    xd = np.zeros(para_my) + para_wx/2
    yd = para_wy * (index_yi-1/2)/(2*para_my + 1)
    zd = np.zeros(para_my) + 0

    length_element_y = np.sqrt((xu-xd)**2 + (yu-yd)**2 + (zu-zd)**2)
    return length_element_y

def func_ringChianDataFit(nw,sigma_y):
    lN0 = 0.3*3

    nw_array = np.array([3,4,5,7,9,12,16,19],dtype='float')
    FN2_array = np.array([16.25e3,18.84e3,44.94e3,69.72e3,80.55e3,110.88e3,177.66e3,209.39e3],dtype='float')
    delta_lN2_array = 0.001*np.array([543.68,535.67,534.59,534.92,521.44,522.54,517.36,507.92],dtype='float')
    dmin1, dmin2 = 0.0022, 0.003
    Area_array = np.pi/4*np.hstack((dmin1**2*nw_array[nw_array<5], dmin2**2*nw_array[nw_array>=5]))
    gamaMax_array = FN2_array/(sigma_y*2*Area_array)

    poly_FN2_func = np.polyfit(nw_array, FN2_array,1)
    poly_delta_lN2_func = np.polyfit(nw_array, delta_lN2_array,1)
    poly_gamaMax_func = np.polyfit(nw_array, gamaMax_array,1)

    after_fit_FN2 = np.polyval(poly_FN2_func, nw)
    after_fit_delta_lN2 = np.polyval(poly_delta_lN2_func, nw)
    after_fit_lN2 = lN0 + after_fit_delta_lN2
    # after_fit_gamaMax = np.polyval(poly_gamaMax_func, nw) * 1.0
    # after_fit_gamaMax = np.array([0.34,0.35,0.36,0.38,0.40,0.43,0.47,0.5])
    after_fit_gamaMax = 0.5

    after_fit_gamaMax1 = np.polyval(poly_gamaMax_func, nw_array) * 1.0
    print('gamaMax_array=', gamaMax_array)
    print('after_fit_gamaMax1=', after_fit_gamaMax1)


    after_fit_FN1 = after_fit_FN2*0.15
    after_fit_lN1 = lN0 + after_fit_delta_lN2*0.85
    after_fit_gamaN1 = after_fit_gamaMax * 0.15

    return after_fit_FN1, after_fit_FN2, lN0, after_fit_lN1, after_fit_lN2, after_fit_gamaN1, after_fit_gamaMax

def func_round(number):
    if number % 1 == 0.5:
        number = number + 0.5
    else:
        number = round(number)
    return int(number)

def func_choose_dmin(para_nw):
	if para_nw < 5:
		para_dmin = 0.0022
	else:
		para_dmin = 0.003
	return para_dmin

# 参数输入----------------------------------------------------------------------------------- #
if __name__ == '__main__':

    nw = 19
    d = 0.3
    Rp = 0.5 
    dmin = func_choose_dmin(nw)
    wx_origin = 2.95
    wy_origin = 2.95
    sigma_y = 1770e6
    ks = 10000000000000  # 弹簧刚度，指代卸扣边界（刚体）
    ls0 = 0.05

    wx = wx_origin - ls0  
    wy = wy_origin - ls0

    A = nw * np.pi*dmin**2/4  # 单肢截面面积
    
    ax = np.pi*d/2 * wy/(wx+wy)  # 加载区域x方向网环边长
    ay = np.pi*d/2 * wx/(wx+wy)  # 加载区域y方向网环边长
    
    mx = func_round(Rp/ax)
    my = func_round(Rp/ay)
    
    # 环链试验----------------------------------------------------------------------------------- #
    FN1, FN2, lN0, lN1, lN2, gama_N1, gama_N2 = func_ringChianDataFit(nw, sigma_y)

    Ef1 = FN1*lN0/(2*A*(lN1 - lN0))
    Ef2 = (FN2-FN1)*lN0 / (2*A*(lN2 - lN1))

    L0_x = func_vector_x_direction(wx, mx, ax, wy, 0)
    L0_y = func_vector_y_direction(wy, my, ay, wx, 0)
    
    lf0_x = L0_x - ls0
    lf0_y = L0_y - ls0
    
    kf1_x = Ef1*A/lf0_x
    kf1_y = Ef1*A/lf0_y  
    
    kf2_x = Ef2*A/lf0_x
    kf2_y = Ef2*A/lf0_y
    
    # 计算变形----------------------------------------------------------------------------------- #
    
    L0_min = np.minimum(np.min(L0_x), np.min(L0_y))

    lf0_min = L0_min - ls0
    
    Ff1 = gama_N1*sigma_y*A
    Ff2 = gama_N2*sigma_y*A

    L1_min = L0_min + Ff1*lf0_min/(Ef1*A) + Ff1/ks
    L2_min = L0_min + Ff1*lf0_min/(Ef1*A) + (Ff2-Ff1)*lf0_min/(Ef2*A) + Ff2/ks
    
    # 勾股定理
    H1 = np.sqrt(L1_min**2 - L0_min**2)
    H2 = np.sqrt(L2_min**2 - L0_min**2)
    
    L1_x = func_vector_x_direction(wx, mx, ax, wy,H1)
    L1_y = func_vector_y_direction(wy, my, ay, wx, H1)
    
    L2_x = func_vector_x_direction(wx, mx, ax, wy,H2)
    L2_y = func_vector_y_direction(wx, mx, ax, wy,H2)
    
    # 计算力值----------------------------------------------------------------------------------- #
    
    F1_x = kf1_x*ks / (kf1_x + ks) * (L1_x-L0_x)
    F2_x = kf2_x*ks / (kf2_x + ks) * (L2_x - L0_x - Ff1/kf1_x + Ff1/kf2_x)

    for i in range(mx):
        if F1_x[i] > Ff1:  # 单肢截面面积取1/2FN1
            F1_x[i] = kf2_x[i]*ks / (kf2_x[i] + ks) * (L1_x[i] - L0_x[i] - Ff1/kf1_x[i] + Ff1/kf2_x[i])
        elif F2_x[i] < Ff1:
            F2_x[i] = kf1_x[i]*ks / (kf1_x[i] + ks) * (L2_x[i]-L0_x[i])
        else:
            pass         
    
    F1_y = kf1_y*ks / (kf1_y + ks) * (L1_y-L0_y)
    F2_y = kf2_y*ks / (kf2_y + ks) * (L2_y - L0_y - Ff1/kf1_y + Ff1/kf2_y)    
    
    for i in range(my):
        if F1_y[i] > Ff1:
            F1_y[i] = kf2_y[i]*ks / (kf2_y[i] + ks) * (L1_y[i] - L0_y[i] - Ff1/kf1_y[i] + Ff1/kf2_y[i])
        elif F2_y[i] < Ff1:
            F2_y[i] = kf1_y[i]*ks / (kf1_y[i] + ks) * (L2_y[i]-L0_y[i])
        else:
            pass 
   
    E1_x = 0.5*F1_x * (L1_x - L0_x)
    E2_x = 0.5*(Ff1*(L2_x - L0_x) + F2_x*(L2_x - L1_x))

    E1_y = 0.5*F1_y * (L1_y - L0_y)
    E2_y = 0.5*(Ff1*(L2_y - L0_y) + F2_y*(L2_y - L1_y))

    displacement = H2

    # 修正了加载区域边缘直线钢丝束如实际网曲面切线方向的差异（按修正30°考虑）
    Force = 4* np.sum(F2_x * np.cos(np.arccos(H2 / L2_x)-np.pi/6), axis=0) + 4* np.sum(F2_y * np.cos(np.arccos(H2 / L2_y)-np.pi/6),axis=0)
    Energy = 4*np.sum(E2_x, axis=0) + 4*np.sum(E2_y, axis=0)

    print('nw=', nw)
    print('gama_N2=', gama_N2)
    print('F2_y=', F2_y)
    print('Force = ', Force)
    print('displacement = ', displacement)
    print('Energy = ', Energy)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Name： Analytical method 1st Edition
Function: 计算环形网片顶破力、顶破位移、耗能能力
Note: 采用国际单位制
Version: 1.1
Author: Liping GUO
Date: 2020/2/27
'''

import numpy as np
import matplotlib.pyplot as plt

def func_vector(ax, ay, Rp, w, m, H):
    xu = np.empty(m)
    yu = np.empty(m)
    zu = np.empty(m)
    xd = np.empty(m)
    yd = np.empty(m)
    zd = np.empty(m)
    dx = np.empty(m)
    dy = np.empty(m)
    dz = np.empty(m)
    L = np.empty(m)

    for i in range(m):
        if w == wx:
            xu[i] = (i + 1) * ax - ax / 2
            yu[i] = np.sqrt(Rp ** 2 - ((i + 1) * ax - ax / 2) ** 2)
            zu[i] = H

            xd[i] = wx * ((i + 1) - 1/2) / (2 * mx + 1)
            yd[i] = wy / 2
            zd[i] = 0

            dx[i] = xu[i] - xd[i]
            dy[i] = yu[i] - yd[i]
            dz[i] = zu[i] - zd[i]
        elif w == wy:
            xu[i] = np.sqrt(Rp ** 2 - ((i + 1) * ay - ay / 2) ** 2)
            yu[i] = (i + 1) * ay - ay / 2
            zu[i] = H

            xd[i] = wx / 2
            yd[i] = wy * ((i + 1) - 1/2) / (2 * my + 1)
            zd[i] = 0

            dx[i] = xu[i] - xd[i]
            dy[i] = yu[i] - yd[i]
            dz[i] = zu[i] - zd[i]
        else:
            break

    L = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

    return L


def func_ringChainData(nw):
    lN0 = 0.3 * 3
    if nw == 3:
        FN2 = 17.57e3
        lN2 = lN0 + 508.36e-3
        FN1 = 0.15*FN2
        lN1 = lN0 + 508.36e-3*0.85
    elif nw == 4:
        FN2 = 31.12e3
        lN2 = lN0 + 534.48e-3
        FN1 = 0.15*FN2
        lN1 = lN0 + 534.48e-3*0.85
    elif nw == 5:
        FN2 = 44.94e3
        lN2 = lN0 + 507.92e-3
        FN1 = 0.15*FN2
        lN1 = lN0 + 507.92e-3*0.85
    elif nw == 7:
        FN2 = 69.72e3
        lN2 = lN0 + 521.44e-3
        FN1 = 0.15*FN2
        lN1 = lN0 + 521.44e-3*0.85
    elif nw == 9:
        FN2 = 80.55e3
        lN2 = lN0 + 535.67e-3
        FN1 = 0.15*FN2
        lN1 = lN0 + 535.67e-3*0.85       
    elif nw == 12:
        FN2 = 110.53e3
        lN2 = lN0 + 522.54e-3
        FN1 = 0.15*FN2
        lN1 = lN0 + 522.54e-3*0.85         
    elif nw == 16:
        FN2 = 177.66e3
        lN2 = lN0 + 534.92e-3
        FN1 = 0.15*FN2
        lN1 = lN0 + 534.92e-3*0.85 
    elif nw == 19:
        FN2 = 209.39e3
        lN2 = lN0 + 534.59e-3
        FN1 = 0.15*FN2
        lN1 = lN0 + 534.59e-3*0.85
    else:
        pass

    return FN1, FN2, lN1, lN2, lN0

def func_ringChianDataFit(nw,sigma_y):
    lN0 = 0.3*3

    nw_array = np.array([3,4,5,7,9,12,16,19],dtype='float')
    FN2_array = np.array([16.25e3,31.09e3,44.94e3,69.72e3,80.55e3,110.88e3,177.66e3,209.39e3],dtype='float')
    delta_lN2_array = 0.001*np.array([517.36,543.68,507.92,521.44,535.67,522.54,534.92,534.59,],dtype='float')
    
    dmin = 0.003
    Area_array = nw_array*np.pi*dmin**2/4 
    gamaMax_array = FN2_array/(sigma_y*2*Area_array)

    poly_FN2_func = np.polyfit(nw_array, FN2_array,1)
    poly_delta_lN2_func = np.polyfit(nw_array, delta_lN2_array,1)
    poly_gamaMax_func = np.polyfit(nw_array, gamaMax_array,1)

    after_fit_FN2 = np.polyval(poly_FN2_func, nw)
    after_fit_delta_lN2 = np.polyval(poly_delta_lN2_func, nw)
    after_fit_lN2 = lN0 + after_fit_delta_lN2
    after_fit_gamaMax = np.polyval(poly_gamaMax_func, nw)

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


# 参数输入----------------------------------------------------------------------------------- #
if __name__ == '__main__':

    nw = 7
    d = 0.3
    Rp = 0.5 
    dmin = 0.003
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

    L0_x = np.array(func_vector(ax, ay, Rp, wx, mx, 0))
    L0_y = np.array(func_vector(ax, ay, Rp, wy, my, 0))
    
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
    
    L1_x = np.array(func_vector(ax, ay, Rp, wx, mx, H1))
    L1_y = np.array(func_vector(ax, ay, Rp, wy, my, H1))
    
    L2_x = np.array(func_vector(ax, ay, Rp, wx, mx, H2))
    L2_y = np.array(func_vector(ax, ay, Rp, wy, my, H2))
    
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
    Force = 4* np.sum(F2_x * H2 / L2_x, axis=0) + 4* np.sum(F2_y * H2 / L2_y,axis=0)
    Energy = 4*np.sum(E2_x, axis=0) + 4*np.sum(E2_y, axis=0)

    print('nw=', nw)
    print('gama_N2=', gama_N2)
    print('F2_y=', F2_y)
    print('Force = ', Force)
    print('displacement = ', displacement)
    print('Energy = ', Energy)

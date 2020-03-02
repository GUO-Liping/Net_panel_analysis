#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Name： NetPanelAnalysis
Function: 计算环形网片顶破力、顶破位移、耗能能力
Note: 采用国际单位制
Version: 1.0.2
Author: Liping GUO
Date: 2020/3/2
Remark: 影响计算结果的因素还有：
	(1)直线传力纤维与变形后的环网曲面传力路径之间的角度差异; 
	(2)三环环链拉伸代表了一种网环受力的最不利情形，实际网片中传力路径上环网轴向应力发展程度可能高于环链试验值
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
    after_fit_gamaMax = np.polyval(poly_gamaMax_func, nw)

    after_fit_lN2 = lN0 + after_fit_delta_lN2

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

def func_inputData():
	nw = 7
	d = 0.3
	Rp = 0.5 
	wx_origin = 2.95
	wy_origin = 2.95
	sigma_y = 1770e6
	ks = 10000000000000  # 弹簧刚度，指代卸扣边界（刚体）
	ls0 = 0.05

	return nw, d, Rp, wx_origin, wy_origin, sigma_y, ks, ls0

# 参数输入----------------------------------------------------------------------------------- #
if __name__ == '__main__':

	nw, d, Rp, wx_origin, wy_origin, sigma_y, ks, ls0 = func_inputData()
	dmin = func_choose_dmin(nw)
	A = nw * np.pi*dmin**2/4  # 单肢截面面积

	wx = max(wx_origin,wy_origin) - ls0  # 指定最小尺寸的弹簧-纤维单元在x方向
	wy = min(wx_origin,wy_origin) - ls0  # 指定最小尺寸的弹簧-纤维单元不在y方向
	
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
	
	K1_x = 1 / (lf0_x/(Ef1*A)+1/ks)
	K2_x = 1 / (lf0_x/(Ef2*A)+1/ks)
	K1_y = 1 / (lf0_y/(Ef1*A)+1/ks)
	K2_y = 1 / (lf0_y/(Ef2*A)+1/ks)

	min_L0_x = min(L0_x)
	K1_xmax = max(K1_x)
	K2_xmax = max(K2_x)
	min_L1_x = min_L0_x + gama_N1*sigma_y*A/K1_xmax
	min_L2_x = min_L1_x + (gama_N2*sigma_y*A - K1_xmax*(min_L1_x-min_L0_x))/K2_xmax

	min_L0 = min_L0_x
	min_L1 = min_L1_x
	min_L2 = min_L2_x

	h1 = np.sqrt(min_L1**2 - min_L0**2)
	h2 = np.sqrt(min_L2**2 - min_L0**2)

	# 计算变形----------------------------------------------------------------------------------- #

	L1_x = func_vector_x_direction(wx, mx, ax, wy, h1)
	L2_x = func_vector_x_direction(wx, mx, ax, wy, h2)
	L1_y = func_vector_x_direction(wy, my, ay, wx, h1)
	L2_y = func_vector_x_direction(wy, my, ay, wx, h2)

	# 计算顶破力----------------------------------------------------------------------------------- #

	F1_x = K1_x * (L1_x - L0_x)
	F2_x = K1_x * (L1_x - L0_x) + K2_x*(L2_x-L1_x)
	F1_y = K1_y * (L1_y - L0_y)
	F2_y = K1_y * (L1_y - L0_y) + K2_y*(L2_y-L1_y)

	# 计算轴向应力发展程度----------------------------------------------------------------------------------- #

	gama_N1_x = F1_x/(A*sigma_y)
	gama_N2_x = F2_x/(A*sigma_y)
	gama_N1_y = F1_y/(A*sigma_y)
	gama_N2_y = F2_y/(A*sigma_y)

	# 修正单元轴力、轴向应力发展程度系数错误值----------------------------------------------------------------------------------- #

	for i in range(mx):
		if gama_N2_x[i] < gama_N1:
			F2_x[i] = K1_x[i] * (L2_x[i] - L0_x[i])
			gama_N2_x[i] = F2_x[i] / (sigma_y*A)
		else:
			pass

	for i in range(my):
		if gama_N2_y[i] < gama_N1:
			F2_y[i] = K1_y[i] * (L2_y[i] - L0_y[i])
			gama_N2_y[i] = F2_y[i] / (sigma_y*A)
		else:
			pass

	print('gama_N1_x=', gama_N1_x)
	print('gama_N2_x=', gama_N2_x)

	# 计算能量----------------------------------------------------------------------------------- # 

	E1_x = K1_x * (L1_x-L0_x)**2 / 2
	E2_x = K1_x * L2_x*(L1_x-L0_x) + K1_x*(L0_x**2-L1_x**2)/2 + K2_x*(L2_x-L1_x)**2 / 2
	E1_y = K1_y * (L1_y-L0_y)**2 / 2
	E2_y = K1_y * L2_y*(L1_y-L0_y) + K1_y*(L0_y**2-L1_y**2)/2 + K2_y*(L2_y-L1_y)**2 / 2

	displacement = h2
	Force = 4* np.sum(F2_x * h2 / L2_x, axis=0) + 4* np.sum(F2_y * h2 / L2_y,axis=0)
	Energy = 4*np.sum(E2_x, axis=0) + 4*np.sum(E2_y, axis=0)

	print('nw=', nw)
	print('gama_N2=', gama_N2)
	print('Force = ', Force)
	print('displacement = ', displacement)
	print('Energy = ', Energy)

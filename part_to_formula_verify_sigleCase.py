#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Name： NetPanelAnalysis
Function: 计算环形网片顶破力、顶破位移、耗能能力
Note: 国际单位制
Version: 1.0.2.alpha1
Author: Liping GUO
Date: 2020/4/1
Remark: 影响计算结果的因素还有：
	(1)直线传力纤维与变形后的环网曲面传力路径之间的角度差异 1.5F; 
	(2)三环环链拉伸代表了一种网环受力的最不利情形，实际网片中传力路径上环网轴向应力发展程度可能高于环链试验值+0.18
	(3)需保证夹持卡扣的强度，一旦卡扣强度不足，将发生钢丝滑移失效，造成网片承载力下降。
	(4) 该版本修正了一个错误：对应网环顶破试验，R3/2.2/300其实为R4/2.2/300，而R4/2.2/300其实为R4/3.0/300。
	(5)由于(3)中的原因，剔除了网片试验RN3对应的试验结果，只保留R4/3.0/300的试验结果
	(6)由于(3)中的原因，对于直径为2.2mm钢丝对应的网片规格R4/2.2/300，进行了单独计算
	(7)Bug: gamma_N2的拟合结果与FN2的拟合结果存在不一致情况
	(8)弹簧-纤维单元的双线性刚度特征，导致F_2及E_2在计算时每个单元分别修正与单元不同阶段实际刚度一致
'''

import numpy as np

def func_vector_x_direction(para_wx, para_mx, para_ax, para_wy, para_h, ex, ey):
	index_xi = np.linspace(1, para_mx, para_mx, endpoint=True)

	xu = para_ax * (index_xi - 1/2) + ex
	yu = np.sqrt(Rp**2 - (para_ax*index_xi - para_ax/2)**2) + ey
	zu = np.zeros(para_mx) + para_h
	xd = para_wx * (index_xi-1/2)/(2*para_mx + 1)
	yd = np.zeros(para_mx) + para_wy/2
	zd = np.zeros(para_mx) + 0

	length_element_xi = np.sqrt((xu-xd)**2 + (yu-yd)**2 + (zu-zd)**2)
	return length_element_xi

def func_vector_y_direction(para_wy, para_my, para_ay, para_wx, para_h, ex, ey):
	index_yi = np.linspace(1, para_my, para_my, endpoint=True)

	xu = np.sqrt(Rp**2 - (para_ay*index_yi - para_ay/2)**2) + ex
	yu = para_ay * (index_yi - 1/2) + ey
	zu = np.zeros(para_my) + para_h
	xd = np.zeros(para_my) + para_wx/2
	yd = para_wy * (index_yi-1/2)/(2*para_my + 1)
	zd = np.zeros(para_my) + 0

	length_element_y = np.sqrt((xu-xd)**2 + (yu-yd)**2 + (zu-zd)**2)
	return length_element_y

def func_ringChianDataFit(nw,sigma_y,d):
	lN0 = 0.3*3

	if d == 0.003:
		nw_array = np.array([4,5,7,9,12,16,19],dtype='float')
		FN2_array = np.array([30.064e3,44.937e3,69.72e3,80.547e3,110.884e3,177.66e3,209.387e3],dtype='float')
		delta_lN2_array = 0.001*np.array([515.05,518.67,508.59,489.92,490.644,475.54,472.36],dtype='float')
		Area_array = np.pi/4*d**2*nw_array
		# print('Area_array=',Area_array)
		gammaN2_array = FN2_array/(sigma_y*2*Area_array)
		# print('gammaN2_array111=', gammaN2_array)
	else:
		nw_array = np.array([3,4],dtype='float')
		FN2_array = np.array([9.87e3,17.57e3],dtype='float')
		delta_lN2_array = np.array([521.16e-3,517.36e-3],dtype='float')
		Area_array = np.pi/4*d**2*nw_array
		# print('Area_array=',Area_array)
		gammaN2_array = FN2_array/(sigma_y*2*Area_array)

	poly_delta_lN2_func = np.polyfit(nw_array, delta_lN2_array,1)
	poly_gammaN2_func = np.polyfit(nw_array, gammaN2_array,1)

	after_fit_delta_lN2 = np.polyval(poly_delta_lN2_func, nw)
	after_fit_gammaN2 = np.polyval(poly_gammaN2_func, nw) + 0.18
	'''
	对比五环试验与三环试验轴向力发展程度可发现，
	五环(5圈0.551，7圈0.554,9圈0.559)，三环(5圈0.359, 7圈0.398, 9圈0.358)
	分别大于三环(5圈0.192, 7圈0.156, 9圈0.201,)均值为0.183
	'''

	after_fit_FN2 = after_fit_gammaN2 * sigma_y*(2*nw*np.pi*d**2/4)
	after_fit_lN2 = lN0 + after_fit_delta_lN2
	after_fit_FN1 = after_fit_FN2*0.15
	after_fit_lN1 = lN0 + after_fit_delta_lN2*0.85
	after_fit_gammaN1 = after_fit_gammaN2 * 0.15

	return after_fit_FN1, after_fit_FN2, lN0, after_fit_lN1, after_fit_lN2, after_fit_gammaN1, after_fit_gammaN2

def func_round(number):
	if number % 1 == 0.5:
		number = number + 0.5
	else:
		number = round(number)
	return int(number)


def funcXY_correct(mx, gamma_N2_x, F2_x, E2_x, gamma_N1, K2_x, K1_x, L2_x, L1_x, L0_x, sigma_y, A):

	for i in range(mx):
		if gamma_N2_x[i] > gamma_N1:
			F2_x[i] = K1_x[i] * (L1_x[i] - L0_x[i]) + K2_x[i]*(L2_x[i]-L1_x[i])
			gamma_N2_x[i] = F2_x[i] / (sigma_y*A)
			E2_x[i] = K1_x[i] * L2_x[i]*(L1_x[i]-L0_x[i]) + K1_x[i]*(L0_x[i]**2-L1_x[i]**2)/2 + K2_x[i]*(L2_x[i]-L1_x[i])**2 / 2
		else:
			pass
	return gamma_N2_x, F2_x, E2_x


def compute_height(L0_x,K1_x,K2_x,gamma_N1,gamma_N2,sigma_y,A):
	min_L0_x = min(L0_x)
	max_K1_x = max(K1_x)
	max_K2_x = max(K2_x)
	min_L1_x = min_L0_x + gamma_N1*sigma_y*A/max_K1_x
	min_L2_x = min_L1_x + (gamma_N2*sigma_y*A - max_K1_x*(min_L1_x-min_L0_x))/max_K2_x

	min_L0 = min_L0_x
	min_L1 = min_L1_x
	min_L2 = min_L2_x

	height1 = np.sqrt(min_L1**2 - min_L0**2)
	height2 = np.sqrt(min_L2**2 - min_L0**2)

	return height1, height2


def func_sensitive(factor_star, factor_array,disp_array,forc_array,ener_array):
	index_ref = np.int(np.where(factor_array==factor_star)[0])
	print('index_ref=',index_ref)
	sens_disp_factor = np.abs((disp_array[index_ref+1]-disp_array[index_ref])/(factor_array[index_ref+1]-factor_star)*(factor_star/disp_array[index_ref]))
	sens_forc_factor = np.abs((forc_array[index_ref+1]-forc_array[index_ref])/(factor_array[index_ref+1]-factor_star)*(factor_star/forc_array[index_ref]))
	sens_ener_factor = np.abs((ener_array[index_ref+1]-ener_array[index_ref])/(factor_array[index_ref+1]-factor_star)*(factor_star/ener_array[index_ref]))

	return sens_disp_factor,sens_forc_factor,sens_ener_factor

def func_return_d(nw):
	if nw > 0:
		if nw <= 4:
			return 0.0022
		elif nw > 4:
			return 0.003
		else:
			raise ValueError
	else:
		raise ValueError


def func_test_exey(ex, ey, wx, wy, Rp):
	if abs(ex) <= wx/2 - Rp and abs(ey) <= wy/2 - Rp:
		pass
	else:
		raise ValueError


# 参数输入----------------------------------------------------------------------------------- #
if __name__ == '__main__':
	nw = 5
	d = func_return_d(nw)
	D = 0.3
	Rp = 0.5 
	kappa = 1
	ks = 500000000  # 弹簧刚度，指代卸扣边界（刚体）
	wx_origin = 3.0
	wy_origin = wx_origin*kappa
	ls0 = 0.05
	ex = 0.0
	ey = 0.0
	sigma_y = 1770e6

	A = nw * np.pi*d**2/4  # 单肢截面面积

	wx = max(wx_origin,wy_origin) - ls0  # 指定矩形网片最长边平行方向为x方向
	wy = min(wx_origin,wy_origin) - ls0  # 指定矩形网片最短边平行方向为y方向
	ax = np.pi*D/2 * wy/(wx+wy)  # 加载区域x方向网环边长
	ay = np.pi*D/2 * wx/(wx+wy)  # 加载区域y方向网环边长
	mx = func_round(Rp/ax)
	my = func_round(Rp/ay)
	
	func_test_exey(ex, ey, wx, wy, Rp)  # 
	# 环链试验----------------------------------------------------------------------------------- #

	FN1, FN2, lN0, lN1, lN2, gamma_N1, gamma_N2 = func_ringChianDataFit(nw, sigma_y, d)

	Ef1 = FN1*lN0/(2*A*(lN1 - lN0))
	Ef2 = (FN2-FN1)*lN0 / (2*A*(lN2 - lN1))
	
	L0_x = func_vector_x_direction(wx, mx, ax, wy, 0, ex, ey)
	L0_y = func_vector_y_direction(wy, my, ay, wx, 0, ex, ey)

	lf0_x = L0_x - ls0
	lf0_y = L0_y - ls0
	
	K1_x = 1 / (lf0_x/(Ef1*A)+1/ks)
	K2_x = 1 / (lf0_x/(Ef2*A)+1/ks)
	K1_y = 1 / (lf0_y/(Ef1*A)+1/ks)
	K2_y = 1 / (lf0_y/(Ef2*A)+1/ks)

	h1, h2 = compute_height(L0_x,K1_x,K2_x,gamma_N1,gamma_N2,sigma_y,A)

	# 计算变形----------------------------------------------------------------------------------- #
	L1_x = func_vector_x_direction(wx, mx, ax, wy, h1, ex, ey)
	L1_y = func_vector_x_direction(wy, my, ay, wx, h1, ex, ey)
	ls1_x = (Ef1*A*(L1_x-lf0_x)+ks*ls0*lf0_x) / (ks*lf0_x+Ef1*A)
	ls1_y = (Ef1*A*(L1_y-lf0_y)+ks*ls0*lf0_y) / (ks*lf0_y+Ef1*A)
	lf1_x = (ks*lf0_x*(L1_x-ls0)+Ef1*A*lf0_x) / (ks*lf0_x+Ef1*A)
	lf1_y = (ks*lf0_y*(L1_y-ls0)+Ef1*A*lf0_y) / (ks*lf0_y+Ef1*A)


	L2_x = func_vector_x_direction(wx, mx, ax, wy, h2, ex, ey)
	L2_y = func_vector_x_direction(wy, my, ay, wx, h2, ex, ey)
	ls2_x = (Ef2*A/lf0_x*(L2_x-lf1_x)+ks*ls1_x) / (ks+Ef2*A/lf0_x)
	ls2_y = (Ef2*A/lf0_y*(L2_y-lf1_y)+ks*ls1_y) / (ks+Ef2*A/lf0_y)
	lf2_x = (ks*(L2_x-ls1_x)+lf1_x*Ef2*A/lf0_x) / (ks+Ef2*A/lf0_x)
	lf2_y = (ks*(L2_y-ls1_y)+lf1_y*Ef2*A/lf0_y) / (ks+Ef2*A/lf0_y)

	# 计算顶破力----------------------------------------------------------------------------------- #

	F1_x = K1_x * (L1_x - L0_x)
	E1_x = K1_x * (L1_x - L0_x)**2 / 2
	gamma_N1_x = F1_x/(A*sigma_y)
	print(gamma_N1 )

	F1_y = K1_y * (L1_y - L0_y)
	E1_y = K1_y * (L1_y - L0_y)**2 / 2
	gamma_N1_y = F1_y/(A*sigma_y)

	# 初始化并修正单元轴力、轴向应力发展程度系数----------------------------------------------------------- #
	init_F2_x = K1_x*(L2_x-L0_x)
	init_E2_x = K1_x * (L2_x-L0_x)**2 / 2
	init_gamma_N2_x = init_F2_x/(A*sigma_y)

	gamma_N2_x, F2_x, E2_x = funcXY_correct(mx, init_gamma_N2_x, init_F2_x, init_E2_x, gamma_N1, K2_x, K1_x, L2_x, L1_x, L0_x, sigma_y, A)

	init_F2_y = K1_y*(L2_y-L0_y)
	init_E2_y = K1_y * (L2_y-L0_y)**2 / 2
	init_gamma_N2_y = init_F2_y/(A*sigma_y)

	gamma_N2_y, F2_y, E2_y = funcXY_correct(my, init_gamma_N2_y, init_F2_y, init_E2_y, gamma_N1, K2_y, K1_y, L2_y, L1_y, L0_y, sigma_y, A)

	# 计算能量----------------------------------------------------------------------------------- # 
	Displacement = h2
	Force = 4*np.sum(F2_x * h2 / L2_x, axis=0) + 4*np.sum(F2_y * h2 / L2_y,axis=0) * 1.4
	Energy = 4*np.sum(E2_x, axis=0) + 4*np.sum(E2_y, axis=0)

	print('Displacement = ', format(Displacement, '.3f'), 'm')
	print('Force = ', format(Force/1000, '.3f'), 'kN')
	print('Energy = ', format(Energy/1000, '.3f'), 'kJ')

	'''
	R19
	Displacement =  1.116 m
	Force =  1180.832 kN
	Energy =  120.232 kJ
	'''

	# np.set_printoptions(formatter={"float": lambda x: format(x, '.3f')})

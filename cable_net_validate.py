#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 本部分代码为求解旋转正方形网片产生面外变形后的钢丝绳长度，所有钢丝绳与y轴平行，仅旋转网片，用于校准另一种方法


import numpy as np
from userfunc_NPA import *


# 本部分代码用于校准另一种方法
def func_CN1_cablenet_test_xyz(theta, H, w, Rp, Rs, a, m):
	i_arr = np.arange(1,m+0.1,step=1)

	xP_arr = a/2*(2*i_arr - m - 1)
	yP_arr = np.sqrt(Rp**2 - xP_arr**2)
	zP_arr = H*np.ones_like(xP_arr)

	theta_1 = np.arcsin(xP_arr[-1]/(w/np.sqrt(2)))
	theta_2 = np.arccos(xP_arr[-1]/(w/np.sqrt(2)))
	if theta>=0 and theta<theta_1:
		m1 = int(m/2 - 1/2*func_round(np.sqrt(2)*w*np.sin(theta)/a))

		i1_arr = np.arange(1,m1+0.1,step=1)
		i2_arr = np.arange(m1+1,m+0.1,step=1)
		yQ1_arr = w/np.sqrt(2)*np.cos(theta) - abs(xP_arr[0] +w/np.sqrt(2)*np.sin(theta))*np.tan(np.pi/4+theta) + a*(i1_arr-1)*np.tan(np.pi/4+theta)
		yQ2_arr = w/np.sqrt(2)*np.cos(theta) - abs(xP_arr[m1]+w/np.sqrt(2)*np.sin(theta))*np.tan(np.pi/4-theta) - a*(i2_arr-m1-1)*np.tan(np.pi/4-theta)
	
		xQ_arr = xP_arr
		yQ_arr = np.concatenate((yQ1_arr,yQ2_arr))
		zQ_arr = np.zeros_like(xP_arr)

	elif theta>=theta_1 and theta<=theta_2:
		xQ_arr = xP_arr
		yQ_arr = w/np.sqrt(2)*np.cos(theta) - abs(xP_arr[0] +w/np.sqrt(2)*np.sin(theta))*np.tan(np.pi/4-theta) - a*(i_arr-1)*np.tan(np.pi/4-theta)
		zQ_arr = np.zeros_like(xP_arr)

	elif theta>theta_2 and theta<np.pi/2:
		m1 = m/2 - 1/2*func_round(np.sqrt(2)*w*np.cos(theta)/a)

		i1_arr = np.arange(1,m1+0.1,step=1)
		i2_arr = np.arange(m1+1,m+0.1,step=1)
		yQ1_arr = w/np.sqrt(2)*np.sin(theta) - abs(xP_arr[0] -w/np.sqrt(2)*np.cos(theta))*np.tan(theta-np.pi/4) + a*(i1_arr-1)*np.tan(theta-np.pi/4)
		yQ2_arr = w/np.sqrt(2)*np.sin(theta) - abs(xP_arr[m1]-w/np.sqrt(2)*np.cos(theta))*np.tan(3*np.pi/4-theta) - a*(i2_arr-m1-1)*np.tan(3*np.pi/4-theta)
			
		xQ_arr = xP_arr
		yQ_arr1 = np.concatenate((yQ1_arr,yQ2_arr))
		zQ_arr = np.zeros_like(xP_arr)
	else:
		raise ValueError

	Lu_PQ = np.sqrt((xQ_arr-xP_arr)**2 + (yQ_arr-yP_arr)**2 + (zQ_arr-zP_arr)**2)
	Ld_PQ = Lu_PQ[::-1]

	if H == 0:
		Lc_PQ = 2*yP_arr
	else:
		Lc_PQ = 2*np.sqrt(Rs**2-xP_arr**2) * np.arctan(np.sqrt(Rp**2-xP_arr**2)/np.sqrt(Rs**2-Rp**2))		

	return Lu_PQ, Lc_PQ, Ld_PQ


# 参数输入----------------------------------------------------------------------------------- #
if __name__ == '__main__':

	Rs = 1.2  # 球罐形加载顶头半径
	Rp = 0.5  # 加载顶头水平投影半径，若加载形状为多边形时考虑为半径为Rp圆内切
	H = 0.55  # 钢丝绳网任意面外高度
	d= 0.3  # 本程序可以用于计算两侧不同的a值（网孔间距）
	m = 2*func_round(Rp/d)  # 第1方向上与加载区域相交的钢丝绳数量（偶数）
	x_1st, y_1st = 1.5, 1.5  # 位于第一象限内的边界角点，特征角度theta_use

	w = np.sqrt(2*(x_1st**2+y_1st**2))
	theta_use = np.arctan(y_1st/x_1st)
	L_left_PQ = func_CN1_cablenet_test_xyz(theta_use, H, w, Rp, Rs, d, m)[0]
	L_center_PQ = func_CN1_cablenet_test_xyz(theta_use, H, w, Rp, Rs, d, m)[1]
	L_right_PQ0 = func_CN1_cablenet_test_xyz(theta_use, H, w, Rp, Rs, d, m)[2]
	L_PQ = L_left_PQ + L_center_PQ + L_right_PQ0

	print('L_PQ0=',L_PQ)

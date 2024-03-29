#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 与cable_net_v1.0版本相比，改进了计算过程，可以绘制全过程曲线

'''
Name： NetPanelAnalysis
Function: 计算柔性防护系统中任意四边形钢丝绳网片顶破力、顶破位移、耗能能力
Note: 国际单位制
Version: 1.2.1
Author: Liping GUO
Date: from 2021/8/31 to 2021/11/9
命名规则：以平行于1方向及2方向分别作为后缀
Remark: 尚未解决的问题：
	(1)考虑矩形之外的网孔形状
	(2)考虑柔性边界刚度
'''

import numpy as np
import matplotlib.pyplot as plt

def func_choose_Origin_xyz_coordinate():  # 判断计算模型采用的坐标原点位置为钢丝绳网片几何中心位置的网孔中心‘centre’，还是采用网孔角点'corner'
	#Origin_xyz_coordinate = 'centre'
	Origin_xyz_coordinate = 'corner'
	return Origin_xyz_coordinate
# 本函数用于考虑更细致的情形：加载高度处于顶头自身高度之内，目前尚不完善
#def func_CN1_lengthArc(H,Rs,Rp,a_DireX,m_DireX,a_DireY,m_DireY):
#	i_DireX = np.arange(1,m_DireX+0.1,step=1)
#	i_DireY = np.arange(1,m_DireY+0.1,step=1)
#
#	d_DireX = abs(a_DireX/2*(2*i_DireX - m_DireX - 1))
#	d_DireY = abs(a_DireY/2*(2*i_DireY - m_DireY - 1))
#
#	minH = Rs-np.sqrt(Rs**2-Rp**2)
#	if H>0.0 and H < minH:
#		Rp_H = np.sqrt(Rs**2-(Rs-H)**2)
#		beta_DireX = np.zeros_like(d_DireX)
#		beta_DireY = np.zeros_like(d_DireY)
#		arc_length_DireX = np.zeros_like(d_DireX)
#		arc_length_DireY = np.zeros_like(d_DireY)
#
#		for iDX in range(len(d_DireX)):
#			if abs(d_DireX[iDX])<Rp_H:
#				beta_DireX[iDX] = 2*np.arccos((Rs-H)/np.sqrt(Rs**2-d_DireX[iDX]**2))
#				arc_length_DireX[iDX] = beta_DireX[iDX]*np.sqrt(Rs**2-d_DireX[iDX]**2)
#			else:
#				arc_length_DireX[iDX] = 2*np.sqrt(Rp**2 - d_DireX[iDX]**2)
#		
#		for iDY in range(len(d_DireY)):
#			if abs(d_DireY[iDY])<Rp_H:
#				beta_DireY[iDY] = 2*np.arccos((Rs-H)/np.sqrt(Rs**2-d_DireY[iDY]**2))
#				arc_length_DireY[iDY] = beta_DireY[iDY]*np.sqrt(Rs**2-d_DireY[iDY]**2)
#			else:
#				arc_length_DireY[iDY] = 2*np.sqrt(Rp**2 - d_DireY[iDY]**2)
#
#	elif H >= minH:
#		alpha_DireX = 2*np.arctan(np.sqrt((Rp**2-d_DireX**2)/(Rs**2-Rp**2)))
#		alpha_DireY = 2*np.arctan(np.sqrt((Rp**2-d_DireY**2)/(Rs**2-Rp**2)))
#		arc_length_DireX = alpha_DireX*np.sqrt(Rs**2-d_DireX**2)
#		arc_length_DireY = alpha_DireY*np.sqrt(Rs**2-d_DireY**2)
#	elif H <= 0.0:
#		arc_length_DireX = 2*np.sqrt(Rp**2 - d_DireX**2)
#		arc_length_DireY = 2*np.sqrt(Rp**2 - d_DireY**2)
#	else:
#		raise ValueError
#	return arc_length_DireX,arc_length_DireY

def func_round(number):
    if number % 1 == 0.5:
        number = number + 0.5
    else:
        number = round(number)
    return int(number)


# 本函数用于考虑粗略情形下的弧长计算：加载高度处于顶头自身高度之内，则认为圆平面加载与球面加载的折中
def func_CN1_lengthArc(H,Rs,Rp,a_DireX,m_DireX,a_DireY,m_DireY):
	i_DireX = np.arange(1,m_DireX+0.1,step=1)
	i_DireY = np.arange(1,m_DireY+0.1,step=1)
	d_DireX = abs(a_DireX/2*(2*i_DireX - m_DireX - 1))
	d_DireY = abs(a_DireY/2*(2*i_DireY - m_DireY - 1))
	minH = Rs-np.sqrt(Rs**2-Rp**2)
	if H < minH:
		Rp1 = np.sqrt(Rp**2-d_DireX**2)
		Rs1 = np.sqrt(Rs**2-d_DireX**2)
		minH1 = np.sqrt(Rs**2-d_DireX**2) - np.sqrt(Rs**2 - Rp**2)
		H1 = H - (minH - minH1)
		arc_line_factor1 = 1+(np.arcsin(Rp1/Rs1)*Rs1/Rp1 - 1)*H1/minH1

		Rp2 = np.sqrt(Rp**2-d_DireY**2)
		Rs2 = np.sqrt(Rs**2-d_DireY**2)
		minH2 = np.sqrt(Rs**2-d_DireY**2) - np.sqrt(Rs**2 - Rp**2)
		H2 = H - (minH - minH2)
		arc_line_factor2 = 1+(np.arcsin(Rp2/Rs2)*Rs2/Rp2 - 1)*H2/minH2

		print('arc_line_factor=',arc_line_factor2)
		arc_length_DireX = 2*np.sqrt(Rp**2 - d_DireX**2)*arc_line_factor1
		arc_length_DireY = 2*np.sqrt(Rp**2 - d_DireY**2)*arc_line_factor2
	elif H >= minH:
		alpha_DireX = 2*np.arctan(np.sqrt((Rp**2-d_DireX**2)/(Rs**2-Rp**2)))
		alpha_DireY = 2*np.arctan(np.sqrt((Rp**2-d_DireY**2)/(Rs**2-Rp**2)))
		arc_length_DireX = alpha_DireX*np.sqrt(Rs**2-d_DireX**2)
		arc_length_DireY = alpha_DireY*np.sqrt(Rs**2-d_DireY**2)
	else:
		raise ValueError
	return arc_length_DireX,arc_length_DireY

# 本函数用于考虑精细情形下的弧长计算：加载高度处于顶头自身高度之内，则认为圆平面加载
def func_CN1_lengthArc_fine(H,Rs,Rp,a_DireX,m_DireX,a_DireY,m_DireY):
	i_DireX = np.arange(1,m_DireX+0.1,step=1)
	i_DireY = np.arange(1,m_DireY+0.1,step=1)
	d_DireX = abs(a_DireX/2*(2*i_DireX - m_DireX - 1))
	d_DireY = abs(a_DireY/2*(2*i_DireY - m_DireY - 1))
	minH = Rs-np.sqrt(Rs**2-Rp**2)

	alpha_DireX = np.empty_like(d_DireX)
	alpha_DireY = np.empty_like(d_DireY)
	arc_length_DireX = np.empty_like(d_DireX)
	arc_length_DireY = np.empty_like(d_DireY)
	lineX = np.empty_like(d_DireX)
	lineY = np.empty_like(d_DireY)

	if H < minH:
		minRp = np.sqrt(Rs**2-(Rs-H)**2)
		for iX in range(len(d_DireX)):
			if d_DireX[iX]>minRp:
				arc_length_DireX[iX] = 2*np.sqrt(Rp**2 - d_DireX[iX]**2)
			else:
				lineX[iX] = 2*np.sqrt(Rp**2 - d_DireX[iX]**2) - 2*np.sqrt(minRp**2 - d_DireX[iX]**2)
				alpha_DireX[iX] = 2*np.arctan(np.sqrt(minRp**2-d_DireX[iX]**2)/(Rs-minH))
				arc_length_DireX[iX] = alpha_DireX[iX]*np.sqrt(Rs**2-d_DireX[iX]**2) + lineX[iX]

		for iY in range(len(d_DireY)):
			if d_DireY[iY]>minRp:
				arc_length_DireY[iY] = 2*np.sqrt(Rp**2 - d_DireY[iY]**2)
			else:
				lineY[iY] = 2*np.sqrt(Rp**2 - d_DireY[iY]**2) - 2*np.sqrt(minRp**2 - d_DireY[iY]**2)
				alpha_DireY[iY] = 2*np.arctan(np.sqrt(minRp**2-d_DireY[iY]**2)/(Rs-minH))
				arc_length_DireY[iY] = alpha_DireY[iY]*np.sqrt(Rs**2-d_DireY[iY]**2) + lineY[iY]
	elif H >= minH:
		alpha_DireX = 2*np.arctan(np.sqrt((Rp**2-d_DireX**2)/(Rs**2-Rp**2)))
		alpha_DireY = 2*np.arctan(np.sqrt((Rp**2-d_DireY**2)/(Rs**2-Rp**2)))
		arc_length_DireX = alpha_DireX*np.sqrt(Rs**2-d_DireX**2)
		arc_length_DireY = alpha_DireY*np.sqrt(Rs**2-d_DireY**2)
	else:
		raise ValueError
	return arc_length_DireX,arc_length_DireY


def func_CN1_sigma(epsilon, sigma_y, E1, E2):
	epsilon1 = sigma_y/E1
	sigma_XY = np.zeros_like(epsilon)
	for i in range (int(len(epsilon))):
		if epsilon[i]>=0 and epsilon[i]<=epsilon1:
			sigma_XY[i] = E1*epsilon[i]
		elif epsilon[i]>epsilon1:
			sigma_XY[i] = sigma_y+E2*(epsilon[i]-epsilon1)
		elif epsilon[i]<0:
			pass
		else:
			raise ValueError
	return sigma_XY


def func_CN1_loaded_xPyP(m, d, alpha, Rp, H, ex, ey):
	alpha = alpha - (alpha//np.pi)*np.pi

	i1_arr = np.arange(1,m+0.1,step=1)  # 第一方向上与加载区域相交的钢丝绳序列（从1开始）

	yP_plus_origin = d/2*(2*i1_arr - m - 1)
	xP_plus_origin = np.sqrt(Rp**2 - yP_plus_origin**2)
	zP_plus_origin = H*np.ones_like(yP_plus_origin)

	yP_minu_origin = yP_plus_origin
	xP_minu_origin =-xP_plus_origin
	zP_minu_origin = zP_plus_origin

	# 坐标旋转，全部基于与x轴平行的钢丝绳与加载区域的交点
	xP_plus = ex + xP_plus_origin*np.cos(alpha) - yP_plus_origin*np.sin(alpha)
	yP_plus = ey + xP_plus_origin*np.sin(alpha) + yP_plus_origin*np.cos(alpha)
	zP_plus = zP_plus_origin

	xP_minu = ex + xP_minu_origin*np.cos(alpha) - yP_minu_origin*np.sin(alpha)
	yP_minu = ey + xP_minu_origin*np.sin(alpha) + yP_minu_origin*np.cos(alpha)
	zP_minu = zP_minu_origin

	return xP_plus, yP_plus, zP_plus, xP_minu, yP_minu, zP_minu

def func_CN1_solve_ABC(para_x1, para_y1, para_x2, para_y2):
	if np.amin(abs(para_x2-para_x1))==0:
		A1_arr = np.ones_like(para_x1)
		B1_arr = np.zeros_like(para_x1)
		C1_arr = -para_x1+np.zeros_like(para_x1)
	else:
		A1_arr = (para_y2-para_y1)/(para_x2-para_x1)
		B1_arr = -1+np.zeros_like(A1_arr)
		C1_arr = para_y1-(para_y2-para_y1)/(para_x2-para_x1)*para_x1
	return A1_arr, B1_arr, C1_arr


def func_CN1_xy_intersection(A1, B1, C1, A2, B2, C2):
	if np.amin(abs(A1*B2-A2*B1))==0:
		x_point = A1 + A2 + 10**100  # 采用大数淹没，避免除0报警
		y_point = A1 + A2 + 10**100  # 采用大数淹没，避免除0报警
	else:
		x_point = (B1*C2-B2*C1)/(A1*B2-A2*B1)
		y_point = (A2*C1-A1*C2)/(A1*B2-A2*B1)
	return x_point, y_point


# 本函数用于删除钢丝绳网与锚固点之间边界线延长线上的交点
def func_CN1_pick_xQyQ(m, xQ_line12, yQ_line12, xQ_line23, yQ_line23, xQ_line34, yQ_line34, xQ_line41, yQ_line41, x1, y1, x2, y2, x3, y3, x4, y4):
	xQ = np.zeros(2*m+4)
	yQ = np.zeros(2*m+4)
	i1 = 0
	for i12 in range(len(xQ_line12)):
		if xQ_line12[i12]-x1<-1e-15 and xQ_line12[i12]-x2<-1e-15:  # 通过x坐标判别是否位于边界线上
			pass
		elif xQ_line12[i12]-x1>1e-15 and xQ_line12[i12]-x2>1e-15:  # 通过x坐标判别是否位于边界线上
			pass
		else:
			if yQ_line12[i12]-y1<-1e-15 and  yQ_line12[i12]-y2<-1e-15:  # 再通过y坐标判别是否位于边界线上
				pass
			elif yQ_line12[i12]-y1>1e-15 and yQ_line12[i12]-y2>1e-15:  # 再通过y坐标判别是否位于边界线上
				pass
			else:
				xQ[i1] = xQ_line12[i12]
				yQ[i1] = yQ_line12[i12]
				i1 = i1 + 1
	for i23 in range(len(xQ_line23)):
		if xQ_line23[i23]-x2<-1e-15 and xQ_line23[i23]-x3<-1e-15:
			pass
		elif xQ_line23[i23]-x2>1e-15 and xQ_line23[i23]-x3>1e-15:
			pass
		else:
			if yQ_line23[i23]-y2<-1e-15 and yQ_line23[i23]-y3<-1e-15:
				pass
			elif yQ_line23[i23]-y2>1e-15 and yQ_line23[i23]-y3>1e-15:
				pass
			else:
				xQ[i1] = xQ_line23[i23]
				yQ[i1] = yQ_line23[i23]
				i1 = i1 + 1
	for i34 in range(len(xQ_line34)):
		if xQ_line34[i34]-x3<-1e-15 and xQ_line34[i34]-x4<-1e-15:
			pass
		elif xQ_line34[i34]-x3>1e-15 and xQ_line34[i34]-x4>1e-15:
			pass
		else:
			if yQ_line34[i34]-y3<-1e-15 and yQ_line34[i34]-y4<-1e-15:
				pass
			elif yQ_line34[i34]-y3>1e-15 and yQ_line23[i34]-y4>1e-15:
				pass
			else:
				xQ[i1] = xQ_line34[i34]
				yQ[i1] = yQ_line34[i34]
				i1 = i1 + 1
	for i41 in range(len(xQ_line41)):
		if xQ_line41[i41]-x4<-1e-15 and xQ_line41[i41]-x1<-1e-15:
			pass
		elif xQ_line41[i41]-x4>1e-15 and xQ_line41[i41]-x1>1e-15:
			pass
		else:
			if yQ_line41[i41]-y4<-1e-15 and yQ_line41[i41]-y1<-1e-15:
				pass
			elif yQ_line41[i41]-y4>1e-15 and yQ_line41[i41]-y1>1e-15:
				print('yQ_line41[i41]', yQ_line41[i41])
				print('y4=', y4)
				pass
			else:
				xQ[i1] = xQ_line41[i41]
				yQ[i1] = yQ_line41[i41]
				i1 = i1 + 1

	###########################################################################################
	# 新添加代码， 用于对重复的坐标进行清理
	xQyQ_all = np.vstack((xQ, yQ))
	xQ_clean = np.unique(xQyQ_all, axis=1)[0,:]  # 对重复的坐标进行清理
	yQ_clean = np.unique(xQyQ_all, axis=1)[1,:]  # 对重复的坐标进行清理
	###########################################################################################
	return xQ_clean[xQ_clean!=0], yQ_clean[yQ_clean!=0]


def func_CN1_sort_xQyQ(m, xQ, yQ, xP_plus, yP_plus, xP_minu, yP_minu):
	xQ_plus = np.zeros(m)
	yQ_plus = np.zeros(m)
	yQ_minu = np.zeros(m)
	xQ_minu = np.zeros(m)

	for i in range(len(xP_plus)):
		if abs(xP_plus[i] - xP_minu[i]) <= 1e-15:
			for jP in range(len(xQ)):
				if abs(xQ[jP] - xP_plus[i]) <= 1e-15:
					if (yQ[jP] - yP_plus[i])>=1e-15:
						xQ_plus[i] = xQ[jP]
						yQ_plus[i] = yQ[jP]
					elif (yQ[jP] - yP_plus[i])<=-1e-15:  # python对于数值的绝对相等判别存在非常非常小1e-15但是不可忽略的误差
						xQ_minu[i] = xQ[jP]
						yQ_minu[i] = yQ[jP]
					else:
						raise ValueError
				else:
					pass
		else:
			k_target = (yP_plus[i] - yP_minu[i])/(xP_plus[i] - xP_minu[i])
			for jQ in range(len(xQ)):
				k_search = (yQ[jQ] - yP_plus[i])/(xQ[jQ] - xP_plus[i])
				if abs(k_search-k_target) <= 1e-8:  # 1e-8是通过求解tan(0.000001°)-tan(0°)获得的：当角度增长0.000001°时满足的精度要求
					if (yQ[jQ] - yP_plus[i])>=1e-15:
						xQ_plus[i] = xQ[jQ]
						yQ_plus[i] = yQ[jQ]
					elif (yQ[jQ] - yP_plus[i])<=-1e-15:  # python对于数值的绝对相等判别存在非常非常小1e-15但是不可忽略的误差
						xQ_minu[i] = xQ[jQ]
						yQ_minu[i] = yQ[jQ]
					elif abs(yQ[jQ] - yP_plus[i])<=1e-15:
						if xQ[jQ] > xP_plus[i]:
							xQ_plus[i] = xQ[jQ]
							yQ_plus[i] = yQ[jQ]
						elif xQ[jQ] < xP_plus[i]:
							xQ_minu[i] = xQ[jQ]
							yQ_minu[i] = yQ[jQ]
						else:
							raise ValueError
					else:
						raise ValueError	
				else:
					continue
			#print('i=',i, 'xQ_plus=',xQ_plus,'yQ_plus=',yQ_plus)

	return xQ_plus, yQ_plus, xQ_minu, yQ_minu


def func_CN1_sort_ks_ls0(origin_k, origin_x, origin_y, target_x, target_y):

	x1 = np.around(origin_x.astype('float'),3)
	y1 = np.around(origin_y.astype('float'),3)
	x2 = np.around(target_x.astype('float'),3)
	y2 = np.around(target_y.astype('float'),3)
	ko = np.around(origin_k.astype('float'),3)
	
	index_k = np.empty_like(x2)
	for i in range(len(x1)):
	    for j in range(len(x2)):
	        if x1[i] == x2[j] and y1[i]==y2[j]:
	            index_k[j] = i
	        else:
	            pass
	#print('index_k=',index_k.astype('int'))
	return ko[index_k.astype('int64')]

def func_check_L0yu(L0_array, Ly_array, Lu_array):
	n_L0yu = len(L0_array)
	for i in range(n_L0yu):
		if Ly_array[i]>=L0_array[i] and Ly_array[i]<=Lu_array[i]:
			pass
		else:
			raise ValueError

if __name__ == '__main__':
	# 参数输入----------------------------------------------------------------------------------- #
	# 钢丝绳网材料参数输入
	E_young = 90.304e9  # 钢丝绳网中的钢丝绳弹性模量（单位：Pa）
	E_tangent = 25.0e9  # 钢丝绳网中的钢丝绳硬化段切线模量（单位：Pa）
	sigma_y = 1350e6  # 钢丝绳网中的钢丝绳屈服强度（单位：Pa）
	sigma_u = 1350e6  # 钢丝绳网中的钢丝绳极限强度（单位：Pa）
	fail_force = 41782  # 钢丝绳网中的钢丝绳破断力（单位：N）

	# 钢丝绳网几何参数输入
	d1 = 0.3  # 1方向钢丝绳间距-网孔间距
	d2 = 0.3  # 2方向钢丝绳间距-网孔间距
	alpha1 = 45*np.pi/180  # 钢丝绳方向角1，取值范围为半闭半开区间[0,pi)
	alpha2 = -45*np.pi/180 # 钢丝绳方向角2，取值范围为半闭半开区间[0,pi)
	A_fibre = fail_force/sigma_u
	#print('A_fibre=',A_fibre)
	initial_sag = 0.05  # 钢丝绳网在重力作用下初始垂度（初始高度)

	# 加载区域几何参数输入
	ex = 0  # 加载区域中心沿x方向偏心距（单位：m）
	ey = 0  # 加载区域中心沿y方向偏心距（单位：m）
	Rp = 0.75  # 加载顶头水平投影半径（单位：m），若加载形状为多边形时考虑为等面积圆的半径
	Rp = Rp + (1e-6)*np.exp(1)  # 用于修复一个bug：即钢丝绳与加载区域边缘相切只有一个交点的情况
	Rs = Rp*12/5  # 球罐形加载顶头半径（单位：m）

	# 锚点坐标输入，可考虑任意四边形钢丝绳网片
	x1, y1 = 1, -1  # 四个锚点中锚点1的坐标
	x2, y2 = 1, 1  # 四个锚点中锚点2的坐标
	x3, y3 = -1, 1  # 四个锚点中锚点3的坐标
	x4, y4 = -1, -1  # 四个锚点中锚点4的坐标

	# 边界刚度输入，以下部分可考虑边界四周连接不同刚度的钢丝绳
	ks12 = 1e15  # 锚点12之间的边界弹簧刚度（单位：N/m），与方向1正方向纤维连接，刚性边界取值为1e15N/m
	ks23 = 1e15  # 锚点23之间的边界弹簧刚度（单位：N/m），与方向1负方向纤维连接
	ks34 = 1e15  # 锚点34之间的边界弹簧刚度（单位：N/m），与方向2正方向纤维连接
	ks41 = 1e15  # 锚点41之间的边界弹簧刚度（单位：N/m），与方向2负方向纤维连接

	l0_s12 = 1e-1  # 方向1边界弹簧初始长度（单位：m），与方向1正方向纤维连接
	l0_s23 = 1e-1  # 方向1边界弹簧初始长度（单位：m），与方向1负方向纤维连接
	l0_s34 = 1e-1  # 方向2边界弹簧初始长度（单位：m），与方向2正方向纤维连接
	l0_s41 = 1e-1  # 方向2边界弹簧初始长度（单位：m），与方向2负方向纤维连接

	# 边界刚度输入，以下部分可考虑纤维两端连接不同刚度的钢丝绳
	#ks1_plus = 1e20  # 方向1边界弹簧刚度（单位：N/m），与方向1正方向纤维连接
	#ks1_minu = 1e20  # 方向1边界弹簧刚度（单位：N/m），与方向1负方向纤维连接
	#ks2_plus = 1e20  # 方向2边界弹簧刚度（单位：N/m），与方向2正方向纤维连接
	#ks2_minu = 1e20  # 方向2边界弹簧刚度（单位：N/m），与方向2负方向纤维连接

	#ls1_plus = 1e-1  # 方向1边界弹簧初始长度（单位：m），与方向1正方向纤维连接
	#ls1_minu = 1e-1  # 方向1边界弹簧初始长度（单位：m），与方向1负方向纤维连接
	#ls2_plus = 1e-1  # 方向2边界弹簧初始长度（单位：m），与方向2正方向纤维连接
	#ls2_minu = 1e-1  # 方向2边界弹簧初始长度（单位：m），与方向2负方向纤维连接

	# 求解过程----------------------------------------------------------------------------------- #
	##############################################################################################
	Origin_xyz_coordinate = func_choose_Origin_xyz_coordinate()     # 判断采用哪种坐标原点
	##############################################################################################
	if Origin_xyz_coordinate == 'centre':
		m1 = 2*func_round(Rp/d1)  # 第1方向上与加载区域相交的钢丝绳数量（偶数）
		m2 = 2*func_round(Rp/d2)  # 第2方向上与加载区域相交的钢丝绳数量（偶数）
	elif  Origin_xyz_coordinate == 'corner':
		m1 = 2*int(Rp/d1) + 1  # 第1方向上与加载区域相交的钢丝绳数量（偶数）
		m2 = 2*int(Rp/d2) + 1  # 第2方向上与加载区域相交的钢丝绳数量（偶数）
	else:
		raise ValueError

	# 初始时刻加载区域边缘力的作用点（P点）坐标，方向1与方向2，P点坐标随着加载位移的变换实时变化
	xP1_plus, yP1_plus, zP1_plus, xP1_minu, yP1_minu, zP1_minu = func_CN1_loaded_xPyP(m1, d1, alpha1, Rp, initial_sag, ex, ey)  # 1方向钢丝绳与加载区域边缘交点坐标
	xP2_plus, yP2_plus, zP2_plus, xP2_minu, yP2_minu, zP2_minu = func_CN1_loaded_xPyP(m2, d2, alpha2, Rp, initial_sag, ex, ey)  # 2方向钢丝绳与加载区域边缘交点坐标

	# 求解计算过程中钢丝绳网片边界上力的作用点（Q点）坐标，方向1与方向2，Q点坐标不随加载位移的变换改变
	A1_arr, B1_arr, C1_arr = func_CN1_solve_ABC(xP1_minu, yP1_minu, xP1_plus, yP1_plus)  # 与加载区域边缘相交的1方向的钢丝绳直线方程系数A1x+B1y+C1=0
	A2_arr, B2_arr, C2_arr = func_CN1_solve_ABC(xP2_minu, yP2_minu, xP2_plus, yP2_plus)  # 与加载区域边缘相交的2方向的钢丝绳直线方程系数A2x+B2y+C2=0

	A_line12, B_line12, C_line12 = func_CN1_solve_ABC(x1, y1, x2, y2)  # 边界线方程（锚点之间的连接线）A_linex+B_liney+C_line=0
	A_line23, B_line23, C_line23 = func_CN1_solve_ABC(x2, y2, x3, y3)
	A_line34, B_line34, C_line34 = func_CN1_solve_ABC(x3, y3, x4, y4)
	A_line41, B_line41, C_line41 = func_CN1_solve_ABC(x4, y4, x1, y1)

	xQ1_line12, yQ1_line12 = func_CN1_xy_intersection(A1_arr, B1_arr, C1_arr, A_line12, B_line12, C_line12)  # 钢丝绳直线束与边界线（锚点1与锚点2连线）的交点，方向1
	xQ1_line23, yQ1_line23 = func_CN1_xy_intersection(A1_arr, B1_arr, C1_arr, A_line23, B_line23, C_line23)  # 钢丝绳直线束与边界线（锚点2与锚点3连线）的交点，方向1
	xQ1_line34, yQ1_line34 = func_CN1_xy_intersection(A1_arr, B1_arr, C1_arr, A_line34, B_line34, C_line34)  # 钢丝绳直线束与边界线（锚点3与锚点4连线）的交点，方向1
	xQ1_line41, yQ1_line41 = func_CN1_xy_intersection(A1_arr, B1_arr, C1_arr, A_line41, B_line41, C_line41)  # 钢丝绳直线束与边界线（锚点4与锚点1连线）的交点，方向1

	xQ2_line12, yQ2_line12 = func_CN1_xy_intersection(A2_arr, B2_arr, C2_arr, A_line12, B_line12, C_line12)  # 钢丝绳直线束与边界线（锚点1与锚点2连线）的交点，方向2
	xQ2_line23, yQ2_line23 = func_CN1_xy_intersection(A2_arr, B2_arr, C2_arr, A_line23, B_line23, C_line23)  # 钢丝绳直线束与边界线（锚点2与锚点3连线）的交点，方向2
	xQ2_line34, yQ2_line34 = func_CN1_xy_intersection(A2_arr, B2_arr, C2_arr, A_line34, B_line34, C_line34)  # 钢丝绳直线束与边界线（锚点3与锚点4连线）的交点，方向2
	xQ2_line41, yQ2_line41 = func_CN1_xy_intersection(A2_arr, B2_arr, C2_arr, A_line41, B_line41, C_line41)  # 钢丝绳直线束与边界线（锚点4与锚点1连线）的交点，方向2

	xQ1_pick, yQ1_pick = func_CN1_pick_xQyQ(m1, xQ1_line12, yQ1_line12, xQ1_line23, yQ1_line23, xQ1_line34, yQ1_line34, xQ1_line41, yQ1_line41, x1, y1, x2, y2, x3, y3, x4, y4)  # 挑选出边界线段范围内的交点，方向1
	xQ2_pick, yQ2_pick = func_CN1_pick_xQyQ(m2, xQ2_line12, yQ2_line12, xQ2_line23, yQ2_line23, xQ2_line34, yQ2_line34, xQ2_line41, yQ2_line41, x1, y1, x2, y2, x3, y3, x4, y4)  # 挑选出边界线段范围内的交点，方向2

	xQ1_plus, yQ1_plus, xQ1_minu, yQ1_minu = func_CN1_sort_xQyQ(m1, xQ1_pick, yQ1_pick, xP1_plus, yP1_plus, xP1_minu, yP1_minu)  # 对挑选出来的交点进行重新排序，使得边界线上的交点与加载边缘上的交点一一对应，与实际钢丝绳网中匹配关系一致，方向1
	xQ2_plus, yQ2_plus, xQ2_minu, yQ2_minu = func_CN1_sort_xQyQ(m2, xQ2_pick, yQ2_pick, xP2_plus, yP2_plus, xP2_minu, yP2_minu)  # 对挑选出来的交点进行重新排序，使得边界线上的交点与加载边缘上的交点一一对应，与实际钢丝绳网中匹配关系一致，方向2
	
	#print('xP1_plus=',xP1_plus)
	#print('yP1_plus=',yP1_plus)
	#print('xQ1_plus=',xQ2_plus)
	#print('yQ1_plus=',yQ2_plus)
	
	zQ1_plus, zQ1_minu = np.zeros_like(xQ1_plus), np.zeros_like(xQ1_plus)
	zQ2_plus, zQ2_minu = np.zeros_like(xQ2_plus), np.zeros_like(xQ2_plus)

	# 用于对ks和ls0进行排序，即满足每个弹簧刚度等于连接边界的刚度
	xQ1_m1 = np.concatenate((xQ1_line12, xQ1_line23, xQ1_line34, xQ1_line41))
	yQ1_m1 = np.concatenate((yQ1_line12, yQ1_line23, yQ1_line34, yQ1_line41))
	xQ2_m2 = np.concatenate((xQ2_line12, xQ2_line23, xQ2_line34, xQ2_line41))
	yQ2_m2 = np.concatenate((yQ2_line12, yQ2_line23, yQ2_line34, yQ2_line41))

	k_spring_m1 = np.concatenate((ks12*np.ones(m1), ks23*np.ones(m1), ks34*np.ones(m1), ks41*np.ones(m1)))
	k_spring_m2 = np.concatenate((ks12*np.ones(m2), ks23*np.ones(m2), ks34*np.ones(m2), ks41*np.ones(m2)))

	l0_spring_m1 = np.concatenate((l0_s12*np.ones(m1), l0_s23*np.ones(m1), l0_s34*np.ones(m1), l0_s41*np.ones(m1)))
	l0_spring_m2 = np.concatenate((l0_s12*np.ones(m2), l0_s23*np.ones(m2), l0_s34*np.ones(m2), l0_s41*np.ones(m2)))

	k_spring1_plus = func_CN1_sort_ks_ls0(k_spring_m1, xQ1_m1, yQ1_m1, xQ1_plus, yQ1_plus)
	k_spring1_minu = func_CN1_sort_ks_ls0(k_spring_m1, xQ1_m1, yQ1_m1, xQ1_minu, yQ1_minu)
	k_spring2_plus = func_CN1_sort_ks_ls0(k_spring_m2, xQ2_m2, yQ2_m2, xQ2_plus, yQ2_plus)
	k_spring2_minu = func_CN1_sort_ks_ls0(k_spring_m2, xQ2_m2, yQ2_m2, xQ2_minu, yQ2_minu)

	l0_spring1_plus = func_CN1_sort_ks_ls0(l0_spring_m1, xQ1_m1, yQ1_m1, xQ1_plus, yQ1_plus)
	l0_spring1_minu = func_CN1_sort_ks_ls0(l0_spring_m1, xQ1_m1, yQ1_m1, xQ1_minu, yQ1_minu)
	l0_spring2_plus = func_CN1_sort_ks_ls0(l0_spring_m2, xQ2_m2, yQ2_m2, xQ2_plus, yQ2_plus)
	l0_spring2_minu = func_CN1_sort_ks_ls0(l0_spring_m2, xQ2_m2, yQ2_m2, xQ2_minu, yQ2_minu)

	#print('xQ1_plus=',xQ1_plus)
	#print('yQ1_plus=',yQ1_plus)
	#print('xQ1_minu=',xQ1_minu)
	#print('yQ1_minu=',yQ1_minu)
	#
#
	#print('xQ2_plus=',xQ2_plus)
	#print('yQ2_plus=',yQ2_plus)
	#print('xQ2_minu=',xQ2_minu)
	#print('yQ2_minu=',yQ2_minu)


	length_PQ1_plus = np.sqrt((xP1_plus-xQ1_plus)**2+(yP1_plus-yQ1_plus)**2+(zP1_plus-zQ1_plus)**2)
	length_PQ1_minu = np.sqrt((xP1_minu-xQ1_minu)**2+(yP1_minu-yQ1_minu)**2+(zP1_minu-zQ1_minu)**2)

	length_PQ2_plus = np.sqrt((xP2_plus-xQ2_plus)**2+(yP2_plus-yQ2_plus)**2+(zP2_plus-zQ2_plus)**2)
	length_PQ2_minu = np.sqrt((xP2_minu-xQ2_minu)**2+(yP2_minu-yQ2_minu)**2+(zP2_minu-zQ2_minu)**2)

	length_Arc1 = func_CN1_lengthArc(initial_sag,Rs,Rp,d1,m1,d2,m2)[0]
	length_Arc2 = func_CN1_lengthArc(initial_sag,Rs,Rp,d1,m1,d2,m2)[1]

	L0_dire1 = length_PQ1_plus + length_PQ1_minu + length_Arc1
	L0_dire2 = length_PQ2_plus + length_PQ2_minu + length_Arc2

	l_f0_dire1 = L0_dire1 - l0_spring1_minu - l0_spring1_plus  # 纤维弹簧单元中1方向纤维初始长度
	l_f0_dire2 = L0_dire2 - l0_spring2_minu - l0_spring2_plus  # 纤维弹簧单元中2方向纤维初始长度

	k_s_dire1 = 1/(1/k_spring1_minu + 1/k_spring1_plus)  # 纤维弹簧单元中1方向边界串联弹簧刚度
	k_s_dire2 = 1/(1/k_spring2_minu + 1/k_spring2_plus)  # 纤维弹簧单元中2方向边界串联弹簧刚度

	K_dire1 = 1/(l_f0_dire1/(E_young*A_fibre) + 1/k_s_dire1)  # 纤维弹簧单元1方向拉伸刚度，线弹性阶段
	K_dire2 = 1/(l_f0_dire2/(E_young*A_fibre) + 1/k_s_dire2)  # 纤维弹簧单元2方向拉伸刚度，线弹性阶段
	
	K_T_dire1 = 1/(l_f0_dire1/(E_tangent*A_fibre) + 1/k_s_dire1)  # 纤维弹簧单元1方向拉伸刚度，进入屈服后阶段
	K_T_dire2 = 1/(l_f0_dire2/(E_tangent*A_fibre) + 1/k_s_dire2)  # 纤维弹簧单元2方向拉伸刚度，进入屈服后阶段

	Ly_dire1 = L0_dire1 + sigma_y*A_fibre/K_dire1  # 纤维单元发生屈服时，1方向纤维弹簧单元总长度
	Ly_dire2 = L0_dire2 + sigma_y*A_fibre/K_dire2  # 纤维单元发生失效时，2方向纤维弹簧单元总长度

	Lu_dire1 = L0_dire1 + sigma_y*A_fibre/K_dire1 + (sigma_u-sigma_y)*A_fibre/K_T_dire1  # 纤维单元发生失效时，1方向纤维弹簧单元总长度
	Lu_dire2 = L0_dire2 + sigma_y*A_fibre/K_dire2 + (sigma_u-sigma_y)*A_fibre/K_T_dire2  # 纤维单元发生失效时，2方向纤维弹簧单元总长度

	L0_all =  np.concatenate((L0_dire1,L0_dire2),axis=0)
	Ly_all = np.concatenate((Ly_dire1,Ly_dire2),axis=0)
	Lu_all = np.concatenate((Lu_dire1,Lu_dire2),axis=0)

	func_check_L0yu(L0_all, Ly_all, Lu_all)  # 检查L0_all, Ly_all, Lu_all三者之间的大小关系，保证求解过程收敛

	n_loop = 0 # 初始增量步数
	Height = initial_sag  # 网片初始面外变形
	step_H = 1e-3  # 位移加载增量步长，单位：m

	target_delta_Lu = np.amin(abs(Lu_all-L0_all))

	Height_list = [0]
	Force_list = [0]
	Energy_list = [0]
	epsilon_u = sigma_y/E_young + (sigma_u-sigma_y)/E_tangent  # 钢丝绳失效应变

	while(n_loop<=10000 and target_delta_Lu>=step_H):  # 判别条件是由一个不等式来确定的（该不等式证明：直角三角形的一个直角边恒定，则另一个直角边的增大程度始终大于斜边长度的增大程度）
		
		n_loop = n_loop+1
		Height = Height+step_H

		xP1_plus, yP1_plus, zP1_plus, xP1_minu, yP1_minu, zP1_minu = func_CN1_loaded_xPyP(m1, d1, alpha1, Rp, Height, ex, ey)
		xP2_plus, yP2_plus, zP2_plus, xP2_minu, yP2_minu, zP2_minu = func_CN1_loaded_xPyP(m2, d2, alpha2, Rp, Height, ex, ey)

		length_PQ1_plus = np.sqrt((xP1_plus-xQ1_plus)**2+(yP1_plus-yQ1_plus)**2+(zP1_plus-zQ1_plus)**2)
		length_PQ1_minu = np.sqrt((xP1_minu-xQ1_minu)**2+(yP1_minu-yQ1_minu)**2+(zP1_minu-zQ1_minu)**2)
		
		length_PQ2_plus = np.sqrt((xP2_plus-xQ2_plus)**2+(yP2_plus-yQ2_plus)**2+(zP2_plus-zQ2_plus)**2)
		length_PQ2_minu = np.sqrt((xP2_minu-xQ2_minu)**2+(yP2_minu-yQ2_minu)**2+(zP2_minu-zQ2_minu)**2)

		length_Arc1 = func_CN1_lengthArc(Height,Rs,Rp,d1,m1,d2,m2)[0]
		length_Arc2 = func_CN1_lengthArc(Height,Rs,Rp,d1,m1,d2,m2)[1]

		L_dire1 = length_PQ1_plus + length_PQ1_minu + length_Arc1
		L_dire2 = length_PQ2_plus + length_PQ2_minu + length_Arc2

		L_all = np.concatenate((L_dire1,L_dire2),axis=0)

		target_delta_Lu = np.amin(abs(L_all-Lu_all))

		force_dire1 = np.zeros_like(L_dire1)
		force_dire2 = np.zeros_like(L_dire2)

		energy_dire1 = np.zeros_like(L_dire1)
		energy_dire2 = np.zeros_like(L_dire2)

		for i_dire1 in range(len(L_dire1)):
			if L_dire1[i_dire1]<Ly_dire1[i_dire1]:
				force_dire1[i_dire1] = K_dire1[i_dire1]*(L_dire1[i_dire1]-L0_dire1[i_dire1])
				energy_dire1[i_dire1] = 0.5*K_dire1[i_dire1]*(L_dire1[i_dire1]-L0_dire1[i_dire1])**2
			else:
				#print('yield L_all=',L_all)
				force_dire1[i_dire1] = K_dire1[i_dire1]*(Ly_dire1[i_dire1]-L0_dire1[i_dire1]) + K_T_dire1[i_dire1]*(L_dire1[i_dire1]-Ly_dire1[i_dire1])
				energy_dire1[i_dire1] = 0.5*K_T_dire1[i_dire1]*(L_dire1[i_dire1]-Ly_dire1[i_dire1])**2 + 0.5*K_dire1[i_dire1]*(Ly_dire1[i_dire1]-L0_dire1[i_dire1])*(2*L_dire1[i_dire1]-Ly_dire1[i_dire1]-L0_dire1[i_dire1])

		for i_dire2 in range(len(L_dire2)):
			if L_dire2[i_dire2]<Ly_dire2[i_dire2]:
				force_dire2[i_dire2] = K_dire2[i_dire2]*(L_dire2[i_dire2]-L0_dire2[i_dire2])
				energy_dire2[i_dire2] = 0.5*K_dire2[i_dire2]*(L_dire2[i_dire2]-L0_dire2[i_dire2])**2
			else:
				#print('yield L_all=',L_all)
				force_dire2[i_dire2] = K_dire2[i_dire2]*(Ly_dire2[i_dire2]-L0_dire2[i_dire2]) + K_T_dire2[i_dire2]*(L_dire2[i_dire2]-Ly_dire2[i_dire2])
				energy_dire2[i_dire2] = 0.5*K_T_dire2[i_dire2]*(L_dire2[i_dire2]-Ly_dire2[i_dire2])**2 + 0.5*K_dire2[i_dire2]*(Ly_dire2[i_dire2]-L0_dire2[i_dire2])*(2*L_dire2[i_dire2]-Ly_dire2[i_dire2]-L0_dire2[i_dire2])
		
		force_proj1_plus = force_dire1*Height/length_PQ1_plus  # 极限破坏状态1方向正侧端点各个纤维弹簧单元内力沿着加载方向的投影
		force_proj1_minu = force_dire1*Height/length_PQ1_minu  # 极限破坏状态1方向负侧端点各个纤维弹簧单元内力沿着加载方向的投影
		force_proj2_plus = force_dire2*Height/length_PQ2_plus  # 极限破坏状态2方向正侧端点各个纤维弹簧单元内力沿着加载方向的投影
		force_proj2_minu = force_dire2*Height/length_PQ2_minu  # 极限破坏状态2方向负侧端点各个纤维弹簧单元内力沿着加载方向的投影

		force = np.sum(force_proj1_plus) + np.sum(force_proj1_minu) + np.sum(force_proj2_plus) + np.sum(force_proj2_minu)  # 极限破坏状态各个纤维弹簧单元内力之和，矢量和运算
		energy = np.sum(energy_dire1) + np.sum(energy_dire2)  # 极限破坏状态各个纤维弹簧单元吸收总能量，标量直接相加

		Height_list.append(Height)
		Force_list.append(force)
		Energy_list.append(energy)

		print('It the',n_loop, 'th loop,','Height=',np.around(Height,3),'Force=',np.around(force,3),'Energy=',np.around(energy,3))

	print('Height=',np.around(Height,3),'Force=',np.around(force,3),'Energy=',np.around(energy,3))
	plt.plot(np.array(Height_list),np.array(Force_list),'*-')
	plt.show()

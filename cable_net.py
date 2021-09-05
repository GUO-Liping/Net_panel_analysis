#!/usr/bin/env python
# -*- coding: UTF-8 -*-


'''
Name： NetPanelAnalysis
Function: 计算环形网片顶破力、顶破位移、耗能能力
Note: 国际单位制
Version: 1.2.1
Author: Liping GUO
Date: from 2021/8/31 to 
命名方式：以平行于x方向及y方向分别作为后缀
Remark: 影响计算结果的细节因素：
	(1)直线传力纤维与变形后的环网曲面传力路径之间的角度差异 1.5F; 
	(2)三环环链拉伸代表了一种网环受力的最不利情形，实际网片中传力路径上环网轴向应力发展程度可能高于环链试验值+0.18
	(3)需保证夹持卡扣的强度，一旦卡扣强度不足，将发生钢丝滑移失效，造成网片承载力下降。
	(4) 该版本修正了一个错误：对应网环顶破试验，R3/2.2/300其实为R4/2.2/300，而R4/2.2/300其实为R4/3.0/300。
	(5)由于(3)中的原因，剔除了网片试验RN3对应的试验结果，只保留R4/3.0/300的试验结果
	(6)由于(3)中的原因，对于直径为2.2mm钢丝对应的网片规格R4/2.2/300，进行了单独计算
	(7)Bug: gamma_N2的拟合结果与FN2的拟合结果存在不一致情况
	(8)弹簧-纤维单元的双线性刚度特征，导致F_2及E_2在计算时每个单元分别修正与单元不同阶段实际刚度一致
	(9)钢柱摆动、残余高度、窗帘效应
'''

import numpy as np
from userfunc_NPA import *

def func_cablenet_xyz(theta, H, w, Rp, Rs, a, m):
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
		print('Lc_PQ=',Lc_PQ)
	else:
		Lc_PQ = 2*np.sqrt(Rs**2-xP_arr**2) * np.arctan(np.sqrt(Rp**2-xP_arr**2)/np.sqrt(Rs**2-Rp**2))		
		print('Lc_PQ=',Lc_PQ)

	return Lu_PQ, Lc_PQ, Ld_PQ


def func_lengthPQ(x1,y1,x2,y2,x3,y3,x4,y4,a_PlusY,m_PlusY,a_PlusX,m_PlusX,H):
	i_PlusY = np.arange(1,m_PlusY+0.1,step=1)
	xP_PlusY = a_PlusY/2*(2*i_PlusY - m_PlusY - 1)
	yP_PlusY = np.sqrt(Rp**2 - xP_PlusY**2)
	zP_PlusY = H*np.ones_like(xP_PlusY)

	xP_MinusY = xP_PlusY
	yP_MinusY = -yP_PlusY
	zP_MinusY = zP_PlusY

	xQ_PlusY,xQ_MinusY = xP_PlusY,xP_PlusY
	yQ_PlusY,yQ_MinusY =  np.zeros_like(xP_PlusY),np.zeros_like(xP_PlusY)
	zQ_PlusY,zQ_MinusY = np.zeros_like(xP_PlusY),np.zeros_like(xP_PlusY)

	for i in range(len(xP_PlusY)):

		if (xP_PlusY[i]>x1 and xP_PlusY[i]<x2) or (xP_PlusY[i]<x1 and xP_PlusY[i]>x2):
			yQ_Y = y1 + (xP_PlusY[i]-x1)*(y2-y1)/(x2-x1)
			if yQ_Y>yP_PlusY[i]:
				yQ_PlusY[i] = yQ_Y
			elif yQ_Y<yP_MinusY[i]:
				yQ_MinusY[i] = yQ_Y
			else:
				raise ValueError

		elif (xP_PlusY[i]>x2 and xP_PlusY[i]<x3) or (xP_PlusY[i]<x2 and xP_PlusY[i]>x3):
			yQ_Y =  y2 + (xP_PlusY-x2)*(y3-y2)/(x3-x2)
			if yQ_Y>yP_PlusY[i]:
				yQ_PlusY[i] = yQ_Y
			elif yQ_Y<yP_MinusY[i]:
				yQ_MinusY[i] = yQ_Y
			else:
				raise ValueError

		elif (xP_PlusY[i]>x3 and xP_PlusY[i]<x4) or (xP_PlusY[i]<x3 and xP_PlusY[i]>x4):
			yQ_Y =  y3 + (xP_PlusY-x3)*(y4-y3)/(x4-x3)
			if yQ_Y>yP_PlusY[i]:
				yQ_PlusY[i] = yQ_Y
			elif yQ_Y<yP_MinusY[i]:
				yQ_MinusY[i] = yQ_Y
			else:
				raise ValueError

		elif (xP_PlusY[i]>x4 and xP_PlusY[i]<x1) or (xP_PlusY[i]<x4 and xP_PlusY[i]>x1):
			yQ_Y =  y4 + (xP_PlusY-x4)*(y1-y4)/(x1-x4)
			if yQ_Y>yP_PlusY[i]:
				yQ_PlusY[i] = yQ_Y
			elif yQ_Y<yP_MinusY[i]:
				yQ_MinusY[i] = yQ_Y
			else:
				raise ValueError

		else:
			raise ValueError

	i_PlusX = np.arange(1,m_PlusX+0.1,step=1)
	yP_PlusX = a_PlusX/2*(2*i_PlusX - m_PlusX - 1)
	xP_PlusX = np.sqrt(Rp**2 - yP_PlusX**2)
	zP_PlusX = H*np.ones_like(yP_PlusX)

	yP_MinusX = yP_PlusX
	xP_MinusX = -xP_PlusX
	zP_MinusX = zP_PlusX

	yQ_PlusX,yQ_MinusX = yP_PlusX,yP_PlusX
	xQ_PlusX,xQ_MinusX = np.zeros_like(yP_PlusX),np.zeros_like(yP_PlusX)
	zQ_PlusX,zQ_MinusX = np.zeros_like(yP_PlusX),np.zeros_like(yP_PlusX)

	for j in range(len(yP_PlusX)):
		if (yP_PlusX[i]>y1 and yP_PlusX[i]<y2) or (yP_PlusX[i]<y1 and yP_PlusX[i]>y2):
			xQ_X[i] = x1 + (yP_PlusX[i] - y1)*(x2-x1)/(y2-y1)
			if xQ_X[i] > xP_PlusX[i]:
				xQ_PlusX[i] = xQ_X[i]
			elif xQ_X[i] < xP_MinusX[i]:
				xQ_MinusX[i] = xQ_X[i]
			else:
				raise ValueError
		elif (yP_PlusX[i]>y2 and yP_PlusX[i]<y3) or (yP_PlusX[i]<y2 and yP_PlusX[i]>y3):
			xQ_X = x2 + (yP_PlusX[i] - y2)*(x3-x2)/(y3-y2)
			if xQ_X > xP_PlusX[i]:
				xQ_PlusX[i] = xQ_X
			elif xQ_X < xP_MinusX[i]:
				xQ_MinusX[i] = xQ_X
			else:
				raise ValueError

		elif (yP_PlusX[i]>y3 and yP_PlusX[i]<y4) or (yP_PlusX[i]<y3 and yP_PlusX[i]>y4):
			xQ_X[i] = x3 + (yP_PlusX[i] - y3)*(x4-x3)/(y4-y3)
			if xQ_X > xP_PlusX[i]:
				xQ_PlusX[i] = xQ_X
			elif xQ_X < xP_MinusX[i]:
				xQ_MinusX[i] = xQ_X
			else:
				raise ValueError

		elif (yP_PlusX[i]>y4 and yP_PlusX[i]<y1) or (yP_PlusX[i]<y4 and yP_PlusX[i]>y1):
			xQ_X[i] =  x4 + (yP_PlusX[i] - y4)*(x1-x4)/(y1-y4)
			if xQ_X > xP_PlusX[i]:
				xQ_PlusX[i] = xQ_X
			elif xQ_X < xP_MinusX[i]:
				xQ_MinusX[i] = xQ_X
			else:
				raise ValueError

		else:
			raise ValueError

	length_PQ_PlusX = np.sqrt((xP_PlusX-xQ_PlusX)**2+(yP_PlusX-yQ_PlusX)**2+(zP_PlusX-zQ_PlusX)**2)
	length_PQ_PlusY = np.sqrt((xP_PlusY-xQ_PlusY)**2+(yP_PlusY-yQ_PlusY)**2+(zP_PlusY-zQ_PlusY)**2)
	length_PQ_MinusX = np.sqrt((xP_MinusX-xQ_MinusX)**2+(yP_MinusX-yQ_MinusX)**2+(zP_MinusX-zQ_MinusX)**2)
	length_PQ_MinusY = np.sqrt((xP_MinusY-xQ_MinusY)**2+(yP_MinusY-yQ_MinusY)**2+(zP_MinusY-zQ_MinusY)**2)

	return length_PQ_PlusX, length_PQ_PlusY, length_PQ_MinusX, length_PQ_MinusY

def func_lengthArc(H,Rs,Rp,a_DireX,m_DireX,a_DireY,m_DireY):

	i_DireX = np.arange(1,m_DireX+0.1,step=1)
	i_DireY = np.arange(1,m_DireY+0.1,step=1)

	d_DireX = abs(a_DireX/2*(2*i_DireX - m_DireX - 1))
	d_DireY = abs(a_DireY/2*(2*i_DireY - m_DireY - 1))

	minH = Rs-np.sqrt(Rs**2-Rp**2)
	if H>0 and H < minH:
		beta_DireX = 2*np.arctan(np.sqrt((2*H*Rs-H**2-d_DireX**2)/(Rs-H)))
		arc_length_DireX = beta_DireX*np.sqrt(Rs**2-d_DireX**2)
	elif H >= minH:
		alpha_DireX = 2*np.arctan(np.sqrt((Rp**2-d_DireX**2)/(Rs**2-Rp**2)))
		alpha_DireY = 2*np.arctan(np.sqrt((Rp**2-d_DireY**2)/(Rs**2-Rp**2)))
		arc_length_DireX = alpha_DireX*np.sqrt(Rs**2-d_DireX**2)
		arc_length_DireY = alpha_DireY*np.sqrt(Rs**2-d_DireY**2)
	elif H == 0:
		arc_length_DireX = 2*np.sqrt(Rp**2 - d_DireX**2)
		arc_length_DireY = 2*np.sqrt(Rp**2 - d_DireY**2)
	else:
		raise ValueError
	return arc_length_DireX,arc_length_DireY


# 参数输入----------------------------------------------------------------------------------- #
if __name__ == '__main__':

	w = 3.0
	Rp = 0.5  # 加载顶头水平投影半径，若加载形状为多边形时考虑为半径为Rp圆内切
	Rs = 1.2
	a_DireX = 0.3  # 本程序可以用于计算两侧不同的a值（网孔间距）
	a_DireY = 0.3  # 本程序可以用于计算两侧不同的a值（网孔间距）
	H0 = 0  # 网片初始位置（初始高度）
	m_DireX = 2*func_round(Rp/a_DireX)  # 本程序可以用于计算两侧不同数量的力矢量
	m_DireY = 2*func_round(Rp/a_DireY)  # 本程序可以用于计算两侧不同数量的力矢量

	theta = 0.25*np.pi
	x1, y1 = 1.5, 1.5
	x2, y2 = -1.5, 1.5
	x3, y3 = -1.5, -1.5
	x4, y4 = 1.5, -1.5

	length_PQ_PlusX  = func_lengthPQ(x1,y1,x2,y2,x3,y3,x4,y4,a_DireX,m_DireX,a_DireY,m_DireY,H0)[0]
	length_PQ_MinusX = func_lengthPQ(x1,y1,x2,y2,x3,y3,x4,y4,a_DireX,m_DireX,a_DireY,m_DireY,H0)[0]
	length_PQ_PlusY  = func_lengthPQ(x1,y1,x2,y2,x3,y3,x4,y4,a_DireX,m_DireX,a_DireY,m_DireY,H0)[0]
	length_PQ_MinusY = func_lengthPQ(x1,y1,x2,y2,x3,y3,x4,y4,a_DireX,m_DireX,a_DireY,m_DireY,H0)[0]

	length_Arc_DireX = func_lengthArc(H0,Rs,Rp,a_DireX,m_DireX,a_DireY,m_DireY)[0]
	length_Arc_DireY = func_lengthArc(H0,Rs,Rp,a_DireX,m_DireX,a_DireY,m_DireY)[1]

	Lu_PQ0 = func_cablenet_xyz(theta, H0, w, Rp, Rs, a_DireY, m_DireY)[0]
	Lc_PQ0 = func_cablenet_xyz(theta, H0, w, Rp, Rs, a_DireY, m_DireY)[1]
	Ld_PQ0 = func_cablenet_xyz(theta, H0, w, Rp, Rs, a_DireY, m_DireY)[2]

	L_PQ0 = Lu_PQ0 + Lc_PQ0 + Ld_PQ0
	L_DireX = length_PQ_PlusX + length_PQ_MinusX + length_Arc_DireX
	print('L_PQ0=',Lu_PQ0)
	print('L_DireX=',length_PQ_MinusX)
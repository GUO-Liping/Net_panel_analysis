#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Name： NetPanelAnalysis
Function: 计算环形网片顶破力、顶破位移、耗能能力
Note: 国际单位制
Version: 1.0.3
Author: Liping GUO
Date: 2021/4/7
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

# 参数输入----------------------------------------------------------------------------------- #
if __name__ == '__main__':
	# MULTIPLE FACTORS INPUT
	nw = 5  # 网环圈数
	d = func_return_d(nw)  # 制作网环的钢丝直径
	D = 0.3  # 单个网环直径
	Rp = 1.0/2  # 加载顶头水平投影半径，若加载形状为多边形时考虑为半径为Rp圆内切
	w = 3.0
	# ns = 12
	# w = (np.sqrt(2)*(ns-1)+1)*0.3+0.2-0.0455844122715714  # 矩形网片短边长度
	# print('w=',w)

	kappa = 1  # 网片长宽比：为大于1的常数

	ls0_PQ = 0.05  # 初始弹簧长度
	ls0_CD = 0.05  # 初始弹簧长度

	ex = 0.0  # 加载位置偏心距离
	ey = 0.0  # 加载位置偏心距离
	sigma_y = 1770e6  # 钢丝材料屈服强度

	blockShape = 'round'  # blockShape must be 'Round' or 'Polygon'!
	curtain = False  # 是否考虑窗帘效应，True为考虑，False为不考虑！
	boundary = 'Flexible'  # boundary must be 'Rigid' or 'Flexible'!

	A = nw * np.pi*d**2/4  # 单肢截面面积
	a = np.pi*D/(2*(1+kappa))  # 变形后网环短边长度
	mPQ, mCD = func_m(blockShape,Rp,kappa,a)  # 坐标系中x（PQ）y(CD)方向力矢量个数
	print('mPQ, mCD=',mPQ, mCD)

	Rope1770Steel = {'3':5.29,'4':9.40,'5':14.7,'6':21.2,'7':28.8,'8':37.6,'9':47.6,'10':58.8,'11':71.1,'12':84.6,'13':99.3,'14':115,'16':150,'18':190,'20':235,'22':284,'24':338}
	sigma_rope = 1770e6
	E_rope = 94.5e9

	d_ropePQ = 18
	F_ropePQ = 1000*Rope1770Steel[str(d_ropePQ)]  # 1000为换算国际单位
	l0_ropePQ = kappa*w  # 钢丝绳初始长度
	sigma_ropePQ = sigma_rope
	E_ropePQ = E_rope  # 钢丝绳弹性模量

	d_ropeCD = 18
	F_ropeCD = 1000*Rope1770Steel[str(d_ropeCD)]  # 1000为换算国际单位,钢丝绳破断力
	l0_ropeCD = w  # 钢丝绳初始长度
	sigma_ropeCD = sigma_rope  # 钢丝绳应力强度
	E_ropeCD = E_rope  # 钢丝绳弹性模量

	lb_onePQ = 0.8  # 单个耗能器最大行程800mm
	b_numPQ = 0  # 边界钢丝绳两端串联的耗能器数量（耗能器连接方式：串联！！）
	lb_maxPQ = b_numPQ * lb_onePQ  # 边界钢丝绳两端串联的耗能器总伸长量

	lb_oneCD= 0.8  # 单个耗能器最大行程800mm
	b_numCD = 0  # 边界钢丝绳一端串联的耗能器数量（耗能器连接方式：串联！！）
	lb_maxCD = b_numCD * lb_oneCD  # 边界钢丝绳两端串联的耗能器总伸长量

	# 环链试验----------------------------------------------------------------------------------- #
  	# 将三环环链试验力位移数据转换为弹簧纤维单元中的纤维双折线E1,E2应力应变关系
	FN1, FN2, lN0, lN1, lN2, gamma_N1, gamma_N2 = func_ringChianDataFit(nw, sigma_y, d)
	E1 = FN1*lN0/(2*A*(lN1 - lN0))
	E2 = (FN2-FN1)*lN0 / (2*A*(lN2 - lN1))

	gamma_ave = gamma_N2/4  # 柔性边界下作用于钢丝绳上的平均分布荷载集度

	dictRigid = {'ks':1e20}
	dictRopePQ = {'l0_rope':l0_ropePQ,'m':mPQ,'F_rope':F_ropePQ,'sigma_rope':sigma_ropePQ,'E_rope':E_ropePQ}
	dictRopeCD = {'l0_rope':l0_ropeCD,'m':mCD,'F_rope':F_ropeCD,'sigma_rope':sigma_ropeCD,'E_rope':E_ropeCD}
	dictBrakerPQ = {'lb_one':lb_maxPQ,'b_num':b_numPQ,'lb_max':lb_maxPQ}
	dictBrakerCD = {'lb_one':lb_maxCD,'b_num':b_numCD,'lb_max':lb_maxCD}

	dictFiber = {'gamma_ave':gamma_ave,'sigma_y':sigma_y,'gamma_N2':gamma_N2,'A':A}

	dictBoundaryPQ = {**dictRigid,**dictRopePQ,**dictBrakerPQ,**dictFiber}  # PQ连接的钢丝绳参数字典
	dictBoundaryCD = {**dictRigid,**dictRopeCD,**dictBrakerCD,**dictFiber}  # CD连接的钢丝绳参数字典

	ks_PQ = func_ks(boundary,**dictBoundaryPQ)  # 弹簧刚度，指代刚性边界或柔性边界
	ks_CD = func_ks(boundary,**dictBoundaryCD)  # 弹簧刚度，指代刚性边界或柔性边界
	#ks11 = 50000000
	#ks_PQ = ks11
	#ks_CD = ks11
	print('ks_PQ=',ks_PQ)
	print('ks_CD=',ks_CD)
	func_inputCheck(nw,d,D,Rp,w,kappa,ks_PQ,ks_CD,ls0_PQ,ls0_CD,ex,ey)  # 检查参数输入有无错误

	# 各个纤维弹簧单元初始长度
	L0_PQxy  ,	L0_CDxy  = func_xyz(blockShape, curtain, '+x+y', w, kappa, Rp, a, ex, ey, 0)
	L0_PQ_xy ,	L0_CD_xy = func_xyz(blockShape, curtain, '-x+y', w, kappa, Rp, a, ex, ey, 0)
	L0_PQx_y ,	L0_CDx_y = func_xyz(blockShape, curtain, '+x-y', w, kappa, Rp, a, ex, ey, 0)
	L0_PQ_x_y,	L0_CD_x_y= func_xyz(blockShape, curtain, '-x-y', w, kappa, Rp, a, ex, ey, 0)
	
	# 各个纤维弹簧单元中纤维的初始长度
	lf0_PQxy  ,	lf0_CDxy  = L0_PQxy  -ls0_PQ, L0_CDxy  -ls0_CD
	lf0_PQ_xy ,	lf0_CD_xy = L0_PQ_xy -ls0_PQ, L0_CD_xy -ls0_CD
	lf0_PQx_y ,	lf0_CDx_y = L0_PQx_y -ls0_PQ, L0_CDx_y -ls0_CD
	lf0_PQ_x_y,	lf0_CD_x_y= L0_PQ_x_y-ls0_PQ, L0_CD_x_y-ls0_CD

	# 第一阶段纤维弹簧单元刚度
	K1_PQxy  , K1_CDxy  = 1/(lf0_PQxy  /(E1*A)+1/ks_PQ), 1/(lf0_CDxy  /(E1*A)+1/ks_CD)
	K1_PQ_xy , K1_CD_xy = 1/(lf0_PQ_xy /(E1*A)+1/ks_PQ), 1/(lf0_CD_xy /(E1*A)+1/ks_CD)
	K1_PQx_y , K1_CDx_y = 1/(lf0_PQx_y /(E1*A)+1/ks_PQ), 1/(lf0_CDx_y /(E1*A)+1/ks_CD)
	K1_PQ_x_y, K1_CD_x_y= 1/(lf0_PQ_x_y/(E1*A)+1/ks_PQ), 1/(lf0_CD_x_y/(E1*A)+1/ks_CD)
	
	# 第二阶段纤维弹簧单元刚度
	K2_PQxy  , K2_CDxy  = 1/(lf0_PQxy  /(E2*A)+1/ks_PQ), 1/(lf0_CDxy  /(E2*A)+1/ks_CD)
	K2_PQ_xy , K2_CD_xy = 1/(lf0_PQ_xy /(E2*A)+1/ks_PQ), 1/(lf0_CD_xy /(E2*A)+1/ks_CD)
	K2_PQx_y , K2_CDx_y = 1/(lf0_PQx_y /(E2*A)+1/ks_PQ), 1/(lf0_CDx_y /(E2*A)+1/ks_CD)
	K2_PQ_x_y, K2_CD_x_y= 1/(lf0_PQ_x_y/(E2*A)+1/ks_PQ), 1/(lf0_CD_x_y/(E2*A)+1/ks_CD)

	# 两个方向最短纤维弹簧单元（最薄弱单元）的长度与该单元的位置，两阶段刚度，用于计算顶破高度
	L0minPQ,idPQ,K1minPQ,K2minPQ = func_minElement(L0_PQxy, L0_PQ_xy, L0_PQx_y, L0_PQ_x_y,K1_PQxy,K2_PQxy)
	L0minCD,idCD,K1minCD,K2minCD = func_minElement(L0_CDxy, L0_CD_xy, L0_CDx_y, L0_CD_x_y,K1_CDxy,K2_CDxy)

	#print('L0minPQ,idPQ,K1minPQ,K2minPQ=',L0minPQ,idPQ,K1minPQ,K2minPQ)
	#print('L0minCD,idCD,K1minCD,K2minCD=',L0minCD,idCD,K1minCD,K2minCD)
	# 两个方向单元确定的两阶段高度
	z1PQ, z2PQ = func_compute_z1z2(L0minPQ,K1minPQ,K2minPQ,gamma_N1,gamma_N2,sigma_y,A)
	z1CD, z2CD = func_compute_z1z2(L0minCD,K1minCD,K2minCD,gamma_N1,gamma_N2,sigma_y,A)

	# 找出计算模型所有单元中的最短纤维弹簧单元
	L0min = np.min([L0minPQ,L0minCD])
	#print('z1PQ,z1CD,z2PQ,z2CD=',z1PQ,z1CD,z2PQ,z2CD)
	z1, z2 = func_Checkz1z2(z1PQ,z1CD,z2PQ,z2CD)
	maxTheta1 = np.arctan(z1/L0min)  # 第一阶段纤维-弹簧单元最大角度
	maxTheta2 = np.arctan(z2/L0min)  # 第二阶段纤维-弹簧单元最大角度
	
	# 第一阶段各个纤维弹簧单元长度
	L1_PQxy  ,	L1_CDxy  = func_xyz(blockShape, curtain, '+x+y', w, kappa, Rp, a, ex, ey, z1)
	L1_PQ_xy ,	L1_CD_xy = func_xyz(blockShape, curtain, '-x+y', w, kappa, Rp, a, ex, ey, z1)
	L1_PQx_y ,	L1_CDx_y = func_xyz(blockShape, curtain, '+x-y', w, kappa, Rp, a, ex, ey, z1)
	L1_PQ_x_y,	L1_CD_x_y= func_xyz(blockShape, curtain, '-x-y', w, kappa, Rp, a, ex, ey, z1)

	# 第二阶段各个纤维弹簧单元长度
	L2_PQxy  ,	L2_CDxy  = func_xyz(blockShape, curtain, '+x+y', w, kappa, Rp, a, ex, ey, z2)
	L2_PQ_xy ,	L2_CD_xy = func_xyz(blockShape, curtain, '-x+y', w, kappa, Rp, a, ex, ey, z2)
	L2_PQx_y ,	L2_CDx_y = func_xyz(blockShape, curtain, '+x-y', w, kappa, Rp, a, ex, ey, z2)
	L2_PQ_x_y,	L2_CD_x_y= func_xyz(blockShape, curtain, '-x-y', w, kappa, Rp, a, ex, ey, z2)

	# 第一阶段各个纤维弹簧单元与加载方向的夹角
	Ang1_PQxy  , Ang1_CDxy   = np.arccos(z1/L1_PQxy)  , np.arccos(z1/L1_CDxy)
	Ang1_PQ_xy , Ang1_CD_xy  = np.arccos(z1/L1_PQ_xy) , np.arccos(z1/L1_CD_xy)
	Ang1_PQx_y , Ang1_CDx_y  = np.arccos(z1/L1_PQx_y) , np.arccos(z1/L1_CDx_y)
	Ang1_PQ_x_y, Ang1_CD_x_y = np.arccos(z1/L1_PQ_x_y), np.arccos(z1/L1_CD_x_y)

	# 第二阶段各个纤维弹簧单元与加载方向的夹角
	Ang2_PQxy  , Ang2_CDxy   = np.arccos(z2/L2_PQxy)  , np.arccos(z2/L2_CDxy)
	Ang2_PQ_xy , Ang2_CD_xy  = np.arccos(z2/L2_PQ_xy) , np.arccos(z2/L2_CD_xy)
	Ang2_PQx_y , Ang2_CDx_y  = np.arccos(z2/L2_PQx_y) , np.arccos(z2/L2_CDx_y)
	Ang2_PQ_x_y, Ang2_CD_x_y = np.arccos(z2/L2_PQ_x_y), np.arccos(z2/L2_CD_x_y)

	chi_ang = 0.65  # chi为考虑实际顶破后环绕加载区域边缘网环内钢丝纤维与竖直方向夹角小于模型角度的修正系数
	
	# 第一阶段各个纤维弹簧单元内力
	F1_PQxy  , F2_PQxy  , E1_PQxy  ,E2_PQxy   = func_vectorFiEi(L0_PQxy  ,L1_PQxy  ,L2_PQxy  ,K1_PQxy  ,K2_PQxy  ,gamma_N1,sigma_y,A)
	F1_PQ_xy , F2_PQ_xy , E1_PQ_xy ,E2_PQ_xy  = func_vectorFiEi(L0_PQ_xy ,L1_PQ_xy ,L2_PQ_xy ,K1_PQ_xy ,K2_PQ_xy ,gamma_N1,sigma_y,A)
	F1_PQx_y , F2_PQx_y , E1_PQx_y ,E2_PQx_y  = func_vectorFiEi(L0_PQx_y ,L1_PQx_y ,L2_PQx_y ,K1_PQx_y ,K2_PQx_y ,gamma_N1,sigma_y,A)
	F1_PQ_x_y, F2_PQ_x_y, E1_PQ_x_y,E2_PQ_x_y = func_vectorFiEi(L0_PQ_x_y,L1_PQ_x_y,L2_PQ_x_y,K1_PQ_x_y,K2_PQ_x_y,gamma_N1,sigma_y,A)

	F1_CDxy  , F2_CDxy  , E1_CDxy  ,E2_CDxy   = func_vectorFiEi(L0_CDxy  ,L1_CDxy  ,L2_CDxy  ,K1_CDxy  ,K2_CDxy  ,gamma_N1,sigma_y,A)
	F1_CD_xy , F2_CD_xy , E1_CD_xy ,E2_CD_xy  = func_vectorFiEi(L0_CD_xy ,L1_CD_xy ,L2_CD_xy ,K1_CD_xy ,K2_CD_xy ,gamma_N1,sigma_y,A)
	F1_CDx_y , F2_CDx_y , E1_CDx_y ,E2_CDx_y  = func_vectorFiEi(L0_CDx_y ,L1_CDx_y ,L2_CDx_y ,K1_CDx_y ,K2_CDx_y ,gamma_N1,sigma_y,A)
	F1_CD_x_y, F2_CD_x_y, E1_CD_x_y,E2_CD_x_y = func_vectorFiEi(L0_CD_x_y,L1_CD_x_y,L2_CD_x_y,K1_CD_x_y,K2_CD_x_y,gamma_N1,sigma_y,A)

	# 第一、二阶段各个纤维弹簧单元中纤维长度与弹簧长度
	ls1_PQxy  ,ls2_PQxy  ,lf1_PQxy  ,lf2_PQxy   = func_lslf(F1_PQxy  ,F2_PQxy  ,L1_PQxy  ,L2_PQxy  ,ls0_PQ,lf0_PQxy  ,ks_PQ,E1,E2,gamma_N1,sigma_y,A)
	ls1_PQ_xy ,ls2_PQ_xy ,lf1_PQ_xy ,lf2_PQ_xy  = func_lslf(F1_PQ_xy ,F2_PQ_xy ,L1_PQ_xy ,L2_PQ_xy ,ls0_PQ,lf0_PQ_xy ,ks_PQ,E1,E2,gamma_N1,sigma_y,A)
	ls1_PQx_y ,ls2_PQx_y ,lf1_PQx_y ,lf2_PQx_y  = func_lslf(F1_PQx_y ,F2_PQx_y ,L1_PQx_y ,L2_PQx_y ,ls0_PQ,lf0_PQx_y ,ks_PQ,E1,E2,gamma_N1,sigma_y,A)
	ls1_PQ_x_y,ls2_PQ_x_y,lf1_PQ_x_y,lf2_PQ_x_y = func_lslf(F1_PQ_x_y,F2_PQ_x_y,L1_PQ_x_y,L2_PQ_x_y,ls0_PQ,lf0_PQ_x_y,ks_PQ,E1,E2,gamma_N1,sigma_y,A)

	ls1_CDxy  ,ls2_CDxy  ,lf1_CDxy  ,lf2_CDxy   = func_lslf(F1_CDxy  ,F2_CDxy  ,L1_CDxy  ,L2_CDxy  ,ls0_CD,lf0_CDxy  ,ks_CD,E1,E2,gamma_N1,sigma_y,A)
	ls1_CD_xy ,ls2_CD_xy ,lf1_CD_xy ,lf2_CD_xy  = func_lslf(F1_CD_xy ,F2_CD_xy ,L1_CD_xy ,L2_CD_xy ,ls0_CD,lf0_CD_xy ,ks_CD,E1,E2,gamma_N1,sigma_y,A)
	ls1_CDx_y ,ls2_CDx_y ,lf1_CDx_y ,lf2_CDx_y  = func_lslf(F1_CDx_y ,F2_CDx_y ,L1_CDx_y ,L2_CDx_y ,ls0_CD,lf0_CDx_y ,ks_CD,E1,E2,gamma_N1,sigma_y,A)
	ls1_CD_x_y,ls2_CD_x_y,lf1_CD_x_y,lf2_CD_x_y = func_lslf(F1_CD_x_y,F2_CD_x_y,L1_CD_x_y,L2_CD_x_y,ls0_PQ,lf0_CD_x_y,ks_PQ,E1,E2,gamma_N1,sigma_y,A)

	H_net = z2  # 顶破高度

	# 顶破时刻各个单元内力在加载方向的分量
	F_PQx = np.sum(F2_PQxy *np.cos(chi_ang*Ang2_PQxy)) + np.sum(F2_PQxy *np.cos(chi_ang*Ang2_PQx_y))
	F_PQ_x= np.sum(F2_PQ_xy*np.cos(chi_ang*Ang2_PQ_xy))+ np.sum(F2_PQ_xy*np.cos(chi_ang*Ang2_PQ_x_y))

	F_CDy = np.sum(F2_CDxy *np.cos(chi_ang*Ang2_CDxy)) + np.sum(F2_CDxy *np.cos(chi_ang*Ang2_CD_xy))
	F_CD_y= np.sum(F2_CDx_y*np.cos(chi_ang*Ang2_CDx_y))+ np.sum(F2_CDx_y*np.cos(chi_ang*Ang2_CD_x_y))

	F_net = F_PQx + F_PQ_x + F_CDy + F_CD_y  # 顶破力

	# 顶破时刻各个单元消耗能量值
	Exy  = np.sum(E2_PQxy)   + np.sum(E2_CDxy)
	E_xy = np.sum(E2_PQ_xy)  + np.sum(E2_CD_xy)
	Ex_y = np.sum(E2_PQx_y)  + np.sum(E2_CDx_y)
	E_x_y= np.sum(E2_PQ_x_y) + np.sum(E2_CD_x_y)
	
	E_net = Exy + E_xy + Ex_y + E_x_y  # 顶破耗能

	print('Displacement = ', format(H_net, '.3f'), 'm')
	print('Force = ', format(F_net/1000, '.3f'), 'kN')
	print('Energy = ', format(E_net/1000, '.3f'), 'kJ')


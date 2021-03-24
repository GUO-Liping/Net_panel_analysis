#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Name： NetPanelAnalysis
Function: 计算环形网片顶破力、顶破位移、耗能能力
Note: 国际单位制
Version: 1.0.2.alpha1
Author: Liping GUO
Date: 2020/4/1
命名方式：以平行于x方向及y方向分别作为后缀
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
from userfunc_NPA import *

# 参数输入----------------------------------------------------------------------------------- #
if __name__ == '__main__':

	nw = 7
	d = func_return_d(nw)
	D = 0.3
	Rp = 0.5 
	w = 2.95
	kappa = 1
	ks_PQ = 500000000  # 弹簧刚度，指代卸扣边界（刚体）
	ks_CD = 500000000  # 弹簧刚度，指代卸扣边界（刚体）
	sigma_y = 1770e6
	A = nw * np.pi*d**2/4  # 单肢截面面积
	a = np.pi*D/(2*(1+kappa))
	ls0_PQ = 0.05
	ls0_CD = 0.05
	ex = 0
	ey = 0
	
	# 环链试验----------------------------------------------------------------------------------- #

	FN1, FN2, lN0, lN1, lN2, gamma_N1, gamma_N2 = func_ringChianDataFit(nw, sigma_y, d)
	E1 = FN1*lN0/(2*A*(lN1 - lN0))
	E2 = (FN2-FN1)*lN0 / (2*A*(lN2 - lN1))

	L0_PQxy  ,	L0_CDxy  = func_xyz('+x+y', w, kappa, Rp, a, ex, ey, 0)
	L0_PQ_xy ,	L0_CD_xy = func_xyz('-x+y', w, kappa, Rp, a, ex, ey, 0)
	L0_PQx_y ,	L0_CDx_y = func_xyz('+x-y', w, kappa, Rp, a, ex, ey, 0)
	L0_PQ_x_y,	L0_CD_x_y= func_xyz('-x-y', w, kappa, Rp, a, ex, ey, 0)

	lf0_PQxy  ,	lf0_CDxy  = L0_PQxy  -ls0_PQ, L0_CDxy  -ls0_CD
	lf0_PQ_xy ,	lf0_CD_xy = L0_PQ_xy -ls0_PQ, L0_CD_xy -ls0_CD
	lf0_PQx_y ,	lf0_CDx_y = L0_PQx_y -ls0_PQ, L0_CDx_y -ls0_CD
	lf0_PQ_x_y,	lf0_CD_x_y= L0_PQ_x_y-ls0_PQ, L0_CD_x_y-ls0_CD

	K1_PQxy  , K1_CDxy  = 1/(lf0_PQxy  /(E1*A)+1/ks_PQ), 1/(lf0_CDxy  /(E1*A)+1/ks_CD)
	K1_PQ_xy , K1_CD_xy = 1/(lf0_PQ_xy /(E1*A)+1/ks_PQ), 1/(lf0_CD_xy /(E1*A)+1/ks_CD)
	K1_PQx_y , K1_CDx_y = 1/(lf0_PQx_y /(E1*A)+1/ks_PQ), 1/(lf0_CDx_y /(E1*A)+1/ks_CD)
	K1_PQ_x_y, K1_CD_x_y= 1/(lf0_PQ_x_y/(E1*A)+1/ks_PQ), 1/(lf0_CD_x_y/(E1*A)+1/ks_CD)

	K2_PQxy  , K2_CDxy  = 1/(lf0_PQxy  /(E2*A)+1/ks_PQ), 1/(lf0_CDxy  /(E2*A)+1/ks_CD)
	K2_PQ_xy , K2_CD_xy = 1/(lf0_PQ_xy /(E2*A)+1/ks_PQ), 1/(lf0_CD_xy /(E2*A)+1/ks_CD)
	K2_PQx_y , K2_CDx_y = 1/(lf0_PQx_y /(E2*A)+1/ks_PQ), 1/(lf0_CDx_y /(E2*A)+1/ks_CD)
	K2_PQ_x_y, K2_CD_x_y= 1/(lf0_PQ_x_y/(E2*A)+1/ks_PQ), 1/(lf0_CD_x_y/(E2*A)+1/ks_CD)

	L0minPQ,idPQ,K1minPQ,K2minPQ = func_minElement(L0_PQxy, L0_PQ_xy, L0_PQx_y, L0_PQ_x_y,K1_PQxy,K2_PQxy)
	L0minCD,idCD,K1minCD,K2minCD = func_minElement(L0_CDxy, L0_CD_xy, L0_CDx_y, L0_CD_x_y,K1_CDxy,K2_CDxy)

	z1PQ, z2PQ = func_compute_z1z2(L0minPQ,K1minPQ,K2minPQ,gamma_N1,gamma_N2,sigma_y,A)
	z1CD, z2CD = func_compute_z1z2(L0minCD,K1minCD,K2minCD,gamma_N1,gamma_N2,sigma_y,A)

	z1, z2 = func_z1z2(z1PQ,z1CD,z2PQ,z2CD)

	L1_PQxy  ,	L1_CDxy  = func_xyz('+x+y', w, kappa, Rp, a, ex, ey, z1)
	L1_PQ_xy ,	L1_CD_xy = func_xyz('-x+y', w, kappa, Rp, a, ex, ey, z1)
	L1_PQx_y ,	L1_CDx_y = func_xyz('+x-y', w, kappa, Rp, a, ex, ey, z1)
	L1_PQ_x_y,	L1_CD_x_y= func_xyz('-x-y', w, kappa, Rp, a, ex, ey, z1)

	L2_PQxy  ,	L2_CDxy  = func_xyz('+x+y', w, kappa, Rp, a, ex, ey, z2)
	L2_PQ_xy ,	L2_CD_xy = func_xyz('-x+y', w, kappa, Rp, a, ex, ey, z2)
	L2_PQx_y ,	L2_CDx_y = func_xyz('+x-y', w, kappa, Rp, a, ex, ey, z2)
	L2_PQ_x_y,	L2_CD_x_y= func_xyz('-x-y', w, kappa, Rp, a, ex, ey, z2)

	F1_PQxy  , F2_PQxy  , E1_PQxy  ,E2_PQxy   = func_vectorFiEi(L0_PQxy  ,L1_PQxy  ,L2_PQxy  ,K1_PQxy  ,K2_PQxy  ,gamma_N1,sigma_y,A)
	F1_CDxy  , F2_CDxy  , E1_CDxy  ,E2_CDxy   = func_vectorFiEi(L0_CDxy  ,L1_CDxy  ,L2_CDxy  ,K1_CDxy  ,K2_CDxy  ,gamma_N1,sigma_y,A)
	F1_PQ_xy , F2_PQ_xy , E1_PQ_xy ,E2_PQ_xy  = func_vectorFiEi(L0_PQ_xy ,L1_PQ_xy ,L2_PQ_xy ,K1_PQ_xy ,K2_PQ_xy ,gamma_N1,sigma_y,A)
	F1_CD_xy , F2_CD_xy , E1_CD_xy ,E2_CD_xy  = func_vectorFiEi(L0_CD_xy ,L1_CD_xy ,L2_CD_xy ,K1_CD_xy ,K2_CD_xy ,gamma_N1,sigma_y,A)
	F1_PQx_y , F2_PQx_y , E1_PQx_y ,E2_PQx_y  = func_vectorFiEi(L0_PQx_y ,L1_PQx_y ,L2_PQx_y ,K1_PQx_y ,K2_PQx_y ,gamma_N1,sigma_y,A)
	F1_CDx_y , F2_CDx_y , E1_CDx_y ,E2_CDx_y  = func_vectorFiEi(L0_CDx_y ,L1_CDx_y ,L2_CDx_y ,K1_CDx_y ,K2_CDx_y ,gamma_N1,sigma_y,A)
	F1_PQ_x_y, F2_PQ_x_y, E1_PQ_x_y,E2_PQ_x_y = func_vectorFiEi(L0_PQ_x_y,L1_PQ_x_y,L2_PQ_x_y,K1_PQ_x_y,K2_PQ_x_y,gamma_N1,sigma_y,A)
	F1_CD_x_y, F2_CD_x_y, E1_CD_x_y,E2_CD_x_y = func_vectorFiEi(L0_CD_x_y,L1_CD_x_y,L2_CD_x_y,K1_CD_x_y,K2_CD_x_y,gamma_N1,sigma_y,A)

	ls1_PQxy  ,ls2_PQxy  ,lf1_PQxy  ,lf2_PQxy   = func_lslf(F1_PQxy  ,F2_PQxy  ,L1_PQxy  ,L2_PQxy  ,ls0_PQ,lf0_PQxy  ,ks_PQ,E1,E2,gamma_N1,sigma_y,A)
	ls1_CDxy  ,ls2_CDxy  ,lf1_CDxy  ,lf2_CDxy   = func_lslf(F1_CDxy  ,F2_CDxy  ,L1_CDxy  ,L2_CDxy  ,ls0_CD,lf0_CDxy  ,ks_CD,E1,E2,gamma_N1,sigma_y,A)
	ls1_PQ_xy ,ls2_PQ_xy ,lf1_PQ_xy ,lf2_PQ_xy  = func_lslf(F1_PQ_xy ,F2_PQ_xy ,L1_PQ_xy ,L2_PQ_xy ,ls0_PQ,lf0_PQ_xy ,ks_PQ,E1,E2,gamma_N1,sigma_y,A)
	ls1_CD_xy ,ls2_CD_xy ,lf1_CD_xy ,lf2_CD_xy  = func_lslf(F1_CD_xy ,F2_CD_xy ,L1_CD_xy ,L2_CD_xy ,ls0_CD,lf0_CD_xy ,ks_CD,E1,E2,gamma_N1,sigma_y,A)
	ls1_PQx_y ,ls2_PQx_y ,lf1_PQx_y ,lf2_PQx_y  = func_lslf(F1_PQx_y ,F2_PQx_y ,L1_PQx_y ,L2_PQx_y ,ls0_PQ,lf0_PQx_y ,ks_PQ,E1,E2,gamma_N1,sigma_y,A)
	ls1_CDx_y ,ls2_CDx_y ,lf1_CDx_y ,lf2_CDx_y  = func_lslf(F1_CDx_y ,F2_CDx_y ,L1_CDx_y ,L2_CDx_y ,ls0_CD,lf0_CDx_y ,ks_CD,E1,E2,gamma_N1,sigma_y,A)
	ls1_PQ_x_y,ls2_PQ_x_y,lf1_PQ_x_y,lf2_PQ_x_y = func_lslf(F1_PQ_x_y,F2_PQ_x_y,L1_PQ_x_y,L2_PQ_x_y,ls0_PQ,lf0_PQ_x_y,ks_PQ,E1,E2,gamma_N1,sigma_y,A)
	ls1_CD_x_y,ls2_CD_x_y,lf1_CD_x_y,lf2_CD_x_y = func_lslf(F1_CD_x_y,F2_CD_x_y,L1_CD_x_y,L2_CD_x_y,ls0_PQ,lf0_CD_x_y,ks_PQ,E1,E2,gamma_N1,sigma_y,A)

	H_net = z2

	Fxy = np.sum(F2_PQxy*z2/L2_PQxy)+np.sum(F2_CDxy*z2/L2_CDxy)
	F_xy =  np.sum(F2_PQ_xy*z2/L2_PQ_xy)+np.sum(F2_CD_xy*z2/L2_CD_xy)
	Fx_y =  np.sum(F2_PQx_y*z2/L2_PQx_y)+np.sum(F2_CDx_y*z2/L2_CDx_y)
	F_x_y =  np.sum(F2_PQ_x_y*z2/L2_PQ_x_y)+np.sum(F2_CD_x_y*z2/L2_CD_x_y)
	F_net = Fxy + F_xy +(Fx_y + F_x_y)

	Exy  = np.sum(E2_PQxy) + np.sum(E2_CDxy)
	E_xy = np.sum(E2_PQ_xy) + np.sum(E2_CD_xy)
	Ex_y = np.sum(E2_PQx_y) + np.sum(E2_CDx_y)
	E_x_y= np.sum(E2_PQ_x_y) + np.sum(E2_CD_x_y)
	E_net = Exy + E_xy + Ex_y + E_x_y

	print('Displacement = ', format(H_net, '.3f'), 'm')
	print('Force = ', format(F_net/1000, '.3f'), 'kN')
	print('Energy = ', format(E_net/1000, '.3f'), 'kJ')



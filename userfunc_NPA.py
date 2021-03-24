#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np

def func_xyz(points, w, kappa, Rp, a, ex, ey, z):
	mPQ = func_round(Rp/a)
	index_mPQ = np.linspace(1, mPQ, mPQ, endpoint=True)

	xP = a * (index_mPQ - 1/2) + ex
	yP = np.sqrt(Rp**2 - (a*index_mPQ - a/2)**2) + ey
	zP = np.zeros(mPQ) + z

	xQ = kappa*w * (index_mPQ-1/2)/(2*mPQ + 1)
	yQ = np.zeros(mPQ) + w/2
	zQ = np.zeros(mPQ) + 0

	mCD = func_round(Rp/(kappa*a))
	index_mCD = np.linspace(1, mCD, mCD, endpoint=True)

	xC = np.sqrt(Rp**2 - (kappa*a*index_mCD - kappa*a/2)**2) + ex
	yC = kappa*a * (index_mCD - 1/2) + ey
	zC = np.zeros(mCD) + z

	xD = np.zeros(mCD) + kappa*w/2
	yD = w * (index_mCD-1/2)/(2*mCD + 1)
	zD = np.zeros(mCD) + 0

	if points == '+x+y':
		xP, xC = xP, xC
		yP, yC = yP, yC
		zP, zC = zP, zC
		xQ, xD = xQ, xD
		yQ, yD = yQ, yD
		zQ, zD = zQ, zD
		LPQ = np.sqrt((xP-xQ)**2 +(yP-yQ)**2 +(zP-zQ)**2)
		LCD = np.sqrt((xC-xD)**2 +(yC-yD)**2 +(zC-zD)**2)
		return LPQ, LCD 

	elif points == '-x+y':
		xPminusX ,xCminusX = 2*ex - xP	,2*ex - xC
		yPminusX ,yCminusX = yP			,yC
		zPminusX ,zCminusX = zP			,zC
		xQminusX ,xDminusX = -xQ		,-xD
		yQminusX ,yDminusX = yQ			,yD
		zQminusX ,zDminusX = zQ			,zD
		LPQ = np.sqrt((xPminusX-xQminusX)**2 +(yPminusX-yQminusX)**2 +(zPminusX-zQminusX)**2)
		LCD = np.sqrt((xCminusX-xDminusX)**2 +(yCminusX-yDminusX)**2 +(zCminusX-zDminusX)**2)
		return LPQ, LCD 

	elif points == '+x-y':
		xPminusY, xCminusY = xP			, xC
		yPminusY, yCminusY = 2*ey - yP	, 2*ey - yC
		zPminusY, zCminusY = zP			, zC
		xQminusY, xDminusY = xQ			, xD
		yQminusY, yDminusY = -yQ		, -yD
		zQminusY, zDminusY = zQ			, zD
		LPQ = np.sqrt((xPminusY-xQminusY)**2 +(yPminusY-yQminusY)**2 +(zPminusY-zQminusY)**2)
		LCD = np.sqrt((xCminusY-xDminusY)**2 +(yCminusY-yDminusY)**2 +(zCminusY-zDminusY)**2)
		return LPQ, LCD 

	elif points == '-x-y':
		xPminusXY, xCminusXY = 2*ex - xP, 2*ex - xC	
		yPminusXY, yCminusXY = 2*ey - yP, 2*ey - yC	
		zPminusXY, zCminusXY = zP		, zC
		xQminusXY, xDminusXY = -xQ		, -xD
		yQminusXY, yDminusXY = -yQ		, -yD
		zQminusXY, zDminusXY = zQ		, zD
		LPQ = np.sqrt((xPminusXY-xQminusXY)**2 +(yPminusXY-yQminusXY)**2 +(zPminusXY-zQminusXY)**2)
		LCD = np.sqrt((xCminusXY-xDminusXY)**2 +(yCminusXY-yDminusXY)**2 +(zCminusXY-zDminusXY)**2)
		return LPQ, LCD 

	else:
		raise ValueError


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
    # after_fit_gammaN2 = np.polyval(poly_gammaN2_func, nw) + 0.18
    after_fit_gammaN2 = np.polyval(poly_gammaN2_func, nw)
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


def funcXY_correct_gammaForceEnergy(mx, gamma_N2_x, F2_x, E2_x, gamma_N1, K2_x, K1_x, L2_x, L1_x, L0_x, sigma_y, A):

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


def func_minElement(L0_CDxy, L0_CD_xy, L0_CDx_y, L0_CD_x_y,K1_CDxy,K2_CDxy):
	c1, c2, c3, c4 = len(L0_CDxy), len(L0_CD_xy), len(L0_CDx_y), len(L0_CD_x_y)
	min_CD = np.min([L0_CDxy, L0_CD_xy, L0_CDx_y, L0_CD_x_y])
	index_minCD = np.argmin([L0_CDxy, L0_CD_xy, L0_CDx_y, L0_CD_x_y])
	if index_minCD>=0 and index_minCD<c1:
		L0minCD = min_CD
		idCD = index_minCD
		K1minCD = K1_CDxy[idCD]
		K2minCD = K2_CDxy[idCD]
	elif index_minCD>=c1 and index_minPQ<(c1+c2):
		L0minCD = min_CD
		idCD = index_minCD-c1
		K1minCD = K1_CDxy[idCD]
		K2minCD = K2_CDxy[idCD]
	elif index_minPQ>=(c1+c2) and index_minPQ<(c1+c2+c3):
		L0minCD = min_CD
		idCD = index_minCD-c1-c2
		K1minCD = K1_CDxy[idCD]
		K2minCD = K2_CDxy[idCD]
	elif index_minPQ>=(c1+c2+c3) and index_minPQ<(c1+c2+c3+c4):
		L0minCD = min_CD
		idCD = index_minCD-c1-c2-c3
		K1minCD = K1_CDxy[idCD]
		K2minCD = K2_CDxy[idCD]
	else:
		raise ValueError
	return L0minCD,idCD,K1minCD,K2minCD


def func_z1z2(z1PQ,z1CD,z2PQ,z2CD):
	if z1PQ<=z1CD and z2PQ<=z2CD:
		z1 = z1PQ
		z2 = z2PQ
	elif z1PQ>z1CD and z2PQ>z2CD:
		z1 = z1CD
		z2 = z2CD
	else:
		raise ValueError
	return z1,z2


def func_compute_z1z2(min_L0,K1,K2,gamma_N1,gamma_N2,sigma_y,A):

	min_L1 = min_L0 + gamma_N1*sigma_y*A/K1
	min_L2 = min_L1 + (gamma_N2 - gamma_N1)*sigma_y*A/K2
	z1 = np.sqrt(min_L1**2 - min_L0**2)
	z2 = np.sqrt(min_L2**2 - min_L0**2)

	return z1, z2

def func_vectorFiEi(L0,L1,L2,K1,K2,gamma_N1,sigma_y,A):
	F_gammaN1 = gamma_N1*sigma_y*A
	L_gammaN1 = F_gammaN1/K1 + L0

	F1 = K1*(L1-L0)
	F2 = K1*(L_gammaN1-L0) + K2*(L2-L_gammaN1)

	E1 = K1*(L1-L0)**2/2
	E2 = K1*L2*(L1-L0) + K1*(L0**2-L1**2)/2 + K2*(L2-L1)**2 / 2

	for i in range(len(L1)):
		if L1[i] <= L_gammaN1[i]:
			pass
		else:
			raise ValueError
	for j in range(len(L2)):
		if L2[j] >= L_gammaN1[j]:
			pass
		else:
			F2[j] = K1[j]*(L2[j]-L0[j])
			E2[j] = K1[j]*(L2[j]-L0[j])**2/2
	return F1,F2,E1,E2


def func_lslf(F1,F2,L1,L2,ls0,lf0,ks,E1,E2,gamma_N1,sigma_y,A):
	gamma_N1 = gamma_N1+1e-6  # 由于Python对于计算精度保持位数的不同，条件判断语句中
	gamma1_N = F1/(sigma_y*A)

	ls1 = np.zeros_like(L1)
	lf1 = np.zeros_like(L1)
	ls2 = np.zeros_like(L2)
	lf2 = np.zeros_like(L2)

	for k1 in range(len(gamma1_N)):

		if gamma1_N[k1] <=gamma_N1:
			ls1[k1] = (E1*A*(L1[k1]-lf0[k1])+ks*ls0*lf0[k1]) / (ks*lf0[k1]+E1*A)
			lf1[k1] = (ks*lf0[k1]*(L1[k1]-ls0)+E1*A*lf0[k1]) / (ks*lf0[k1]+E1*A)
		
		elif gamma1_N[k1] >gamma_N1:
			raise ValueError

	gamma2_N = F2/(sigma_y*A)
	for k2 in range(len(gamma2_N)):

		if gamma2_N[k2] <=gamma_N1:
			ls2[k2] = (E1*A*(L2[k2]-lf0[k2])+ks*ls0*lf0[k2]) / (ks*lf0[k2]+E1*A)
			lf2[k2] = (ks*lf0[k2]*(L2[k2]-ls0)+E1*A*lf0[k2]) / (ks*lf0[k2]+E1*A)

		elif gamma2_N[k2] >gamma_N1:
			ls2[k2] = (E2*A/lf0[k2]*(L2[k2]-lf1[k2])+ks*ls1[k2]) / (ks+E2*A/lf0[k2])
			lf2[k2] = (ks*(L2[k2]-ls1[k2])+lf1[k2]*E2*A/lf0[k2]) / (ks+E2*A/lf0[k2])

	return ls1,ls2,lf1,lf2


def func_sensitive(factor_star, factor_array,disp_array,forc_array,ener_array):
	index_ref = np.int(np.where(factor_array==factor_star)[0])

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


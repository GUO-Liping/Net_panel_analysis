#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np


def	func_inputCheck(nw,d,D,Rp,w,kappa,ks_PQ,ks_CD,ls0_PQ,ls0_CD,ex,ey):
	
	inputData = np.array([nw,d,D,Rp,w,kappa,ks_PQ,ks_CD,ls0_PQ,ls0_CD,ex,ey])
	for i in range(len(inputData)):
		if inputData[i]<0:
			print('All of the input data should be greater than 0!')
		else:
			pass

	if not(isinstance(nw,int)):
		print('nw should be an integer!')
	elif D > w:
		print('Load area should be smaller than ring net!')
	elif kappa <1:
		print('kappa should be greater than 1!')
	elif ex > ((kappa*w)/2-ls0_CD-Rp):
		print('load area is beyound the boundary of the net along x direction!')
	elif ey > (w/2-ls0_PQ-Rp):
		print('load area is beyound the boundary of the net along y direction!')
	else:
		pass

def func_m(BC,Rp,kappa,a):
	if BC == 'round' or BC == 'Round':
		mPQ = func_round(Rp/a)
		mCD = func_round(Rp/(kappa*a))
		return mPQ, mCD
	elif BC == 'polygon' or BC == 'Polygon':
		mPQ = func_round((5*Rp/np.sqrt(34))/a)
		mCD = func_round((5*Rp/np.sqrt(34))/(kappa*a))
		return mPQ, mCD
	else:
		raise ValueError


def func_ks(BC,**kwargs):
	if BC=='rigid' or BC=='Rigid':
		return kwargs['ks']
	elif BC=='flexible' or BC=='Flexible':
		l0_rope = kwargs['l0_rope']
		q_rope = kwargs['gamma_ave'] * kwargs['sigma_y']*kwargs['A']*kwargs['m']/(kwargs['l0_rope']/2)
		A_rope = kwargs['F_rope']/kwargs['sigma_rope']
		vr_max = (3*q_rope*kwargs['l0_rope']**4/(64*kwargs['E_rope']*A_rope))**(1/3)
		l_rope = func_Lrope(l0_rope,vr_max)
		T_rx = kwargs['E_rope']*A_rope*(l_rope-l0_rope)/l0_rope
		T_r = T_rx*np.sqrt(1+((q_rope*l0_rope)/(2*T_rx))**2)
		delta_l_rope = T_rx*l0_rope/(kwargs['E_rope']*A_rope)  # 两边跨钢丝绳弹性伸长量
		print('l0_rope=',l0_rope)
		print('delta_l_rope=',delta_l_rope)
		l_ropeBmax = l_rope + kwargs['lb_max'] + (3)*delta_l_rope  # 两边跨钢丝绳弹性伸长量
		vr_maxB = func_vr(l_ropeBmax,l0_rope)
		print('vr_maxB=',vr_maxB)
		ks = kwargs['gamma_N2']*kwargs['sigma_y']*kwargs['A']/(vr_maxB)
		return ks
	else:
		raise ValueError


def func_Lrope(w,vr):
	L1 = np.sqrt(w**2/4 + 4*vr**2)
	L2 = w**2/(8*vr) * np.arcsinh(4*vr/w)
	return L1+L2


def func_vr(L,w):
	up_vr = L/2
	low_vr = 0
	vr = (up_vr+low_vr)/2
	test_L = func_Lrope(w,vr)
	errL = test_L-L
	numL = 0
	while(abs(errL)>1e-5 and numL<1000):
		if errL>0:
			up_vr = vr
			vr = (up_vr+low_vr)/2
			errL = func_Lrope(w,vr) - L
		elif errL<0:
			low_vr = vr
			vr = (up_vr+low_vr)/2
			errL = func_Lrope(w,vr) - L
		else:
			raise ValueError
		numL = numL+1
	return vr


def func_xyz(blockShape,curtain,points, w, kappa, Rp, a, ex, ey, z):
	if blockShape == 'round' or blockShape == 'Round':
		mPQ = func_round(Rp/a)
		index_mPQ = np.linspace(1, mPQ, mPQ, endpoint=True)
	
		xP = a * (index_mPQ - 1/2) + ex
		yP = np.sqrt(Rp**2 - (a*index_mPQ - a/2)**2) + ey
		zP = np.zeros(mPQ) + z
	
		yQ = np.zeros(mPQ) + w/2
		zQ = np.zeros(mPQ) + 0
	
		mCD = func_round(Rp/(kappa*a))
		index_mCD = np.linspace(1, mCD, mCD, endpoint=True)
	
		xC = np.sqrt(Rp**2 - (kappa*a*index_mCD - kappa*a/2)**2) + ex
		yC = kappa*a * (index_mCD - 1/2) + ey
		zC = np.zeros(mCD) + z
	
		xD = np.zeros(mCD) + kappa*w/2
		zD = np.zeros(mCD) + 0
		#print('xC,xD,yC,yD,zC,zD=',xC,xD,yC,yD,zC,zD)
		if curtain == True:
			xQ = xP
			yD = yC	
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

		elif curtain==False:
			xQ = kappa*w * (index_mPQ-1/2)/(2*mPQ + 1)
			yD = w * (index_mCD-1/2)/(2*mCD + 1)

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

	elif blockShape == 'polygon' or blockShape == 'Polygon':
		mPQ = func_round((5*Rp/np.sqrt(34))/a)
		mPQ1 = func_round((3*Rp/np.sqrt(34))/a)
		index_mPQ = np.linspace(1, mPQ, mPQ, endpoint=True)
	
		xP = a * (index_mPQ - 1/2) + ex
		yP1 = np.zeros(mPQ1) + (5*Rp/np.sqrt(34)) + ey
		yP2 = 5*Rp/np.sqrt(34) -(xP[mPQ1:]-3*Rp/np.sqrt(34))+ ey
		yP = np.concatenate((yP1,yP2),axis=0)
		zP = np.zeros(mPQ) + z
	
		yQ = np.zeros(mPQ) + w/2
		zQ = np.zeros(mPQ) + 0
		
		mCD = func_round((5*Rp/np.sqrt(34))/(kappa*a))
		#print('mCD=',mCD)
		mCD1 = func_round((3*Rp/np.sqrt(34))/(kappa*a))
		#print('mCD1=',mCD1)
		index_mCD = np.linspace(1, mCD, mCD, endpoint=True)
		
		yC = kappa*a * (index_mCD - 1/2) + ey
		xC1 = np.zeros(mCD1) + 5*Rp/np.sqrt(34) + ex
		#print('xC1=',xC1)
		xC2 = 5*Rp/np.sqrt(34) - (yC[mCD1:] - 3*Rp/np.sqrt(34))+ ex
		xC = np.concatenate((xC1,xC2),axis=0)
		zC = np.zeros(mCD) + z

		xD = np.zeros(mCD) + kappa*w/2
		zD = np.zeros(mCD) + 0
		#print('xC,xD,yC,yD,zC,zD=',xC,xD,yC,yD,zC,zD)
		if curtain == True:
			xQ = xP
			yD = yC
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

		elif curtain == False:
			xQ = kappa*w * (index_mPQ-1/2)/(2*mPQ + 1)
			yD = w * (index_mCD-1/2)/(2*mCD + 1)
		
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
		else:
			raise ValueError		
	else:
		raise ValueError


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

    chi_gammaN = 0.18
    after_fit_gammaN2 = np.polyval(poly_gammaN2_func, nw)+chi_gammaN

    '''
    对比五环试验与三环试验轴向力发展程度可发现，
    五环(5圈0.551，7圈0.554,9圈0.559)，三环(5圈0.359, 7圈0.398, 9圈0.358)
    分别大于三环(5圈0.192, 7圈0.156, 9圈0.201,)均值约0.1至0.2之间
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
	elif index_minCD>=c1 and index_minCD<(c1+c2):
		L0minCD = min_CD
		idCD = index_minCD-c1
		K1minCD = K1_CDxy[idCD]
		K2minCD = K2_CDxy[idCD]
	elif index_minCD>=(c1+c2) and index_minCD<(c1+c2+c3):
		L0minCD = min_CD
		idCD = index_minCD-c1-c2
		K1minCD = K1_CDxy[idCD]
		K2minCD = K2_CDxy[idCD]
	elif index_minCD>=(c1+c2+c3) and index_minCD<(c1+c2+c3+c4):
		L0minCD = min_CD
		idCD = index_minCD-c1-c2-c3
		K1minCD = K1_CDxy[idCD]
		K2minCD = K2_CDxy[idCD]
	else:
		raise ValueError
	return L0minCD,idCD,K1minCD,K2minCD


def func_Checkz1z2(z1PQ,z1CD,z2PQ,z2CD):

	if z1PQ<=(z1CD+1e-9):
		if z2PQ<=(z2CD+1e-9):
			z1 = z1PQ
			z2 = z2PQ
		else:
			z1 = z1PQ
			z2 = z2CD
	elif z1PQ>(z1CD+1e-9):
		if z2PQ>(z2CD+1e-9):
			z1 = z1CD
			z2 = z2CD
		else:
			z1 = z1CD
			z2 = z2PQ
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
	gamma_N1 = gamma_N1+1e-5
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


#!/usr/bin/env python
# -*- coding: UTF-8 -*-


'''
Name： Elastic cable
Function: 计算柔性防护系统中钢丝绳柔性边界的等效边界刚度
Method: 集中力作用下的柔性钢丝绳变形 cite: The suspended elastic cable under the action of concentrated vertical loads
Note: 国际单位制
Version: 0.0.1
Author: Liping GUO
Date: from 2021/12/31 to 
Remark: 尚未解决的问题：

'''

import numpy as np
from sympy import symbols, Array
from sympy import asinh, sqrt, diff, Sum

xi, eta, sigma, delta, gamma, tau, chi, phi, beta = symbols('xi eta sigma delta gamma tau chi phi beta')
psi_i, Psi_i, Psi_i_1, sigma_i = symbols('psi_i Psi_i Psi_i_1 sigma_i')
i,j = symbols('i j', integer=True)

F_1, F_2, F_3, F_4, F_5, F_6, F_7 = symbols('F_1, F_2, F_3, F_4, F_5, F_6, F_7')
s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8 = symbols('s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8')
L_0, W, E, A_0 = symbols('L_0, W, E, A_0')

F = Array([0, F_1, F_2, F_3, 0])  # 首位、末尾必须为0，保证F(i=0)=0,F(i=-1)=0
s = Array([0, s_1, s_2, s_3, s_4])  # 首位必须为0，保证s(i=0)=0

N = len(F)-2  # N为集中荷载的数量，除去首位、末位

sigma_i = s[i]/L_0
psi_i = F[i]/W
Psi_N = Sum(F[j]/W, (j,-1,N))
Psi_i = Sum(F[j]/W, (j,-1,i))
Psi_i_1 = Sum(F[j]/W, (j,-1,i-1))
#Psi_N = Psi_N.subs(N,3).doit()
#Psi_N

f1_1 = gamma/chi - beta
f1_2 = asinh(phi/chi) - asinh((phi-Psi_N-1)/chi)
f1_3 = Sum(asinh((phi-Psi_i-sigma_i)/chi) - asinh((phi-Psi_i_1-sigma_i)/chi), (i,0,N))
f1 = -f1_1 + f1_2 + f1_3
expr_f1 = f1.doit()

f2_1 = delta
f2_2 = beta*(phi-1/2) + sqrt(phi**2+chi**2) - sqrt((phi-Psi_N-1)**2+chi**2)
f2_3 = Sum(beta*psi_i*(sigma_i-1) + sqrt((phi-Psi_i-sigma_i)**2+chi**2) - sqrt((phi-Psi_i_1-sigma_i)**2+chi**2), (i,0,N))
f2 = -f2_1 + f2_2 + f2_3
expr_f2 = f2.doit()

diff_f1_chi = diff(expr_f1,chi)
diff_f1_phi = diff(expr_f1,phi)
diff_f2_chi = diff(expr_f2,chi)
diff_f2_phi = diff(expr_f2,phi)

dict_F = {F_1:1, F_2:1, F_3: 1}
dict_s = {s_1:1, s_2:1, s_3: 1}
dict_const = {W:1, L_0:1, beta:1, delta:0.1, gamma:0.5}
dict_values = {**dict_F, **dict_s, **dict_const}

a_11 = diff_f1_chi.evalf(subs=dict_values)  # 这种是精确计算方法，仅用subs只能获得近似值
a_12 = diff_f1_phi.evalf(subs=dict_values)
a_21 = diff_f2_chi.evalf(subs=dict_values)
a_22 = diff_f2_phi.evalf(subs=dict_values)

value_f1 = expr_f1.evalf(subs=dict_values)
value_f2 = expr_f2.evalf(subs=dict_values)

dict_init = {chi:1, phi:0}
n_loop = 0
while n_loop<10:

	print('dict_init=',dict_init)
	n_loop = n_loop + 1
	
	a_11 = a_11.evalf(subs=dict_init)  # 这种是精确计算方法，仅用subs只能获得近似值
	a_12 = a_12.evalf(subs=dict_init)
	a_21 = a_21.evalf(subs=dict_init)
	a_22 = a_22.evalf(subs=dict_init)
	
	value_f1 = value_f1.evalf(subs=dict_init)
	value_f2 = value_f2.evalf(subs=dict_init)
	
	Jacobi_f1f2 = Array([[a_11, a_12],[a_21, a_22]])
	Jacobi_array = np.asarray(Jacobi_f1f2,dtype=float)
	
	Jacobi_f1f2_inv = np.linalg.inv(Jacobi_array)
	Incre_array = np.asarray([value_f1,value_f2],dtype=float)
	
	iter_array = Jacobi_f1f2_inv.dot(Incre_array)
	dict_init = {chi:iter_array[0], phi:iter_array[0]}


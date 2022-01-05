#!/usr/bin/env python
# -*- coding: UTF-8 -*-


'''
Name： sympy_elastic_cable
Function1: 牛顿法解非线性方程组
Function2: 计算柔性防护系统中钢丝绳柔性边界的等效边界刚度
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

xi, eta, sigma, delta, gamma, tau, chi, phi, beta = symbols('xi, eta, sigma, delta, gamma, tau, chi, phi, beta')
i,j,n = symbols('i,j,n', integer=True)

F_1, F_2, F_3, F_4, F_5, F_6, F_7 = symbols('F_1, F_2, F_3, F_4, F_5, F_6, F_7')
s, s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8 = symbols('s, s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8')
L_0, W, E, A_0, l, h = symbols('L_0, W, E, A_0, l, h')

dict_F = {F_1:100, F_2:100, F_3: 1000}
dict_s = {s_1:0.25, s_2:0.25, s_3: 0.65}
dict_const = {W:1, L_0:1, E:120e9, A_0:np.pi*0.01**2/4, l:1, h:0}
dict_known = {**dict_F, **dict_s, **dict_const}

chi_value = 100  # 牛顿法求解过程赋予chi的初始值
phi_value = 100  # 牛顿法求解过程赋予phi的初始值

F_array = Array([0, F_1, F_2, F_3, 0])  # 首位、末尾必须为0，保证F(i=0)=0,F(i=-1)=0
s_array = Array([0, s_1, s_2, s_3, s_4])  # 首位必须为0，保证s(i=0)=0

n = 2  # 需要输入，目标钢丝绳分段（n至n+1段）
sigma = s/L_0
N = len(F_array)-2  # N为集中荷载的数量，除去首位、末位
beta = W/(E*A_0)
delta = h/L_0
gamma = l/L_0

sigma_i = s_array[i]/L_0
psi_i = F_array[i]/W
Psi_N = Sum(F_array[j]/W, (j,-1,N))
Psi_i = Sum(F_array[j]/W, (j,-1,i))
Psi_i_1 = Sum(F_array[j]/W, (j,-1,i-1))
Psi_n = Sum(F_array[j]/W, (j,-1,n))

# 牛顿法求解非线性方程组
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

a_11 = diff_f1_chi.evalf(subs=dict_known)  # 这种是精确计算方法，仅用subs只能获得近似值
a_12 = diff_f1_phi.evalf(subs=dict_known)
a_21 = diff_f2_chi.evalf(subs=dict_known)
a_22 = diff_f2_phi.evalf(subs=dict_known)

value_f1 = expr_f1.evalf(subs=dict_known)
value_f2 = expr_f2.evalf(subs=dict_known)

n_loop = 0
max_loop = 1000

error_chi = np.empty(max_loop)
error_phi = np.empty(max_loop)
error_chi[0] = chi_value
error_phi[0] = phi_value
error = 1
while n_loop<max_loop and error>1e-8:

	dict_init = {chi:chi_value, phi:phi_value}

	a11 = a_11.evalf(subs=dict_init)  # 这种是精确计算方法，仅用subs只能获得近似值
	a12 = a_12.evalf(subs=dict_init)
	a21 = a_21.evalf(subs=dict_init)
	a22 = a_22.evalf(subs=dict_init)
	
	valuef1 = value_f1.evalf(subs=dict_init)
	valuef2 = value_f2.evalf(subs=dict_init)
	
	Jacobi_f1f2 = Array([[a11, a12],[a21, a22]])
	Jacobi_array = np.asarray(Jacobi_f1f2,dtype=float)
	
	Jacobi_f1f2_inv = np.linalg.inv(Jacobi_array)
	Incre_array = np.asarray([valuef1,valuef2],dtype=float)
	iter_array = -Jacobi_f1f2_inv.dot(Incre_array)

	chi_value = chi_value + iter_array[0]
	phi_value = phi_value + iter_array[1]

	error_chi[n_loop+1] = chi_value
	error_phi[n_loop+1] = phi_value
	error = np.amin([abs(error_phi[n_loop+1]-error_phi[n_loop]), abs(error_phi[n_loop+1]-error_phi[n_loop])])
	print('This is the', n_loop+1, 'th loop, ', 'chi=', chi_value, 'phi=', phi_value, 'error=',error)

	n_loop = n_loop + 1


# 无量纲公式
xi_1 = beta*sigma + asinh(phi/chi) - asinh((phi-Psi_n-sigma)/chi)
xi_2 = Sum(asinh((phi-Psi_i-sigma_i)/chi) - asinh((phi-Psi_i_1-sigma_i)/chi), (i,0,n))
xi = chi*(xi_1 + xi_2)
expr_xi = xi.doit().evalf(subs=dict_known)

eta_1 = beta*sigma*(phi-sigma/2) + sqrt(phi**2+chi**2) - sqrt((phi-Psi_n-sigma)**2+chi**2)
eta_2 = Sum(beta*psi_i*(sigma_i-sigma) + sqrt((phi-Psi_i-sigma_i)**2+chi**2) - sqrt((phi-Psi_i_1-sigma_i)**2+chi**2), (i,0,n))
eta = eta_1 + eta_2
expr_eta = eta.doit().evalf(subs=dict_known)
expr_xi
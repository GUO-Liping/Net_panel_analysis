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
W, F1, F2, F3, F4, F5, F6, F7 = symbols('W F1 F2 F3 F4 F5 F6 F7')
F = Array([F1, F2, F3, F4, F5, F6, F7])
#i = 1
N = len(F)
psi = F/W
Psi_N = Sum(psi[j], (j,0,N-1))
Psi_i = Sum(psi[j], (j,0,i-1))
Psi_i_1 = Sum(psi[j], (j,0,i-2))
#Psi_i = Psi_i.doit()
#Psi_i_1 = Psi_i_1.doit()
#Psi_N = Psi_N.doit()
#Psi_i_1

f1_1 = gamma/chi - beta
f1_2 = asinh(phi/chi) - asinh((phi-Psi_N-1)/chi)
f1_3 = Sum(asinh((phi-Psi_i-sigma_i)/chi) - asinh((phi-Psi_i_1-sigma_i)/chi), (i,0,N-1))
f1 = -f1_1 + f1_2 + f1_3
f1

f2_1 = delta
f2_2 = beta*(phi-1/2) + sqrt(phi**2+chi**2) - sqrt((phi-Psi_N-1)**2+chi**2)
f2_3 = Sum(beta*psi_i*(sigma_i-1) + sqrt((phi-Psi_i-sigma_i)**2+chi**2) - sqrt((phi-Psi_i_1-sigma_i)**2+chi**2), (i,0,N))
f2 = -f2_1 + f2_2 + f2_3
f2

diff_f1_chi = diff(f1,chi)
diff_f1_chi

aaa = diff_f1_chi.subs(i,2)
print(aaa.doit())
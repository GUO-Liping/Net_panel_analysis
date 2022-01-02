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
from sympy import symbols
from sympy import asinh, sqrt

xi, eta, sigma, delta, gamma, tau, chi, phi, beta = symbols('xi eta sigma delta gamma tau chi phi beta')
psi_i, Psi_i, Psi_i_1, Psi_N, sigma_i = symbols('psi_i Psi_i Psi_i_1 Psi_N sigma_i')

f1_1 = gamma/chi - beta
f1_2 = asinh(phi/chi) - asinh((phi-Psi_N-1)/chi)
f1_3 = asinh((phi-Psi_i-sigma_i)/chi) - asinh((phi-Psi_i_1-sigma_i)/chi)
f1 = -f1_1 + f1_2 + f1_3

f2_1 = delta
f2_2 = beta*(phi-1/2) + sqrt(phi**2+chi**2) - sqrt((phi-Psi_N-1)**2+chi**2)
f2_3 = beta*psi_i*(sigma_i-1) + sqrt((phi-Psi_i-sigma_i)**2+chi**2) - sqrt((phi-Psi_i_1-sigma_i)**2+chi**2)
f2 = -f2_1 + f2_2 + f2_3

sigma_array = s_array / L_0
psi_array = F_array / W
psi_N = psi_array[-1]

T_s = np.sqrt((Y_0 - sum_F - W*s/L_0)**2 + X**2)
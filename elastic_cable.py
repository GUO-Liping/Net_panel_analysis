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
from scipy.optimize import root

sigma_array = s_array / L_0
psi_array = F_array / W
psi_N = psi_array[-1]

T_s = np.sqrt((Y_0 - sum_F - W*s/L_0)**2 + X**2)
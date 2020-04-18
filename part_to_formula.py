from sympy import symbols
from sympy import pi
from sympy import Eq, solve
from sympy import summation, diff, sqrt
from sympy import simplify
import numpy as np

'''
还有两个问题：
(1) 3圈、4圈顶破位移与5圈~19圈顶破位移不一致
(2) 当边界不在为刚性时，由于圈数越大，轴向应力发展程度越大，破断时钢丝纤维束轴向力更大，圈数增大
对弹簧伸长值可能超过刚性边界下圈数增大对链破断时长度的减小值而使得最终顶破高度值的减小。
(3)由于环形网片的变形能力、承载能力、耗能能力均为nw、Rp、d的非连续函数，不可导，对影响因素进行敏感
性分析时应该采用敏感度函数应按照离散形式的表达式计算
'''

R_p, n_w = symbols('R_p, n_w')
d, d_min = symbols('d, d_min')
w_x, w_y = symbols('w_x, w_y')
m_x, m_y = symbols('m_x, m_y')
k_s, l_s0 = symbols('k_s, l_s0')
z = symbols('z')

index_i, index_j = symbols('index_i, index_j')
gamma_N1, gamma_N2 = symbols('gamma_N1, gamma_N2')
sigma_y, epsilon_N1, epsilon_N2 = symbols('sigma_y, epsilon_N1, epsilon_N2')

def func_ringChianDataFit(nw,sigma_y,dmin):
    lN0 = 0.3*3

    if dmin == 0.003:
        nw_array = np.array([4,5,7,9,12,16,19],dtype='float')
        FN2_array = np.array([30.064e3,44.937e3,69.72e3,80.547e3,110.884e3,177.66e3,209.387e3],dtype='float')
        delta_lN2_array = 0.001*np.array([515.05,518.67,508.59,489.92,490.644,475.54,472.36],dtype='float')
        Area_array = np.pi/4*dmin**2*nw_array
        # print('Area_array=',Area_array)
        gammaN2_array = FN2_array/(sigma_y*2*Area_array)
        # print('gammaN2_array111=', gammaN2_array)
    else:
        nw_array = np.array([3,4],dtype='float')
        FN2_array = np.array([9.87e3,17.57e3],dtype='float')
        delta_lN2_array = np.array([521.16e-3,517.36e-3],dtype='float')
        Area_array = np.pi/4*dmin**2*nw_array
        # print('Area_array=',Area_array)
        gammaN2_array = FN2_array/(sigma_y*2*Area_array)

    poly_delta_lN2_func = np.polyfit(nw_array, delta_lN2_array,1)
    poly_gammaN2_func = np.polyfit(nw_array, gammaN2_array,1)

    after_fit_delta_lN2 = np.polyval(poly_delta_lN2_func, nw)
    after_fit_gammaN2 = np.polyval(poly_gammaN2_func, nw) + 0.18
    '''
    对比五环试验与三环试验轴向力发展程度可发现，
    五环(5圈0.551，7圈0.554,9圈0.559)，三环(5圈0.359, 7圈0.398, 9圈0.358)
    分别大于三环(5圈0.192, 7圈0.156, 9圈0.201,)均值为0.183
    '''

    after_fit_FN2 = after_fit_gammaN2 * sigma_y*(2*nw*np.pi*dmin**2/4)
    after_fit_lN2 = lN0 + after_fit_delta_lN2
    after_fit_FN1 = after_fit_FN2*0.15
    after_fit_lN1 = lN0 + after_fit_delta_lN2*0.85
    after_fit_gammaN1 = after_fit_gammaN2 * 0.15

    A = nw*np.pi*dmin**2/4

    Ef1 = after_fit_FN1*lN0/(2*A*(after_fit_lN1 - lN0))
    Ef2 = (after_fit_FN2-after_fit_FN1)*lN0 / (2*A*(after_fit_lN2 - after_fit_lN1))

    value_epsilon_N1 = after_fit_gammaN1*sigma_y/Ef1
    value_epsilon_N2 = after_fit_gammaN1*sigma_y/Ef1+(after_fit_gammaN2-after_fit_gammaN1)*sigma_y/Ef2

    return after_fit_gammaN1, after_fit_gammaN2, value_epsilon_N1, value_epsilon_N2

def func_m(R_p, d):
	a = np.pi*d/4
	if R_p/a ==0.5:
		m = int(R_p/a)+1
	else:
		m=round(R_p/a)
	return m

data_nw = 7
data_Rp = 0.5
data_d = 0.3
data_dmin = 0.003
data_m = func_m(data_Rp, data_d)
data_sigma_y = 1770e6
data_ks = 5000000
data_ls0 = 0.05
data_wx, data_wy = 2.95, 2.95
data_gamma_N1, data_gamma_N2, data_epsilon_N1, data_epsilon_N2 = func_ringChianDataFit(data_nw, data_sigma_y, data_dmin)

my_dict_reference = {n_w:data_nw, R_p:data_Rp, d:data_d, d_min:data_dmin, 
w_x:data_wx, w_y:data_wy, m_x:data_m,k_s:data_ks, l_s0:data_ls0,
gamma_N1:data_gamma_N1, gamma_N2:data_gamma_N2,sigma_y:data_sigma_y,
epsilon_N1:data_epsilon_N1, epsilon_N2:data_epsilon_N2, index_i:1}
print('gamma_N2=', data_gamma_N2)
A = n_w * (pi*d_min**2/4)

E_f1 = gamma_N1*sigma_y/epsilon_N1
E_f2 = (gamma_N2-gamma_N1)/(epsilon_N2-epsilon_N1) * sigma_y

a_x = pi * d / 2 * w_y / (w_x + w_y)  # 加载区域x方向网环边长
a_y = pi * d / 2 * w_x / (w_x + w_y)  # 加载区域y方向网环边长

x_Pi = a_x*(index_i-1/2)
y_Pi = sqrt(R_p**2-(a_x*(index_i-1/2))**2)
z_Pi = z
x_Qi = w_x*(index_i-1/2)/(2*m_x+1)
y_Qi = w_y/2
z_Qi = 0
L_PQ = sqrt((x_Pi-x_Qi)**2+(y_Pi-y_Qi)**2+(z_Pi-z_Qi)**2)

L0_PQ = L_PQ.subs({z:0})  # fx.subs({x:1})与fx.evalf(subs={x:1,y:2},n=16)的区别在于evalf精度高，但只能对全部自变量赋值
l_f0_PQ = L0_PQ - l_s0

K1_PQ = 1/(l_f0_PQ/(E_f1*A)+1/k_s)
K2_PQ = 1/(l_f0_PQ/(E_f2*A)+1/k_s)
L1_PQ = L0_PQ + gamma_N1*sigma_y*A/K1_PQ
L2_PQ = L1_PQ + (gamma_N2-gamma_N1)*sigma_y*A/K2_PQ
F2_PQ = gamma_N2*sigma_y*A

H_PQ = sqrt(L2_PQ**2-L0_PQ**2)
F_PQ = F2_PQ*H_PQ/L2_PQ * 1.4
E_PQ = K1_PQ*(L0_PQ**2-L1_PQ**2)/2 + K2_PQ*(L2_PQ-L1_PQ)**2/2

diff_n_w = diff(H_PQ, n_w)
diff_d_min = diff(H_PQ, d_min)
diff_d = diff(H_PQ, d)
diff_m_x = diff(H_PQ, m_x)
diff_R_p = diff(H_PQ, R_p)
diff_k_s = diff(H_PQ, k_s)

print('H=', H_PQ.evalf(subs=my_dict_reference))
print('diff_n_w=', diff_n_w.evalf(subs=my_dict_reference))
print('diff_d_min=', diff_d_min.evalf(subs=my_dict_reference))
print('diff_d=', diff_d.evalf(subs=my_dict_reference))
print('diff_R_p=', diff_R_p.evalf(subs=my_dict_reference))
print('diff_k_s=', diff_k_s.evalf(subs=my_dict_reference))

S_H_n_w = abs(diff_n_w.evalf(subs=my_dict_reference))*data_nw/H_PQ.evalf(subs=my_dict_reference)
S_H_d_min = abs(diff_d_min.evalf(subs=my_dict_reference))*data_dmin/H_PQ.evalf(subs=my_dict_reference)
S_H_d = abs(diff_d.evalf(subs=my_dict_reference))*data_d/H_PQ.evalf(subs=my_dict_reference)
S_H_R_p = abs(diff_R_p.evalf(subs=my_dict_reference))*data_Rp/H_PQ.evalf(subs=my_dict_reference)
S_H_k_s = abs(diff_k_s.evalf(subs=my_dict_reference))*data_ks/H_PQ.evalf(subs=my_dict_reference)

print('S_H_n_w = ', S_H_n_w )
print('S_H_d_min= ', S_H_d_min)
print('S_H_d = = ', S_H_d)
print('S_H_R_p = ', S_H_R_p)
print('S_H_k_s = ', S_H_k_s)

from sympy import symbols
from sympy import pi
from sympy import Eq, solve
from sympy import summation, diff, sqrt
from sympy import simplify

R_p, n_w = symbols('R_p, n_w')
d, d_min = symbols('d, d_min')
w_x, w_y = symbols('w_x, w_y')
m_x, m_y = symbols('m_x, m_y')
k_s, l_s0 = symbols('k_s, l_s0')
z = symbols('z')

index_i, index_j = symbols('index_i, index_j')
gamma_N1, gamma_N2 = symbols('gamma_N1, gamma_N2')
sigma_y, epsilon_N1, epsilon_N2 = symbols('sigma_y, epsilon_N1, epsilon_N2')

my_dict = {n_w:7, R_p:0.5, d:0.3, d_min:0.003, w_x:2.90, w_y:2.90, m_x:2,
k_s:10000000000000, l_s0:0.05, gamma_N1:0.056944056806819555, gamma_N2:0.37962704537879705,
sigma_y:1770e6, epsilon_N1:0.5369106349290562, epsilon_N2:0.6316595705047718,
index_i:1}

my_dict_reference = {n_w:9, R_p:0.5, d:0.3, d_min:0.003, w_x:2.90, w_y:2.90, m_x:2,
k_s:10000000000000, l_s0:0.05, gamma_N1:0.056944056806819555, gamma_N2:0.37962704537879705,
sigma_y:1770e6, epsilon_N1:0.5369106349290562, epsilon_N2:0.6316595705047718,
index_i:1}

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
print('L0_PQ=',((y_Pi-y_Qi)**2).evalf(subs=my_dict))
l_f0_PQ = L0_PQ - l_s0
print('l_f0_PQ=',l_f0_PQ.evalf(subs=my_dict))
K1_PQ = 1/(l_f0_PQ/(E_f1*A)+1/k_s)
K2_PQ = 1/(l_f0_PQ/(E_f2*A)+1/k_s)
L1_PQ = L0_PQ + gamma_N1*sigma_y*A/K1_PQ
L2_PQ = L1_PQ + (gamma_N2-gamma_N1)*sigma_y*A/K2_PQ
F2_PQ = gamma_N2*sigma_y*A

H_PQ = sqrt(L2_PQ**2-L0_PQ**2)
F_PQ = F2_PQ*H_PQ/L2_PQ
E_PQ = K1_PQ*(L0_PQ**2-L1_PQ**2)/2 + K2_PQ*(L2_PQ-L1_PQ)**2/2

diff_n_w = diff(H_PQ, n_w)
diff_d_min = diff(H_PQ, d_min)
diff_m_x = diff(H_PQ, m_x)

print('H=', H_PQ.evalf(subs=my_dict))
print('diff_n_w=', diff_n_w.evalf(subs=my_dict_reference))
print('diff_d_min=', diff_d_min.evalf(subs=my_dict))

import math, matplotlib.pyplot as plt
import random
import numpy as np
from diplom import special, navigation as  navi
#------------------------------------------------- Наблюдатель -------------------------------------------------#
Sxn = 0
Syn = 0
Vn = 15 # М/с
Kn = 0
Rcrk = 600
#---------------------------------------------- Объект наблюдения ----------------------------------------------#
Sxk = 3000
Syk = 3000
Vk = 10 # М/с
Kk = 90
#----------------------------------------------- Истиные значения ----------------------------------------------#
Sx_ist = Sxk
Sy_ist = Syk
Vk_ist = Vk
K_ist = Kk
#----------------------------------------------- Работа с циклом -----------------------------------------------#
time = 0
time_prev = 0
ind = 0
InitKet = 0
turn = 0
#---------------------------------------------------- Списки ---------------------------------------------------#
X_list = []
Y_list = []
Way_xk = []
Way_yk = []
Way_xist = []
Way_yist = []
Way_xn = []
Way_yn = []
bearing = []
bearing_ist = []
i = 0
A = np.zeros((3,3))
B = np.zeros((3,1))
#===============================================================================================================#
Kk = special.priv_360(Kk)
Kn = special.priv_360(Kn)
K_ist = special.priv_360(K_ist)

while InitKet < 18:
    dt = time - time_prev
    #-------------------------------------- Пересчет координат наблюдателя -------------------------------------#
    if InitKet >= 6:
        Kn, turn = navi.current_course(K_ist, Kn, Vn, Rcrk, dt)
    elif InitKet >= 1:
        Kn, turn = navi.current_course(P0, Kn, Vn, Rcrk, dt)
    Vxn, Vyn = special.projection(Vn, Kn)
    Sxn += Vxn * dt
    Syn += Vyn * dt
    Way_xn.append(Sxn)
    Way_yn.append(Syn)
    #------------------------------------ Пересчет истиных координат объекта -----------------------------------#
    Vx_ist, Vy_ist = special.projection(Vk_ist, K_ist)
    Sx_ist += Vx_ist * dt
    Sy_ist += Vy_ist * dt
    Way_xist.append(Sx_ist)
    Way_yist.append(Sy_ist)

    if (ind % 50 == 0 and turn == 0) or time == 0:
        if InitKet == 0:
            T0 = time
            dT = time
            P0 = special.priv_2pi(special.circular_arc([Sx_ist, Sxn], [Sy_ist, Syn]))
            P0 = random.uniform(P0-.0087, P0+.0087)
            Pi = P0
            Sxn0 = Sxn
            Syn0 = Syn
            Way_xk.append(Sx_ist)
            Way_yk.append(Sy_ist)
            X_list.append(Sxk)
            X_list.append(Sxn)
            Y_list.append(Syk)
            Y_list.append(Syn)
        else:
            Pi = special.priv_2pi(special.circular_arc([Sx_ist, Sxn], [Sy_ist, Syn]))
            Pi = random.uniform(Pi-.0087, Pi+.0087)

        Sx = Sxn - Sxn0
        Sy = Syn - Syn0
        a = math.sin(P0 - Pi)
        b = (time - T0) * math.cos(Pi)
        c = - (time - T0) * math.sin(Pi)
        h = (Sx * math.cos(Pi)) - (Sy * math.sin(Pi))
        if (a or b or c or h) != 0:
            A[i, 0] = a
            A[i, 1] = b
            A[i, 2] = c
            B[i] = h
            i += 1
        if i == 3 and np.linalg.det(A) != 0:
            A = np.linalg.inv(A)
            X = A.dot(B)
            D0 = float(X[0])
            Vxk = float(X[1])
            Vyk = float(X[2])
            Vk = math.sqrt(Vxk**2 + Vyk**2)
            Sxk += Vxk * (time - dT)
            Syk += Vyk * (time - dT)
            print(f"""
                Kk  >>>  {special.rad_in_degrees(Kk)}
                Vk  >>>  {Vk} 
                Sxk >>> {Sxk} 
                Syk >>> {Syk}""")

            print(f"""
                K_ist  >>> {special.rad_in_degrees(K_ist)}
                Vk_ist >>> {Vk_ist} 
                Sx_ist >>> {Sx_ist} 
                Sy_ist >>> {Sy_ist}""")
            print()
            Kk = special.circular_arc2(Vxk, Vyk)
            Way_xk.append(Sxk)
            Way_yk.append(Syk)
            X_list.append(Sxk)
            X_list.append(Sxn)
            Y_list.append(Syk)
            Y_list.append(Syn)

            A = np.zeros((3, 3))
            B = np.zeros((3, 1))
            X = np.zeros((3, 1))
            dT = time
            i = 0

        InitKet += 1

    ind += 1
    time_prev = time
    time += 1
#===============================================================================================================#
print(bearing)
print(bearing_ist)
i = 0
x = max(Way_xn)//1
y = max(Way_yn)//1
fig, coord = plt.subplots()
xx = np.linspace(-x, x, 100)
yy = np.linspace(-y, y, 100)
coord.plot(xx, yy, color="white")
coord.plot(Way_xn, Way_yn, color="green", label="Наблюдатель")
coord.plot(Way_xist, Way_yist,"b--", label="Объект(И)")
coord.plot(Way_xk, Way_yk,"red", label="Объект(P)")
while i < len(X_list):
    coord.plot([X_list[i], X_list[i+1]], [Y_list[i], Y_list[i+1]], "b-")
    i += 2
coord.set_xlabel(f"x (метры), Время (cек): {time}")
coord.set_ylabel("y (метры)")
coord.legend()
plt.show()

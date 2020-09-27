import math
import numpy as np
from diplom import figure, special, navigation as  navi

#=======================================================================================================#
#------------------------------------------ Начальные данные -------------------------------------------#
V_zv = 1500              # Скорость звука в воде (м/с)
#--------------------------------------------- Наблюдатель ---------------------------------------------#
Vn =  19.44
Vn = special.speed(Vn)
An =  12
Cn = None
Vn_cur = Vn
Rc = 2                  # Шаг поворота
#----------------------------------- Начальные координаты наблюдателя ----------------------------------#
way_x = 0
way_y = 0
#------------------------------ Списки для хранения координат наблюдателя ------------------------------#
x_list = []
y_list = []
#---------------------------------------- Объект наблюдения (Р) ----------------------------------------#
Vc = 15
Vc = special.speed(Vc)
Ac = 12
Cc = special.priv_360(135)
Vc_cur = Vc
#---------------------------------------- Объект наблюдения (И) ----------------------------------------#
V_ist = Vc
A_ist = Ac
C_ist = Cc
V_ist_cut = V_ist
#------------------------------- Начальные координаты объекта наблюдения -------------------------------#
wayObj_x = 1
wayObj_y = 3
obj_x = []
obj_y = []
#=======================================================================================================#
x_obj = []
y_obj = []
bearing = []
x_meas = []
y_meas = []
a_list = np.array([])
b_list = np.array([])
c_list = np.array([])
h_list = np.array([])
k_list = np.array([])
dt = 0
#-------------------------------------------- Работа с циклом ------------------------------------------#
hour = .000278
ind = 0
time = 0
t_prev = 0
dCn_prev = 0
dCn = 10000
tack = 1
turn = None
#=======================================================================================================#

while ind < 16:
    # ==================================================================================================#
    d_time = time - t_prev
    # ==================================================================================================#
    # ------------------------------ Расчет траектории объектра наблюдения ------------------------------#
    V_ist_cut = navi.current_speed(V_ist, V_ist_cut, A_ist, d_time)
    Vist_x, Vist_y = special.projection(V_ist_cut, C_ist)
    C_ist = special.circular_arc2(Vist_x, Vist_y)
    wayObj_x, wayObj_y = navi.trajectory(
        Vist_x, Vist_y, d_time, wayObj_x, wayObj_y)
    obj_x.append(wayObj_x)
    obj_y.append(wayObj_y)
    # ------------------------------------------- Нулевой замер ------------------------------------------#
    if time == 0:
        D_obj = math.sqrt((abs(wayObj_x - way_x) ** 2) + (abs(wayObj_y - way_y) ** 2))
        P0 = special.circular_arc([wayObj_x, way_x], [wayObj_y, way_y])
        D_obj_x, D_obj_y = special.projection(D_obj, P0)
        way_xobj, way_yobj = way_x + D_obj_x, way_y + D_obj_y
        bearing.append(P0)
        t_meas = 2 * D_obj / (V_zv * 0.00062137)
        time += t_meas * hour
        t_meas = time
        T = 0
        Cn = P0
        ind += 1
    # -------------------------------------- Обработчик поворота ---------------------------------------#
    if turn != None:
        dCn_prev = Cn
        Cn = navi.current_course(new_Cn, Cn, Vn_cur, Rc, d_time)
        if Cn < 0 or Cn > 2*math.pi:
            Cn = special.priv_2pi(Cn)
        if dCn_prev == Cn:
            turn = None
            t_meas = time

    # ---------------------------------- Условия начала маневрирования ----------------------------------#
    if ind == 6 and tack !=2:
        new_Cn, turn = navi.turn(Cn, Cc)
        tack = 2
    # ==================================================================================================#

    Vn_cur = navi.current_speed(Vn, Vn_cur, An, d_time)                     # Вектор текущей скорости наблюдателя
    Vn_x, Vn_y = special.projection(Vn_cur, Cn)                             # Разложение текущей скорости на
                                                                            # оси координат

    way_x, way_y = navi.trajectory1(Vn_cur, Cn, d_time, way_x, way_y)        # Вычисление текущих координат
                                                                            # наблюдателя
    # ----------------------------------- Списки коодинат наблюдателя -----------------------------------#
    x_list.append(way_x)
    y_list.append(way_y)
    # ------------------------------------------ N-ый замер -----------------------------------------#
    if turn == None and time // .001 == (t_meas + 30 * hour)// .001:
        D_obj_x = wayObj_x - way_x
        D_obj_y = wayObj_y - way_y
        D_obj = math.sqrt((abs(D_obj_x) ** 2) + (abs(D_obj_y) ** 2))
        D_ist = D_obj
        Pizm = special.circular_arc2(D_obj_x, D_obj_y)
        time += t_meas
        t_meas = time
        bearing.append(Pizm)
        Pi = bearing[-1]
        dt = time - T
        T = time
        # ------------------------------- Вычисление элементов матрицы ------------------------------#
        Sx = x_list[0] - x_list[-1]
        Sy = y_list[0] - y_list[-1]
        a = math.sin(P0 - Pi)
        b = math.cos(Pi) * time
        c = - math.sin(Pi) * time
        h = Sx * math.cos(Pi) - Sy * math.sin(Pi)



        a_list = np.append(a_list, a)
        b_list = np.append(b_list, b)
        c_list = np.append(c_list, c)
        h_list = np.append(h_list, h)

        sum_a = np.sum(np.square(a_list))
        sum_b = np.sum(np.square(b_list))
        sum_c = np.sum(np.square(c_list))

        sum_ab = np.sum(a_list * b_list)
        sum_ac = np.sum(a_list * c_list)
        sum_bc = np.sum(b_list * c_list)

        sum_ah = np.sum(a_list * h_list)
        sum_bh = np.sum(b_list * h_list)
        sum_ch = np.sum(c_list * h_list)
        # -------------------------------------- Коэффициенты матриц ------------------------------------#

        # ------------------------------------ Матрицы коэффициентов ------------------------------------#
        A = np.array([[sum_a, sum_ab, sum_ac],
                      [sum_ab, sum_b, sum_bc],
                      [sum_ac, sum_bc, sum_c]])
        B = np.array([[sum_ah],
                      [sum_bh],
                      [sum_ch]])

        A.transpose()
        if np.linalg.det(A) !=0 :
            print("det(A) >>> ", np.linalg.det(A))
            X = A.dot(B)
            D_obj = float(abs(X[0]))
            D_obj_x, D_obj_y = special.projection(D_obj, Pi)
            Vc_x = float(X[1])
            Vc_y = float(X[2])
            Cc = special.circular_arc2(Vc_x, Vc_y)
            #Cc = C_ist
            Vc_cur = math.sqrt(Vc_x ** 2 + Vc_y ** 2)
            way_xobj, way_yobj = way_xobj + D_obj_x, way_yobj + D_obj_y
            # ----------------------------- Списки координат объекта наблюдения -----------------------------#
            x_obj.append(way_xobj)
            y_obj.append(way_yobj)
            #------------------------------------------------------------------------------------------------#

            # ------------------- Cписки координат наблюдателя и  объекта в момент замера -------------------#
            x_meas.append(way_x)
            x_meas.append(way_xobj)
            y_meas.append(way_y)
            y_meas.append(way_yobj)
            print(f"""  
                V_cur >>> {Vc_cur}
                V_ist >>> {V_ist}\n
                D_obj >>> {D_obj}
                D_ist >>> {D_ist}\n
                Cc    >>> {Cc}   
                C_ist >>> {C_ist}\n""")
        else:
            print(f"det(A) = {np.linalg.det(A)}")


        ind += 1
#=======================================================================================================#
    t_prev = time
    time += hour
#=======================================================================================================#
print(f"Время  >>> {time}")
figure.maps(x_list,y_list,x_obj,y_obj, x_meas, y_meas, obj_x, obj_y)

import math

#=======================================================================================================#
#------------------------------------------ Функции перевода -------------------------------------------#
def rad_in_degrees(rad):
    deg = rad * 180 / math.pi
    return deg

def degrees_in_rad(deg):
    rad = deg * math.pi / 180
    return rad

#=======================================================================================================#
#---------------------------------- Функции проверки введеных значений ---------------------------------#
def speed(speed: int):
    if speed <= 0 or speed > 60:
        speed = None
        print("Ошибка, Вы ввели не верное значение! Попробуй ещё раз.")
        while speed == None:
            speed = int(input("Введите начальную скорость объекта (от 0 до 60): "))
            if speed <= 0 or speed > 60:
                speed = None
    return speed

#=======================================================================================================#
#--------------------------------- Разложение значения на оси координат --------------------------------#
def projection(value, corner_rad):
    value_x = value * math.sin(corner_rad)
    value_y = value * math.cos(corner_rad)
    return value_x, value_y

#=======================================================================================================#
#-------------------------------------- Функции приведения углов ---------------------------------------#
def priv_360(deg):
    while deg < 0 or deg >= 360:
        if deg >= 360:
            deg -= 360
        else: deg += 360
    return degrees_in_rad(deg)

def priv_2pi(rad):
    while rad <= 0 or rad > 2*math.pi:
        if rad >= 2*math.pi:
            rad -= 2*math.pi
        else: rad += 2*math.pi
    return rad

def priv_180(deg):
    while deg < -180 or deg >= 180:
        if deg > 180:
            deg -= 360
        else: deg += 360
    return degrees_in_rad(deg)

def priv_pi(rad):
    while rad < -math.pi or rad >= math.pi:
        if rad > math.pi:
            rad -= 2*math.pi
        else: rad += 2*math.pi
    return rad

#=======================================================================================================#
#---------------------------------------------- Сигнатура ----------------------------------------------#
def sign(first, second):
    if first - second >= 0:
        return 1
    else: return -1

def sign1(value):
    if value > 0:
        return (1)
    elif value == 0:
        return (0)
    else:
        return (-1)

#=======================================================================================================#
#------------------------------------ Функция кругового арктангенса ------------------------------------#
def circular_arc(arr_x, arr_y):
    i = len(arr_x)
    i -= 2
    X1 = arr_x[i]       # Обращение к предпоследнему элементу списка
    X2 = arr_x[-1]      # Обращение к последнему элементу списка
    j = len(arr_y)
    j -= 2
    Y1 = arr_y[j]       # Обращение к предпоследнему элементу списка
    Y2 = arr_y[-1]      # Обращение к последнему элементу списка
    if abs(Y1-Y2)>=.01 and Y1-Y2>0 and X1-X2>=0:
        rad = math.atan((X1-X2)/(Y1-Y2))
    elif abs(Y1-Y2)>=.01 and Y1-Y2>0 and X1-X2<0:
        rad = 2*math.pi + math.atan((X1-X2)/(Y1-Y2))
    elif abs(Y1-Y2)>=.01 and Y1-Y2<0:
        rad = math.pi + math.atan((X1-X2)/(Y1-Y2))
    elif abs(Y1-Y2)<=.01 and X1-X2>=0:
        rad = math.pi/2
    elif abs(Y1-Y2)<=.01 and X1-X2<0:
        rad = 3*math.pi/2
    else:
        print("Круговой арктангенс, ошибка!")
    return rad

def circular_arc2(X, Y):

    if Y>0:
        rad = math.atan(X/Y)
    elif Y<0:
        rad = math.pi + math.atan(X/Y)
    elif Y==0 and X>0:
        rad = math.pi/2
    elif Y==0 and X<0:
        rad = 3*math.pi/2
    else:
        print("Круговой арктангенс2, ошибка!")
    rad = priv_2pi(rad)
    return rad
#=======================================================================================================#








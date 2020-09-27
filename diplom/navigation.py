import math
import random
import numpy as np
from diplom import special

#========================================================================================================#
#-------------------------------------- Обработчик текущей скорости -------------------------------------#
def current_speed(st_speed, speed, acceleration, d_time):
    if abs(st_speed - speed) > acceleration*d_time/2:
        speed = speed + acceleration*d_time*special.sign(st_speed, speed)
    elif abs(st_speed - speed) <= acceleration*d_time/2:
        speed = st_speed
    return speed

#========================================================================================================#
#-------------------------------------------- Обработчик курса ------------------------------------------#
def current_course(new_course, course, speed, Rc, dt):
    Temp1 = special.priv_pi(new_course - course)
    Temp2 = speed * dt/(2*Rc)
    if abs(Temp1) > Temp2:
        course += 2 * Temp2 * special.sign1(Temp1)
        turn = 1
    else:
        course = new_course
        turn = 0
    return  course, turn
#========================================================================================================#
#----------------------------------------- Вычисление координат -----------------------------------------#
def trajectory(speed_x,speed_y,d_time,x,y):
    dx = speed_x * d_time
    dy = speed_y * d_time
    x += dx
    y += dy
    return x,y

def trajectory1(speed, course, dt, Sx, Sy):
    dSx= speed * math.sin(course) * dt
    dSy = speed * math.cos(course) * dt
    Sx += dSx
    Sy += dSy
    return Sx, Sy
#========================================================================================================#
#------------------------------------- Определение стороны поворота -------------------------------------#
def turn(course, course_obj):
    new_course = course_obj
    #new_speed = int(input("Скорость после манёвра >>> "))
    #new_speed = special.speed(new_speed)
    new_course = special.priv_2pi(new_course)
    if math.pi/2 >= new_course - course >= 0:
        turn = 1    # right turn
    elif course - math.pi/2 >= new_course:
        turn = 1
    elif new_course - course > math.pi/2:
        turn = -1  # left turn
    elif new_course - course < 0:
        turn = 0
    else: print("turn, что то пошло не так!")
    return new_course, turn
#========================================================================================================#

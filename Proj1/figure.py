import matplotlib.pyplot as plt
import numpy as np

def maps(X_obs, Y_obs, X_obj, Y_obj, X_meas, Y_meas, Obj_X, Obj_Y):
    j = 0
    i = 0
    x = max(X_obs)//1
    y = max(Y_obs)//1
    fig, coord = plt.subplots()
    xx = np.linspace(-x, x, 10)
    yy = np.linspace(-x, x, 10)
    coord.plot(xx, yy, color="white")
    coord.plot(X_obs, Y_obs,"-", color="green", label="Наблюдатель")
    coord.plot(X_obj, Y_obj, color="red", label="Объект(P)")
    coord.plot(Obj_X, Obj_Y, color="blue", label="Объект(И)")
    while i < len(X_meas):
        X = [X_meas[i], X_meas[i + 1]]
        Y = [Y_meas[i], Y_meas[i + 1]]
        coord.plot(X, Y, ":", color="black")
        i += 2

    coord.set_xlabel("x (seamiles)")
    coord.set_ylabel("y (seamiles)")
    coord.legend()
    plt.show()


from math import sqrt, pi

def Calcula_angulo(x_init, y_init):
    return (4.5-y_init) / (4.125-x_init)

def Calcula_tempo(init, ace, pos_final):
    return sqrt(((pos_final-init)*2)/ace)

def Calcula_modulo(C1, C2):
    return sqrt((C1*C1)+(C2*C2))

def Converter_rad(rad):
    return (rad*180)/pi
import funcoes
from math import cos, sin, atan, pi

x_init = 0
y_init = 0
angulo_rad = atan(funcoes.Calcula_angulo(x_init, y_init)) #A partir do ioio mixoxo o programa calcula o coeficiente angular (funcao calcula_angulo) e calcula o arco tangente do coeficiente chegando assim no angulo em radianos

angulo = funcoes.Converter_rad(angulo_rad) #Converte de radianos para graus 

coss = cos(angulo_rad)
seno = sin(angulo_rad)

acele_x = 2.8*coss
acele_y = 2.8*seno

velo_x = 6.5*coss
velo_y = 6.5*seno

tempo_x = funcoes.Calcula_tempo(x_init, acele_x, 4.125)
tempo_y = funcoes.Calcula_tempo(y_init, acele_y, 4.5)

tempo_final = funcoes.Calcula_modulo(tempo_x, tempo_y)

print(angulo)
print(acele_x)
print(acele_y)

print(coss)
print(seno)

print(tempo_final)
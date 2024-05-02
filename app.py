import funcoes
from math import cos, sin, atan, pi
from flask import Flask, render_template, request

# x_init = 0.5
# y_init = 0
# angulo_rad = atan(funcoes.Calcula_angulo(x_init, y_init)) #A partir do ioio mixoxo o programa calcula o coeficiente angular (funcao calcula_angulo) e calcula o arco tangente do coeficiente chegando assim no angulo em radianos

# angulo = funcoes.Converter_rad(angulo_rad) #Converte de radianos para graus 

# print(angulo)

# coss = cos(angulo_rad)
# seno = sin(angulo_rad)

# acele_x = 0.5*coss
# acele_y = 0.5*seno

# velo_x = 2.5*coss
# velo_y = 2.5*seno

# tempo_x = funcoes.Calcula_tempo(x_init, acele_x, 4.125)
# tempo_y = funcoes.Calcula_tempo(y_init, acele_y, 4.5)

# funcoes.Calculo_ponto_a_ponto(x_init, y_init, acele_x, acele_y)
# funcoes.Calculo_velocidade(acele_x, acele_y, coss, seno)

app = Flask(__name__)
@app.route("/")
def index():
    nome = "Fernanda"

    return render_template("index.html", nome=nome)

@app.route('/processar', methods=['POST'])
def processar():
    x_init = float(request.form['x'])
    y_init = float(request.form['y'])
    angulo_rad = atan(funcoes.Calcula_angulo(x_init, y_init)) #A partir do ioio mixoxo o programa calcula o coeficiente angular (funcao calcula_angulo) e calcula o arco tangente do coeficiente chegando assim no angulo em radianos

    angulo = funcoes.Converter_rad(angulo_rad) #Converte de radianos para graus 

    print(angulo)

    coss = cos(angulo_rad)
    seno = sin(angulo_rad)

    acele_x = 0.5*coss
    acele_y = 0.5*seno

    # velo_x = 2.5*coss
    # velo_y = 2.5*seno

    # tempo_x = funcoes.Calcula_tempo(x_init, acele_x, 4.125)
    # tempo_y = funcoes.Calcula_tempo(y_init, acele_y, 4.5)

    funcoes.Calculo_ponto_a_ponto(x_init, y_init, acele_x, acele_y)
    funcoes.Calculo_velocidade(acele_x, acele_y, coss, seno)
    
    return render_template("index.html", valor=angulo)

if __name__ == "__main__":
    app.run(debug=True)

import funcoes
from math import cos, sin, atan, pi
from flask import Flask, render_template, request

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

    funcoes.Calculo_ponto_a_ponto(x_init, y_init, acele_x, acele_y)
    funcoes.Calculo_velocidade(acele_x, acele_y, coss, seno)
    
    return render_template("index.html", valor=angulo)

if __name__ == "__main__":
    app.run(debug=True)

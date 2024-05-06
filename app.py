import funcoes
import csv
from math import cos, sin, atan, pi
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# @app.route('/processar', methods=['POST'])
# def processar():
#     # Ler os dados dos arquivos CSV na memória
#     bola_data = ler_csv('posicao-bola.csv')
#     robo_data = ler_csv('posicao.csv')

#     # Enviar os dados para o frontend
#     return render_template('processa.html', bola_data=bola_data, robo_data=robo_data)

@app.route('/')
def index():

    # Enviar os dados para o frontend
    return render_template('index.html')

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
    
    bola_data = ler_csv('posicao-bola.csv')
    robo_data = ler_csv('posicao.csv')

    # Enviar os dados para o frontend
    return render_template('processa.html', bola_data=bola_data, robo_data=robo_data)


def ler_csv(arquivo):
    pos_x = []
    pos_y = []
    with open(arquivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            pos_x.append(float(row[1]) *75)
            pos_y.append(float(row[2]) *75)

        return pos_x, pos_y

if __name__ == "__main__":
    app.run(debug=True)

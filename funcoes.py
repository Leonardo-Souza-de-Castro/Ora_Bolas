from math import sqrt, pi
import csv

def Calcula_angulo(x_init, y_init):
    return (4.5-y_init) / (4.125-x_init)

def Calcula_tempo(init, ace, pos_final):
    return sqrt(((pos_final-init)*2)/ace)

def Calcula_modulo(C1, C2):
    return sqrt((C1*C1)+(C2*C2))

def Converter_rad(rad):
    return (rad*180)/pi

def Calculo_ponto_a_ponto(initx, inity, ace_x, ace_y):
    tempo = 5
    with open("posicao.csv", "w", encoding='utf-8') as arquivoCSV: #Cria arquivo csv no modo escrita
        fieldnames=['Tempo(s)', 'X(M)', 'Y(M)'] # Inicializa os cabecalhos

        escrever = csv.DictWriter(arquivoCSV, fieldnames=fieldnames, lineterminator='\r') #inicializa o escritor de linhas
        if arquivoCSV.tell == 0: #Caso seja a linha 0
            escrever.writeheader() #Escreve o cabecalho do arquivo

        x = 0 #Inicializa a contagem do tempo no t = 0
        while(x <= tempo):
            pos_x = initx+((ace_x*(x*x))/2)

            pos_y = inity+((ace_y*(x*x))/2)

            if (x>=2.0881):
                pos_x = 4.125
                pos_y = 4.5

            escrever.writerow({'Tempo(s)': '{:.4f}'.format(x), 'X(M)': '{:.3f}'.format(pos_x), 'Y(M)':'{:.3f}'.format(pos_y)}) #Escreve a info certa na coluna certa

            x += 0.0001

def Calculo_velocidade(ace_x, ace_y,vx_init=0, vy_init=0):
    tempo = 5
    with open("velocidade.csv", "w", encoding='utf-8') as arquivoCSV: #Cria arquivo csv no modo escrita
        fieldnames=['Tempo(s)', 'Vx(M)', 'Vy(M)'] # Inicializa os cabecalhos

        escrever = csv.DictWriter(arquivoCSV, fieldnames=fieldnames, lineterminator='\r') #inicializa o escritor de linhas
        if arquivoCSV.tell == 0: #Caso seja a linha 0
            escrever.writeheader() #Escreve o cabecalho do arquivo

        x = 0 #Inicializa a contagem do tempo no t = 0
        while(x <= tempo):

            if(x>=2.0878 and x<=2.0881):
                pos_x = pos_x - ace_x
                if pos_x < 0:
                    pos_x = 0
            else:
                pos_x = vx_init+(ace_x*x)

            if(pos_x >= 4.39):
                pos_x = 4.39

            if(x>=2.0878 and x<=2.0881):
                pos_y = pos_y - ace_y
                if pos_y < 0:
                    pos_y = 0
            else:
                pos_y = vy_init+(ace_y*x)
            if(pos_y >= 4.79):
                pos_y = 4.79

            if (x>2.0881):
                pos_x = 0
                pos_y = 0


            escrever.writerow({'Tempo(s)': '{:.4f}'.format(x), 'Vx(M)': '{:.3f}'.format(pos_x), 'Vy(M)':'{:.3f}'.format(pos_y)}) #Escreve a info certa na coluna certa

            x += 0.0001
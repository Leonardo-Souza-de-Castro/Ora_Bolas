from math import sqrt, pi
import csv
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

def Upload_azure(caminho_arq, nome):

    # Defina suas credenciais do Azure
    connection_string = "connection_string"
    container_name = "teste"

    # Caminho local do arquivo que você deseja enviar para o Azure Blob Storage
    local_file_path = caminho_arq
    blob_name = nome

    # Criar um BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Criar um ContainerClient
    container_client = blob_service_client.get_container_client(container_name)

    # Upload do arquivo para o Blob Storage
    blob_client = container_client.get_blob_client(blob_name)
    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print("Arquivo enviado com sucesso para o Azure Blob Storage.")

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
        escrever.writeheader() #Escreve o cabecalho do arquivo

        x = 0 #Inicializa a contagem do tempo no t = 0
        while(x <= tempo):
            pos_x = initx+((ace_x*(x**2))/2)

            pos_y = inity+((ace_y*(x**2))/2)

            if pos_x >= 4.125:
                pos_x = 4.125

            if pos_y >= 4.5:
                pos_y = 4.5

            escrever.writerow({'Tempo(s)': '{:.4f}'.format(x), 'X(M)': '{:.3f}'.format(pos_x), 'Y(M)':'{:.3f}'.format(pos_y)}) #Escreve a info certa na coluna certa

            x += 0.02
    Upload_azure("posicao.csv","posicao.csv" )

def Calculo_velocidade(ace_x, ace_y,coss, seno, vx_init=0, vy_init=0):
    tempo = 5
    with open("velocidade.csv", "w", encoding='utf-8') as arquivoCSV: #Cria arquivo csv no modo escrita
        fieldnames=['Tempo(s)', 'Vx(M)', 'Vy(M)'] # Inicializa os cabecalhos

        escrever = csv.DictWriter(arquivoCSV, fieldnames=fieldnames, lineterminator='\r') #inicializa o escritor de linhas
        escrever.writeheader() #Escreve o cabecalho do arquivo

        x = 0 #Inicializa a contagem do tempo no t = 0
        while(x <= tempo):

            pos_x = vx_init+(ace_x*x)

            pos_y = vy_init+(ace_y*x)

            if Calcula_modulo(pos_x, pos_y) >= 2.5:
                pos_x = 2.5*coss
                pos_y = 2.5*seno


            escrever.writerow({'Tempo(s)': '{:.4f}'.format(x), 'Vx(M)': '{:.3f}'.format(pos_x), 'Vy(M)':'{:.3f}'.format(pos_y)}) #Escreve a info certa na coluna certa

            x += 0.02

    Upload_azure("velocidade.csv","velocidade.csv" )
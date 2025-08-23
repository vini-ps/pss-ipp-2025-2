import pandas as pd
import numpy as np

def ler_arquivo_csv():
  dataframe = pd.read_csv('Agenda_BL_Rua_Carnaval_Rio-2018_Imprensa.csv', encoding='latin1', sep=';')
  return dataframe

def ajustar_dataframe(dataframe):
  
  #removendo acentos da string
  dataframe['Bairro'] = dataframe['Bairro'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

  #deixando todas em minusculo
  dataframe['Bairro'] = dataframe['Bairro'].str.lower()

  #remover espaço em branco no final da string
  dataframe['Bairro'] = dataframe['Bairro'].str.rstrip()

def listar_blocos_bairro(dataframe):
  bairro = input("Escolha um bairro: ")
  bairro = bairro.lower()
  print('\n')
  for data in dataframe[dataframe['Bairro'] == bairro]['Data'].unique():
    bloco = dataframe[(dataframe['Bairro'] == bairro) & (dataframe['Data'] == data)]['Bloco'].iloc[:]
    resultado = f"Data: {data}\nBlocos:\n{bloco}\n"
    print(resultado)
  resultado = dataframe[(dataframe['Bairro'] == bairro)]
  return resultado

def exportar_csv(dataframe):
  if input("Deseja Salvar? (S ou N): ").upper() == 'S':
    lista_de_blocos = dataframe[['Bloco','Data']]
    lista_de_blocos.to_csv('lista_de_blocos.csv', index=False)

if __name__ == "__main__":
  AgendaBlocosRJ = ler_arquivo_csv()
  ajustar_dataframe(AgendaBlocosRJ)
  ListaBlocosBairro = listar_blocos_bairro(AgendaBlocosRJ)
  exportar_csv(ListaBlocosBairro)
  
  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Agenda_BL_Rua_Carnaval_Rio-2018_Imprensa.csv', encoding='latin1', sep=';')

#removendo acentos da string
df['Bairro'] = df['Bairro'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

#deixando todas em minusculo
df['Bairro'] = df['Bairro'].str.lower()

#remover espaço em branco no final da string
df['Bairro'] = df['Bairro'].str.rstrip()
bairro = input("Escolha um bairro: ")
bairro = bairro.lower()
print('\n')
for data in df[df['Bairro'] == bairro]['Data'].unique():
  bloco = df[(df['Bairro'] == bairro) & (df['Data'] == data)]['Bloco'].iloc[:]
  resultado = f"Data: {data}\nBlocos:\n{bloco}\n"
  print(resultado)
resultado = df[(df['Bairro'] == bairro)]
if input("Deseja Salvar? (S ou N): ").upper() == 'S':
  resultado.to_csv('resultado.csv', index=False)

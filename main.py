import csv
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. cria o arquivo
f = open('analise_java.csv', 'w', newline='', encoding='utf-8')

# 2. cria o objeto de gravação
w = csv.writer(f)

# 3. descrição colunas
w.writerow(['Valor de entrada', 'Divisores', 'Tempo gasto'])

# 4. grava as linhas
for i in range(5):
  w.writerow([i, i*2, i*3])
  os.system()
  #executar codigo java
  #executar o codigo c

  # Gera relatório
  plt.rcParams["figure.figsize"] = [7.50, 3.50]
  plt.rcParams["figure.autolayout"] = True

  headers = ['Valor de entrada', 'Divisores', 'Tempo gasto']

  df = pd.read_csv('analise_java.csv', names=headers)

  df.set_index('Tempo gasto').plot()

  plt.show()

  plt.rcParams()
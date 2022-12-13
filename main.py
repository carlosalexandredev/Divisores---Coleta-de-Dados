import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
import numpy as np


def cria_arquivo():
  # 1. Cria o arquivo
  jfile = open('analise_java.csv', 'w', newline='', encoding='utf-8')
  cfile = open('analise_c.csv', 'w', newline='', encoding='utf-8')

  # 2. Cria o objeto de gravação CSV
  jw = csv.writer(jfile)
  cw = csv.writer(cfile)
  descricao = ['Valor de entrada', 'Divisores', 'Tempo gasto']

  # 3. Descrição colunas
  jw.writerow(descricao)
  cw.writerow(descricao)

  grava_dados(jw, cw)

  jfile.close()
  cfile.close()

# 4. Grava as linhas
def compila_divisores():
  os.system('javac Divisores.java')
  os.system('gcc divisores.c -o divisores')

def grava_dados(jw, cw):
  i = 1000
  while i <= 1000000000:
    # 5. Executa codigo java
    saida_java = eval(os.popen(f'java Divisores {i}').read())
    print(f'Código em JAVA: \n{str(saida_java)}')
    jw.writerow([saida_java['entrada'], saida_java['divisores'], saida_java['tempogasto']])

    # 6. Executa o codigo c
    saida_c = eval(os.popen(f'./divisores {i}').read())
    print(f'Código em C: \n{str(saida_c)}')
    cw.writerow([saida_c['entrada'], saida_c['divisores'], saida_c['tempogasto']])

    i = i*10


# Gera relatório
def gera_relatorio():
  arquivo = open('analise_java.csv')
  csv_java = csv.DictReader(arquivo)
  entrada = []
  java_tempo_gasto = []

  arquivo = open('analise_c.csv')
  csv_c = csv.DictReader(arquivo)
  c_entrada = []
  c_tempo_gasto = []

  for csv_line in csv_java:
    entrada.append(int(csv_line["Valor de entrada"]))
    java_tempo_gasto.append(float(csv_line["Tempo gasto"]))

  for csv_line in csv_c:
    c_entrada.append(int(csv_line["Valor de entrada"]))
    c_tempo_gasto.append(float(csv_line["Tempo gasto"]))

  plt.title('Análise Java/C')

  labels = entrada

  x = np.arange(len(labels))  # the label locations
  width = 0.35  # the width of the bars

  fig, ax = plt.subplots()
  rects1 = ax.bar(x - width / 2, java_tempo_gasto, width, label='Java')
  rects2 = ax.bar(x + width / 2, c_tempo_gasto, width, label='C')

  ax.bar_label(rects1, padding=5)
  ax.bar_label(rects2, padding=5)

  # Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_ylabel('Tempo de Processamento')
  ax.set_xticks(x, labels)
  ax.legend()

  fig.tight_layout()

  plt.show()

if __name__ == "__main__":
  compila_divisores()
  cria_arquivo()
  gera_relatorio()

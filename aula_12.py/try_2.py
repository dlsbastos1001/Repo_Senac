import numpy as np
import pandas as pd

dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])
q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)
mediana = np.median(dados)
q3 = np.percentile(dados, 75)
print(f'Mediana: {mediana}')
print(f'Primeiro quartil (Q1): {q1}')
print(f'Segundo quartil (Q2): {q2}')
print(f'Terceiro quartil (Q3): {q3}')

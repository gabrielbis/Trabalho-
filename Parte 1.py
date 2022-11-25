#integrantes:
#Adriel Luiz Agostini
#Alex Augusto Rosa Ramos
#Gabriel Fernando Deroldo Bis
#Rafael de Mello Castro Bacha

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0,0.05,300) #time steps

#onda fundamental
s = np.sin(60 * 2 * np.pi * t)

#primeira harmonica
harmonica1 = np.sin(120 * 2 * np.pi * t)

#segunda harmonica
harmonica2 = np.sin(180 * 2 * np.pi * t)

#terceira harmonica
harmonica3 = np.sin(240 * 2 * np.pi * t)

#sinal distorcido
sinaldistorcido = s + harmonica1 + harmonica2 + harmonica3

#plotando o sinal distorcido
plt.plot(t,sinaldistorcido)
plt.xlabel('Tempo (S)')
plt.ylabel('Sinal')
plt.legend(['Sinal Distorcido'])
plt.title('Onda Distorcida')
plt.show()

#Criando um arquivo csv
arr = np.append(t.reshape(-1, 1), sinaldistorcido.reshape(-1, 1), axis=1)
df = pd.DataFrame(arr, columns=['tempo', 'sinal'])
df.to_csv('dados.csv', index=False, index_label=False)


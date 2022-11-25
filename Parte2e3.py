import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importando qualquer arquivo de outra pessoa
df = pd.read_csv('dados.csv', sep=',',decimal='.',encoding = 'unicode_escape')
df.head()
N = len(df['tempo'].tolist())

#Armazenando o tempo e o sinal em listas separadas
tempo = df['tempo'].tolist()
sinal = df['sinal'].tolist()

Fs=300
time_step=1/Fs 
fstep= Fs/N

# espectro da onda harmonica
t=np.linspace(0,(N-1)*time_step,N) #time steps
f=np.linspace(0,(N-1)*fstep,N) #time


y_s=len(tempo)
EspectroHarmonica=np.fft.fft(sinal)/y_s
sh= np.abs(EspectroHarmonica)
fh_plot=f[0:int(y_s/2+1)]
sh_plot=2*sh[0:int(y_s/2+1)]
sh_plot[0]=sh_plot[0]/2


#plot do espectro da onda Harmonico
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(t,sinal)
plt.xlabel('Tempo (S)',fontsize=14)
plt.ylabel('Sinal',fontsize=14)

plt.subplot(1,2,2)
fft_harmonic, =plt.plot(fh_plot, sh_plot, color='r')
plt.xlabel('Frequencia (Hz)',fontsize=14)
plt.ylabel('Amplitude',fontsize=14)
plt.grid()
plt.show()

#declarando as variaveis 
freq= 60 
res1 = 100
cicl = 5
resist = 4

#  Tensão/Corrente Eficaz
peaks_Tensão = []
V_RMS = []
frequencia_harmonicas = []
for i in range(1, int(res1 / 2)):
    if sh[i-1] < sh[i] > sh[i+1]:
        V_RMS.append(sh[i] * 0.7071)
        peaks_Tensão.append(sh[i])
        frequencia_harmonicas.append(i * freq / cicl)
current_RMS = np.multiply(V_RMS, 1 / resist)

#THD
Vne = 0
for i in range(1, len(V_RMS)):
    Vne = Vne + (V_RMS[i] ** 2)
THD = np.sqrt(Vne) / V_RMS[0]

#TDD
In = 0
for i in range(1, len(current_RMS)):
    In = In + (current_RMS[i] ** 2)
TDD = np.sqrt(In) / current_RMS[0]

#  Tensão RMS
Vrms_temp = 0
for i in range(len(V_RMS)):
    Vrms_temp = Vrms_temp + (V_RMS[i] ** 2)
Vrms = np.sqrt(Vrms_temp)

#  Corrente Eficaz
Irms_temp = 0
for i in range(len(current_RMS)):
    Irms_temp = Irms_temp + (current_RMS[i] ** 2)
Irms = np.sqrt(Irms_temp)

#  Potencia de distorção harmonica
Pot = Vrms * Irms

#  Informações de tela
print(f'Distorcao Harmonica Total (THD): {round(THD * 100, 3)}%')
print(f'Distorcao Harmonica de Demanda Total (TDD): {round(TDD * 100, 3)}%')
print(f'Potencia de distorcao harmonica: {round(Pot, 3)}W')

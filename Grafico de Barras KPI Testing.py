import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(10,7))

sprints                 = [2, 3, 4, 5, 6, 7]
cpPorSprint             = [5, 9, 12, 9, 4, 5]
cpTesteadosPorSprint    = [0.2, 5, 9, 12, 0.2, 13]
posiciones              = [0, 1, 2, 3, 4, 5]
posiciones2             = [0.2, 1.2, 2.2, 3.2, 4.2, 5.2]

y = np.arange(0, max(cpPorSprint)+1, 1)
#Barra nro 1
plt.bar(posiciones, cpPorSprint, width=0.45, color='#47d4ff', label='CP Identificados', edgecolor='black')
plt.xticks(posiciones, sprints)
plt.yticks(y)
plt.xlabel('Sprint')
#Barra nro 2
plt.bar(posiciones2, cpTesteadosPorSprint, width=0.4, color='#d154c9', label='CP Testeados', edgecolor='black')

cpTotales = sum(cpPorSprint)
cpTesteados = int(sum(cpTesteadosPorSprint) - 0.4)
coverage = (cpTesteados / cpTotales) * 100

plt.figtext(0.1,0.01,f'CP Totales: {cpTotales}                                            CP Testeados: {cpTesteados}\
                                            Coverage: {round(coverage, 2)}%', fontsize=12, )

plt.title('KPI Sprints Testing de Aplicaciones')
plt.legend()
plt.show()

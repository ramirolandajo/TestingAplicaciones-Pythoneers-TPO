import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,7))

severidadBugs   = [2, 7, 1] #baja, media, alta
labels          = ['Baja', 'Media', 'Alta']
colores = ['#c42759', '#6345c4', '#3cc0de']
titulo = 'Porcentaje de Bugs segun severidad'

plt.title(titulo)
plt.pie(severidadBugs, colors=colores, labels=labels, autopct='%1.1f%%')

plt.show()


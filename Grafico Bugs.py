import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,7))

severidadBugs   = [3, 9, 1] #baja, media, alta
labels          = ['Baja', 'Media', 'Alta']
colores = ['#c42759', '#6345c4', '#3cc0de']
titulo = 'Porcentaje de Bugs segun severidad'

plt.title(titulo)
plt.pie(severidadBugs, colors=colores, labels=labels, autopct='%1.1f%%')

plt.figtext(0.1,0.01,f'Bugs severidad Baja: {severidadBugs[0]}                                            Bugs severidad Media: {severidadBugs[1]}\
                                            Bugs severidad Alta: {severidadBugs[2]}', fontsize=10, )

plt.show()


import numpy as np
import matplotlib.pyplot as plt
import csv

# Latitud de Bellaterra
lat= np.radians(41.5037)


# Dies de l'any
dies = np.arange(1, 369)

# Equació del temps
def EoT_2025(d):
    a = -7.659 * np.sin(163.316 + 0.017 * d)
    b =  9.863 * np.sin(326.631 + 0.034 * d + 3.5932)
    return a + b  # minutos

# Declinació solar
def declinacion(d):
    return np.radians(-23.44 * np.cos(2 * np.pi * (d + 10) / 365.25))

# Listas para guardar altura y azimut
altures = []
azimuts = []



for d in dies:
    delta = declinacion(d)         # declinació en radiants
    EoT = EoT_2025(d)                     # en minuts
    H = np.radians(0.25 * EoT)            # hora angular en radiants (0° a 12:00)

    # Altura solar
    h = np.arcsin(np.sin(lat) * np.sin(delta) + np.cos(lat) * np.cos(delta) * np.cos(H))
    altures.append(np.degrees(h))

    # Azimut solar
    if H > 0:
      A = np.arccos((np.sin(delta)*np.cos(lat)-np.cos(delta)*np.sin(lat)*np.cos(H))/np.cos(h))
    else:
      A = 2 * np.pi - np.arccos((np.sin(delta)*np.cos(lat)-np.cos(delta)*np.sin(lat)*np.cos(H))/np.cos(h))

    azimuts.append(np.degrees(A))


# Gràfica
plt.style.use('classic')
plt.figure(facecolor='white', figsize=(6,8))
plt.scatter(azimuts, altures, s=50, edgecolors='none')
plt.xlabel('Azimut (°)')
plt.ylabel('Altura (°)')
plt.grid(True)
plt.gca().invert_xaxis()   # Canviem l'orientació horitzontal del gràfic per a què l'oest es trobi a la dreta.
plt.tight_layout()
plt.show()


#Càlcul de les mesures angulars de l'analema obtingut

altura_max = max(altures)
altura_min = min(altures)


azimut_max = max(azimuts)
azimut_min = min(azimuts)




#Càlcul de les mesures angulars de l'analema obtingut amb Stellarium

azimuts_ = []
altures_ = []


# Llegir l'arxiu exportat de Stellarium
with open('dades_stellarium/analema_12h.csv', newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f, delimiter=';')
    for fila in lector:
        azimut_deg = float(fila['Azimuts'])
        altura_deg = float(fila['Altures'])
        azimuts_.append(azimut_deg)
        altures_.append(altura_deg)
        

#Imprimir valors per comparar mides

print('ANALEMA 12H')

print('Mida altitudinal analema: ', altura_max - altura_min, 'graus')
print('Mida altitudinal analema Stellarium: ', max(altures_) - min(altures_), 'graus')

print('Mida azimutal analema: ', azimut_max - azimut_min, 'graus')
print('Mida azimutal analema Stellarium: ', max(azimuts_) - min(azimuts_), 'graus')
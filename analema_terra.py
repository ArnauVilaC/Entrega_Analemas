import numpy as np
import matplotlib.pyplot as plt

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
altituts = []
azimuts = []

for d in dies:
    delta = declinacion(d)         # declinació en radiants
    EoT = EoT_2025(d)                     # en minuts
    H = np.radians(0.25 * EoT)            # hora angular en radiants (0° a 12:00)

    # Altura solar
    h = np.arcsin(np.sin(lat) * np.sin(delta) + np.cos(lat) * np.cos(delta) * np.cos(H))
    altituts.append(np.degrees(h))

    # Azimut solar
    if H > 0:
      A = np.arccos((np.sin(delta)*np.cos(lat)-np.cos(delta)*np.sin(lat)*np.cos(H))/np.cos(h))
    else:
      A = 2 * np.pi - np.arccos((np.sin(delta)*np.cos(lat)-np.cos(delta)*np.sin(lat)*np.cos(H))/np.cos(h))

    azimuts.append(np.degrees(A))


# Gràfica
plt.style.use('classic')
plt.figure(facecolor='white', figsize=(6,8))
plt.scatter(azimuts, altituts, s=100, edgecolors='none')
plt.title('Analema solar vist desde Bellaterra a les 12:00')
plt.xlabel('Azimut (°)')
plt.ylabel('Altura (°)')
plt.grid(True)
plt.gca().invert_xaxis()   # Canviem l'orientació el gràfic per a què l'oest es trobi a la dreta.
plt.tight_layout()
plt.show()




#Analema Solar a les 9:00h

altituts_1 = []
azimuts_1 = []

for d in dies:
    delta = declinacion(d)         # declinació en radiants
    EoT = EoT_2025(d)                     # en minuts
    H = np.radians(15 * (9-12+EoT/60))            # hora angular en radiants (0° a les 6:00)

    # Altura solar
    h = np.arcsin(np.sin(lat) * np.sin(delta) + np.cos(lat) * np.cos(delta) * np.cos(H))
    altituts_1.append(np.degrees(h))

    # Azimut solar
    if H > 0:
      A = np.arccos((np.sin(delta)*np.cos(lat)-np.cos(delta)*np.sin(lat)*np.cos(H))/np.cos(h))
    else:
      A = 2 * np.pi - np.arccos((np.sin(delta)*np.cos(lat)-np.cos(delta)*np.sin(lat)*np.cos(H))/np.cos(h))

    azimuts_1.append(np.degrees(A))
    
plt.style.use('classic')
plt.figure(facecolor='white', figsize=(6,8))
plt.scatter(azimuts_1, altituts_1, s=100, edgecolors='none')
plt.title('Analema solar vist desde Bellaterra a les 9:00')
plt.xlabel('Azimut (°)')
plt.ylabel('Altura (°)')
plt.grid(True)
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()


#Analema Solar a les 15:00

altituts_2 = []
azimuts_2 = []

for d in dies:
    delta = declinacion(d)         # declinació en radiants
    EoT = EoT_2025(d)                     # en minuts
    H = np.radians(15 * (15-12+EoT/60))            # hora angular en radiants (0° a les 18:00)

    # Altura solar
    h = np.arcsin(np.sin(lat) * np.sin(delta) + np.cos(lat) * np.cos(delta) * np.cos(H))
    altituts_2.append(np.degrees(h))

    # Azimut solar
    if H > 0:
      A = np.arccos((np.sin(delta)*np.cos(lat)-np.cos(delta)*np.sin(lat)*np.cos(H))/np.cos(h))
    else:
      A = 2 * np.pi - np.arccos((np.sin(delta)*np.cos(lat)-np.cos(delta)*np.sin(lat)*np.cos(H))/np.cos(h))

    azimuts_2.append(np.degrees(A))
    
    
plt.style.use('classic')
plt.figure(facecolor='white', figsize=(6,8))
plt.scatter(azimuts_2, altituts_2, s=100, edgecolors='none')
plt.title('Analema solar vist desde Bellaterra a les 15:00')
plt.xlabel('Azimut (°)')
plt.ylabel('Altura (°)')
plt.grid(True)
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn


latitud_observador_graus = 41.5
hora_observacio = 12
latitud_observador_rad = np.radians(latitud_observador_graus)
termes_bessel = 20

desfasament_periheli_mart = 16.5
periode_orbital_mart = 686.98
dies_martians = np.linspace(0, periode_orbital_mart, 1000)

excentricitat_mart = 0.0934
inclinacio_mart = np.radians(25.19)
longitud_periheli_mart = np.radians(286.502)

anomalia_mitjana_mart = 2 * np.pi * (dies_martians - desfasament_periheli_mart) / periode_orbital_mart
solucio_kepler_mart = anomalia_mitjana_mart.copy()
for n in range(1, termes_bessel + 1):
    solucio_kepler_mart += (2 / n) * jn(n, n * excentricitat_mart) * np.sin(n * anomalia_mitjana_mart)

anomalia_vertadera_mart = np.arctan2(
    np.sqrt(1 - excentricitat_mart**2) * np.sin(solucio_kepler_mart),
    np.cos(solucio_kepler_mart) - excentricitat_mart
)
longitud_ecliptica_mart = (anomalia_vertadera_mart + longitud_periheli_mart) % (2 * np.pi)

ascensio_recta_mart = np.unwrap(np.arctan2(
    np.cos(inclinacio_mart) * np.sin(longitud_ecliptica_mart),
    np.cos(longitud_ecliptica_mart)
))
declinacio_mart = np.arcsin(np.sin(inclinacio_mart) * np.sin(longitud_ecliptica_mart))

equacio_del_temps_rad_mart = anomalia_mitjana_mart - ascensio_recta_mart
equacio_del_temps_min_mart = equacio_del_temps_rad_mart * (1440 / (2 * np.pi))
equacio_del_temps_min_mart -= np.mean(equacio_del_temps_min_mart)


angle_horari_graus_mart = 15 * (hora_observacio + equacio_del_temps_min_mart / 60 - 12)
angle_horari_rad_mart = np.radians(angle_horari_graus_mart)

elevacio_mart = np.degrees(np.arcsin(
    np.sin(latitud_observador_rad) * np.sin(declinacio_mart) +
    np.cos(latitud_observador_rad) * np.cos(declinacio_mart) * np.cos(angle_horari_rad_mart)
))

acimut_mart = np.degrees(np.arctan2(
    -np.sin(angle_horari_rad_mart),
    -np.cos(angle_horari_rad_mart) * np.sin(latitud_observador_rad) + np.tan(declinacio_mart) * np.cos(latitud_observador_rad)
)) % 360

plt.figure(figsize=(8, 10))
plt.scatter(acimut_mart, elevacio_mart)
plt.xlabel("Acimut (°)")
plt.ylabel("Alçada (°)")
plt.grid(True)
plt.tight_layout()
plt.show()


dades_planetes = {
    'Júpiter': {'excentricitat': 0.0489, 'long_periheli_graus': 14.75385 + 180, 'inclinacio_graus': 3.13, 'desfasament_tau': 14.0, 'periode': 4332.59},
    'Saturn':  {'excentricitat': 0.0565, 'long_periheli_graus': 92.43194 + 180, 'inclinacio_graus': 26.73, 'desfasament_tau': 27.0, 'periode': 10759.22},
}

for planeta, parametres in dades_planetes.items():
    excentricitat = parametres['excentricitat']
    long_periheli = np.radians(parametres['long_periheli_graus'])
    inclinacio = np.radians(parametres['inclinacio_graus'])
    desfasament_tau = parametres['desfasament_tau']
    periode = parametres['periode']
    dies_planetaris = np.linspace(0, periode, 1000)

    anomalia_mitjana = 2 * np.pi * (dies_planetaris - desfasament_tau) / periode
    solucio_kepler = anomalia_mitjana.copy()
    for n in range(1, termes_bessel + 1):
        solucio_kepler += (2 / n) * jn(n, n * excentricitat) * np.sin(n * anomalia_mitjana)

    anomalia_vertadera = np.arctan2(
        np.sqrt(1 - excentricitat**2) * np.sin(solucio_kepler),
        np.cos(solucio_kepler) - excentricitat
    )
    longitud_ecliptica = (anomalia_vertadera + long_periheli) % (2 * np.pi)

    ascensio_recta = np.unwrap(np.arctan2(np.cos(inclinacio) * np.sin(longitud_ecliptica), np.cos(longitud_ecliptica)))
    declinacio = np.arcsin(np.sin(inclinacio) * np.sin(longitud_ecliptica))

    equacio_del_temps = (anomalia_mitjana - ascensio_recta) * (1440 / (2 * np.pi))
    equacio_del_temps -= np.mean(equacio_del_temps)

    angle_horari_graus = 15 * (hora_observacio + equacio_del_temps / 60 - 12)
    angle_horari_rad = np.radians(angle_horari_graus)

    elevacio = np.degrees(np.arcsin(
        np.sin(latitud_observador_rad) * np.sin(declinacio) +
        np.cos(latitud_observador_rad) * np.cos(declinacio) * np.cos(angle_horari_rad)
    ))
    acimut = np.degrees(np.arctan2(
        -np.sin(angle_horari_rad),
        -np.cos(angle_horari_rad) * np.sin(latitud_observador_rad) + np.tan(declinacio) * np.cos(latitud_observador_rad)
    )) % 360

    plt.figure(figsize=(8, 10))
    plt.scatter(acimut, elevacio)
    plt.xlabel("Azimut (°)")
    plt.ylabel("Altura (°)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

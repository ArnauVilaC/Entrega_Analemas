Aquest repositori conté el material creat per Arnau Vila Crespo (NIU: 1657695) per a la realització de l'entrega sobre analemes de l'assignatura Introducció a l'Astrofísica. Consta de dos arxius python i un pdf amb l'enunciat de l'entrega. L'arxiu analema_terra.py conté un script de python que calcula i grafica l'analema solar vist desde Bellaterra a l'any 2025 a les 9:00h, a les 12:00h i a les 15:00h. L'arxiu analema_planetes.py conté un script de python que calcula i grafica l'analema solar vist desde Mart, Saturn i Júpiter.

---------

**1. ANALEMA VIST DESDE BELLATERRA**

**Arxiu:** analema_terra.py

Aquest arxiu conté un script de python que calcula i grafica l'analema solar vist desde Bellaterra a l'any 2025. Es calculen tres analemas capturats a diferents hores del dia: a les 9:00h, a les 12:00h i a les 15:00h. D'aquesta manera s'observa la forma i l'inclinació que presenten els analemes a diferents fases del dia.

El codi defineix dues funcions bàsiques que depenen del dia de l’any: una per calcular l’equació del temps i una altra per determinar la declinació solar. A partir d’aquestes funcions, es calcula la posició aparent del Sol per a cada dia de l’any, obtenint-ne l’azimut i l’altura solar. Aquestes coordenades es guarden en llistes i es fan servir per generar les gràfiques corresponents. En la representació, l’altura solar es mostra a l’eix vertical i l’azimut a l’eix horitzontal, que ha estat invertit per tal que l’oest quedi representat a la dreta, seguint la convenció habitual en aquest tipus de gràfiques.

A més del càlcul i la representació gràfica, l’script inclou una comparació entre els resultats teòrics obtinguts i les dades simulades amb el programa Stellarium. Per fer aquesta comparació, s’han exportat arxius .csv des de Stellarium amb les coordenades azimutals i altitudinals del Sol per als mateixos horaris i dies. Aquestes dades s’han llegit i analitzat per calcular les dimensions angulars de cada analema (en altura i en azimut), i posteriorment comparar-les amb les que es deriven del model calculat amb Python.

----------


**1. ANALEMA VIST DESDE ALTRES PLANETES**

**Arxiu:** analema_planetes.py

Aquest arxiu implementa un script de Python que calcula i representa l’analema solar tal com es veuria des de Mart, Júpiter i Saturn. Per a cada planeta, es tenen en compte els valors específics de l’excentricitat orbital, la inclinació de l’eix de rotació (obliqüitat), la longitud del període orbital i el desfasament respecte al periheli.

Els càlculs es basen en la resolució de l’equació de Kepler mitjançant una aproximació amb sèries de Bessel, cosa que permet determinar la posició del Sol al llarg de l’any planetari. A partir d’aquesta posició, es calcula la declinació solar, l’equació del temps i, finalment, les coordenades azimutals i d’elevació solar que defineixen la forma de l’analema.

Les gràfiques generades mostren l’altura solar respecte a l’azimut per a cada planeta, proporcionant una comparació visual de com canvia la figura de l’analema segons les característiques orbitals i rotacionals de cada món.
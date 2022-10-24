import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import numpy as np
import matplotlib.patches as mpatches

TIMEOUT = 5.00

n = 24;
plt.title("GoalPostManagerPlot - Palla esterna alla porta");

	##C1 = portiere al centro, palla esterna sx sulla linea di fondo	C2 = portiere al centro, palla esterna sx	C3 = portiere a sx, palla esterna sx	C4 = portiere a sx, palla esterna sx sulla linea di fondo	C5-C8 = C1-C4 a dx	C5-C8 la butta fuori	C7 rimane attaccato a palo
	##C9 = portiere al centro, palla fuori dal palo	C10 = portiere al centro, palla subito fuori dal palo	C10 rimane attaccato a palo	C11 = portiere a sx, palla subito fuori dal palo	C12 = portiere a sx, palla fuori dal palo	C13-C16 = C9-C12 a dx	C14 butta fuori
	##C17 = portiere al centro, palla a filo palo più vicino	C18 = portiere al centro, palla a filo palo	C19 = portiere a sx, palla a filo palo più vicino	C20 = portiere a sx, palla a filo palo	C21-C24 = C17-C20 a dx
timesMe = [1.63, 1.63, 1.58, 1.63, 1.60, 1.52, 1.52, 1.58]
vecchio = [1.63, 1.64, 1.67, 1.60, TIMEOUT, 1.55, TIMEOUT, TIMEOUT]


Diff = np.zeros(shape=8)
for i in range(8):
	Diff[i] = -timesMe[i] + vecchio[i]
Mean = Diff.sum()/8
Mean = round(Mean, 3)
Variance = 0
for i in range(8):
	Variance += (Diff[i] - Mean)*(Diff[i] - Mean)
Variace = Variance/8
Variace = round(Variace, 3)


names = ['C1\nPalla a fondo sx,\nportiere al centro', 'C2\nPalla a sx,\nportiere al centro', 'C3\nPalla a sx,\nportiere a sx', 'C4\nPalla a fondo sx,\nportiere a sx', 'C5\nPalla a fondo dx,\nportiere al centro', 'C6\nPalla a dx,\nportiere al centro', 'C7\nPalla a dx,\nportiere a dx', 'C8\nPalla a fondo dx,\nportiere a dx'];
plt.bar(names, timesMe, width = -0.2, align='edge', color="b", label = 'GoalPostManager');
plt.bar(names, vecchio, width = 0.2, align='edge', color="r", label = 'BasikStriker');
plt.axhline(y = TIMEOUT, color = 'grey', linestyle = '--', label = 'Timeout')
plt.ylabel("Tempo per segnare [m]");
plt.xlabel("Configurazioni");
##plt.tick_params(axis='x', rotation=30)	

plt.legend();

text = "Differenza media = " + str(Mean) + "\nVarianza = " + str(Variance)
fig, ax = plt.subplots()
plt.title("Variazione delle prestazioni - Palla esterna alla porta")
ax.bar(names, Diff, color="g", label = 'Variazione di prestazione');

at = AnchoredText(
    text, prop=dict(size=15), frameon=True, loc='upper left')
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")

ax.add_artist(at)
plt.ylabel("Variazione temporale [m]");
plt.xlabel("Configurazioni");
	
plt.legend();
	
plt.show();

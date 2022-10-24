import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import numpy as np
import matplotlib.patches as mpatches
TIMEOUT = 5.00

plt.title("GoalPostManagerPlot - Palla esterna, ma molto vicina ai pali");

	##C1 = portiere al centro, palla esterna sx sulla linea di fondo	C2 = portiere al centro, palla esterna sx	C3 = portiere a sx, palla esterna sx	C4 = portiere a sx, palla esterna sx sulla linea di fondo	C5-C8 = C1-C4 a dx	C5-C8 la butta fuori	C7 rimane attaccato a palo
	##C9 = portiere al centro, palla fuori dal palo	C10 = portiere al centro, palla subito fuori dal palo	C10 rimane attaccato a palo	C11 = portiere a sx, palla subito fuori dal palo	C12 = portiere a sx, palla fuori dal palo	C13-C16 = C9-C12 a dx	C14 butta fuori
	##C17 = portiere al centro, palla a filo palo più vicino	C18 = portiere al centro, palla a filo palo	C19 = portiere a sx, palla a filo palo più vicino	C20 = portiere a sx, palla a filo palo	C21-C24 = C17-C20 a dx
timesMe = [1.49, 1.51, 1.48, 1.53, 1.44, 1.46, 1.52, 1.53]
vecchio = [TIMEOUT, 2.70, 2.75, 1.51, 2.55, TIMEOUT, TIMEOUT, 2.51]

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


timesOld2 = [2.70, 2.75, 1.51, 2.55];
timesOld3 = 2.51;
names = ['C9\nPalla a sx palo,\nportiere al centro', 'C10\nPalla a sx vicina palo,\nportiere al centro', 'C11\nPalla a sx vicina palo,\nportiere a sx', 'C12\nPalla a sx palo,\nportiere a sx', 'C13\nPalla a dx palo,\nportiere al centro', 'C14\nPalla a dx vicina palo,\nportiere al centro', 'C15\nPalla a dx vicina palo,\nportiere a dx', 'C16\nPalla a dx palo,\nportiere a dx'];
plt.bar(names, timesMe, width = -0.2, align='edge', color="b", label = 'GoalPostManager');
plt.bar(names, vecchio, width = 0.2, align='edge', color="r", label = 'BasikStriker');
plt.axhline(y = TIMEOUT, color = 'grey', linestyle = '--', label = 'Timeout')
plt.ylabel("Tempo per segnare [m]");
plt.xlabel("Configurazioni");

plt.legend(loc = 'upper right');


text = "Differenza media = " + str(Mean) + "\nVarianza = " + str(Variance)
fig, ax = plt.subplots()
plt.title("Variazione nelle prestazioni - Palla esterna, molto vicina ai pali")
ax.bar(names, Diff, color="g", label = 'Variazione di prestazione');
at = AnchoredText(
    text, prop=dict(size=15), frameon=True, loc='upper left')
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")

ax.add_artist(at)


plt.ylabel("Variazione temporale [m]");
plt.xlabel("Configurazioni");

	
plt.legend();
	
plt.show();
	

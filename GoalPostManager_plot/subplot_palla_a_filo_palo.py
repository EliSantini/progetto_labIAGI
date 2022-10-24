import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import numpy as np
import matplotlib.patches as mpatches

INFINITE = 5.00

plt.title("GoalPostManagerPlot - Palla a filo palo")

Config3 = [17,18,19,20,21,22,23,24];
	##C1 = portiere al centro, palla esterna sx sulla linea di fondo	C2 = portiere al centro, palla esterna sx	C3 = portiere a sx, palla esterna sx	C4 = portiere a sx, palla esterna sx sulla linea di fondo	C5-C8 = C1-C4 a dx	C5-C8 la butta fuori	C7 rimane attaccato a palo
	##C9 = portiere al centro, palla fuori dal palo	C10 = portiere al centro, palla subito fuori dal palo	C10 rimane attaccato a palo	C11 = portiere a sx, palla subito fuori dal palo	C12 = portiere a sx, palla fuori dal palo	C13-C16 = C9-C12 a dx	C14 butta fuori
	##C17 = portiere al centro, palla a filo palo più vicino	C18 = portiere al centro, palla a filo palo	C19 = portiere a sx, palla a filo palo più vicino	C20 = portiere a sx, palla a filo palo	C21-C24 = C17-C20 a dx
timesMe = [0.99, 0.99, 0.98, 0.98, 0.99, 0.95, 1.0, 0.97];
	##timesOld = [1.63, 1.64, 1.67, 1.60, INFINITE, 1.55, INFINITE, INFINITE,
	##	    INFINITE, 2.70, 2.75, 1.51, 2.55, INFINITE, INFINITE, 2.51,
	##	    1.5, 2.0, 1.82, 1.01, 1.48, 1.46, 1.96, 0.98
	##	    ];
	

timesOld3 = [1.50, 2.00, 1.82, 1.01, 1.48, 1.46, 1.96, 0.98]
Diff = np.subtract(timesOld3, timesMe)
Mean = Diff.sum()/8
Mean = round(Mean, 3)
Variance = 0
for i in range(8):
	Variance += (Diff[i] - Mean)*(Diff[i] - Mean)
Variace = Variance/8
Variace = round(Variace, 3)
names = ['C17\nPalla vicino palo sx,\nPortiere al centro', 'C18\nPalla filo palo sx,\nPortiere al centro', 'C19\nPalla vicino palo sx,\nPortiere a sx', 'C20\nPalla filo palo sx,\nPortiere a sx', 'C21\nPalla vicino palo dx,\nPortiere al centro', 'C22\nPalla filo palo dx,\nPortiere al centro', 'C23\nPalla vicino palo dx,\nPortiere a dx', 'C24\nPalla filo palo dx,\nPortiere a dx']
plt.bar(names, timesMe, width = -0.2, align='edge', color="b", label = 'GoalPostManager')
plt.bar(names, timesOld3, width = 0.2, align='edge', color="r", label = 'BasikStriker')


plt.ylabel("Tempo per segnare [m]")
plt.xlabel("Configurazioni")
plt.legend()
text = "Differenza media = " + str(Mean) + "\nVarianza = " + str(Variance)
fig, ax = plt.subplots()
plt.title("Variazione nelle prestazioni - Palla a filo palo")
#ax.plot(names, timesMe, "white");
ax.bar(names, Diff, color="g", label = 'Variazione di prestazione')

at = AnchoredText(
    text, prop=dict(size=15), frameon=True, loc='upper left')
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")

	##plt.xlim(0, 25);
ax.add_artist(at)
	
	##plt.xlim(0, 25);
plt.legend();
plt.ylabel("Variazione temporale [m]")
plt.xlabel("Configurazioni")	
plt.show();
	

import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
import numpy as np
import matplotlib.patches as mpatches

def draw_brace(ax, xspan, yy, text, c, off):

    xmin, xmax = xspan
    xspan = xmax - xmin
    ax_xmin, ax_xmax = ax.get_xlim()
    xax_span = ax_xmax - ax_xmin

    ymin, ymax = ax.get_ylim()
    yspan = ymax - ymin
    resolution = int(xspan/xax_span*100)*2+1 # guaranteed uneven
    beta = 300./xax_span # the higher this is, the smaller the radius

    x = np.linspace(xmin, xmax, resolution)
    x_half = x[:int(resolution/2)+1]
    y_half_brace = (1/(1.+np.exp(-beta*(x_half-x_half[0])))
                + 1/(1.+np.exp(-beta*(x_half-x_half[-1]))))
    y = np.concatenate((y_half_brace, y_half_brace[-2::-1]))
    y = yy + (.05*y - .01)*yspan # adjust vertical position

    ax.autoscale(False)
    ax.plot(x, -y, color=c, lw=1, clip_on=False)

    ax.text((xmax+xmin)/2., -yy-off, text, ha='center', va='bottom', color=c)


TIMEOUT = 5.00

n = 24;
plt.title("GoalPostManagerPlot");
##plt.figure(figsize=(9, 3))
Diff = np.zeros(shape=24)

Config1 = [1,2,3,4];
Config2 = [10,11,12,13];
Config3 = [16,17,18,19,20,21,22,23,24];
	##C1 = portiere al centro, palla esterna sx sulla linea di fondo	C2 = portiere al centro, palla esterna sx	C3 = portiere a sx, palla esterna sx	C4 = portiere a sx, palla esterna sx sulla linea di fondo	C5-C8 = C1-C4 a dx	C5-C8 la butta fuori	C7 rimane attaccato a palo
	##C9 = portiere al centro, palla fuori dal palo	C10 = portiere al centro, palla subito fuori dal palo	C10 rimane attaccato a palo	C11 = portiere a sx, palla subito fuori dal palo	C12 = portiere a sx, palla fuori dal palo	C13-C16 = C9-C12 a dx	C14 butta fuori
	##C17 = portiere al centro, palla a filo palo più vicino	C18 = portiere al centro, palla a filo palo	C19 = portiere a sx, palla a filo palo più vicino	C20 = portiere a sx, palla a filo palo	C21-C24 = C17-C20 a dx
timesMe = [1.63, 1.63, 1.58, 1.63, 1.60, 1.52, 1.52, 1.58,
		 1.49, 1.51, 1.48, 1.53, 1.44, 1.46, 1.52, 1.53,
		 0.99, 0.99, 0.98, 0.98, 0.99, 0.95, 1.0, 0.97
		 ];
vecchio = [1.63, 1.64, 1.67, 1.60, TIMEOUT, 1.55, TIMEOUT, TIMEOUT,
		 TIMEOUT, 2.70, 2.75, 1.51, 2.55, TIMEOUT, TIMEOUT, 2.51,
		 1.5, 2.0, 1.82, 1.01, 1.48, 1.46, 1.96, 0.98
		 ];
for i in range(24):
	#if vecchio[i] == TIMEOUT:
	#	Diff[i] = -timesMe[i] + TIMEOUT
	#else:
	Diff[i] = -timesMe[i] + vecchio[i]
Mean = Diff.sum()/24
Mean = round(Mean, 3)
Variance = 0
for i in range(24):
	Variance += (Diff[i] - Mean)*(Diff[i] - Mean)
Variace = Variance/24
Variace = round(Variace, 3)	
##timesOld = [1.63, 1.64, 1.67, 1.60];
##timesOld1 = 1.55;
##timesOld2 = [2.70, 2.75, 1.51, 2.55];
##timesOld3 = [2.51, 1.50, 2.00, 1.82, 1.01, 1.48, 1.46, 1.96, 0.98];
names = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10','C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24'];
plt.bar(names, timesMe, width = -0.2, align='edge', color="b", label = 'GoalPostManager');
plt.bar(names, vecchio, width = 0.2, align='edge', color="r", label = 'BasikStriker');
plt.axhline(y = TIMEOUT, color = 'grey', linestyle = '--', label = 'Timeout')
#plt.annotate("TIMEOUT",(4,TIMEOUT))
#, (6,TIMEOUT), (7,TIMEOUT), (8,TIMEOUT), (13,TIMEOUT), (14,TIMEOUT)
##plt.bar(names[:4], timesOld, "or-", label = 'BasikStriker');
##plt.bar(names[9:13], timesOld2, "or-");
##plt.bar(names[15:], timesOld3, "or-");
##plt.bar(names[5], timesOld1, "or");

##plt.axvline(x = 4, color = 'r', linestyle = '--')
##plt.axvline(x = 6, color = 'r', linestyle = '--')
##plt.axvline(x = 7, color = 'r', linestyle = '--')
##plt.axvline(x = 8, color = 'r', linestyle = '--')
##plt.axvline(x = 13, color = 'r', linestyle = '--')
##plt.axvline(x = 14, color = 'r', linestyle = '--')
ax = plt.gca()
draw_brace(ax, (0, 7), 0.2, 'Palla esterna', 'orange', 0.5)
draw_brace(ax, (8, 15), 0.2, 'Palla dietro palo', 'cyan', 0.5)
draw_brace(ax, (16, 23), 0.2, 'Palla a filo palo', 'magenta', 0.5)
plt.legend();
##plt.annotate('Palla esterna alla porta', xy=(0, 7), xytext=(0, 7), xycoords='data', 
##            ha='center', va='top',
##            bbox=dict(boxstyle='square', fc='white'),
##            arrowprops=dict(arrowstyle='-[, widthB=9.0, lengthB=2.5', lw=2.0))
	##plt.plot(Config, timesMe, "k", Config, timesMe, "o", Config, timesOld, "b", Config, timesOld, "o");
	##plt.plot(names, timesMe, "k", names, timesMe, "o", names, timesOld, "b", names, timesOld, "o");
	
##plt.named_plot("GoalPostManager", Config, timesMe);
	##plt.named_plot("BasicStriker", Config, timesOld);


##ax.plot(range(25))



	
plt.ylabel("Tempo per segnare [m]");
plt.xlabel("Configurazioni");


text = "Differenza media = " + str(Mean) + "\nVarianza = " + str(Variance)
fig, ax = plt.subplots()
plt.title("Variazione nelle prestazioni")
##ax.plot(names, timesMe, "white");
##ax.plot(names[:4], Diff[:4], "og-", label = 'Differenza');
##ax.axvline(x = 4, color = 'g', linestyle = '--')
##ax.plot(names[5], Diff[5], "og");
##ax.axvline(x = 6, color = 'g', linestyle = '--')
##ax.axvline(x = 7, color = 'g', linestyle = '--')
##ax.axvline(x = 8, color = 'g', linestyle = '--')
##ax.plot(names[9:13], Diff[9:13], "og-");
##ax.axvline(x = 13, color = 'g', linestyle = '--')
##ax.axvline(x = 14, color = 'g', linestyle = '--')
##ax.plot(names[15:], Diff[15:], "og-");
ax.bar(names, Diff, color="g", label = 'Variazione di prestazione');

at = AnchoredText(
    text, prop=dict(size=15), frameon=True, loc='upper left')
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")

	##plt.xlim(0, 25);
ax.add_artist(at)
draw_brace(ax, (0, 7), 0.3, 'Palla esterna', 'orange', 0.4)
draw_brace(ax, (8, 15), 0.3, 'Palla dietro palo', 'cyan', 0.4)
draw_brace(ax, (16, 23), 0.3, 'Palla a filo palo', 'magenta', 0.4)
##red_patch = mpatches.Patch(color='white', label=text)
##plt.legend(handles=[red_patch]);
plt.legend();
plt.ylabel("Tempo per segnare [m]");
plt.xlabel("Configurazioni");	
plt.show();
	

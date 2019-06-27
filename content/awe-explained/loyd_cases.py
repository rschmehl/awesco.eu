# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 07:09:55 2016

@author: rschmehl
"""
from pylab import np, plot, legend
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import newton
mpl.rcParams['font.family'] = "Open Sans"
mpl.rcParams.update({'font.size': 14})
mpl.rc('xtick', labelsize=14) 
mpl.rc('ytick', labelsize=14)
mpl.rc('axes', titlesize=14)
mpl.rcParams['svg.fonttype'] = 'none'

# disable outline paths for inkscape > PDF+Latex 
# important: comment out all other local font settings
#mpl.rcParams['svg.fonttype'] = 'none'

# crosswind kite
def zetac(CL, G, f):
#   return CL*G**2*f*(1-f)**2 # was wrong
    return CL*f*(1-f)**2*(1+G**2)/G*np.sqrt(1+G**2)

def zcopt(CL, G):
#   return 4./27.*CL*G**2
    return 4./27.*CL*(1+G**2)/G*np.sqrt(1+G**2)
    
def fcopt(CL, G):
    return 1./3.

# regular kite
def zetar(CL, G, f):
#    return CL*f*(np.sqrt(1+G**2*(1-f)**2)-f)**2/np.sqrt(1+G**2) # was wrong
    return CL*f*(np.sqrt(1+G**2*(1-f**2))-f)**2/(G*np.sqrt(1+G**2))
    
def dzrdf(f, CL, G):
    r= np.sqrt(1+G**2*(1-f**2))
#   return CL*(f-r)*(2*f*(G**2*(1-f)+r)+(f-r)*r)/(np.sqrt(G**2+1)*r) # this is still wrong!
    return CL/(G*np.sqrt(1+G**2))*(r-f)*(r-3*f-2*G**2*f**2/r)
    
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

axes[0].set_xlabel('reeling factor $f\, [-]$')
axes[0].set_ylabel('power harvesting factor $\zeta\, [-]$')
axes[0].set_title('regular kite')
axes[0].set_ylim(0, 0.4)
axes[0].set_xlim(0, 1)
axes[1].set_xlabel('reeling factor $f\, [-]$')
axes[1].set_ylabel('power harvesting factor $\zeta\, [-]$')
axes[1].set_title('crosswind kite')
axes[1].set_ylim(0, 140)
axes[1].set_xlim(0, 1)

f  = np.linspace(0,1,100)
CL = 1

G  = 5
axes[0].plot(f, zetar(CL, G, f), 'r')
axes[1].plot(f, zetac(CL, G, f), 'r')
#axes[2].plot(f, dzrdf(f, CL, G), 'r')
G  = 10
axes[0].plot(f, zetar(CL, G, f), 'r')
axes[1].plot(f, zetac(CL, G, f), 'r')
#axes[2].plot(f, dzrdf(f, CL, G), 'r')
G  = 15
axes[0].plot(f, zetar(CL, G, f), 'r')
axes[1].plot(f, zetac(CL, G, f), 'r')
#axes[2].plot(f, dzrdf(f, CL, G), 'r')
G  = 20
axes[0].plot(f, zetar(CL, G, f), 'r')
axes[1].plot(f, zetac(CL, G, f), 'r')
#axes[2].plot(f, dzrdf(f, CL, G), 'r')
G  = 25
#axes[0].plot(f, zetar(CL, G, f), 'r')
#axes[1].plot(f, zetac(CL, G, f), 'r')
#axes[2].plot(f, dzrdf(f, CL, G), 'r')
G  = 30
axes[0].plot(f, zetar(CL, G, f), 'r')
axes[1].plot(f, zetac(CL, G, f), 'r')
#axes[2].plot(f, dzrdf(f, CL, G), 'r')

G  = 100000
axes[0].plot(f, zetar(CL, G, f), 'r', linestyle="--")

# numerical calculation of optimum for regular kite
Gr   = np.arange(1, 30.1, 0.1)
n = Gr.shape[0]
fopt = [None]*n
zopt = [None]*n
ffopt = [1./3.]*n
zzopt = [None]*n
f0 = 0.5
i  = 0
for G in Gr:
    fopt[i] = newton(dzrdf, f0, args=(CL,G))
#    fopt[i] = 0
    zopt[i] = zetar(CL, G, fopt[i]) 
    zzopt[i] = zcopt(CL, G) 
    #axes[0].plot(fopt, zopt, 'o', color="#80C0FF", markersize=2) 
    print(i, G, fopt[i], zopt[i])
    i += 1
axes[0].plot(fopt,  zopt,  'b', linestyle=":")
axes[1].plot(ffopt, zzopt, 'b', linestyle=":")
#axes[1].plot([1./3.,1./3.], [0.,140.], color='b', linestyle='dotted')

# numerical calculation of optimum for regular kite
Gr   = [40, 50, 60, 70, 80, 90, 100, 1000, 10000, 100000]
n = 10
fopt = [None]*n
zopt = [None]*n
zzopt = [None]*n
i  = 0
for G in Gr:
    fopt[i] = newton(dzrdf, f0, args=(CL,G))
    zopt[i] = zetar(CL, G, fopt[i])
    print(i, G, fopt[i], zopt[i])
    i += 1
axes[0].plot(fopt,  zopt,  'b', linestyle=":")    
    
#G = 5
#axes[1].plot(fcopt(CL, G),zcopt(CL, G),'o',color="#80C0FF", label="optimal")

plt.tight_layout()

plt.savefig("loyd_cases.svg")
plt.show() # show the plot
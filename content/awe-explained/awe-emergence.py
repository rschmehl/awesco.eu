# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 07:09:55 2016

@author: rschmehl
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import np
mpl.rcParams['font.family'] = "Open Sans"
mpl.rcParams.update({'font.size': 18})
mpl.rcParams['figure.figsize'] = 21, 9
mpl.rc('xtick', labelsize=22) 
mpl.rc('ytick', labelsize=22)
mpl.rc('axes', titlesize=22)
mpl.rcParams['pdf.fonttype'] = 42 # Output Type 3 (Type3) or Type 42 (TrueType)

# disable outline paths for inkscape > PDF+Latex 
# important: comment out all other local font settings
#mpl.rcParams['svg.fonttype'] = 'none'

nyears = 19
minyear = 2000
ind = np.arange(nyears)
width = 0.8

n = ( 3, 4, 5, 6, 8, 9, 12, 13, 18, 28, 38, 40, 46, 50, 52, 55, 58, 60, 63 )

fig, ax = plt.subplots()

# some layout advice from http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.tick_params(axis='x', which='both',length=0)
ax.get_yaxis().tick_left()

ax.bar(ind, n, width, color='#9bdcef', linewidth=0, zorder=3)
ax.yaxis.grid(zorder=0) 

ax.set_ylim(0, 70)
ax.set_xlim(-0.4, nyears)
ax.set_xticks(ind)
ax.set_xticklabels([str(minyear+i) for i in ind])

#ax.set_xlabel('years' )
#ax.set_ylabel('number of institutions')
ax.set_title('number of institutions involved in AWE', pad=20)

plt.tight_layout()

plt.savefig("awe-emergence.svg")
plt.show()

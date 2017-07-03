# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:17:49 2016

@author: Erbil ŞİLİk
"""


import itertools
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 

marker = ["o", "s", "p", "*", "h", "+", "<"]

g = itertools.cycle(marker)

# loop over all files in the current directory ending with .txt
for fname in glob("*.txt"):
    # read file, skip header (1 line) and unpack into 3 variables
    WL, ABS, T = np.genfromtxt(fname, skip_header=1, unpack=True)
    plt.plot(WL, T, label=fname[0:3], marker = g.__next__(), markevery=30)

plt.xlabel('Wavelength (nm)')
plt.xlim(300,1000)
plt.ylim(0,100)
plt.ylabel('Transmittance, T%')

plt.legend(loc=4)


params = {'legend.fontsize': 14,
          'axes.labelsize': 16,
          'axes.titlesize': 14,
          'xtick.labelsize' :16,
          'ytick.labelsize': 16,
          'mathtext.fontset': 'cm',
          'mathtext.rm': 'serif',
          'grid.color': 'grey',
          'grid.linestyle': '-',
          'grid.linewidth': 0.5,
         }
matplotlib.rcParams.update(params)



plt.tight_layout()
plt.grid(True)
#plt.legend(loc='lower center')
plt.savefig('Transmittance.tiff', dpi=600)


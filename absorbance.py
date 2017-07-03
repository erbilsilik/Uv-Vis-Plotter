# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 00:20:41 2016

@author: erbil
"""

import itertools
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

marker = ["o", "s", "p", "*", "h", "+", "<"]
g = itertools.cycle(marker)

# loop over all files in the current directory ending with .txt
for fname in glob("*.txt"):
    # read file, skip header (1 line) and unpack into 3 variables
    WL, ABS, T = np.genfromtxt(fname, skip_header=1, unpack=True)
    plt.plot(WL, ABS, label=fname[0:3], marker = g.__next__(), markevery=30)


plt.xlabel('Wavelength (nm)')
plt.xlim(300,1000)
plt.ylim(0,2.5)
plt.ylabel('Absorbance (%)')
mpl.rcParams.update({'font.size': 12})
plt.legend(loc=1,prop={'size':10})
plt.grid(True)
#plt.legend(loc='lower center')
plt.savefig('Absorbance.tiff', dpi=600)
    


    

   
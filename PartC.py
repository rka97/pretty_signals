# -*- coding: utf-8 -*-
"""
Created on Thu May 17 01:32:30 2018

@author: rka97
"""

import numpy as np
from main import PlotFunction, partCFunction

xvalues3 = np.arange(-15.5, 15.5, 0.0001)
PlotFunction(xvalues3, partCFunction, "Part C (a) z(t)", "Part C\\")
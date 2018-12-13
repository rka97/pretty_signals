# -*- coding: utf-8 -*-
"""
Created on Thu May 17 01:30:34 2018

@author: rka97
"""

import numpy as np
from main import PlotFourFunctions, partBAFunction

xvalues = np.arange(-5.5, 5.5, 0.0001)
PlotFourFunctions(xvalues, partBAFunction, "PartB y(t)", "y(3t)", 
                  "y(t+2)", "y(4-2t)", "Part B\\")
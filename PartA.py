# -*- coding: utf-8 -*-
"""
Created on Thu May 17 01:26:00 2018

@author: rka97
"""

import numpy as np
from main import PlotFunction, rect, triangl, ustep, triangl2, partADFunction

# Part A
xvalues = np.arange(-5.5, 5.5, 0.0001)
PlotFunction(xvalues, rect, "Rect Function", "Part A\\")
PlotFunction(xvalues, triangl, "Triangle Function", "Part A\\")
PlotFunction(xvalues, ustep, "Unit Step Function", "Part A\\")
PlotFunction(xvalues, triangl2, "Part A (c) x(t)", "Part A\\")
xvalues2 = np.arange(-4.5, 3.5, 0.0001)
PlotFunction(xvalues2, partADFunction, "Part A (d) x(t)", "Part A\\")
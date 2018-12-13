# -*- coding: utf-8 -*-
"""
Created on Thu May 17 01:33:12 2018

@author: rka97
"""

import numpy as np
from main import PlotFunction, KFourierSeriesCoefficient, partDFunction, PlotArray

xvalues = np.arange(-5.5, 5.5, 0.0001)
num_coefficients = 25
PlotFunction(xvalues, partDFunction, "Part D h(t)", "Part D\\")
FSCoefficients = np.arange(-1*num_coefficients, num_coefficients, 1, dtype=complex)
for i in range(-1*num_coefficients, num_coefficients, 1):
    FSCoefficients[i] = KFourierSeriesCoefficient(i, 6, partDFunction, 0.01)
PlotArray(np.arange(-1*num_coefficients, num_coefficients, 1), np.absolute(FSCoefficients), "FS Magnitudes", "Part D\\")
PlotArray(np.arange(-1*num_coefficients, num_coefficients, 1), np.angle(FSCoefficients), "FS Phases", "Part D\\")
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 01:35:10 2018

@author: rka97
"""

import numpy as np
from main import PlotFunction, partEFunction, partEFourierTransform, partEBFunction, partEBFourierTransform

xvalues = np.arange(-2.5, 2.5, 0.0001)
PlotFunction(xvalues, partEFunction, "Part E m(t)", "Part E\\")
PlotFunction(np.arange(-25, 25, 0.01), partEFourierTransform, "Part E FT", "Part E\\")
PlotFunction(xvalues, partEBFunction, "Part E r(t)", "Part E\\")
PlotFunction(np.arange(-150, 150, 0.01), partEBFourierTransform, "Part E (b) FT", "Part E\\")
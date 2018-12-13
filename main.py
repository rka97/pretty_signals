# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:49:03 2018

@author: rka97
"""

import matplotlib.pyplot as plt
import numpy as np

def rect(X):
    return (np.sign(X + 0.5) - np.sign(X - 0.5) > 0)

def triangl(X):
    return (1 - np.abs(X)) * (X >= -1) * (X < 1);

def ustep(X):
    return 1.0 * (X >= 0)

def triangl2(X):
    X = X / 3;
    return 2 * (1 - np.abs(X)) * (X >= -1) * (X < 1)

def partADFunction(X):
    X = X * (X >= -4) * (X <= 3)
    return np.exp(-3 * X) * np.sin(8.0 * np.pi * X / 5.0) * ustep(X + 2)

def partBAFunction(X):
    return np.exp(-np.abs(X)/5.0) * (ustep(X+1) - ustep(X-3))

def partCAFunction(X):
    return np.exp(- np.abs(X) / 3.0) * np.sin(4 * np.pi * X) * (ustep(X) - ustep(X-5))

def periodizeFunction(X, func, period, minimum, maximum):
    Y = np.zeros(X.shape)
    for i in range(minimum*period, maximum*period, period):
        Xi = X  - i
        Y += func(Xi)
    return Y

def partCFunction(X):
    return periodizeFunction(X, partCAFunction, 6, -4, 4)

def partDAFunction(X):
    return (1 - 2*abs(X)) * (abs(X) <= 0.5)

def partDFunction(X):
    return periodizeFunction(X, partDAFunction, 6, -3, 3)

def PlotFunction(X, func, label, dir = "/"):
    Y = func(X)
    plt.plot(X, Y)
    plt.ylabel(label)
    fig = plt.gcf()
    fig.set_size_inches(5, 5)
    fig.savefig(dir + label, dpi=100)
    plt.show()

def PlotArray(X, Y, label, dir = "/", discrete = True):
    if discrete:
        plt.stem(X, Y)
    else:
        plt.plot(X, Y)
    plt.ylabel(label)
    fig = plt.gcf()
    fig.set_size_inches(5, 5)
    fig.savefig(dir + label, dpi=100)
    plt.show()

def PlotFourFunctions(X, func, label1, label2, label3, label4, dir):
    Y0 = func(X)
    Y1 = func(3*X)
    Y2 = func(X+2)
    Y3 = func(4 - 2*X)
    _, axarr = plt.subplots(2,2)
    axarr[0, 0].plot(X, Y0)
    axarr[0, 0].set_title(label1)
    axarr[0, 1].plot(X, Y1)
    axarr[0, 1].set_title(label2)
    axarr[1, 0].plot(X, Y2)
    axarr[1, 0].set_title(label3)
    axarr[1, 1].plot(X, Y3)
    axarr[1, 1].set_title(label4)
    plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
    fig = plt.gcf()
    fig.set_size_inches(20, 20)
    fig.savefig(dir + label1, dpi=100)

def KFourierSeriesCoefficient(k, period, func, step):
    riemannSum = 0
    omega0 = np.pi * 2 / period
    i = 0.0;
    while i < period:
        riemannSum += func(np.array(i)) * np.exp(1j * k * omega0 * i) * step
        i += step
    riemannSum /= period
    return riemannSum
    
def partEFunction(X):
    return np.sin(5*np.pi*X)/(np.pi*X)

def partEFourierTransform(X):
    return (np.sign(5*np.pi-X) + np.sign(5*np.pi+X))/(2*np.sqrt(2*np.pi))

def partEBFunction(X):
    return partEFunction(X)*np.cos(30*np.pi*X)

def partEBFourierTransform(X):
    val = np.sign(35*np.pi-X) + np.sign(-25*np.pi+X) - np.sign(25*np.pi+X) + np.sign(35*np.pi + X)
    return val/(4 * np.sqrt(2*np.pi))
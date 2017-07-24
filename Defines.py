#coding=utf-8
import numpy as np
from scipy.special import comb

MaxFPS = 60
FrameClock = 1000 / MaxFPS

def Normalize(clock):
    return clock * MaxFPS / 1000.0

def print_bits(mask):
    rows, cols = mask.shape[:2]
    print (rows, cols)
    for r in range(rows):
        for c in range(cols):
            if mask[r,c]:
                print 1,
            else:
                print 0,
        print ""


def bezier(arr, t):
    n = len(arr)
    a = np.power(t, np.arange(n))
    b = np.power(1.0 - t, n - 1 - np.arange(n))
    r = a * b * comb(n - 1, np.arange(n)) 
    w = arr * r.reshape((n,1))
    return np.sum(w, 0)


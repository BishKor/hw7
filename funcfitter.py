__author__ = 'BisharaKorkor'

from math import sin, pow

def linearplussine(t, m, y0, amp, omega, phi):
    return y0 + m * t + amp * sin(omega * t + phi)

def fitter(ind, dep, m, y0, amp, omega, phi):

    if len(dep) != len(ind):
        print "dependent and independent arrays need to be of same length. will result in error"

    chisquared = 0

    for i in range(len(dep)):
        fe = linearplussine(ind[i], m, y0, amp, omega, phi)
        chisquared += pow(dep[i]-fe, 2)/fe

    return [chisquared, m, y0, amp, omega, phi]
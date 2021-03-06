#!/usr/bin/env python3

import numpy

''' this file contains coefficients of the class 2 - pcff potential for iPP 
    All these coefficents are simplified, as their initial as shown is 
    repeatitive '''
# Class 2 Bonding related coefficients
paircoef = numpy.array([[1, 0.054, 4.01],
                        [2, 0.02, 2.995]])

bondcoef = numpy.array([[1, 1.53, 299.67, -501.77, 679.81],
                        [2, 1.101, 345.0, -691.89, 844.60]])

# Class 2 Angle related coefficients 
anglecoef = numpy.array([[1, 112.67, 39.516, -7.443, -9.5583],
                         [2, 110.77, 41.453, -10.604, 5.1290],
                         [3, 107.66, 39.641, -12.921, -2.432]])    

bondbondcoef = numpy.array([[1, 0, 1.53, 1.53],
                            [2, 3.3872, 1.53, 1.101],
                            [3, 5.3316, 1.101, 1.101]])

bondanglecoef = numpy.array([[1, 8.016, 8.016, 1.53, 1.53],
                             [2, 20.754, 11.421, 1.53, 1.101],
                             [3, 18.103, 18.103, 1.101, 1.101]])

# Class 2 Proper Dihedral related coefficients
dihedralcoef = numpy.array([[1, 0, 0, 0.0514, 0, -0.143, 0],
                            [2, 0, 0, 0.0316, 0, -0.1681, 0],
                            [3, -0.1432, 0, 0.0617, 0, -0.1083, 0]])

angelangletorsioncoef = numpy.array([[1, -22.045, 112.67, 112.67],
                                     [2, -16.164, 112.67, 110.77],
                                     [3, -12.564, 110.77, 110.77]])

endbondtorsioncoef = numpy.array([[1, -0.0732, 0, 0, -0.0732, 0, 
                                      0, 1.53, 1.53],
                                  [2, 0.2486, 0.2422, -0.0925, 0.0814, 0.0591,
                                      0.2219, 1.53, 1.101],
                                  [3, 0.213, 0.312, 0.0777, 0.213, 0.312, 
                                      0.0777, 1.101, 1.101]])

middlebondtorsioncoef = numpy.array([[1, -17.787, -7.1877, 0, 1.53],
                                     [2, -14.879, -3.6581, -0.3138, 1.53],
                                     [3, -14.261, -0.5322, -0.4864, 1.53]])

bondbond13 = numpy.array([[1, 0, 1.53, 1.53],
                          [2, 0, 1.53, 1.101],
                          [3, 0, 1.101, 1.101]])

angletorsioncoef = numpy.array([[1, 0.3886, -0.3139, 0.1389, 0.3886, -0.3139, 
                                    0.1389, 112.67, 112.67],
                                [2, -0.2454, 0, -0.1136, 0.3113, 0.4516, 
                                    -0.1988, 112.67, 110.77],
                                [3, -0.8085, 0.5569, -0.2466, -0.8085, 0.5569, 
                                    -0.2466, 110.77, 110.77]])
                                
# Class 2 Improper Dihedral related coefficients
impropercoef = numpy.array([[1, 0, 0],
                            [2, 0, 0],
                            [3, 0, 0],
                            [4, 0, 0],
                            [5, 0, 0],
                            [6, 0, 0],
                            [7, 0, 0]])

angleanglecoef = numpy.array([[1, -1.3199, -1.3199, 0.1184, 112.67, 110.77, 
                                   110.77],
                              [2, 0.2738, -0.4825, 0.2738, 110.77, 107.66,
                                  110.77],
                              [3, -0.3157, -0.3157, -0.3157, 107.66, 107.66, 
                                  107.66],
                              [4, 0.1184, -1.3199, -1.3199, 110.77, 110.77,
                                  112.67],
                              [5, 0.2738, 0.2738, -0.4825, 107.66, 110.77,
                                  110.77],
                              [6, -0.1729, -0.1729, -0.1729, 112.67, 112.67,
                                  112.67],
                              [7, -1.3199, 0.1184, -1.3199, 110.77, 112.67,
                                  110.77]])

'''
Here are the original, initial, class 2 coefficints 

# Angle related coefficients
bondanglecoef = numpy.array([[1, 8.016, 8.016, 1.53, 1.53],
                             [2, 20.754, 11.421, 1.53, 1.101],
                             [3, 20.754, 11.421, 1.53, 1.101],
                             [4, 18.103, 18.103, 1.101, 1.101],
                             [5, 20.754, 11.421, 1.53, 1.101],
                             [6, 18.103, 18.103, 1.101, 1.101],
                             [7, 8.016, 8.016, 1.53, 1.53],
                             [8, 11.421, 20.754, 1.101, 1.53],
                             [9, 8.016, 8.016, 1.53, 1.53],
                             [10, 20.754, 11.421, 1.53, 1.101],
                             [11, 20.754, 11.421, 1.53, 1.101],
                             [12, 8.016, 8.016, 1.53, 1.53],
                             [13, 11.421, 20.754, 1.101, 1.53],
                             [14, 8.016, 8.016, 1.53, 1.53],
                             [15, 8.016, 8.016, 1.53, 1.53]])

bondbondcoef = numpy.array([[1, 0, 1.53, 1.53],
                            [2, 3.3872, 1.53, 1.101],
                            [3, 3.3872, 1.53, 1.101],
                            [4, 5.3316, 1.101, 1.101],
                            [5, 3.3872, 1.53, 1.101],
                            [6, 5.3316, 1.101, 1.101],
                            [7, 0, 1.53, 1.53],
                            [8, 3.3872, 1.101, 1.53],
                            [9, 0, 1.53, 1.53],
                            [10, 3.3872, 1.53, 1.101],
                            [11, 3.3872, 1.53, 1.101],
                            [12, 0, 1.53, 1.53],
                            [13, 3.3872, 1.101, 1.53],
                            [14, 0, 1.53, 1.53],
                            [15, 0, 1.53, 1.53]])

# Proper Dihedral related coefficients
dihedralcoef = numpy.array([[1, 0, 0, 0.0316, 0, -0.1681, 0],
                            [2, -0.1432, 0, 0.0617, 0, -0.1083, 0],
                            [3, 0, 0, 0.0316, 0, -0.1681, 0],
                            [4, 0, 0, 0.0514, 0, -0.143, 0],
                            [5, -0.1432, 0, 0.0617, 0, -0.1083, 0],
                            [6, 0, 0, 0.0316, 0, -0.1681, 0],
                            [7, 0, 0, 0.0514, 0, -0.143, 0],
                            [8, 0, 0, 0.0514, 0, -0.143, 0],
                            [9, 0, 0, 0.0316, 0, -0.1681, 0],
                            [10, 0, 0, 0.0316, 0, -0.1681, 0],
                            [11, 0, 0, 0.0316, 0, -0.1681, 0],
                            [12, -0.1432, 0, 0.0617, 0, -0.1083, 0],
                            [13, 0, 0, 0.0316, 0, -0.1681, 0],
                            [14, -0.1432, 0, 0.0617, 0, -0.1083, 0],
                            [15, 0, 0, 0.0514, 0, -0.143, 0],
                            [16, 0, 0, 0.0316, 0, -0.1681, 0],
                            [17, 0, 0, 0.0514, 0, -0.143, 0],
                            [18, 0, 0, 0.0316, 0, -0.1681, 0]])

angelangletorsioncoef = numpy.array([[1, -16.164, 112.67, 110.77],
                                     [2, -12.564, 110.77, 110.77],
                                     [3, -16.164, 112.67, 110.77],
                                     [4, -22.045, 112.67, 112.67],
                                     [5, -12.564, 110.77, 110.77],
                                     [6, -16.164, 110.77, 112.67],
                                     [7, -22.045, 112.67, 112.67],
                                     [8, -22.045, 112.67, 112.67],
                                     [9, -16.164, 112.67, 110.77],
                                     [10, -16.164, 110.77, 112.67],
                                     [11, -16.164, 110.77, 112.67],
                                     [12, -12.564, 110.77, 110.77],
                                     [13, -16.164, 110.77, 112.67],
                                     [14, -12.564, 110.77, 110.77],
                                     [15, -22.045, 112.67, 112.67],
                                     [16, -16.164, 112.67, 110.77],
                                     [17, -22.045, 112.67, 112.67],
                                     [18, -16.164, 110.77, 112.67]])

endbondtorsioncoef = numpy.array([[1, 0.2486, 0.2422, -0.0925, 0.0814, 0.0591, 
                                      0.2219, 1.53, 1.101],
                                  [2, 0.213, 0.312, 0.0777, 0.213, 0.312, 
                                      0.0777, 1.101, 1.101],
                                  [3, 0.2486, 0.2422, -0.0925, 0.0814, 0.0591,
                                      0.2219, 1.53, 1.101],
                                  [4, -0.0732, 0, 0, -0.0732, 0, 
                                      0, 1.53, 1.53],
                                  [5, 0.213, 0.312, 0.0777, 0.213, 0.312,
                                      0.0777, 1.101, 1.101],
                                  [6, 0.0814, 0.0591, 0.2219, 0.2486, 0.2422,
                                      -0.0925, 1.101, 1.53],
                                  [7, -0.0732, 0, 0, -0.0732, 0,
                                      0, 1.53, 1.53],
                                  [8, -0.0732, 0, 0, -0.0732, 0,
                                      0, 1.53, 1.53],
                                  [9, 0.2486, 0.2422, -0.0925, 0.0814, 0.0591,
                                      0.2219, 1.53, 1.101],
                                  [10, 0.0814, 0.0591, 0.2219, 0.2486, 0.2422,
                                      -0.0925, 1.101, 1.53],
                                  [11, 0.0814, 0.0591, 0.2219, 0.2486, 0.2422,
                                       -0.0925, 1.101, 1.53],
                                  [12, 0.213, 0.312, 0.0777, 0.213, 0.312,
                                       0.0777, 1.101, 1.101],
                                  [13, 0.0814, 0.0591, 0.2219, 0.2486, 0.2422,
                                       -0.0925, 1.101, 1.53],
                                  [14, 0.213, 0.312, 0.0777, 0.213, 0.312,
                                       0.0777, 1.101, 1.101],
                                  [15, -0.0732, 0, 0, -0.0732, 0,
                                       0, 1.53, 1.53],
                                  [16, 0.2486, 0.2422, -0.0925, 0.0814, 0.0591,
                                       0.2219, 1.53, 1.101],
                                  [17, -0.0732, 0, 0, -0.0732, 0,
                                       0, 1.53, 1.53],
                                  [18, 0.0814, 0.0591, 0.2219, 0.2486, 0.2422,
                                       -0.0925, 1.101, 1.53]])

middlebondtorsioncoef = numpy.array([[1, -14.879, -3.6581, -0.3138, 1.53],
                                     [2, -14.261, -0.5322, -0.4864, 1.53],
                                     [3, -14.879, -3.6581, -0.3138, 1.53],
                                     [4, -17.787, -7.1877, 0, 1.53],
                                     [5, -14.261, -0.5322, -0.4864, 1.53],
                                     [6, -14.879, -3.6581, -0.3138, 1.53],
                                     [7, -17.787, -7.1877, 0, 1.53],
                                     [8, -17.787, -7.1877, 0, 1.53],
                                     [9, -14.879, -3.6581, -0.3138, 1.53],
                                     [10, -14.879, -3.6581, -0.3138, 1.53],
                                     [11, -14.879, -3.6581, -0.3138, 1.53],
                                     [12, -14.261, -0.5322, -0.4864, 1.53],
                                     [13, -14.879, -3.6581, -0.3138, 1.53],
                                     [14, -14.261, -0.5322, -0.4864, 1.53],
                                     [15, -17.787, -7.1877, 0, 1.53],
                                     [16, -14.879, -3.6581, -0.3138, 1.53],
                                     [17, -17.787, -7.1877, 0, 1.53],
                                     [18, -14.879, -3.6581, -0.3138, 1.53]])

bondbond13 = numpy.array([[1, 0, 1.53, 1.101],
                          [2, 0, 1.101, 1.101],
                          [3, 0, 1.53, 1.101],
                          [4, 0, 1.53, 1.53],
                          [5, 0, 1.101, 1.101],
                          [6, 0, 1.101, 1.53],
                          [7, 0, 1.53, 1.53],
                          [8, 0, 1.53, 1.53],
                          [9, 0, 1.53, 1.101],
                          [10, 0, 1.101, 1.53],
                          [11, 0, 1.101, 1.53],
                          [12, 0, 1.101, 1.101],
                          [13, 0, 1.101, 1.53],
                          [14, 0, 1.101, 1.101],
                          [15, 0, 1.53, 1.53],
                          [16, 0, 1.53, 1.101],
                          [17, 0, 1.53, 1.53],
                          [18, 0, 1.101, 1.53]])

angletorsioncoef = numpy.array([[1, -0.2454, 0, -0.1136, 0.3113, 0.4516,
                                    -0.1988, 112.67, 110.77],
                                [2, -0.8085, 0.5569, -0.2466, -0.8085, 0.5569,
                                    -0.2466, 110.77, 110.77],
                                [3, -0.2454, 0, -0.1136, 0.3113, 0.4516,
                                    -0.1988, 112.67, 110.77],
                                [4, 0.3886, -0.3139, 0.1389, 0.3886, -0.3139,
                                    0.1389, 112.67, 112.67],
                                [5, -0.8085, 0.5569, -0.2466, -0.8085, 0.5569,
                                    -0.2466, 110.77, 110.77],
                                [6, 0.3113, 0.4516, -0.1988, -0.2454, 0,
                                    -0.1136, 110.77, 112.67],
                                [7, 0.3886, -0.3139, 0.1389, 0.3886, -0.3139,
                                    0.1389, 112.67, 112.67],
                                [8, 0.3886, -0.3139, 0.1389, 0.3886, -0.3139,
                                    0.1389, 112.67, 112.67],
                                [9, -0.2454, 0, -0.1136, 0.3113, 0.4516,
                                    -0.1988, 112.67, 110.77],
                                [10, 0.3113, 0.4516, -0.1988, -0.2454, 0, 
                                     -0.1136, 110.77, 112.67],
                                [11, 0.3113, 0.4516, -0.1988, -0.2454, 0,
                                     -0.1136, 110.77, 112.67],
                                [12, -0.8085, 0.5569, -0.2466, -0.8085, 0.5569,
                                     -0.2466, 110.77, 110.77],
                                [13, 0.3113, 0.4516, -0.1988, -0.2454, 0,
                                     -0.1136, 110.77, 112.67],
                                [14, -0.8085, 0.5569, -0.2466, -0.8085, 0.5569,
                                     -0.2466, 110.77, 110.77],
                                [15, 0.3886, -0.3139, 0.1389, 0.3886, -0.3139,
                                     0.1389, 112.67, 112.67],
                                [16, -0.2454, 0, -0.1136, 0.3113, 0.4516,
                                     -0.1988, 112.67, 110.77],
                                [17, 0.3886, -0.3139, 0.1389, 0.3886, -0.3139,
                                     0.1389, 112.67, 112.67],
                                [18, 0.3113, 0.4516, -0.1988, -0.2454, 0,
                                     -0.1136, 110.77, 112.67]])

# Imporoper Dihedral related coefficients
impropercoef = numpy.array([[1, 0, 0],
                            [2, 0, 0],
                            [3, 0, 0],
                            [4, 0, 0],
                            [5, 0, 0],
                            [6, 0, 0],
                            [7, 0, 0],
                            [8, 0, 0],
                            [9, 0, 0],
                            [10, 0, 0],
                            [11, 0, 0],
                            [12, 0, 0],
                            [13, 0, 0],
                            [14, 0, 0]])

angleanglecoef = numpy.array([[1, -1.3199, -1.3199, 0.1184, 112.67, 110.77,
                                  110.77],
                              [2, 0.2738, -0.4825, 0.2738, 110.77, 107.66,
                                  110.77],
                              [3, 0.2738, -0.4825, 0.2738, 110.77, 107.66,
                                  110.77],
                              [4, 0.2738, -0.4825, 0.2738, 110.77, 107.66,
                                  110.77],
                              [5, -0.3157, -0.3157, -0.3157, 107.66, 107.66,
                                  107.66],
                              [6, 0.1184, -1.3199, -1.3199, 110.77, 110.77,
                                  112.67],
                              [7, 0.2738, 0.2738, -0.4825, 107.66, 110.77,
                                  110.77],
                              [8, -1.3199, -1.3199, 0.1184, 112.67, 110.77,
                                  110.77],
                              [9, -0.1729, -0.1729, -0.1729, 112.67, 112.67,
                                  112.67],
                              [10, -1.3199, -1.3199, 0.1184, 112.67, 110.77,
                                   110.77],
                              [11, 0.2738, 0.2738, -0.4825, 107.66, 110.77,
                                   110.77],
                              [12, -1.3199, 0.1184, -1.3199, 110.77, 112.67,
                                   110.77],
                              [13, -1.3199, -1.3199, 0.1184, 112.67, 110.77,
                                   110.77],
                              [14, -0.1729, -0.1729, -0.1729, 112.67, 112.67,
                                   112.67]])

'''
# Bond related coefficients
# Pair Coeffs # lj/class2/coul/long
def pair_coeffs(f):
    ''' This function write the pair coefficients in the output file '''
    for i in range(len(paircoef)):
        for j in range(len(paircoef[i])):
            if j == 0:
                f.write(str(int(paircoef[i,j]))+' ')
            else:
                f.write(str(paircoef[i,j])+' ')
        f.write('\n')

# Bond Coeffs # class2
def bond_coeffs(f):
    ''' This function write the bond coefficients in the output file '''
    for i in range(len(bondcoef)):
        for j in range(len(bondcoef[i])):
            if j == 0:
                f.write(str(int(bondcoef[i,j]))+' ')
            else:
                f.write(str(bondcoef[i,j])+' ')
        f.write('\n')

# Angle related coefficients
# Angle Coeffs # class2
def angle_coeffs(f):
    ''' This function write the angle coefficients in the output file '''
    for i in range(len(anglecoef)):
        for j in range(len(anglecoef[i])):
            if j == 0:
                f.write(str(int(anglecoef[i,j]))+' ')
            else:
                f.write(str(anglecoef[i,j])+' ')
        f.write('\n')

# BondBond Coeffs
def bond_bond_coeffs(f):
    ''' This function write the bond bond coefficients in the output file '''
    for i in range(len(anglecoef)):
        for j in range(len(bondbondcoef[i])):
            if j == 0:
                f.write(str(int(bondbondcoef[i,j]))+' ')
            else:
                f.write(str(bondbondcoef[i,j])+' ')
        f.write('\n')
        
# BondAngle Coeffs
def bond_angle_coeffs(f):
    ''' This function write the bond angle coefficients in the output file '''
    for i in range(len(anglecoef)):
        for j in range(len(bondanglecoef[i])):
            if j == 0:
                f.write(str(int(bondanglecoef[i,j]))+' ')
            else:
                f.write(str(bondanglecoef[i,j])+' ')
        f.write('\n')

# Proper Dihedral coefficients 
# Dihedral Coeffs # class2
def dihedral_coeffs(f):
    ''' This function write the dihedral coefficients in the output file '''
    for i in range(len(dihedralcoef)):
        for j in range(len(dihedralcoef[i])):
            if j == 0:
                f.write(str(int(dihedralcoef[i,j]))+' ')
            else:
                f.write(str(dihedralcoef[i,j])+' ')
        f.write('\n')
   
# AngleAngleTorsion Coeffs
def angle_angle_torsion_coeffs(f):
    ''' This function write the angle angle torsion 
        coefficients in the output file '''
    for i in range(len(dihedralcoef)):
        for j in range(len(angelangletorsioncoef[i])):
            if j == 0:
                f.write(str(int(angelangletorsioncoef[i,j]))+' ')
            else:
                f.write(str(angelangletorsioncoef[i,j])+' ')
        f.write('\n')

# EndBondTorsion Coeffs
def end_bond_torsion_coeffs(f):
    ''' This function write the end bond torsion 
        coefficients in the output file '''
    for i in range(len(dihedralcoef)):
        for j in range(len(endbondtorsioncoef[i])):
            if j == 0:
                f.write(str(int(endbondtorsioncoef[i,j]))+' ')
            else:
                f.write(str(endbondtorsioncoef[i,j])+' ')
        f.write('\n')

# MiddleBondTorsion Coeffs
def middle_bond_torsion_coeffs(f):
    ''' This function write the middle bond torsion 
        coefficients in the output file '''
    for i in range(len(dihedralcoef)):
        for j in range(len(middlebondtorsioncoef[i])):
            if j == 0:
                f.write(str(int(middlebondtorsioncoef[i,j]))+' ')
            else:
                f.write(str(middlebondtorsioncoef[i,j])+' ')
        f.write('\n')

# BondBond13 Coeffs
def bond_bond13_coeffs(f):
    ''' This function write the bond bond 13 
        coefficients in the output file '''
    for i in range(len(dihedralcoef)):
        for j in range(len(bondbond13[i])):
            if j == 0:
                f.write(str(int(bondbond13[i,j]))+' ')
            else:
                f.write(str(bondbond13[i,j])+' ')
        f.write('\n')

# AngleTorsion Coeffs
def angle_torsion_coeffs(f):
    ''' This function write the angle torsion 
        coefficients in the output file '''
    for i in range(len(dihedralcoef)):
        for j in range(len(angletorsioncoef[i])):
            if j == 0:
                f.write(str(int(angletorsioncoef[i,j]))+' ')
            else:
                f.write(str(angletorsioncoef[i,j])+' ')
        f.write('\n')

# Improper Dihedral coefficients
# Improper Coeffs # class2
def improper_coeffs(f):
    ''' This function write the improper 
        coefficients in the output file '''
    for i in range(len(impropercoef)):
        for j in range(len(impropercoef[i])):
            if j == 0:
                f.write(str(int(impropercoef[i,j]))+' ')
            else:
                f.write(str(impropercoef[i,j])+' ')
        f.write('\n')
    
# AngleAngle Coeffs
def angle_angle_coeffs(f):
    ''' This function write the angle angle 
        coefficients in the output file '''
    for i in range(len(impropercoef)):
        for j in range(len(angleanglecoef[i])):
            if j == 0:
                f.write(str(int(angleanglecoef[i,j]))+' ')
            else:
                f.write(str(angleanglecoef[i,j])+' ')
        f.write('\n')



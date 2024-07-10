# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:46:06 2024

@author: PiazzeseC
"""

import math

# Input for the weight
weight = input('Please enter your weight in Kg ')

# Input for the height
height = input('Please enter your height in m ')


#Calculate BMI
BMI = round(float(weight)/(float(height)*float(height)), 1)

print(f'Your BMI is {BMI}')
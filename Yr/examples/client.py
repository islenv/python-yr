#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from libyr import Yr

temp = Yr('Hamar', 'en').get_temperature()
temp2 = Yr('Porsgrunn', 'nb').get_temperature()
temp3 = Yr('Oslo', 'nn').get_temperature()

print("The temperature in Hamar is %s %s") % (temp['value'], temp['unit'])

# -*- coding: utf-8 -*-
"""title_sinegraph.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10c7txWVtL7eaF4GdIKSuc4Q-m1yG_dvo

##09-04

###sine graph
"""

import pylab as py

x_deg = py.arange(-180, 180 +1)
x_rad = py.deg2rad(x_deg)  #도를 라디안으로 변환, deg to rad
y = py.sin(x_rad)

py.plot(x_deg, y)

py.xlabel('x(deg)')
py.ylabel('sin(x)')
py.grid(True)


from math import atan, sqrt, asin, cos, sin

x,y=2,8
x1,y1=4,10
x0,y0=3,5
r=2.5

k=(y1-y)/(x1-x)
betta=atan(k)

BC=sqrt((x1-x0)**2+(y1-y0)**2)
AC=r
AB=sqrt(BC**2-AC**2)

gamma=asin(AB/BC)

alpha=180-betta-gamma

x=x0+r*cos(alpha)
y=y0+r*sin(alpha)

import time
from tk_drawer import *

tk = TkDrawer()
tk.clean()
from r2point import R2Point

O=R2Point(x0, y0)
B=R2Point()

tk.draw_line(R2Point(), R2Point())



time.sleep(5)

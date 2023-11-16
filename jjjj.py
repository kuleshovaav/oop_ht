#!/usr/bin/env -S python3 -B
from tk_drawer_kanatovo1 import TkDrawer
from points1 import Point
import time
from math import sqrt

class Competition:
    def __init__(self, px, py, qx, qy, radius):
        self.px=
        self.py=
        self.qx=
        self.qy=

        
        
        
        self.p = Point(px, py)
        self.q = Point(qx, qy)
        self.radius = radius
        self.o = Point(0,0)
        
        self.tk = TkDrawer()
        self.tk.clean()
        self.tk.draw_circle(self.o, radius, "grey80")
        self.tk.draw_point(self.p, "red")
        self.tk.draw_point(self.q, "green")
 
    def draw_path(self):

        k=(self.py-self.qy)/(self.px-self.qx)
        b=self.py-k*self.px
        b1=k*self.px-self.px/k+b
        x=(b1-b)/(k-1/k)
        y=k*x+b

        if sqrt(x**2+y**2)>self.radius:
            print('gntyn')



        self.tk.draw_line(self.p, self.q, "navy")

for _ in range(int(input())):
    ls = map(int, input().split())
    c = Competition(*ls)


    
    c.draw_path()
    time.sleep(10)
   
    c.tk.root.mainloop()


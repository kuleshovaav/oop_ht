from vodopad import *
from convex import *

x0, y0=3.2, 4.9

x1_0, y1_0, x1_1, y1_1= 1.7, 3.5, 4.6, 4.1 #первый отрезок
x2_0, y2_0, x2_1, y2_1=0.6, 2.7, 3.3, 2.1 #второй отрезок
koord={y1_0: x1_0, y1_1: x1_1, y2_0: x2_0, y2_1: x2_1}

x_otr1=[x1_0, x1_1]
x_otr2=[x2_0, x2_1]
y_otr1=[y1_0, y1_1]
y_otr2=[y2_0, y2_1]

xs=[x_otr1, x_otr2] #координаты по x каждого отрезка
ys=[y_otr1, y_otr2] #координаты по y каждого отрезка

y_min=sorted([min(ys[i])for i in range(len(ys))])
x_min=sorted([min(xs[i])for i in range(len(xs))])

yki={min(y_otr1): max(y_otr1), min(y_otr2): max(y_otr2)}
xki={min(x_otr1): max(x_otr1), min(x_otr2): max(x_otr2)}

if __name__ == "__main__":

    import time
    from r2point import R2Point
    tk = TkDrawer()
    tk.clean()
    tk.draw_point(R2Point(x0, y0))
    tk.draw_line(R2Point(x1_0, y1_0), R2Point(x1_1, y1_1))
    tk.draw_line(R2Point(x2_0, y2_0), R2Point(x2_1, y2_1))



for i in range (len(y_min)-1, -1, -1):
    if x0>=koord[y_min[i]] and x0<=koord[yki[y_min[i]]] or x0<=koord[y_min[i]] and x0>=koord[yki[y_min[i]]]:

        y_job=y_min[i]
        y_other=yki[y_job]
        x_job=koord[y_job]
        x_other=koord[y_other]

        x_pad=x0
        y_pad=(x0-x_job)*(y_other-y_job)/(x_other-x_job)+y_job
        time.sleep(1)
        tk.draw_line(R2Point(x0, y0), R2Point(x_pad, y_pad), "blue")
        time.sleep(1)
        tk.draw_line(R2Point(x_pad, y_pad), R2Point(x_job, y_job), "blue")
        time.sleep(1)

        x0=x_job
        y0=y_job

tk.draw_line(R2Point(x0, y0), R2Point(x0, 0), "blue")



time.sleep(3)



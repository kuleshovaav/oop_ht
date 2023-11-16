from tkinter import *
from points1 import Point

# Размер окна
SIZE = 600
# Коэффициент гомотетии
SCALE = 60


def x(p):
    """ преобразование x-координаты """
    return SIZE/2 + SCALE*p.x


def y(p):
    """ преобразование y-координаты """
    return SIZE/2 - SCALE*p.y

class TkDrawer:
    """ Графический интерфейс """

    # Конструктор
    def __init__(self):
        self.root = Tk()
        self.root.title("Проблема с канатами в Канатово")
        self.root.geometry(f"{SIZE+5}x{SIZE+5}")
        self.root.resizable(False, False)
        self.root.bind('<Control-c>', quit)
        self.canvas = Canvas(self.root, width=SIZE, height=SIZE)
        self.canvas.pack(padx=5, pady=5)

    # Завершение работы
    def close(self):
        self.root.quit()

    # Стирание существующей картинки и рисование осей координат
    def clean(self):
        null = Point(0,0)
        self.canvas.create_rectangle(0, 0, SIZE, SIZE, fill="white")
        #self.canvas.create_line(0, y(null), SIZE, y(null), fill="blue")
        #self.canvas.create_line(x(null), 0, x(null), SIZE, fill="blue")
        self.root.update()

    # Рисование точки
    def draw_point(self, p, color= "black"):
        self.canvas.create_oval(
            x(p)+4, y(p)+4, x(p)-4, y(p)-4, fill=color)
        self.root.update()

    # Рисование линии
    def draw_line(self, p, q, color = "black", w = 2):
        self.canvas.create_line(x(p), y(p), x(q), y(q), fill=color, width=w)
        self.root.update()

    # Рисование круга
    def draw_circle(self, o, r, color = "salmon"):
        self.canvas.create_oval(x(o)-r*SCALE, y(o)-r*SCALE, 
                                x(o)+r*SCALE, y(o)+r*SCALE, fill = color)
        self.root.update()

    # Рисование дуги (углы в градусах!)    
    def draw_arc(self, o, r, start_angle, stop_angle, color = "green", w = 1):
        self.canvas.create_arc(x(o)-r*SCALE, y(o)-r*SCALE, 
                               x(o)+r*SCALE, y(o)+r*SCALE, 
                               outline = color, width = w,
                               fill = 'green',
                               start = start_angle, 
                               extent = stop_angle, 
                               style = ARC
                               )
        self.root.update()

if __name__ == "__main__":

    import time
    tk = TkDrawer()
    tk.clean()
    tk.draw_point(Point(4.9, 4.9))
    tk.draw_line(Point(2.0, 3.0), Point(2.0, 1.0))
    tk.draw_line(Point(-1.0, 2.0), Point(-2.0, 1.0))
    o = Point(0, 0)
    tk.draw_circle(o, 1, "grey80")
    tk.draw_arc(o, 1, -45, 90, "red", 3)
    time.sleep(50)
    tk.root.mainloop()
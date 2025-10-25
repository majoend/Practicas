
from tkinter import *
import time 

ventana = Tk()
x = velocidad = 1
y = velocidad = 1   

canvas = Canvas(width=500, height=500, bg="black")
canvas.pack()

fotoimagen = PhotoImage(file='homero.gif')
my_image = canvas.create_image(0, 0, image=fotoimagen, anchor=NW)

while True:
    coordenadas = canvas.coords(my_image)
    print(coordenadas)
    if coordenadas[0] >= 500:
        x = -velocidad
    canvas.move(my_image, x, 0)
    ventana.update()
    time.sleep(0.01)


ventana.mainloop()

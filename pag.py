
from tkinter import *
from ball import *
import time

ancho = 400
alto = 400

ventana = Tk()
canvas = Canvas(ventana, width=ancho, height=alto)
canvas.pack()
pelota_voley = pelota(canvas, 0, 0, 100, 1 , 1,  "red")

while True:
    pelota_voley.mover()
    ventana.update()
    time.sleep(0.001)



ventana.mainloop()
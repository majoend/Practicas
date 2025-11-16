
from tkinter import *
from time import *


def hora():
    hora_actual = strftime("%H:%M:%S %p")
    labelhora.config(text=hora_actual)

    dia = strftime("%A")
    labeldia.config(text=dia)

    ventana.after(1000, hora)

ventana = Tk()

labelhora = Label(ventana, font=("Arial", 48), bg="black", fg="white")
labelhora.pack()

labeldia = Label(ventana, font=("Arial", 48))
labeldia.pack()

hora()

ventana.mainloop()

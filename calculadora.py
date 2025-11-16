
from tkinter import *

def boton_presionar(num):
    global equation
    equation = equation + str(num)
    equation_label.set(equation)

def igual():
    global equation
    resultado_total = str(eval(equation))
    equation_label.set(resultado_total)
    equation = resultado_total

def clear ():
    global equation
    equation = ""
    equation_label.set("")

ventana = Tk()
ventana.title("Calculadora Python")
foto = PhotoImage(file="bird.png")
ventana.iconphoto(False, foto)


ventana.geometry("300x300")
ventana.config(bg="gray")

equation = ""
equation_label = StringVar()

label = Label(ventana, textvariable=equation_label, 
              font=('Times ', 20), 
              bg="pink", fg="black", 
             width=24, height=2)
label.pack()

frame = Frame(ventana, bg="gray")
frame.pack()

boton1 = Button(frame, text='1', height=2, width=7, command=lambda: boton_presionar('1'))
boton1.grid(row=0, column=0)

boton2 = Button(frame, text='2', height=2, width=7, command=lambda: boton_presionar('2'))
boton2.grid(row=0, column=1)

boton3 = Button(frame, text='3', height=2, width=7, command=lambda: boton_presionar('3'))
boton3.grid(row=0, column=2)

boton4 = Button(frame, text='4', height=2, width=7, command=lambda: boton_presionar('4'))
boton4.grid(row=1, column=0)    

boton5 = Button(frame, text='5', height=2, width=7, command=lambda: boton_presionar('5'))
boton5.grid(row=1, column=1)    

boton6 = Button(frame, text='6', height=2, width=7, command=lambda: boton_presionar('6'))
boton6.grid(row=1, column=2)

boton7 = Button(frame, text='7', height=2, width=7, command=lambda: boton_presionar('7'))
boton7.grid(row=2, column=0)

boton8 = Button(frame, text='8', height=2, width=7, command=lambda: boton_presionar('8'))
boton8.grid(row=2, column=1)

boton9 = Button(frame, text='9', height=2, width=7, command=lambda: boton_presionar('9'))
boton9.grid(row=2, column=2)

boton0 = Button(frame, text='0', height=2, width=7, command=lambda: boton_presionar('0'))
boton0.grid(row=3, column=0)

plus = Button(frame, text='+', height=2, width=7, command=lambda: boton_presionar('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=2, width=7, command=lambda: boton_presionar('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=2, width=7, command=lambda: boton_presionar('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=2, width=7, command=lambda: boton_presionar('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=2, width=7, command=igual)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=2, width=7, command=lambda: boton_presionar('.'))
decimal.grid(row=3, column=1)

clear = Button(ventana, text='clear', height=2, width=7, command=clear)
clear.pack()

ventana.mainloop()
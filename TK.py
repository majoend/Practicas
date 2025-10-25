
import time
import tkinter as tk
window = tk.Tk()
window.title("My time")


etiqueta = tk.Label(window, text="Hello, Tkinter!")
etiqueta.config(font=("Arial", 24))
etiqueta.pack()

def hora_actual():
    mihora = time.strftime("%H:%M:%S")
    etiqueta.config(text=mihora, fg="pink", bg="black")
    etiqueta.after(1000, hora_actual)

hora_actual()
window.mainloop()

class pelota:

    def __init__(self, canvas,  x, y, diameter, velocidad_x, velocidad_y, color):
       self.canvas = canvas
       self.image =canvas.create_oval(x, y, diameter, diameter, fill=color)
       self.velocidad_x = velocidad_x 
       self.velocidad_y = velocidad_y

    def mover(self):
       coordenadas = self.canvas.coords(self.image)
       print (coordenadas)

       if coordenadas[2] >= self.canvas.winfo_width() or coordenadas[0] < 0:
            self.velocidad_x = -self.velocidad_x
            
       if coordenadas[3] >= self.canvas.winfo_height() or coordenadas[1] < 0:
            self.velocidad_y = -self.velocidad_y

        
       self.canvas.move(self.image, self.velocidad_x, self.velocidad_y)

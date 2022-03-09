import tkinter as tk
from constantes import style
from screens import Home
from screens import Game


class Manager(tk.Tk):  #VENTANA PRINCIPAL DE LA APLICACION


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("TALLER#1 - PARSEAR XML")
        container = tk.Frame(self) #Creando un Frame incrustado dentro de la ventana CONTAINER
        self.mode = "Normal"
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )

        container.configure(background = style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1) #COLUMNAS QUE SE USAN, 0. Y EL PESO, ESPACIO QUE ABARCA
        container.grid_rowconfigure(0, weight=1) #FILAS QUE SE USAN, 0. Y EL PESO, ESPACIO QUE ABARCA

        self.frames = {} #DICCIONARIO VACIO 
        for F in (Home, Game):
            frame = F(container, self)   
            self.frames[F] = frame #GUARDAMOS EN UN DICCIONARIO LAS CLASES QUE SON 'SCREENS' EN MANAGER
            frame.grid(row = 0, column = 0, sticky = tk.NSEW) #Sticky se ancla a todos los costados
        
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container] #Llamo al diccionario con sus frames 
        frame.tkraise() #tkrise toma el frame Home y lo coloca como principal, la que se mira de primero
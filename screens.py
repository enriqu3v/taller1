import tkinter as tk

import xml.etree.ElementTree as ET


tree = ET.parse('./XML/Prueba.xml') #ENLAZAR EL ARCHIVO XML
root = tree.getroot() #OBTENER EL ELEMENTO RAIZ

from constantes import style


class Data:
    def __init__(self, name): #CONSTRUCTOR
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return " %s" %(self.name)      

class Persona(Data):
    def __init__(self, nombre, cedula): #CONSTRUCTOR
        self.nombre = nombre
        self.cedula = cedula

    def get_nombre(self):
        return self.nombre

    def get_cedula(self):
        return self.cedula 

    def __str__(self):
        return " %s, %s" %(self.nombre, self.cedula)       

class Estudiante(Persona):

    def __init__(self, nombre, cedula, color, comida, lugar, hobbie): #CONSTRUCTOR
        Persona.__init__(self, nombre, cedula)
        self.color = color
        self.comida = comida
        self.lugar = lugar
        self.hobbie = hobbie
        
    def set_color(self, color):
        self.color = color

    def set_comida(self, comida):
        self.comida = comida

    def set_lugar(self, lugar):
        self.lugar = lugar

    def set_hobbie(self, hobbie):
        self.hobbie = hobbie 

    def get_color(self):
        return self.color

    def get_comida(self):
        return self.comida

    def get_lugar(self):
        return self.lugar

    def get_hobbie (self):
        return self.hobbie 

    def __str__(self):
        return " %s: %s, %s, %s, %s" %(str(self.cedula), self.color, self.comida, self.lugar, self.hobbie)
                


class Home(tk.Frame): #widget


    def __init__(self, parent, controller):
        
        super().__init__(parent)
        self.configure(background = style.BACKGROUND) #configure - atributo de la clase Home y asi sucevivamente con los demas
        self.controller = controller
        self.gameMode = tk.StringVar(self, value="Normal")

        self.init_widgets()


    def encontrar_raiz(self):
        bandera=True
        for elemento in root.iter():
            if(bandera==True):
                return elemento.tag
                bandera=False

    def move_to_game(self):
        self.controller.mode = self.gameMode.get()
        self.controller.show_frame(Game)    


    def agregarNietos(self, est):

        tk.Label(
            self, #Apunta al contenedor que lo contiene
            text = est.cedula,  #Asocia una funcion como un objeto}
            **style.STYLE_ARCHIVO,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 100, 
            pady = 11
        )

        tk.Label(
            self, #Apunta al contenedor que lo contiene
            text = est.color,  #Asocia una funcion como un objeto}
            **style.STYLE_ARCHIVO,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 100, 
            pady = 11
        )

        tk.Label(
            self, #Apunta al contenedor que lo contiene
            text = est.comida,  #Asocia una funcion como un objeto}
            **style.STYLE_ARCHIVO,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 100, 
            pady = 11
        )

        tk.Label(
            self, #Apunta al contenedor que lo contiene
            text = est.lugar,  #Asocia una funcion como un objeto}
            **style.STYLE_ARCHIVO,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 100, 
            pady = 11
        )

        tk.Label(
            self, #Apunta al contenedor que lo contiene
            text = est.hobbie,  #Asocia una funcion como un objeto}
            **style.STYLE_ARCHIVO,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 100, 
            pady = 11
        )
    
    def agregarHijos(self, est1, est2, est3):

        tk.Button(
            self, #Apunta al contenedor que lo contiene
            text = est1.nombre,  #Asocia una funcion como un objeto}
            command = lambda: self.agregarNietos(est1),
            **style.STYLE_CARPETA,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 80, 
            pady = 11
        )

        tk.Button(
            self, #Apunta al contenedor que lo contiene
            text = est2.nombre,  #Asocia una funcion como un objeto}
            command = lambda: self.agregarNietos(est2),
            **style.STYLE_CARPETA,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
                side = tk.TOP,
                fill = tk.X,
                padx = 80, 
                pady = 11
        )

        tk.Button(
            self, #Apunta al contenedor que lo contiene
            text = est3.nombre,  #Asocia una funcion como un objeto}
            command = lambda: self.agregarNietos(est3),
            **style.STYLE_CARPETA,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 80, 
            pady = 11
        )
 

    def buscarHijos(self):

        for i in range(3):
            nombreEst = "<"+root[i].tag.upper()+">"+root[i].get('name')
            cedula = root[i][0].text 
            color = root[i][1].text 
            comida = root[i][2].text 
            lugar = root[i][3].text 
            hobbie = root[i][4].text
            if(i==0):
                est1 = Estudiante(nombreEst, cedula, color, comida, lugar, hobbie)

            if(i==1):
                est2 = Estudiante(nombreEst, cedula, color, comida, lugar, hobbie)

            if(i==2):
                est3 = Estudiante(nombreEst, cedula, color, comida, lugar, hobbie)  

        self.agregarHijos(est1, est2, est3)


    def init_widgets(self):

        tk.Label(
            self,
            text="Hola, Bienvenido!",
            justify=tk.CENTER,
            **style.STYLE
        ).pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 22, pady = 11) # style.STYLE - LO QUE HACE ES TRAER EL DICCIONARIO DESCOMPRIMIDO EN CADA PARAMETRO /// fil = tk.BOTH - LO QUE HACE ES EXTENDER ESE ELEMENTO A SU MAXIMO EN ANCHO Y ALTO.

        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background = style.COMPONENT)
        optionsFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH, #FILL - ENLAZA CONTENIDO A ALGUN EJE, X,Y O AMBOS (BOTH)
            expand = True,
            padx = 22,
            pady = 11
        )

        tk.Label(
            optionsFrame,
            text = " 📂 GESTOR DE ARCHIVOS XML",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(side = tk.TOP, fill = tk.X, padx = 22, pady = 11)  #FILL - ENLAZA CONTENIDO A ALGUN EJE, X,Y O AMBOS (BOTH) CON BOTH
        
        
        tk.Button(
            self, #Apunta al contenedor que lo contiene
            text = "<"+self.encontrar_raiz().upper()+">",  #Asocia una funcion como un objeto}
            command = lambda: self.buscarHijos(),
            **style.STYLE_CARPETA,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22, 
            pady = 11
        )  


class Game(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = "red") 
        self.controller = controller
        self.currentQuestion = tk.StringVar(self, value=" VAMOSSS !!")
        self.fichero = None

        self.init_widgets()

    def update_question(self):
        self.mode = self.controller.mode
        if(self.fichero == None) or (self.controller.mode.lower() not in self.fichero.name.lower()):
            self.fichero = open(f'./ficheros/{self.mode}.txt', 'r', encoding = "utf-8")

        tmp = self.fichero.readline()
        if(tmp != ""):
            self.currentQuestion.set(tmp)
        else:
            self.currentQuestion.set("CUESTIONARIO TERMINADO!")
            self.fichero.close() 
            self.fichero = open(f'./ficheros/{self.mode}.txt', 'r', encoding = "utf-8")


    def return_to_home(self):
        self.currentQuestion.set(" VAMOSSS !!")
        self.controller.show_frame(Home)
        

    def init_widgets(self):
  
        tk.Label(
            self,
            text = " Are you ready? 💪",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(side = tk.TOP, fill = tk.X, padx = 22, pady = 11)  #FILL - ENLAZA CONTENIDO A ALGUN EJE, X,Y O AMBOS (BOTH) CON BOTH
        
        tk.Label(
            self,
            text="",
            textvar = self.currentQuestion,
            justify=tk.CENTER,
            **style.STYLE
        ).pack(side = tk.TOP, fill = tk.BOTH, expand = True, padx = 22, pady = 11) # style.STYLE - LO QUE HACE ES TRAER EL DICCIONARIO DESCOMPRIMIDO EN CADA PARAMETRO /// fil = tk.BOTH - LO QUE HACE ES EXTENDER ESE ELEMENTO A SU MAXIMO EN ANCHO Y ALTO.


        tk.Button(
            self, #Apunta al contenedor que lo contiene
            text = "SIGUIENTE ->",
            command = self.update_question,   #Asocia una funcion como un objeto
            **style.STYLE,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH, #Definir limites de boton
            expand = True, #Definir si se quiere expandir los contenidos de adentro conforme cambia el contenedor
            padx = 22, 
            pady = 11
        )      

        tk.Button(
            self, #Apunta al contenedor que lo contiene
            text = "<- Home",
            command = self.return_to_home,   #Asocia una funcion como un objeto
            **style.STYLE,
            relief = tk.FLAT, #Quita los bordes de los botones
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH, #Definir limites de boton
            expand = True, #Definir si se quiere expandir los contenidos de adentro conforme cambia el contenedor
            padx = 22, 
            pady = 11
        )    

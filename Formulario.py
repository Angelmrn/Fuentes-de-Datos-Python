from tkinter import *
from tkinter import ttk


class datos:
    def __init__(self,raiz):
        #VARIABLES
        
        principal=ttk.Frame(raiz)
        principal.grid()
        principal=ttk.Frame(raiz)
        principal.grid()
        
        Nombre = StringVar()
        AParerno = StringVar()
        AMaterno = StringVar()
        Correo = StringVar()
        Movil = StringVar()
        estado = StringVar()
        raiz.title("Muestra Widgets")
    
        comboEstados = ttk.Combobox(principal, textvariable=estado)
        comboEstados.grid(column=1, row= 10)
        comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

        #FRAME CHECk
        emple = ttk.Frame(principal, padding="10 10 10 10")
        emple.grid(column= 1, row= 2)

        Estudiante = ttk.Radiobutton(emple, text="Estudiante")
        Estudiante.grid(column=5,row=1, sticky=(W))
        Empleado = ttk.Radiobutton(emple, text="Empleado")
        Empleado.grid(column=5,row=2,pady=5, sticky=(W))
        Desempleado = ttk.Radiobutton(emple, text="Desempleado")
        Desempleado.grid(column=5,row=3,pady=5, sticky=(W))

        #FRAME AFICIONES
        Aficiones = ttk.Frame(principal, padding="10 10 30 30",relief="raised")
        Aficiones.grid(column=0, row=9, rowspan=5)

        Leer = ttk.Checkbutton(Aficiones, text="Leer")
        Leer.grid(column=0,row=0)
        Musica = ttk.Checkbutton(Aficiones, text="Musica")
        Musica.grid(column=1,row=0)
        VideoJuegos = ttk.Checkbutton(Aficiones, text="VideoJuegos")
        VideoJuegos.grid(column=2,row=0)


        #FRAME BOTONES
        botones = ttk.Frame(principal, padding="10 10 10 10")
        botones.grid(column=0, row=20)

        btnCancelar = ttk.Button(botones, text="Cancelar", compound="bottom")
        btnCancelar.grid(column=1,row=1)

    
        self.Nombre=StringVar()
        self.AParerno=StringVar()
        self.AMaterno=StringVar()
        self.Correo=StringVar()
        self.Movil=StringVar()

        Usuario = ttk.Frame(principal, padding="10 10 10 10", relief="raised")
        Usuario.grid(column=0, row=1,rowspan=5)

        Nombre = ttk.Entry(Usuario, width=30, textvariable=self.Nombre)
        Nombre.grid(column=1, row=0)

        AParerno = ttk.Entry(Usuario, width=30, textvariable=self.AParerno)
        AParerno.grid(column=1, row=1)
        AMaterno = ttk.Entry(Usuario, width=30, textvariable=self.AMaterno)
        AMaterno.grid(column=1, row=2)
        Correo = ttk.Entry(Usuario, width=30, textvariable=self.Correo)
        Correo.grid(column=1, row=3)
        Movil = ttk.Entry(Usuario, width=30, textvariable=self.Movil)
        Movil.grid(column=1, row=4)

        ttk.Label(Usuario, text="Nombre").grid(column=0, row=0, pady=20)
        ttk.Label(Usuario, text="A.Paterno").grid(column=0, row=1, pady=20)
        ttk.Label(Usuario, text="A.Materno").grid(column=0, row=2,pady=20)
        ttk.Label(Usuario, text="Correo").grid(column=0, row=3,pady=20)
        ttk.Label(Usuario, text="Movil").grid(column=0, row=4,pady=20)

        btnGuardar = ttk.Button(botones, text="Guardar", command=self.guardar).grid(column=0,row=1)
        
    def guardar(self, *args):
            print("Boton GUARDAR precionado")
            nomUsuario = self.Nombre.get()
            print("Nombre ingresado:", nomUsuario)
            apPaternoUsu = self.AParerno.get()
            print("ApPaterno Ingresado:", apPaternoUsu)
            apMaternoUsu = self.AMaterno.get()
            print("apMaterno Ingresado:", apMaternoUsu)
            correoUsuario = self.Correo.get()
            print("Correo Ingresado:", correoUsuario)
            movilUsu = self.Movil.get()
            print('Movil Ingresado:' , movilUsu)
 
            nom=str(nomUsuario)
            apat=str(apPaternoUsu)
            amat=str(apMaternoUsu)
            corr=str(correoUsuario)
            mov=str(movilUsu)

            info=(nom + ',' + apat + ',' + amat + ',' + corr + ',' + mov + '\n')

            with open('info.csv', 'a', newline='') as file:
                file.writelines(info)
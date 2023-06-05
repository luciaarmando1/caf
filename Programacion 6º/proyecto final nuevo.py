from cgitb import text
from select import select
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql


global guardar, var_buscar, id_seleccionado, dni_1
guardar = "Nuevo"
var_buscar = 0
#------------------------Ventana-de-Inicio----------------------------


def ventana_Login():
			global ventana1
			ventana1 = Tk()
			w = 380
			h = 350
			ws = ventana1.winfo_screenwidth()
			hs = ventana1.winfo_screenheight()
			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)
			ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))
			
			#-----------------------------------------------------------------
			ventana1.title("Iniciar Sesion")
			ventana1.configure(bg="#ADD8E6")
		#---------------------------------------------------------
		#-----------------------------------------------------------------
			def login_admin():
				if(usuario1.get() == ""):
					entry_usuario1.focus()
					messagebox.showinfo("Faltan datos", "Ingrese Usuario")

					return
				elif(contrasena1.get()==""):
					messagebox.showinfo("Faltan datos", "Ingrese Contraseña")
					entry_constrasena1.focus()
					return

				basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="admi")
				fcursor = basedatos.cursor()

				fcursor.execute("SELECT Usuario FROM admi WHERE Usuario='" + usuario1.get() + "' and Contrasena='" + contrasena1.get() + "'")

				if fcursor.fetchall():
					deRegistro_a_escuela()
				else:
					messagebox.showerror("Error", "Usuario y Contraseña Incorrecta")

				login_admin.resizable(0,0)
				login_admin.iconbitmap("icons/FOLDER02.ico")
				basedatos.close()


#----------------------------------------------------------------
			Label(ventana1, text="Usuario " ,font= "calibri").place(x=50, y=50)
			Label(ventana1, text="Contraseña", font= "calibri").place(x=50, y=80)

			usuario1 = StringVar()
			contrasena1 = StringVar()

			entry_usuario1 = Entry(ventana1, textvariable=usuario1)
			entry_usuario1.pack()
			entry_usuario1.place(x=150,y=50)

			entry_constrasena1 = Entry(ventana1, textvariable=contrasena1, show="*")
			entry_constrasena1.pack()
			entry_constrasena1.place(x=150,y=80)

			Button(ventana1, text="Registrarse").place(x=50, y=200)
			Button(ventana1, text="Entrar       ").place(x=180, y=200)


			mainloop()

ventana_Login ()

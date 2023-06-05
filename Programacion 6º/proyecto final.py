import tkinter as tk 

def ventana_login():
		global ventana1
		ventana1 = TK()
		w = 750
		h = 500
		ws = ventana1.winfo_screenmmwidth()
		hs = ventana1.winfo_screenmmwidth()
		x = (ws/2) - (w/2)
		y=  (ws/2) - (w/2)
		ventana1.geometry('%dx%d+%d%d' % (w,h,x,y))
		#---------------------------------------------------------------
		ventana1.title("Iniciar sesion")
		ventanal.config(bg="#ADD8E6")
		ventana1.configure
		#---------------------------------------------------------------
		#---------------------------------------------------------------
		
		
		
		etiqueta_usuario = tk.Label(ventanal, text="Usuario")
		etiqueta_usuario.configure

		etiqueta_usuario.grid(row=0, column=0)

		entrada_usuario = tk.Entry(ventanal)
		entrada_usuario.grid(row=0, column=1)

		etiqueta_contrasena = tk.Label(ventanal, text="Contraseña")
		etiqueta_contrasena.configure

		etiqueta_contrasena.grid(row=1, column=0)

		entrada_contrasena = tk.Entry(ventanal, show="*")
		entrada_contrasena.grid(row=1, column=1)

		boton_ingresar = tk.Button(ventanal, text="Ingresar", command=verificar)
		boton_ingresar.grid(row=2, column=0, columnspan=2)

		boton_resgistrar = tk.Button(ventanal, text="registrar", command=ventana_registrar)
		boton_resgistrar.grid(row=3, column=0, columnspan=3)

		mainloop()

				
def verificar():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    modulo.login=(usuario, contrasena)

def ventana_registrar():
    ventana_l.destroy()
    import registro_usuario
    
ventana_login()
    


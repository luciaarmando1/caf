def login_admin():
			if(usuario1.get()==""):
				entry_usuario1.focus()
				messagebox.showinfo("Falta datos","Ingrese usuario")
				return 

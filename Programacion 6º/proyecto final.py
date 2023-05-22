import tkinter as tk
import estilos, modulo 

def verificar():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    modulo.login=(usuario, contrasena)

def ventana_registrar():
    ventana_l.destroy()
    import registro_usuario

ventana_l = tk.Tk()
ventana_l.title("Inicio de Sesión")

ventana_l.geometry(estilos.size_ventana)
ventana_l.config(bg=estilos.color_fondo)

etiqueta_usuario = tk.Label(ventana_l, text="Usuario", font=estilos.fuente_normal)
etiqueta_usuario.configure(bg=estilos.color_fondo)

etiqueta_usuario.grid(row=0, column=0)

entrada_usuario = tk.Entry(ventana_l)
entrada_usuario.grid(row=0, column=1)

etiqueta_contrasena = tk.Label(ventana_l, text="Contraseña", font=estilos.fuente_normal)
etiqueta_contrasena.configure(bg=estilos.color_fondo)

etiqueta_contrasena.grid(row=1, column=0)

entrada_contrasena = tk.Entry(ventana_l, show="*")
entrada_contrasena.grid(row=1, column=1)

boton_ingresar = tk.Button(ventana_l, text="Ingresar", command=verificar, font=estilos.fuente_normal, bg=estilos.color_botones)
boton_ingresar.grid(row=2, column=0, columnspan=2)

boton_resgistrar = tk.Button(ventana_l, text="registrar", command=ventana_registrar, font=estilos.fuente_normal, bg=estilos.color_botones)
boton_resgistrar.grid(row=3, column=0, columnspan=3)

ventana_l.mainloop()
